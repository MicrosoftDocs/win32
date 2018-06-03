---
title: IStoreNamespace GetNextSubFolder method
description: Continues enumeration of folders using a provided handle and retrieves information about the next result.
ms.assetid: 6bd4dc63-41f1-461f-b9e2-2cc9bd9d2f6c
keywords:
- GetNextSubFolder method Windows Mail (formerly Outlook Express)
- GetNextSubFolder method Windows Mail (formerly Outlook Express) , IStoreNamespace interface
- IStoreNamespace interface Windows Mail (formerly Outlook Express) , GetNextSubFolder method
topic_type:
- apiref
api_name:
- IStoreNamespace.GetNextSubFolder
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

# IStoreNamespace::GetNextSubFolder method

Continues enumeration of folders using a provided handle and retrieves information about the next result.

## Syntax


```C++
HRESULT GetNextSubFolder(
  [in]      HENUMSTORE    hEnum,
  [in, out] LPFOLDERPROPS pProps
);
```



## Parameters

<dl> <dt>

*hEnum* \[in\]
</dt> <dd>

Type: **HENUMSTORE**

Handle that specifies an existing enumeration to continue.

</dd> <dt>

*pProps* \[in, out\]
</dt> <dd>

Type: **LPFOLDERPROPS**

Pointer to a [**FOLDERPROPS**](oe-folderprops.md) structure that receives information about the enumerated folder.

</dd> </dl>

## Return value

Type: **HRESULT**

The function will return S\_OK if there are more folders to enumerate. If there are no more folders, the function will return S\_FALSE. If an error occurs, one of the following error codes will be returned.



| Return code                                                                                                  | Description                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                 | The value of *pProps* is **NULL** or *hEnum* is invalid.<br/>                                                                                        |
| <dl> <dt>**MSOEAPI\_E\_STORE\_INITIALIZE**</dt> </dl> | The namespace has not been initialized. To initialize the namespace, call [**IStoreNamespace::Initialize**](oe-istorenamespace-initialize.md).<br/> |



 

## Remarks

The first argument to this method is the handle to an existing enumeration. To get a handle, you must first call [**IStoreNamespace::GetFirstSubFolder**](oe-istorenamespace-getfirstsubfolder.md).

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

[**GetFirstSubFolder**](oe-istorenamespace-getfirstsubfolder.md)
</dt> <dt>

[**GetSubFolderClose**](oe-istorenamespace-getsubfolderclose.md)
</dt> </dl>

 

 





