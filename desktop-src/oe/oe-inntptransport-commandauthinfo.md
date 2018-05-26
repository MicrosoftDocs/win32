---
title: INNTPTransport CommandAUTHINFO method
description: Issues an NNTPAUTHINFO command to the server along with the information provided.
ms.assetid: 726d08a1-07f7-42ae-8f8e-abcb59127e11
keywords:
- CommandAUTHINFO method Windows Mail (formerly Outlook Express)
- CommandAUTHINFO method Windows Mail (formerly Outlook Express) , INNTPTransport interface
- INNTPTransport interface Windows Mail (formerly Outlook Express) , CommandAUTHINFO method
topic_type:
- apiref
api_name:
- INNTPTransport.CommandAUTHINFO
api_location:
- Inetcomm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# INNTPTransport::CommandAUTHINFO method

\[**INNTPTransport::CommandAUTHINFO** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Issues an NNTPAUTHINFO command to the server along with the information provided.

## Syntax


```C++
HRESULT CommandAUTHINFO(
  [in] LPNNTPAUTHINFO pAuthInfo
);
```



## Parameters

<dl> <dt>

*pAuthInfo* \[in\]
</dt> <dd>

Type: **LPNNTPAUTHINFO**

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                   |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | An invalid parameter was passed in<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | A memory allocation failed<br/>         |



 

## Remarks

RFC 977 provides the following formats as valid AUTHINFO commands:

-   AUTHINFO USER name\|PASS password
-   AUTHINFO SIMPLE user password

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





