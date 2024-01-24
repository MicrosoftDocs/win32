---
description: Tokens are written as little-endian WORDs. The following list of token values is divided into record-bearing and stand-alone tokens.
ms.assetid: 'vs|directx_sdk|~\tokens.htm'
title: Tokens
ms.topic: article
ms.date: 05/31/2018
---

# Tokens

Tokens are written as little-endian WORDs. The following list of token values is divided into record-bearing and stand-alone tokens.

The record-bearing tokens are defined as follows.


```
#define TOKEN_NAME         1
#define TOKEN_STRING       2
#define TOKEN_INTEGER      3
#define TOKEN_GUID         5
#define TOKEN_INTEGER_LIST 6
#define TOKEN_FLOAT_LIST   7
```



The stand-alone tokens are defined as follows.


```
#define TOKEN_OBRACE      10
#define TOKEN_CBRACE      11
#define TOKEN_OPAREN      12
#define TOKEN_CPAREN      13
#define TOKEN_OBRACKET    14
#define TOKEN_CBRACKET    15
#define TOKEN_OANGLE      16
#define TOKEN_CANGLE      17
#define TOKEN_DOT         18
#define TOKEN_COMMA       19
#define TOKEN_SEMICOLON   20
#define TOKEN_TEMPLATE    31
#define TOKEN_WORD        40
#define TOKEN_DWORD       41
#define TOKEN_FLOAT       42
#define TOKEN_DOUBLE      43
#define TOKEN_CHAR        44
#define TOKEN_UCHAR       45
#define TOKEN_SWORD       46
#define TOKEN_SDWORD      47
#define TOKEN_VOID        48
#define TOKEN_LPSTR       49
#define TOKEN_UNICODE     50
#define TOKEN_CSTRING     51
#define TOKEN_ARRAY       52
```



## Related topics

<dl> <dt>

[Binary Encoding](binary-encoding.md)
</dt> </dl>

 

 



