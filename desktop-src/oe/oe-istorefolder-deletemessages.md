---
title: IStoreFolder DeleteMessages method
description: Deletes the specified messages from the folder.
ms.assetid: 5a634c1b-f0eb-4acc-b710-140e534417a0
keywords:
- DeleteMessages method Windows Mail (formerly Outlook Express)
- DeleteMessages method Windows Mail (formerly Outlook Express) , IStoreFolder interface
- IStoreFolder interface Windows Mail (formerly Outlook Express) , DeleteMessages method
topic_type:
- apiref
api_name:
- IStoreFolder.DeleteMessages
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

# IStoreFolder::DeleteMessages method

Deletes the specified messages from the folder.

## Syntax


```C++
HRESULT DeleteMessages(
  [in] LPMESSAGEIDLIST pMsgIdList,
  [in] DWORD           dwReserved,
  [in] IProgressNotify *pProgress
);
```



## Parameters

<dl> <dt>

*pMsgIdList* \[in\]
</dt> <dd>

Type: **LPMESSAGEIDLIST**

Pointer to a [**MESSAGEIDLIST**](oe-messageidlist.md) structure that specifies the messages to be deleted.

</dd> <dt>

*dwReserved* \[in\]
</dt> <dd>

Type: **DWORD**

Reserved value. Must be 0.

</dd> <dt>

*pProgress* \[in\]
</dt> <dd>

Type: **[IProgressNotify](http://msdn.microsoft.com/library/com/htm/cmi_n2p_1b7d.asp)\***

Pointer to an [IProgressNotify](http://msdn.microsoft.com/library/com/htm/cmi_n2p_1b7d.asp) interface that will receive notifications during the deletion process.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns S\_OK if successful, or one of the following error values.



| Return code                                                                                                  | Description                                                                                                                                                                          |
|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                 | Occurs if the value of *dwReserved* is not 0, if *pMsgIdList* is **NULL**, or if the **prgdwMsgId** member value of the structure referenced by *pMsgIdList* is **NULL**.<br/> |
| <dl> <dt>**MSOEAPI\_E\_STORE\_INITIALIZE**</dt> </dl> | The namespace has not been initialized. To initialize the namespace, call [**Initialize**](oe-istorenamespace-initialize.md).<br/>                                            |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





