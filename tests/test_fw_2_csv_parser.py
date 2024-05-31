import pytest
from unittest.mock import patch, mock_open


from parser.fw_2_csv_parser import FW2CSVParser

@pytest.fixture
def parser():
    column_names = ["Name", "Age", "City"]
    offsets = [10, 3, 15]
    fixed_width_encoding = "utf-8"
    include_header = True
    delimited_encoding = "utf-8"
    return FW2CSVParser(column_names, offsets, fixed_width_encoding, include_header, delimited_encoding)

def test_init(parser):
    assert parser.column_names == ["Name", "Age", "City"]
    assert parser.offsets == [10, 3, 15]
    assert parser.fixed_width_encoding == "utf-8"
    assert parser.include_header is True
    assert parser.delimited_encoding == "utf-8"

def test_init_value_error():
    with pytest.raises(ValueError):
        FW2CSVParser(["Name"], [10, 3], "utf-8", True, "utf-8")

@patch("builtins.open", new_callable=mock_open, read_data='{"ColumnNames":["Name","Age","City"], "Offsets":[10, 3, 15], "FixedWidthEncoding":"utf-8", "IncludeHeader":"True", "DelimitedEncoding":"utf-8"}')
@patch("os.path.exists", return_value=True)
def test_from_json(mock_exists, mock_open_file):
    parser = FW2CSVParser.from_json("fake_path.json")
    assert parser.column_names == ["Name", "Age", "City"]
    assert parser.offsets == [10, 3, 15]
    assert parser.fixed_width_encoding == "utf-8"
    assert parser.include_header is True
    assert parser.delimited_encoding == "utf-8"

@patch("os.path.exists", return_value=False)
def test_from_json_file_not_found(mock_exists):
    with pytest.raises(FileNotFoundError):
        FW2CSVParser.from_json("fake_path.json")

def test_get_column_offset(parser):
    assert parser.get_column_offset("Name") == 10
    assert parser.get_column_offset("Age") == 3
    assert parser.get_column_offset("City") == 15

def test_get_row_length(parser):
    assert parser.get_row_length() == 28

def test_convert_row_to_fields(parser):
    row_str = "John Doe  023New York       "
    expected_output = ["John Doe", "023", "New York"]
    assert parser.convert_row_to_fields(row_str) == expected_output

def test_convert_row_to_fields_value_error(parser):
    row_str = "John Doe   023New York"
    with pytest.raises(ValueError):
        parser.convert_row_to_fields(row_str)

@patch("builtins.open", new_callable=mock_open, read_data="John Doe  023New York       ")
def test_parse_fw_to_csv(mock_open_file, parser):
    with patch("csv.writer") as mock_csv_writer:
        mock_writer = mock_csv_writer.return_value
        parser.parse_fw_to_csv("input_path.txt", "output_path.csv")
        mock_writer.writerow.assert_any_call(["Name", "Age", "City"])
        mock_writer.writerow.assert_any_call(["John Doe", "023", "New York"])

