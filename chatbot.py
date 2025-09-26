# -*- coding: utf-8 -*-
"""
차치업무 도우미 챗봇 - 로직 모듈
키워드 매칭 기반의 간단한 챗봇 구현
"""

import random
from datetime import datetime
from data import (
    WORK_CATEGORIES, GREETING_RESPONSES, DEFAULT_RESPONSES, 
    FAQ_DATA, TIME_GREETINGS, EMERGENCY_KEYWORDS, DEPARTMENT_CONTACTS
)

class SimpleHospitalChatbot:
    """차치업무 도우미 챗봇 클래스"""
    
    def __init__(self):
        """챗봇 초기화"""
        self.conversation_history = []
        self.user_name = None
        print("🏥 차치업무 도우미 챗봇이 시작되었습니다!")
    
    def process_message(self, user_input):
        """
        사용자 입력을 처리하고 응답 생성
        Args:
            user_input (str): 사용자가 입력한 메시지
        Returns:
            dict: 응답 정보가 담긴 딕셔너리
        """
        if not user_input or not user_input.strip():
            return self._format_response("메시지를 입력해주세요.", "오류")
        
        user_input = user_input.lower().strip()
        
        # 대화 기록에 추가
        self.conversation_history.append({
            "user": user_input,
            "timestamp": self._get_current_time()
        })
        
        # 응급상황 우선 처리
        emergency_response = self._check_emergency(user_input)
        if emergency_response:
            return emergency_response
        
        # 1. 인사말 처리
        if self._is_greeting(user_input):
            response = self._get_greeting_response()
            return self._format_response(response, "인사")
        
        # 2. 사용자 이름 설정
        name_response = self._check_name_setting(user_input)
        if name_response:
            return name_response
        
        # 3. FAQ 검색
        faq_response = self._search_faq(user_input)
        if faq_response:
            return self._format_response(faq_response, "FAQ")
        
        # 4. 부서 연락처 검색
        contact_response = self._search_contacts(user_input)
        if contact_response:
            return self._format_response(contact_response, "연락처")
        
        # 5. 카테고리별 키워드 매칭
        category_response = self._match_category(user_input)
        if category_response:
            return category_response
        
        # 6. 기본 응답
        response = random.choice(DEFAULT_RESPONSES)
        return self._format_response(response, "기본")
    
    def _check_emergency(self, text):
        """응급상황 키워드 확인"""
        for keyword, response in EMERGENCY_KEYWORDS.items():
            if keyword in text:
                return self._format_response(
                    f"🚨 {response}", 
                    "응급상황", 
                    priority="HIGH"
                )
        return None
    
    def _is_greeting(self, text):
        """인사말 감지"""
        greetings = ["안녕", "hello", "hi", "반가워", "처음", "시작", "헬로"]
        return any(greeting in text for greeting in greetings)
    
    def _get_greeting_response(self):
        """시간대별 인사말 생성"""
        current_hour = datetime.now().hour
        
        if 6 <= current_hour < 12:
            time_greeting = TIME_GREETINGS["morning"]
        elif 12 <= current_hour < 18:
            time_greeting = TIME_GREETINGS["afternoon"]
        elif 18 <= current_hour < 22:
            time_greeting = TIME_GREETINGS["evening"]
        else:
            time_greeting = TIME_GREETINGS["night"]
        
        base_greeting = random.choice(GREETING_RESPONSES)
        
        if self.user_name:
            return f"{self.user_name}님, {time_greeting} {base_greeting}"
        else:
            return f"{time_greeting} {base_greeting}"
    
    def _check_name_setting(self, text):
        """사용자 이름 설정 확인"""
        # 다양한 이름 설정 패턴 처리
        if "이름" in text:
            # 패턴 1: "제 이름은 김철수입니다"
            if "이름은" in text or "이름는" in text:
                parts = text.split()
                for i, part in enumerate(parts):
                    if "이름은" in part or "이름는" in part:
                        if i + 1 < len(parts):
                            name = parts[i + 1].replace("입니다", "").replace(".", "").replace("예요", "")
                            if name and len(name) <= 10:  # 유효한 이름 길이 체크
                                self.user_name = name
                                return self._format_response(
                                    f"반갑습니다, {name}님! 앞으로 {name}님이라고 부르겠습니다.",
                                    "이름설정"
                                )
            
            # 패턴 2: "김철수라고 불러주세요"
            elif "불러" in text or "부르" in text:
                # 이름 추출 시도
                parts = text.split()
                for part in parts:
                    clean_part = part.replace("라고", "").replace("으로", "").replace("님", "")
                    if clean_part and len(clean_part) <= 10 and clean_part != "이름":
                        self.user_name = clean_part
                        return self._format_response(
                            f"알겠습니다, {clean_part}님! 앞으로 {clean_part}님이라고 부르겠습니다.",
                            "이름설정"
                        )
        
        return None
    
    def _search_faq(self, text):
        """FAQ 검색"""
        for keyword, answer in FAQ_DATA.items():
            if keyword in text:
                return f"📋 {answer}"
        return None
    
    def _search_contacts(self, text):
        """부서 연락처 검색"""
        if "연락처" in text or "번호" in text or "내선" in text:
            for department, contact in DEPARTMENT_CONTACTS.items():
                if department in text:
                    return f"📞 {department}: {contact}"
            
            # 전체 연락처 목록 요청
            if "전체" in text or "모든" in text:
                contact_list = "\n".join([f"{dept}: {num}" for dept, num in DEPARTMENT_CONTACTS.items()])
                return f"📞 부서별 연락처:\n{contact_list}"
        
        return None
    
    def _match_category(self, text):
        """카테고리 키워드 매칭"""
        for category, data in WORK_CATEGORIES.items():
            for keyword in data["keywords"]:
                if keyword in text:
                    response = random.choice(data["responses"])
                    return self._format_response(response, category)
        return None
    
    def _format_response(self, message, category, priority="NORMAL"):
        """응답 포맷팅"""
        return {
            "message": message,
            "category": category,
            "timestamp": self._get_current_time(),
            "priority": priority,
            "conversation_count": len(self.conversation_history)
        }
    
    def _get_current_time(self):
        """현재 시간 반환"""
        return datetime.now().strftime("%H:%M")
    
    def get_conversation_summary(self):
        """대화 요약 정보"""
        if not self.conversation_history:
            return "아직 대화 기록이 없습니다."
        
        total_messages = len(self.conversation_history)
        first_message_time = self.conversation_history[0]["timestamp"]
        last_message_time = self.conversation_history[-1]["timestamp"]
        
        return {
            "총 메시지 수": total_messages,
            "첫 메시지 시간": first_message_time,
            "마지막 메시지 시간": last_message_time,
            "사용자 이름": self.user_name or "미설정"
        }
    
    def get_help_message(self):
        """도움말 메시지"""
        help_text = """
🏥 차치업무 도우미 챗봇 사용법

📋 주요 기능:
• 수리: 의료기기 수리 요청 (DARWIN 시스템)
• 물품: 물품 구매형태 조회, 청구
• 제제약/수액: 소독제, 수액 관련 문의
• 멸균품/거즈: 거즈 공급, 멸균품 청구
• 격리실: VRE, CPE, 음압격리 운영
• ICU전동: ICU 전동 절차 안내
• 임종실: 임종실 입실기준
• 신규백업: 신규 백업 업무 안내

💬 사용 예시:
• "EKG 수리 요청"
• "거즈 공급 언제 되나요?"
• "VRE 격리실 절차"
• "의공기술실 연락처"
• "ICU 전동 방법"

🆘 응급상황:
• "응급", "화재", "코드블루" 등의 키워드 사용
        """
        
        return self._format_response(help_text.strip(), "도움말")

