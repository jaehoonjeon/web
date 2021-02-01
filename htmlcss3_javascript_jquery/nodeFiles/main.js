//모듈을 추출합니다.
const http = require("http")

//서버를 생성하고 실행합니다.
const server = http.createServer((request, response) => {
    //요청 정보 확인
    console.log(request.method) //GET POST
    console.log(request.url)    //URL
    console.log()

    if(request.url === "/hello"){
        //응답 방법
        response.writeHead(200, {
            "Content-Type": "text/html"
        })
        response.write("<meta charset='utf-8'/><h1>안녕하세요</h1>")
        response.end()
    }else{
        //응답 방법
        response.writeHead(200, {
            "Content-Type": "text/html"
        })
        response.write("<h1>Hello World</h1>")
        response.end()
    }
})

server.listen(52273, () => {
    console.log("Server Runnig at http://127.0.0.1:52273")
})