---
title: IXPRESULT structure
description: Holds information about a server response or a transport result error.
ms.assetid: 308b841c-7083-4724-a9f3-722741bb7441
keywords:
- IXPRESULT structure Windows Mail (formerly Outlook Express)
- LPIXPRESULT structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- IXPRESULT
api_location:
- Imnxport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# IXPRESULT structure

\[**IXPRESULT** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Holds information about a server response or a transport result error.

## Syntax


```C++
typedef struct tagIXPRESULT {
  HRESULT hrResult;
  LPSTR   pszResponse;
  UINT    uiServerError;
  HRESULT hrServerError;
  DWORD   dwSocketError;
  LPSTR   pszProblem;
} IXPRESULT, *LPIXPRESULT;
```



## Members

<dl> <dt>

**hrResult**
</dt> <dd>

Type: **HRESULT**

</dd> <dd>

Contains the error code from the transport.

</dd> <dt>

**pszResponse**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains the last response from the server.

</dd> <dt>

**uiServerError**
</dt> <dd>

Type: **UINT**

</dd> <dd>

Contains the server-generated error number.

</dd> <dt>

**hrServerError**
</dt> <dd>

Type: **HRESULT**

</dd> <dd>

Contains the associated HRESULT of the server error.

</dd> <dt>

**dwSocketError**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

Contains the socket error.

</dd> <dt>

**pszProblem**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains additional information.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





