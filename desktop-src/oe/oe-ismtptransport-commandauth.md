---
title: ISMTPTransport CommandAUTH method
description: Sends the AUTH command to the server.
ms.assetid: 'e346f4d2-9b77-4c94-887d-91b278ccf1fc'
keywords: ["CommandAUTH method Windows Mail (formerly Outlook Express)", "CommandAUTH method Windows Mail (formerly Outlook Express) , ISMTPTransport interface", "ISMTPTransport interface Windows Mail (formerly Outlook Express) , CommandAUTH method"]
topic_type:
- apiref
api_name:
- ISMTPTransport.CommandAUTH
api_location:
- Inetcomm.dll
api_type:
- COM
---

# ISMTPTransport::CommandAUTH method

\[**ISMTPTransport::CommandAUTH** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

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



| Return code                                                                                                 | Description                                                        |
|-------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                        | Indicates success. <br/>                                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                | Indicates that *pszAuthType* is **NULL**. <br/>              |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>               | Indicates that an attempt to allocate memory failed. <br/>   |
| <dl> <dt>**IXP\_E\_BUSY**</dt> </dl>                 | Indicates that the server connection is busy. <br/>          |
| <dl> <dt>**IXP\_E\_NOT\_INIT**</dt> </dl>            | Indicates that the transport has not been initialized. <br/> |
| <dl> <dt>**IXP\_E\_SOCKET\_WRITE\_ERROR**</dt> </dl> | Indicates that a transmission error occurred. <br/>          |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





