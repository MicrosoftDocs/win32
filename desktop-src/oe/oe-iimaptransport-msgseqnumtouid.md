---
title: IIMAPTransport MsgSeqNumToUID method
description: Returns the unique identifier (UID) that maps to the specified message sequence number in the MsgSeqNumToUID table.
ms.assetid: f6d0303b-9bd2-49f9-b98e-13c999b0fc29
keywords:
- MsgSeqNumToUID method Windows Mail (formerly Outlook Express)
- MsgSeqNumToUID method Windows Mail (formerly Outlook Express) , IIMAPTransport interface
- IIMAPTransport interface Windows Mail (formerly Outlook Express) , MsgSeqNumToUID method
topic_type:
- apiref
api_name:
- IIMAPTransport.MsgSeqNumToUID
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

# IIMAPTransport::MsgSeqNumToUID method

\[**IIMAPTransport::MsgSeqNumToUID** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the unique identifier (UID) that maps to the specified message sequence number in the MsgSeqNumToUID table.

## Syntax


```C++
HRESULT MsgSeqNumToUID(
  [in]  DWORD dwMsgSeqNum,
  [out] DWORD *pdwUID
);
```



## Parameters

<dl> <dt>

*dwMsgSeqNum* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a **DWORD** that contains the message sequence number.

</dd> <dt>

*pdwUID* \[out\]
</dt> <dd>

Type: **DWORD\***

Receives a pointer to a **DWORD** that contains the UID. Returns zero if no matching UID is found.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                                                         |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                                                                      |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | Indicates that *dwMsgSeqNum* is out of range or the MsgSeqNumToUID table doesn't exist. <br/> |
| <dl> <dt>**OLE\_E\_BLANK**</dt> </dl> | Indicates that there is no matching UID for *dwMsgSeqNum*. <br/>                              |



 

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



 

 





