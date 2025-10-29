import sys
import os
import pytest

# Thêm thư mục cha vào sys.path để import được module main
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from main import credit_card_decision

@pytest.mark.parametrize("age,score,expected", [
    (-101, -110, "Dữ liệu không hợp lệ"),
    (15, 110, "Từ chối mở thẻ"),
    (15, 101, "Từ chối mở thẻ"),
    (20, 490, "Mở thẻ hạn mức thấp"),
    (65, 320, "Từ chối mở thẻ"),
    (-100, -106, "Dữ liệu không hợp lệ"),
    (15, 110, "Từ chối mở thẻ"),
    (20, 403, "Mở thẻ hạn mức thấp"),
    (20, 610, "Mở thẻ hạn mức trung bình"),
    (67, 406, "Từ chối mở thẻ"),
    (67, 610, "Mở thẻ hạn mức thấp"),
    (20, 600, "Mở thẻ hạn mức trung bình"),
    (20, 920, "Mở thẻ hạn mức cao"),
    (67, 601, "Mở thẻ hạn mức thấp"),
    (67, 800, "Mở thẻ hạn mức trung bình"),
])
def test_credit_card_decision(age, score, expected):
    result = credit_card_decision(age, score)
    assert result == expected, f"Input ({age},{score}) => got '{result}', expected '{expected}'"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
