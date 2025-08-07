def generate_response(text):
    if "bật đèn" in text:
        return "Tôi sẽ bật đèn cho bạn"
    elif "tắt đèn" in text:
        return "Tôi sẽ tắt đèn"
    else:
        return "Tôi chưa hiểu yêu cầu của bạn"

def parse_intent(text):
    if "bật đèn" in text:
        return "turn_on_light"
    elif "tắt đèn" in text:
        return "turn_off_light"
    return None
