---
title: IIMAPTransport Capability method
description: Returns a value that indicates the capabilities of the Internet Message Access Protocol (IMAP) server.
ms.assetid: 4fc521fd-3e8a-4b90-be7e-efa7e53bcc98
keywords:
- Capability method Windows Mail (formerly Outlook Express)
- Capability method Windows Mail (formerly Outlook Express) , IIMAPTransport interface
- IIMAPTransport interface Windows Mail (formerly Outlook Express) , Capability method
topic_type:
- apiref
api_name:
- IIMAPTransport.Capability
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

# IIMAPTransport::Capability method

\[**IIMAPTransport::Capability** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a value that indicates the capabilities of the Internet Message Access Protocol (IMAP) server.

## Syntax


```C++
HRESULT Capability(
  [out] DWORD *pdwCapabilityFlags
);
```



## Parameters

<dl> <dt>

*pdwCapabilityFlags* \[out\]
</dt> <dd>

Type: **DWORD\***

Receives a **DWORD** that indicates which capabilities the IMAP server supports. The result may be one or more of the following values.



| Value                                                                                                                                                                                                                                                                                                          | Meaning                                                                                   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| <span id="IMAP_CAPABILITY_IMAP4"></span><span id="imap_capability_imap4"></span><dl> <dt>**IMAP\_CAPABILITY\_IMAP4**</dt> <dt>0x00000001</dt> </dl>                                                         | Indicates that the server supports the original IMAP4 protocol. <br/>               |
| <span id="IMAP_CAPABILITY_IMAP4rev1"></span><span id="imap_capability_imap4rev1"></span><span id="IMAP_CAPABILITY_IMAP4REV1"></span><dl> <dt>**IMAP\_CAPABILITY\_IMAP4rev1**</dt> <dt>0x00000002</dt> </dl> | Indicates that the server supports the updated version of the IMAP4 protocol. <br/> |
| <span id="IMAP_CAPABILITY_IDLE"></span><span id="imap_capability_idle"></span><dl> <dt>**IMAP\_CAPABILITY\_IDLE**</dt> <dt>0x00000004</dt> </dl>                                                            | Indicate that the server supports real-time updates through the IDLE command. <br/> |
| <span id="IMAP_CAPABILITY_ALLFLAGS"></span><span id="imap_capability_allflags"></span><dl> <dt>**IMAP\_CAPABILITY\_ALLFLAGS**</dt> <dt>0x00000007</dt> </dl>                                                | Indicates that all three capabilities are supported by the server. <br/>            |



 

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                     | Description                                             |
|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                            | Indicates success. <br/>                          |
| <dl> <dt>**IXP\_E\_IMAP\_IMPROPER\_SVRSTATE**</dt> </dl> | Indicates that the server is not connected. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





