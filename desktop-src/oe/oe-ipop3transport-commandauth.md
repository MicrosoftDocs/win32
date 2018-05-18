---
title: IPOP3Transport CommandAUTH method
description: Sends the AUTH command to the server.
ms.assetid: '1c82eed1-dd97-4283-9c06-1f3c2bbf4a33'
keywords: ["CommandAUTH method Windows Mail (formerly Outlook Express)", "CommandAUTH method Windows Mail (formerly Outlook Express) , IPOP3Transport interface", "IPOP3Transport interface Windows Mail (formerly Outlook Express) , CommandAUTH method"]
topic_type:
- apiref
api_name:
- IPOP3Transport.CommandAUTH
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IPOP3Transport::CommandAUTH method

\[**IPOP3Transport::CommandAUTH** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sends the AUTH command to the server.

## Syntax


```C++
HRESULT CommandAUTH(
  [in] LPSTR pszAuthType
);
```



## Parameters

<dl> <dt>

*pszAuthType* \[in\]
</dt> <dd>

Type: **LPSTR**

Specifies an **LPSTR** that contains the SASL authentication mechanism.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                 | Description                                                                     |
|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                        | Indicates success. <br/>                                                  |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                | Indicates that *pszAuthType* is **NULL**. <br/>                           |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>               | Indicates that an attempt to allocate memory failed. <br/>                |
| <dl> <dt>**IXP\_E\_NOT\_INIT**</dt> </dl>            | Indicates that a connection to the server has not been established. <br/> |
| <dl> <dt>**IXP\_E\_BUSY**</dt> </dl>                 | Indicates that the server connection is busy. <br/>                       |
| <dl> <dt>**IXP\_E\_SOCKET\_WRITE\_ERROR**</dt> </dl> | Indicates that a transmission error occurred. <br/>                       |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





