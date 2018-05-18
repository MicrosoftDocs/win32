---
title: HTTPMAILPOST structure
description: Contains the response information for the CommandPOST, CommandPUT, and SendMessage methods.
ms.assetid: 'a0deca93-ed85-4787-9813-2be773ac20d0'
keywords: ["HTTPMAILPOST structure Windows Mail (formerly Outlook Express)", "LPHTTPMAILPOST structure pointer Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- HTTPMAILPOST
api_location:
- Imnxport.h
api_type:
- HeaderDef
---

# HTTPMAILPOST structure

\[**HTTPMAILPOST** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Contains the response information for the [**CommandPOST**](oe-ihttpmailtransport-commandpost.md), [**CommandPUT**](oe-ihttpmailtransport-commandput.md), and [**SendMessage**](oe-ihttpmailtransport-sendmessage.md) methods.

## Syntax


```C++
typedef struct tagHTTPMAILPOST {
  LPSTR pszLocation;
  BOOL  fResend;
  DWORD cbIncrement;
  DWORD cbCurrent;
  DWORD cbTotal;
} HTTPMAILPOST, *LPHTTPMAILPOST;
```



## Members

<dl> <dt>

**pszLocation**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains an **LPCSTR** that contains the URL to the location the entity is stored on the server.

</dd> <dt>

**fResend**
</dt> <dd>

Type: **BOOL**

</dd> <dd>

Contains a **BOOL** that indicates whether the download was restarted since the last time this method was called. If this parameter is **TRUE**, **cbCurrent** was reset to zero.

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

Contains a **DWORD** that contains the size in bytes of the entire response.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





