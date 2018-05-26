---
title: IStoreFolder MarkMessagesAsRead method
description: Marks a specified list of messages as read or unread.
ms.assetid: e0016e34-6b14-4b9b-8405-1b921b173e7e
keywords:
- MarkMessagesAsRead method Windows Mail (formerly Outlook Express)
- MarkMessagesAsRead method Windows Mail (formerly Outlook Express) , IStoreFolder interface
- IStoreFolder interface Windows Mail (formerly Outlook Express) , MarkMessagesAsRead method
topic_type:
- apiref
api_name:
- IStoreFolder.MarkMessagesAsRead
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

# IStoreFolder::MarkMessagesAsRead method

Marks a specified list of messages as read or unread.

## Syntax


```C++
HRESULT MarkMessagesAsRead(
  [in] BOOL            fRead,
  [in] DWORD           dwReserved,
  [in] LPMESSAGEIDLIST pMsgIdList
);
```



## Parameters

<dl> <dt>

*fRead* \[in\]
</dt> <dd>

Type: **BOOL**

Flag that specifies whether the messages specified by *pMsgIdList* are to be marked as read. If 1, messages will be marked as read. If 0, messages will be marked as unread.

</dd> <dt>

*dwReserved* \[in\]
</dt> <dd>

Type: **DWORD**

Reserved value. Must be 0.

</dd> <dt>

*pMsgIdList* \[in\]
</dt> <dd>

Type: **LPMESSAGEIDLIST**

Pointer to a [**MESSAGEIDLIST**](oe-messageidlist.md) structure that specifies the messages to be marked.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns S\_OK if successful, or the following error value.



| Return code                                                                                  | Description                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Occurs if the value of *dwReserved* is not 0, if *pMsgIdList* is **NULL**, or if the **prgdwMsgId** member value of the structure referenced by *pMsgIdList* is **NULL**.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





