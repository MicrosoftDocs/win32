---
title: IIMAPTransport GetMsgSeqNumToUIDArray method
description: Returns a copy of the MsgSeqNumToUID table in an array.
ms.assetid: eb989090-bca5-48df-8d88-d064b313fc49
keywords:
- GetMsgSeqNumToUIDArray method Windows Mail (formerly Outlook Express)
- GetMsgSeqNumToUIDArray method Windows Mail (formerly Outlook Express) , IIMAPTransport interface
- IIMAPTransport interface Windows Mail (formerly Outlook Express) , GetMsgSeqNumToUIDArray method
topic_type:
- apiref
api_name:
- IIMAPTransport.GetMsgSeqNumToUIDArray
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

# IIMAPTransport::GetMsgSeqNumToUIDArray method

\[**IIMAPTransport::GetMsgSeqNumToUIDArray** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns a copy of the MsgSeqNumToUID table in an array.

## Syntax


```C++
HRESULT GetMsgSeqNumToUIDArray(
  [out] DWORD **ppdwMsgSeqNumToUIDArray,
  [out] DWORD *pdwNumberOfElements
);
```



## Parameters

<dl> <dt>

*ppdwMsgSeqNumToUIDArray* \[out\]
</dt> <dd>

Type: **DWORD\*\***

Receives the address of a pointer to a **DWORD** that contains the MsgSeqNumToUID array. If no array is available or it is empty, the returned pointer value is **NULL**. The client is responsible for freeing this pointer.

</dd> <dt>

*pdwNumberOfElements* \[out\]
</dt> <dd>

Type: **DWORD\***

Receives a pointer to a **DWORD** that contains the size of the MsgSeqNumToUID array.

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

The client may want to call this method when deleting messages from the cache that no longer exist on the server.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





