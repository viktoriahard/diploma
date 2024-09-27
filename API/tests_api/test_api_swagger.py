import allure
import pytest
from assertpy import assert_that


@allure.title('API testing')
@allure.description('Getting a pet by its id')
@pytest.mark.api_test
def test_get_pet_by_id(api_client):
    response = api_client.pet.get_pet_by_id(5)
    assert response.status_code == 200


@allure.description('Creating a pet')
def test_post_pet(api_client):
    response = api_client.pet.post_add_pet()
    assert response.json()["name"] == "Asia"
    assert_that(response.status_code).is_equal_to(200)


@allure.description('Updating a pet')
def test_update_pet(api_client):
    response = api_client.pet.update_pet()
    assert response.json()["name"] == "Asia2"
    assert_that(response.status_code).is_equal_to(200)


@allure.description('Creating a pet by its id')
def test_add_pet_by_id(api_client):
    response = api_client.pet.post_add_pet_by_id(5)
    assert response.status_code == 200


@allure.description('Deleting a pet by its id')
def test_delete_pet_by_id(api_client):
    response1 = api_client.pet.delete_pet_by_id(5)
    assert response1.status_code == 200
    response2 = api_client.pet.check_delete_pet(5)
    assert response2.status_code == 404


@allure.description('Getting a pet status')
def test_get_pet_by_status(api_client):
    response = api_client.pet.get_pet_by_status()
    assert response.status_code == 200


@allure.description('Trying to upload an image of pet')
@pytest.mark.xfail  # no file
def test_upload_image_pet(api_client):
    response = api_client.pet.upload_pet_image(75)
    assert response.status_code == 200
