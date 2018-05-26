---
title: IPOP3Transport CommandPASS method
description: Sends the PASS command to the server.
ms.assetid: ce7537ba-1b6b-4739-a9a1-3156aca00648
keywords:
- CommandPASS method Windows Mail (formerly Outlook Express)
- CommandPASS method Windows Mail (formerly Outlook Express) , IPOP3Transport interface
- IPOP3Transport interface Windows Mail (formerly Outlook Express) , CommandPASS method
topic_type:
- apiref
api_name:
- IPOP3Transport.CommandPASS
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

# IPOP3Transport::CommandPASS method

\[**IPOP3Transport::CommandPASS** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sends the PASS command to the server. Usually follows the [**IPOP3Transport::CommandUSER**](oe-ipop3transport-commanduser.md) method.

## Syntax


```C++
HRESULT CommandPASS(
  [in] LPSTR pszPassword
);
```



## Parameters

<dl> <dt>

*pszPassword* \[in\]
</dt> <dd>

Type: **LPSTR**

Specifies an **LPSTR** that contains the user password.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                 | Description                                                                     |
|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                        | Indicates success. <br/>                                                  |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                | Indicates that *pszPassword* is **NULL**. <br/>                           |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>               | Indicates that an attempt to allocate memory failed. <br/>                |
| <dl> <dt>**IXP\_E\_NOT\_INIT**</dt> </dl>            | Indicates that a connection to the server has not been established. <br/> |
| <dl> <dt>**IXP\_E\_BUSY**</dt> </dl>                 | Indicates that the server connection is busy. <br/>                       |
| <dl> <dt>**IXP\_E\_SOCKET\_WRITE\_ERROR**</dt> </dl> | Indicates that a transmission error occurred. <br/>                       |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





