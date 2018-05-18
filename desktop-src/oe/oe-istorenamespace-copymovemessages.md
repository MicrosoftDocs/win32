---
title: IStoreNamespace CopyMoveMessages method
description: Copies or moves messages from one message folder to another.
ms.assetid: '90ed34a6-0476-4f90-8b4e-9d8441dccf16'
keywords: ["CopyMoveMessages method Windows Mail (formerly Outlook Express)", "CopyMoveMessages method Windows Mail (formerly Outlook Express) , IStoreNamespace interface", "IStoreNamespace interface Windows Mail (formerly Outlook Express) , CopyMoveMessages method"]
topic_type:
- apiref
api_name:
- IStoreNamespace.CopyMoveMessages
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IStoreNamespace::CopyMoveMessages method

Copies or moves messages from one message folder to another.

## Syntax


```C++
HRESULT CopyMoveMessages(
  [in] IStoreFolder    *pSource,
  [in] IStoreFolder    *pDest,
  [in] LPMESSAGEIDLIST pMsgIdList,
  [in] DWORD           dwFlags,
  [in] DWORD           dwFlagsRemove,
  [in] IProgressNotify *pProgress
);
```



## Parameters

<dl> <dt>

*pSource* \[in\]
</dt> <dd>

Type: **[**IStoreFolder**](oe-istorefolder.md)\***

Pointer to an [**IStoreFolder**](oe-istorefolder.md) interface that represents the source folder to move messages from.

</dd> <dt>

*pDest* \[in\]
</dt> <dd>

Type: **[**IStoreFolder**](oe-istorefolder.md)\***

Pointer to an [**IStoreFolder**](oe-istorefolder.md) interface that represents the destination folder to move messages to.

</dd> <dt>

*pMsgIdList* \[in\]
</dt> <dd>

Type: **LPMESSAGEIDLIST**

Pointer to a [**MESSAGEIDLIST**](oe-messageidlist.md) structure that specifies the messages to be moved.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Value that specifies how the messages are to be handled. Set to 0 to leave a copy of each message in the source folder. Set to 1 to delete the source messages after they are copied to the destination folder.

</dd> <dt>

*dwFlagsRemove* \[in\]
</dt> <dd>

Type: **DWORD**

A combination of state flags to clear from the list of messages specified by the *pMsgIdList* parameter. For a list of flags, see [**Message State Flags**](oe-message-state-flags.md).

</dd> <dt>

*pProgress* \[in\]
</dt> <dd>

Type: **[IProgressNotify](http://msdn.microsoft.com/library/com/htm/cmi_n2p_1b7d.asp)\***

Pointer to an [IProgressNotify](http://msdn.microsoft.com/library/com/htm/cmi_n2p_1b7d.asp) interface that will receive notifications during the copy process.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns S\_OK if successful, or one of the following error values.



| Return code                                                                                                  | Description                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                 | The value of *pSource*, *pDest*, or *pMsgIdList* is **NULL**.<br/>                                                                                   |
| <dl> <dt>**MSOEAPI\_E\_STORE\_INITIALIZE**</dt> </dl> | The namespace has not been initialized. To initialize the namespace, call [**IStoreNamespace::Initialize**](oe-istorenamespace-initialize.md).<br/> |



 

## Remarks

To add flags to a list of messages, call the [**SetFlags**](oe-istorefolder-setflags.md) method.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





