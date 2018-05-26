---
title: IStoreNamespace GetFirstSubFolder method
description: Begins enumeration of the child folders of a specified parent folder and retrieves information about the first result.
ms.assetid: 865f0caf-5146-4ce2-bca0-ce8c4cec0022
keywords:
- GetFirstSubFolder method Windows Mail (formerly Outlook Express)
- GetFirstSubFolder method Windows Mail (formerly Outlook Express) , IStoreNamespace interface
- IStoreNamespace interface Windows Mail (formerly Outlook Express) , GetFirstSubFolder method
topic_type:
- apiref
api_name:
- IStoreNamespace.GetFirstSubFolder
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

# IStoreNamespace::GetFirstSubFolder method

Begins enumeration of the child folders of a specified parent folder and retrieves information about the first result.

## Syntax


```C++
HRESULT GetFirstSubFolder(
  [in]      STOREFOLDERID dwFolderId,
  [in, out] LPFOLDERPROPS pProps,
  [out]     LPHENUMSTORE  phEnum
);
```



## Parameters

<dl> <dt>

*dwFolderId* \[in\]
</dt> <dd>

Type: **STOREFOLDERID**

Specifies the folder at which enumeration will begin. Use **FOLDERID\_ROOT** to enumerate at the top level.

</dd> <dt>

*pProps* \[in, out\]
</dt> <dd>

Type: **LPFOLDERPROPS**

Pointer to a [**FOLDERPROPS**](oe-folderprops.md) structure that receives properties for the first enumerated folder.

</dd> <dt>

*phEnum* \[out\]
</dt> <dd>

Type: **LPHENUMSTORE**

Pointer that receives a handle that allows for further enumeration.

</dd> </dl>

## Return value

Type: **HRESULT**

The function will return S\_OK if there are more folders to enumerate. If there are no folders, the function will return S\_FALSE. If an error occurs, one of the following error codes will be returned.



| Return code                                                                                                  | Description                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                 | The value of *pProps* or *phEnum* is **NULL**.<br/>                                                                                                  |
| <dl> <dt>**MSOEAPI\_E\_STORE\_INITIALIZE**</dt> </dl> | The namespace has not been initialized. To initialize the namespace, call [**IStoreNamespace::Initialize**](oe-istorenamespace-initialize.md).<br/> |



 

## Remarks

This method will begin enumeration on a folder to list the child folders underneath it, but will only return the first result. To continue enumerating folders, call [**IStoreNamespace::GetNextSubFolder**](oe-istorenamespace-getnextsubfolder.md), passing the handle stored in *phEnum* as the first argument.

When you have completed enumerating folders, call [**IStoreNamespace::GetSubFolderClose**](oe-istorenamespace-getsubfolderclose.md) to free memory associated with the enumeration.

The enumeration is not recursive.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**IStoreNamespace**](oe-istorenamespace.md)
</dt> <dt>

**Reference**
</dt> <dt>

[**GetNextSubFolder**](oe-istorenamespace-getnextsubfolder.md)
</dt> <dt>

[**GetSubFolderClose**](oe-istorenamespace-getsubfolderclose.md)
</dt> </dl>

 

 





