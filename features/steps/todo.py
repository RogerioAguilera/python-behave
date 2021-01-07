from json import loads
from behave import given, when, then
from selenium.webdriver import Chrome

@given('que eu esteja na página')
def go_to_page(context):
    context.browser = Chrome()
    context.browser.get ('http://selenium.dunossauro.live/todo_list.html')

@when ('criar um todo')
def create_todo(context):

    texto_do_step = loads(context.text)

    context.browser.find_element_by_id('todo-name').send_keys
    (texto_do_step['nome']
    
    )
    context.browser.find_element_by_id('todo-desc').send_keys
    (texto_do_step['descricao']
    
    )

    context.browser.find_element_by_id('todo-submit').click()

@then('o todo deve estar na pilha "{pilha}"')
def check_todo(context,pilha):
    ...
