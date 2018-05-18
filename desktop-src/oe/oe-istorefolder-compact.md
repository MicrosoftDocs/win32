---
title: IStoreFolder Compact method
description: Compacts the contents of this folder.
ms.assetid: 'f2736012-b071-43f7-b3f2-7b90ec6529a9'
keywords: ["Compact method Windows Mail (formerly Outlook Express)", "Compact method Windows Mail (formerly Outlook Express) , IStoreFolder interface", "IStoreFolder interface Windows Mail (formerly Outlook Express) , Compact method"]
topic_type:
- apiref
api_name:
- IStoreFolder.Compact
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IStoreFolder::Compact method

Compacts the contents of this folder.

## Syntax


```C++
HRESULT Compact(
  [in] DWORD dwReserved
);
```



## Parameters

<dl> <dt>

*dwReserved* \[in\]
</dt> <dd>

Type: **DWORD**

Reserved value. Must be 0 or 1.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns S\_OK if successful, or the following error value.



| Return code                                                                                  | Description                                         |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The value of *dwReserved* is not 0 or 1.<br/> |



 

## Remarks

If *dwReserved* is 0, the user will be presented with a UI if the compacting operation fails. If *dwReserved* is set to 1, the user will not be shown the UI if the compacting operation fails.

Messages marked as deleted will be permanently removed when compacted.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





