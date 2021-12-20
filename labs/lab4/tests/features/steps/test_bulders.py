from behave import given, when, then
from chair_factory import VintageBuilder, ModernBuilder, ModernChair, VintageChair


@given("The chair style is {style}, weight is {weight} lbs, cost is {cost} dollars")
def have_chair_params(context, style, weight, cost):
    context.style = style
    context.weight = weight
    context.cost = cost


@when("We choosing factory we must choose appropriate one")
def build_chair(context):
    if context.style == "vintage":
        context.chair = VintageBuilder().build_chair(context.weight, context.cost)
    if context.style == "modern":
        context.chair = ModernBuilder().build_chair(context.weight, context.cost)


@then(
    "Produced chair should be {style} with given parameters: weight is {weight} lbs, cost is {cost} dollars"
)
def expect_result(context, style, weight, cost):
    if style == "vintage":
        assert isinstance(context.chair, VintageChair)
    if style == "modern":
        assert isinstance(context.chair, ModernChair)
    assert context.chair.weight == weight
    assert context.chair.cost == cost
    print(str(style))
    print(context.chair.get_style_name())
    assert context.chair.get_style_name() == str(style)
