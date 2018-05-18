---
title: HTTPMAILGET structure
description: Contains the response information for the CommandGET method.
ms.assetid: 'f2332915-a767-493d-bdac-fb4e5cae8608'
keywords: ["HTTPMAILGET structure Windows Mail (formerly Outlook Express)", "LPHTTPMAILGET structure pointer Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- HTTPMAILGET
api_location:
- Imnxport.h
api_type:
- HeaderDef
---

# HTTPMAILGET structure

\[**HTTPMAILGET** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains the response information for the [**CommandGET**](oe-ihttpmailtransport-commandget.md) method.

## Syntax


```C++
typedef struct tagHTTPMAILGET {
  BOOL   fTotalKnown;
  DWORD  cbIncrement;
  DWORD  cbCurrent;
  DWORD  cbTotal;
  LPVOID pvBody;
  LPSTR  pszContentType;
} HTTPMAILGET, *LPHTTPMAILGET;
```



## Members

<dl> <dt>

**fTotalKnown**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Contains a **BOOL** that indicates whether the server provided an HTTP content-length header. When this parameter is **TRUE**, **cbTotal** contains the response size.

</dd> <dt>

**cbIncrement**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that contains the number of bytes downloaded since the last time this method was called.

</dd> <dt>

**cbCurrent**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that contains the total number of bytes downloaded for this response so far.

</dd> <dt>

**cbTotal**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains a **DWORD** that contains the size in bytes of the entire response when **fTotalKnown** is **TRUE**.

</dd> <dt>

**pvBody**
</dt> <dd>

Type: **LPVOID**

</dd> <dd>

Contains an **LPVOID** that contains the downloaded data.

</dd> <dt>

**pszContentType**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPSTR** that contains the content type, for example, text/html.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





