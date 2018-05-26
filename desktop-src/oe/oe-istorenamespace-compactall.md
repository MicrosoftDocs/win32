---
title: IStoreNamespace CompactAll method
description: Compacts the contents of all message folders.
ms.assetid: e61c0e69-65aa-4ce7-929a-7f75f090d042
keywords:
- CompactAll method Windows Mail (formerly Outlook Express)
- CompactAll method Windows Mail (formerly Outlook Express) , IStoreNamespace interface
- IStoreNamespace interface Windows Mail (formerly Outlook Express) , CompactAll method
topic_type:
- apiref
api_name:
- IStoreNamespace.CompactAll
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

# IStoreNamespace::CompactAll method

Compacts the contents of all message folders.

## Syntax


```C++
HRESULT CompactAll(
  [in] DWORD dwReserved
);
```



## Parameters

<dl> <dt>

*dwReserved* \[in\]
</dt> <dd>

Type: **DWORD**

Reserved value. Must be 0 or 1. If the value is 0, the user will be presented with a UI if the compacting operation fails. If the value is 1, the user will not be shown the UI if the compacting operation fails.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns S\_OK if successful, or one of the following error values.



| Return code                                                                                                  | Description                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                 | The value of *dwReserved* is not 0 or 1.<br/>                                                                                                        |
| <dl> <dt>**MSOEAPI\_E\_STORE\_INITIALIZE**</dt> </dl> | The namespace has not been initialized. To initialize the namespace, call [**IStoreNamespace::Initialize**](oe-istorenamespace-initialize.md).<br/> |



 

## Remarks

Messages marked as deleted will be permanently removed when compacted.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





