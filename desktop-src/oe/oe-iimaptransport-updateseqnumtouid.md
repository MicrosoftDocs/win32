---
title: IIMAPTransport UpdateSeqNumToUID method
description: Updates the MsgSeqNumToUID table so that specified message sequence number maps to the specified unique identifier (UID).
ms.assetid: bc4889a5-5cb0-4b7d-ba3f-5188fb018c71
keywords:
- UpdateSeqNumToUID method Windows Mail (formerly Outlook Express)
- UpdateSeqNumToUID method Windows Mail (formerly Outlook Express) , IIMAPTransport interface
- IIMAPTransport interface Windows Mail (formerly Outlook Express) , UpdateSeqNumToUID method
topic_type:
- apiref
api_name:
- IIMAPTransport.UpdateSeqNumToUID
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

# IIMAPTransport::UpdateSeqNumToUID method

\[**IIMAPTransport::UpdateSeqNumToUID** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Updates the MsgSeqNumToUID table so that specified message sequence number maps to the specified unique identifier (UID). Called when a FETCH response returns both a message sequence number and a UID number from the Internet Message Access Protocol (IMAP) server.

## Syntax


```C++
HRESULT UpdateSeqNumToUID(
  [in] DWORD dwMsgSeqNum,
  [in] DWORD dwUID
);
```



## Parameters

<dl> <dt>

*dwMsgSeqNum* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a **DWORD** that contains the message sequence number returned in the FETCH response.

</dd> <dt>

*dwUID* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a **DWORD** that contains the UID for the given message sequence number.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                      |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *dwMsgSeqNum* or *dwUID* is **NULL**. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed. <br/> |



 

## Remarks

The MsgSeqNumToUID table maps message sequence numbers to unique identifiers (UIDs). If the client uses message sequence numbers exclusively to identify messages to the server, then this method is not required.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





