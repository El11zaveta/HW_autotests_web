import yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(email_input, password_input, submit, error, result_error, site):  #авторизация
    input1 = site.find_element("xpath", email_input)
    input1.send_keys("test")
    input2 = site.find_element("xpath", password_input)
    input2.send_keys("test")
    btn = site.find_element("css", submit)
    btn.click()
    error_label = site.find_element("xpath", error)
    assert error_label.text == result_error


def test_step2(email_input, password_input, submit, error, result_error, site): #отображение юзернейма
    input1 = site.find_element("xpath", email_input)
    input1.send_keys(testdata['username'])
    input2 = site.find_element("xpath", password_input)
    input2.send_keys(testdata['password'])
    btn = site.find_element("css", submit)
    btn.click()
    hello_text = site.find_element("xpath", '//*[@id="app"]/main/nav/ul/li[3]/a').text
    assert f"Hello, {testdata['username']}" == hello_text


def test_step3(email_input, password_input, submit, error, result_error, site, create_button, title_input,
               description_input, content_input, switch_draft, image_add, calendare, save_button,
               home_button, title_new_post): #создание поста
    input1 = site.find_element("xpath", email_input)
    input1.send_keys(testdata['username'])
    input2 = site.find_element("xpath", password_input)
    input2.send_keys(testdata['password'])
    btn = site.find_element("css", submit)
    btn.click()
    create_post = site.find_element("xpath", create_button)
    create_post.click()
    input3 = site.find_element("xpath", title_input)
    input3.send_keys(testdata['title'])
    input4 = site.find_element("xpath", description_input)
    input4.send_keys(testdata['description'])
    input5 = site.find_element("xpath", content_input)
    input5.send_keys(testdata['content'])
    btn_save = site.find_element("xpath", save_button)
    btn_save.click()
    btn_home = site.find_element("xpath", home_button)
    btn_home.click()
    new_post_title = site.find_element("xpath", title_new_post)
    assert new_post_title.text == 'Create Post'