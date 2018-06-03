---
title: IIMAPTransport RemoveSequenceNum method
description: Removes the specified message sequence number from the MsgSeqNumToUID table.
ms.assetid: 8829f0af-b429-472f-bc2c-6e52c14c35ef
keywords:
- RemoveSequenceNum method Windows Mail (formerly Outlook Express)
- RemoveSequenceNum method Windows Mail (formerly Outlook Express) , IIMAPTransport interface
- IIMAPTransport interface Windows Mail (formerly Outlook Express) , RemoveSequenceNum method
topic_type:
- apiref
api_name:
- IIMAPTransport.RemoveSequenceNum
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

# IIMAPTransport::RemoveSequenceNum method

\[**IIMAPTransport::RemoveSequenceNum** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Removes the specified message sequence number from the MsgSeqNumToUID table. This method also compacts the table so that all message sequence numbers following the deleted one are resequenced. Called when an EXPUNGE response is received from the Internet Message Access Protocol (IMAP) server.

## Syntax


```C++
HRESULT RemoveSequenceNum(
  [in] DWORD dwDeletedMsgSeqNum
);
```



## Parameters

<dl> <dt>

*dwDeletedMsgSeqNum* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a **DWORD** that contains the message sequence number of deleted message.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                            | Description                                                                                                |
|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Indicates success. <br/>                                                                             |
| <dl> <dt>**E\_FAIL**</dt> </dl> | Indicates that *dwDeletedMsgSeqNum* is out of range or the MsgSeqNumToUID table doesn't exist. <br/> |



 

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



 

 





