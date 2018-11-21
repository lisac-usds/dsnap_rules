from . import dgi_calculator
from .rules import Rule, Result, SimplePredicateRule


class AuthorizedRule(SimplePredicateRule):
    success_finding = "Either head of household or authorized representative"
    failure_finding = "Neither head of household nor authorized representative"

    def predicate(self, payload, disaster):
        return (payload["is_head_of_household"]
                or payload["is_authorized_representative"])


class FoodPurchaseRule(SimplePredicateRule):
    """
    The household must plan on purchasing food during the disaster benefit
    period or have purchased food during that time if the benefit period has
    passed.
    """
    success_finding = "Either purchased or plans to purchase food during "\
                      "benefit period"
    failure_finding = "Neither purchased nor plans to purchase food during "\
                      "benefit period"

    def predicate(self, payload, disaster):
        return (payload["plans_to_purchase_food_during_benefit_period"]
                or payload["purchased_food_during_benefit_period"])


class AdverseEffectRule(SimplePredicateRule):
    """
    Disaster-related adverse effects fall into three categories: loss of
    income, inaccessible resources, and disaster expenses. The household must
    have experienced at least one of these adverse effects in order to be
    eligible.
    """
    success_finding = "Experienced disaster-related adverse effects"
    failure_finding = "Did not experience any disaster-related adverse effect"

    def predicate(self, payload, disaster):
        return (
            payload["has_lost_or_inaccessible_income"]
            or payload["has_inaccessible_liquid_resources"]
            or payload["incurred_deductible_disaster_expenses"])


class ResidencyRule(SimplePredicateRule):
    """
    In most cases, the household must have lived in the disaster area at the
    time of the disaster. States may also choose to extend eligibility to those
    who worked in the disaster area at the time of the disaster.
    """

    success_finding = "Resided or worked in disaster area at disaster time"
    failure_finding = "Did not reside or work in disaster area at disaster "\
                      "time"

    def predicate(self, payload, disaster):
        return (
            payload["resided_in_disaster_area_at_disaster_time"]
            or (
                payload["worked_in_disaster_area_at_disaster_time"]
                and disaster.worked_is_dsnap_eligible)
        )


class SNAPSupplementalBenefitsRule(SimplePredicateRule):
    """
    Supplemental benefits provide parity between new D-SNAP households
    and ongoing clients, who are not eligible for D-SNAP benefits.
    """
    success_finding = "Does not receive benefits from SNAP"
    failure_finding = "SNAP beneficiaries should apply for supplemental "\
                      "benefits through SNAP"

    def predicate(self, payload, disaster):
        return not payload["receives_SNAP_benefits"]


class ConflictingUSDAProgramRule(SimplePredicateRule):
    """
    A household is not eligible for D-SNAP if it is already being served by
    the other programs of USDA Foods, such as Food Distribution on Indian
    Reservations (FDPIR) and The Emergency Food Assistance Program (TEFAP).
    """
    success_finding = "Does not receive benefits from conflicting USDA "\
                      "programs"
    failure_finding = "Receives benefits from conflicting USDA programs"

    def predicate(self, payload, disaster):
        return not(
            payload["receives_FDPIR_benefits"]
            or payload["receives_TEFAP_food_distribution"])


class IncomeAndResourceRule(Rule):
    """
    The household's take-home income received (or expected to be received)
    during the benefit period plus its accessible liquid resources minus
    disaster related expenses (unreimbursed disaster related expenses paid or
    anticipated to be paid out of pocket during the disaster benefit period)
    shall not exceed the Disaster Gross Income Limit (DGIL).
    """

    def execute(self, payload, disaster):
        gross_income = self.disaster_gross_income(payload)
        income_limit, allotment = self.get_limit_and_allotment(payload, disaster)
        result = gross_income <= income_limit
        if result:
            finding = (
                f"Gross income {gross_income} within limit of "
                f"{income_limit}"
            )
            metrics = {"allotment": allotment}
        else:
            finding = (
                f"Gross income {gross_income} exceeds limit of "
                f"{income_limit}"
            )
            metrics = {}
        return Result(result, [finding], metrics)

    def disaster_gross_income(self, payload):
        return (
            payload["total_take_home_income"]
            + payload["accessible_liquid_resources"]
            - payload["deductible_disaster_expenses"]
        )

    def get_limit_and_allotment(self, payload, disaster):
        calculator = dgi_calculator.get_dgi_calculator(
                        disaster.state_or_territory)
        return (
            calculator.get_limit(payload["size_of_household"]),
            calculator.get_allotment(payload["size_of_household"])
        )
