import allure
from allure_commons.types import AttachmentType


def make_attachment(data, name):
    allure.attach(data, name, AttachmentType.TEXT)
