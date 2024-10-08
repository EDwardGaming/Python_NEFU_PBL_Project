# 刷题题库URL配置

## API接口

POST `http://localhost:8060/adapter-service/search`

## 参数

#### URL 请求参数

| 参数         | 描述                                          | 是否必须 | 示例值                           | Token获取方式                                         |
| ------------ | --------------------------------------------- | -------- | -------------------------------- | ----------------------------------------------------- |
| use          | 你想要使用哪些题库,不填写默认使用所有免费题库 | 否       | local,icodef,buguake,wanneng     |                                                       |
| wannengToken | 万能付费题库的Token值(10位)                   | 否       | E196FD8B49                       | https://lyck6.cn/pay                                  |
| icodefToken  | Icodef 题库Token值                            | 否       | UafYcHViJMGzSVNh                 | 关注微信公众号"一之哥哥"发送"token"获取               |
| enncyToken   | enncy 题库Token值                             | 否       | a21ae2403b414b94b512736c30c69940 | [https://tk.enncy.cn](https://tk.enncy.cn/)           |
| aidianYToken | 爱点题库(亿级题库API)Token值                  | 否       | cvor7f3HxZ7nF2M3ljmA             | [https://www.51aidian.com](https://www.51aidian.com/) |
| lemonToken   | 柠檬题库 Token值                              | 否       | 8a3debe92e2ba83d6786e186bef2a424 | [https://www.lemtk.xyz](https://www.lemtk.xyz/)       |

http://localhost:8060/adapter-service/search?use=wanneng,icodef&icodefToken=84yqJngi6f6Qrs2D

## 使用延溪题库URL配置：

Token：cb1df7db180a45c7b948c4e45b358732

```http
http://localhost:8060/adapter-service/search?use=enncy&enncyToken=cb1df7db180a45c7b948c4e45b358732
```

## Icodef题库URL配置:

Token：84yqJngi6f6Qrs2D

```http
http://localhost:8060/adapter-service/search?use=icodef&icodefToken=84yqJngi6f6Qrs2D
```

## 爱点题库URL配置:

Token:eIjtWCP8Kx54DiQ6Z10E

```http
http://localhost:8060/adapter-service/search?use=aidianY&aidianYToken=eIjtWCP8Kx54DiQ6Z10E
```

## 合体

```http
http://localhost:8060/adapter-service/search?use=enncy,icodef,aidianY&enncyToken=cb1df7db180a45c7b948c4e45b358732,icodefToken=84yqJngi6f6Qrs2D,aidianYToken=eIjtWCP8Kx54DiQ6Z10E
```

fff
