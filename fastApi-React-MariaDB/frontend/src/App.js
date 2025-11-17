import React, { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  // message라는 state(상태)와 그 값을 바꾸는 setMessage 함수 선언
  // 초기값은 "" 빈 문자열로 선언

  useEffect(() => {
    // 컴포넌트가 화면에 처음 렌더링될 때 한 번 실행되는 Effect를 정의
    // FastAPI 백엔드 호출
    fetch("http://127.0.0.1:8000/hello") // 백엔드의 엔드포인트 설정
      .then((res) => res.json()) // 서버에서 응답이오면 JSON 형태로 변환
      .then((data) => {
              // JSON으로 변환된 데이터를 받아서 실행하는 부분
        setMessage(data.message);
             // data 안에 있는 message 필드를 react 상태 message에 넣음
              // -> 화면이 다시 렌더링 되면서 새로운 메세지가 표시됨
      })
      
      .catch((err) => { // 통신 오류나 JSON 파싱 오류가 나면 이 catch에서 에러를 콘솔에 출력
        console.error("API 호출 오류:", err);
      });
  }, []);
      // 두번째 인자로 빈 배열 []을 넣었기 때문에
      // 이 useEffect는 컴포넌트가 처음 렌더링 될 때 딱 한번만 실행 됨

  return (
    <div style={{ padding: "40px", 
    fontSize: "24px",
    border : "solid 1px"
    }}>
      <h1>React + FastAPI 연동 테스트</h1>
      <p>백엔드에서 온 메시지: {message}</p>
    </div>
  );
}

export default App;
// App 컴포넌트를 default(기본) export(내보내기)해서
// 다른 파일에서 import하여 사용할 수 있게 함