import pytest
from module import Site
import yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

@pytest.fixture
def email_input():
    return '//*[@id="login"]/div[1]/label/input'

@pytest.fixture
def password_input():
    return '//*[@id="login"]/div[2]/label/input'

@pytest.fixture
def error():
    return '//*[@id="app"]/main/div/div/div[2]/h2'

@pytest.fixture
def submit():
    return "button"

@pytest.fixture
def result_error():
    return "401"

@pytest.fixture
def site():
    site_instance = Site(testdata["address"])
    yield site_instance
    site_instance.close()

@pytest.fixture
def create_button():
    return '//*[@id="create-btn"]'

@pytest.fixture
def title_input():
    return '//*[@id="create-item"]/div/div/div[1]/div/label'

@pytest.fixture
def description_input():
    return '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea'

@pytest.fixture
def content_input():
    return '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea'

@pytest.fixture
def switch_draft():
    return '//*[@id="SMUI-form-field-0"]/div[2]/div/div[2]'

@pytest.fixture
def calendare():
    return '//*[@id="create-item"]/div/div/div[5]/div/div/label/input'

@pytest.fixture
def image_add():
    return '//*[@id="create-item"]/div/div/div[6]/div/div/label/input'

@pytest.fixture
def save_button():
    return '//*[@id="create-item"]/div/div/div[7]/div/button/span'

@pytest.fixture
def home_button():
    return '//*[@id="app"]/main/nav/a/span'

@pytest.fixture()
def title_new_post():
    return '//*[@id="app"]/main/div/div[1]/h1'

