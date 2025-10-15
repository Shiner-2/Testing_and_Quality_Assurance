import sys
import os
# Thêm thư mục cha vào sys.path để import được module main
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pytest
from main import credit_card_decision

@pytest.mark.parametrize("age,score,expected", [
    (-1, 200, "Dữ liệu không hợp lệ"),
    (10, 400, "Từ chối mở thẻ"),
    (25, 400, "Mở thẻ hạn mức thấp"),
    (30, 600, "Mở thẻ hạn mức trung bình"),
    (45, 900, "Mở thẻ hạn mức cao"),
    (60, 400, "Từ chối mở thẻ"),
    (70, 600, "Mở thẻ hạn mức thấp"),
    (80, 900, "Mở thẻ hạn mức trung bình"),
])
def test_credit_card_decision(age, score, expected):
    assert credit_card_decision(age, score) == expected


if __name__ == "__main__":
    # Chạy test với pytest khi file được execute trực tiếp
    pytest.main([__file__, "-v"])
    
