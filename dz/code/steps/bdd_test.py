from behave import Given,When,Then
from main import *

@Given("ordering albums with answers in bot queen album - {a} rhcp album - {b} green day album - {c}")
def given_answers(context,a,b,c):
    context.ans1=int(a)
    context.ans2=int(b)
    context.ans3=int(c)

@When("we form summary of check")
def make_summary(context):
    res = summary(queen_albums,queen_albums_price,rhcp_albums,rhcp_albums_price,green_day_albums,green_day_albums_price,context.ans1,context.ans2,context.ans3)
    context.result=res

@Then("check should be with correct price {out}")
def compare_results(context, out):
    corres = "Итоговая сумма заказа = " + str(out)+ "\n"
    assert(context.result == corres)
