from behave import given, when, then
from main import get_roots, check


@given(u"Biquadratic equation app is run")
def step_impl(context):
    print(u'Step: Given Biquadratic equation app is run')

@when(u'I have the odds "{a}", "{b}", and "{c}"')
def step_impl(context, a, b, c):
    print(u'Step: I have the odds "{}", "{}", and "{}"'. format(a, b, c))
    b = str(get_roots(int(a), int(b), int(c))).rpartition(']')[0]
    c = b.partition('[')[2]
    context.result = c
    print(u'Stored result "{}" in context'. format(context.result))

@then(u'I get result "{out}"')
def step_impl(context, out):
    if (context.result == str(out)):
        print(u'Step: Then I get right result "{}", "{}"'.format(context.result, out))
        pass
    else :
        raise Exception ("Invalid root is returned.")