---
title: IIMAPTransport ResetMsgSeqNumToUID method
description: Resets the variables used to maintain the MsgSeqNumToUID table.
ms.assetid: 8268c0a1-88d8-4384-842e-76cd90b70d8b
keywords:
- ResetMsgSeqNumToUID method Windows Mail (formerly Outlook Express)
- ResetMsgSeqNumToUID method Windows Mail (formerly Outlook Express) , IIMAPTransport interface
- IIMAPTransport interface Windows Mail (formerly Outlook Express) , ResetMsgSeqNumToUID method
topic_type:
- apiref
api_name:
- IIMAPTransport.ResetMsgSeqNumToUID
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

# IIMAPTransport::ResetMsgSeqNumToUID method

\[**IIMAPTransport::ResetMsgSeqNumToUID** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Resets the variables used to maintain the MsgSeqNumToUID table. Called automatically whenever the MsgSeqNumToUID table becomes invalid, such as when a new mailbox is selected or the server connect is interrupted.

## Syntax


```C++
HRESULT ResetMsgSeqNumToUID();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The MsgSeqNumToUID table maps message sequence numbers to unique identifiers (UIDs). If the client uses message sequence numbers exclusively to identify messages to the server, then this method is not required.

Because this method is called automatically, it does not normally need to be called by the client.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