# 챗봇 인스턴스를 전역으로 사용할 수 있도록 생성
chatbot_instance = SimpleHospitalChatbot()

def get_chatbot_response(user_input):
    """
    외부에서 챗봇 응답을 받기 위한 함수
    Args:
        user_input (str): 사용자 입력
    Returns:
        dict: 챗봇 응답
    """
    return chatbot_instance.process_message(user_input)

if __name__ == "__main__":
    # 테스트용 대화형 실행
    print("=" * 50)
    print("🏥 차치업무 도우미 챗봇 테스트")
    print("=" * 50)
    print("종료하려면 'quit' 또는 'exit'를 입력하세요")
    print("도움말을 보려면 'help'를 입력하세요")
    print("-" * 50)
    
    chatbot = SimpleHospitalChatbot()
    
    while True:
        try:
            user_input = input("👤 당신: ").strip()
            
            if user_input.lower() in ['quit', 'exit', '종료', '나가기']:
                print("👋 챗봇을 종료합니다. 수고하셨습니다!")
                break
            
            if user_input.lower() in ['help', '도움말']:
                response = chatbot.get_help_message()
            elif user_input.lower() in ['summary', '요약']:
                summary = chatbot.get_conversation_summary()
                response = {"message": str(summary), "category": "요약"}
            else:
                response = chatbot.process_message(user_input)
            
            print(f"🤖 챗봇: {response['message']}")
            print(f"   [카테고리: {response['category']} | 시간: {response['timestamp']}]")
            print("-" * 50)
            
        except KeyboardInterrupt:
            print("\n👋 챗봇을 종료합니다.")
            break
        except Exception as e:
            print(f"❌ 오류가 발생했습니다: {e}")
