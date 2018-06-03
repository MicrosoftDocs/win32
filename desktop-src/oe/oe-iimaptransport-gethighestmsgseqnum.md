---
title: IIMAPTransport GetHighestMsgSeqNum method
description: Returns the highest message sequence number in the MsgSeqNumToUID table.
ms.assetid: aae34215-ee0b-4650-8ac2-8e9304e00c6f
keywords:
- GetHighestMsgSeqNum method Windows Mail (formerly Outlook Express)
- GetHighestMsgSeqNum method Windows Mail (formerly Outlook Express) , IIMAPTransport interface
- IIMAPTransport interface Windows Mail (formerly Outlook Express) , GetHighestMsgSeqNum method
topic_type:
- apiref
api_name:
- IIMAPTransport.GetHighestMsgSeqNum
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

# IIMAPTransport::GetHighestMsgSeqNum method

\[**IIMAPTransport::GetHighestMsgSeqNum** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the highest message sequence number in the MsgSeqNumToUID table.

## Syntax


```C++
HRESULT GetHighestMsgSeqNum(
  [out] DWORD *pdwHighestMSN
);
```



## Parameters

<dl> <dt>

*pdwHighestMSN* \[out\]
</dt> <dd>

Type: **DWORD\***

Receives a pointer to a **DWORD** that contains the highest message sequence number in the table.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

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



 

 





