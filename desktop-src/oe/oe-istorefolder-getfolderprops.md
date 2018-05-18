---
title: IStoreFolder GetFolderProps method
description: Gets properties of the folder represented by the interface.
ms.assetid: '53f65ef5-f18a-41d9-81aa-a97ba5ed685c'
keywords: ["GetFolderProps method Windows Mail (formerly Outlook Express)", "GetFolderProps method Windows Mail (formerly Outlook Express) , IStoreFolder interface", "IStoreFolder interface Windows Mail (formerly Outlook Express) , GetFolderProps method"]
topic_type:
- apiref
api_name:
- IStoreFolder.GetFolderProps
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IStoreFolder::GetFolderProps method

Gets properties of the folder represented by the interface.

## Syntax


```C++
HRESULT GetFolderProps(
  [in]      DWORD         dwReserved,
  [in, out] LPFOLDERPROPS pProps
);
```



## Parameters

<dl> <dt>

*dwReserved* \[in\]
</dt> <dd>

Type: **DWORD**

Reserved value. Must be 0.

</dd> <dt>

*pProps* \[in, out\]
</dt> <dd>

Type: **LPFOLDERPROPS**

Pointer to a [**FOLDERPROPS**](oe-folderprops.md) structure that receives the properties.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns S\_OK if successful, or the following error value.



| Return code                                                                                  | Description                                                                        |
|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The *dwReserved* parameter is not 0, or the *pProps* value is **NULL**.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





