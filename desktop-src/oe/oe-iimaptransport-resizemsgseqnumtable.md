---
title: IIMAPTransport ResizeMsgSeqNumTable method
description: Resizes the MsgSeqNumToUID table to match the current size of the mailbox.
ms.assetid: '705e3db2-f667-4b27-92d9-34b3213222d5'
keywords: ["ResizeMsgSeqNumTable method Windows Mail (formerly Outlook Express)", "ResizeMsgSeqNumTable method Windows Mail (formerly Outlook Express) , IIMAPTransport interface", "IIMAPTransport interface Windows Mail (formerly Outlook Express) , ResizeMsgSeqNumTable method"]
topic_type:
- apiref
api_name:
- IIMAPTransport.ResizeMsgSeqNumTable
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IIMAPTransport::ResizeMsgSeqNumTable method

\[**IIMAPTransport::ResizeMsgSeqNumTable** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Resizes the MsgSeqNumToUID table to match the current size of the mailbox. Called when an EXISTS response is received from the Internet Message Access Protocol (IMAP) server.

## Syntax


```C++
HRESULT ResizeMsgSeqNumTable(
  [in] DWORD dwSizeOfMbox
);
```



## Parameters

<dl> <dt>

*dwSizeOfMbox* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a **DWORD** that contains the number returned by the EXISTS response. It indicates the number of messages in the mailbox.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                      |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                   |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed. <br/> |



 

## Remarks

The MsgSeqNumToUID table maps message sequence numbers to unique identifiers (UIDs). If the client uses message sequence numbers exclusively to identify messages to the server, then this method is not required.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





