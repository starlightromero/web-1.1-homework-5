"""Import pytest and app."""
import pytest
from .app import app


#######################
# Index Tests
# (there's only one here because there is only one possible scenario!)
#######################


def test_index():
    r"""Test that the index page shows \"Hello, World!\"."""
    res = app.test_client().get("/")
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    expected_page_text = "Hello, World!"
    assert expected_page_text == result_page_text


#######################
# Color Tests
#######################


def test_color_results_blue():
    """Test that the color_results page shows blue."""
    result = app.test_client().get("/color_results?color=blue")

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "Wow, blue is my favorite color, too!"
    assert expected_page_text == result_page_text


def test_color_results_red():
    """Test that the color_results page shows red."""
    result = app.test_client().get("/color_results?color=red")

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "Wow, red is my favorite color, too!"
    assert expected_page_text == result_page_text


def test_color_results_edgecase1():
    """Test that the color_results page handles edgecase."""
    result = app.test_client().get("/color_results?color=")

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "I love all colors!"
    assert expected_page_text == result_page_text


#######################
# Froyo Tests
#######################


def test_froyo_results_scenario1():
    """Test that the froyo_results page shows strawberry and nuts."""
    result = app.test_client().get(
        "/froyo_results?flavor=strawberry&toppings=nuts"
    )

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = (
        "You ordered strawberry flavored Fro-Yo with toppings nuts!"
    )
    assert expected_page_text == result_page_text


def test_froyo_results_scenario2():
    """Test that the froyo_results page shows vanilla and cookies."""
    result = app.test_client().get(
        "/froyo_results?flavor=vanilla&toppings=cookies"
    )

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = (
        "You ordered vanilla flavored Fro-Yo with toppings cookies!"
    )
    assert expected_page_text == result_page_text


def test_froyo_results_edgecase1():
    """Test that the froyo_results handles and edgecase."""
    result = app.test_client().get("/froyo_results?flavor=mint")

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "You ordered mint flavored Fro-Yo!"
    assert expected_page_text == result_page_text


def test_froyo_results_edgecase2():
    """Test that the froyo_results handles and edgecase with no input."""
    result = app.test_client().get("/froyo_results")

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "We didn't receive your order."
    assert expected_page_text == result_page_text


#######################
# Reverse Message Tests
#######################


def test_message_results_helloworld():
    r"""Test that the message_results shows \"dlroW olleH\"."""
    form_data = {"message": "Hello World"}
    res = app.test_client().post("/message_results", data=form_data)

    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert "dlroW olleH" in result_page_text


def test_message_results_dlrowolleh():
    r"""Test that the message_results shows \"Hello World\"."""
    form_data = {"message": "dlroW olleH"}
    res = app.test_client().post("/message_results", data=form_data)

    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert "Hello World" in result_page_text


def test_message_results_edgecase1():
    """Test that the message_results handles edgecases."""
    form_data = {"message": ""}
    res = app.test_client().post("/message_results", data=form_data)

    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert "We didn't receive a message." in result_page_text


#######################
# Calculator Tests
#######################


def test_calculator_results_scenario1():
    """Test that the message_results handles add."""
    result = app.test_client().get(
        "/calculator_results?operand1=3&operation=add&operand2=4"
    )

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "Your result is: 7"
    assert expected_page_text in result_page_text


def test_calculator_results_scenario2():
    """Test that the message_results handles subtract."""
    result = app.test_client().get(
        "/calculator_results?operand1=10&operation=subtract&operand2=8"
    )

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "Your result is: 2"
    assert expected_page_text in result_page_text


def test_calculator_results_scenario3():
    """Test that the message_results handles multiply."""
    result = app.test_client().get(
        "/calculator_results?operand1=5&operation=multiply&operand2=5"
    )

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "Your result is: 25"
    assert expected_page_text in result_page_text


def test_calculator_results_scenario4():
    """Test that the message_results handles divide."""
    result = app.test_client().get(
        "/calculator_results?operand1=20&operation=divide&operand2=2"
    )

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "Your result is: 10.0"
    assert expected_page_text in result_page_text


def test_calculator_results_edgecase1():
    """Test that the message_results handles edgecases."""
    result = app.test_client().get(
        "/calculator_results?operand1=fish&operation=add&operand2=4"
    )

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "Please enter a valid number and operation."
    assert expected_page_text in result_page_text


def test_calculator_results_edgecase2():
    """Test that the message_results handles edgecases."""
    result = app.test_client().get(
        "/calculator_results?operand1=fish&operation=a&operand2=4"
    )

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "Please enter a valid number and operation."
    assert expected_page_text in result_page_text
