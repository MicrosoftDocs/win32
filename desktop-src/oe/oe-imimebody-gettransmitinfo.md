---
title: IMimeBody GetTransmitInfo method
description: Gets information about how the body should be encoded so that it can be transmitted across the Internet.
ms.assetid: 7f7f9249-c3ec-4f72-8220-155e48746596
keywords:
- GetTransmitInfo method Windows Mail (formerly Outlook Express)
- GetTransmitInfo method Windows Mail (formerly Outlook Express) , IMimeBody interface
- IMimeBody interface Windows Mail (formerly Outlook Express) , GetTransmitInfo method
topic_type:
- apiref
api_name:
- IMimeBody.GetTransmitInfo
api_location:
- Inetcomm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMimeBody::GetTransmitInfo method

Gets information about how the body should be encoded so that it can be transmitted across the Internet.

## Syntax


```C++
HRESULT GetTransmitInfo(
  [in, out] LPTRANSMITINFO pTransmitInfo
);
```



## Parameters

<dl> <dt>

*pTransmitInfo* \[in, out\]
</dt> <dd>

Type: **LPTRANSMITINFO**

Receives a pointer to a [**TRANSMITINFO**](oe-transmitinfo.md) structure that contains information about the body.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                 | Description                                                                                                                                                                                                                                |
|-------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                        | Indicates success.<br/>                                                                                                                                                                                                              |
| <dl> <dt>**E\_FAIL**</dt> </dl>                      | Indicates that an unknown error has occurred.<br/>                                                                                                                                                                                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                | Indicates that *pTransmitInfo* is **NULL**. <br/>                                                                                                                                                                                    |
| <dl> <dt>**MIME\_E\_MULTIPART\_NO\_DATA**</dt> </dl> | Indicates that the body has a multipart primary [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp) and getting transmission data on this body type is not supported. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>               | Indicates that an attempt to allocate memory failed.<br/>                                                                                                                                                                            |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





