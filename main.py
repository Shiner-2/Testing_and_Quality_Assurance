def credit_card_decision(age, score):
    if not (0 <= age <= 100) or not (0 <= score <= 1000):
        return "Dữ liệu không hợp lệ"
    if age < 18:
        return "Từ chối mở thẻ"
    if 18 <= age <= 55:
        if score < 500:
            return "Mở thẻ hạn mức thấp"
        elif score < 700:
            return "Mở thẻ hạn mức trung bình"
        else:
            return "Mở thẻ hạn mức cao"
    if 56 <= age <= 100:
        if score < 500:
            return "Từ chối mở thẻ"
        elif score < 700:
            return "Mở thẻ hạn mức thấp"
        else:
            return "Mở thẻ hạn mức trung bình"