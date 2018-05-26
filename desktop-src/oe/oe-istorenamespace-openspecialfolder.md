---
title: IStoreNamespace OpenSpecialFolder method
description: Opens one of the special message folders in the namespace inbox, outbox, sent items, deleted items, and draft items. Special folders are preassigned to each namespace, and cannot be renamed, moved, or deleted.
ms.assetid: a1ae35fc-aa95-4dbf-bd60-eff9141ac38b
keywords:
- OpenSpecialFolder method Windows Mail (formerly Outlook Express)
- OpenSpecialFolder method Windows Mail (formerly Outlook Express) , IStoreNamespace interface
- IStoreNamespace interface Windows Mail (formerly Outlook Express) , OpenSpecialFolder method
topic_type:
- apiref
api_name:
- IStoreNamespace.OpenSpecialFolder
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

# IStoreNamespace::OpenSpecialFolder method

Opens one of the special message folders in the namespace: inbox, outbox, sent items, deleted items, and draft items. Special folders are preassigned to each namespace, and cannot be renamed, moved, or deleted.

## Syntax


```C++
HRESULT OpenSpecialFolder(
  [in]  SPECIALFOLDER sfType,
  [in]  DWORD         dwReserved,
  [out] IStoreFolder  **ppFolder
);
```



## Parameters

<dl> <dt>

*sfType* \[in\]
</dt> <dd>

Type: **[**SPECIALFOLDER**](oe-specialfolder.md)**

Identifies the special folder to open. Must be one of the following values:



| Value                                                                                                                                                            | Meaning                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| <span id="FOLDER_INBOX"></span><span id="folder_inbox"></span><dl> <dt>**FOLDER\_INBOX**</dt> </dl>       | Specifies the inbox folder.<br/>           |
| <span id="FOLDER_OUTBOX"></span><span id="folder_outbox"></span><dl> <dt>**FOLDER\_OUTBOX**</dt> </dl>    | Specifies the outbox folder.<br/>          |
| <span id="FOLDER_SENT"></span><span id="folder_sent"></span><dl> <dt>**FOLDER\_SENT**</dt> </dl>          | Specifies the sent message folder.<br/>    |
| <span id="FOLDER_DELETED"></span><span id="folder_deleted"></span><dl> <dt>**FOLDER\_DELETED**</dt> </dl> | Specifies the deleted message folder.<br/> |
| <span id="FOLDER_DRAFT"></span><span id="folder_draft"></span><dl> <dt>**FOLDER\_DRAFT**</dt> </dl>       | Specifies the draft message folder.<br/>   |



 

</dd> <dt>

*dwReserved* \[in\]
</dt> <dd>

Type: **DWORD**

Reserved value. Must be 0.

</dd> <dt>

*ppFolder* \[out\]
</dt> <dd>

Type: **[**IStoreFolder**](oe-istorefolder.md)\*\***

Reference to a pointer that will receive the created [**IStoreFolder**](oe-istorefolder.md) object that represents the opened folder.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns S\_OK if successful, or one of the following error values.



| Return code                                                                                                  | Description                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                 | The value of *dwReserved* is not 0, or *sfType* is not one of the values specified above.<br/>                                                       |
| <dl> <dt>**MSOEAPI\_E\_STORE\_INITIALIZE**</dt> </dl> | The namespace has not been initialized. To initialize the namespace, call [**IStoreNamespace::Initialize**](oe-istorenamespace-initialize.md).<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





