---
title: IStoreNamespace GetSubFolderClose method
description: Frees memory associated with a folder enumeration handle.
ms.assetid: eeb06967-136c-4140-889f-974de3c136e2
keywords:
- GetSubFolderClose method Windows Mail (formerly Outlook Express)
- GetSubFolderClose method Windows Mail (formerly Outlook Express) , IStoreNamespace interface
- IStoreNamespace interface Windows Mail (formerly Outlook Express) , GetSubFolderClose method
topic_type:
- apiref
api_name:
- IStoreNamespace.GetSubFolderClose
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

# IStoreNamespace::GetSubFolderClose method

Frees memory associated with a folder enumeration handle.

## Syntax


```C++
HRESULT GetSubFolderClose(
  [in] HENUMSTORE hEnum
);
```



## Parameters

<dl> <dt>

*hEnum* \[in\]
</dt> <dd>

Type: **HENUMSTORE**

Specifies an enumeration handle to close.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns S\_OK if successful, or one of the following error values.



| Return code                                                                                                  | Description                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                 | The value of *hEnum* is invalid.<br/>                                                                                                                |
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



## See also

<dl> <dt>

[**IStoreNamespace**](oe-istorenamespace.md)
</dt> <dt>

**Reference**
</dt> <dt>

[**GetFirstSubFolder**](oe-istorenamespace-getfirstsubfolder.md)
</dt> <dt>

[**GetNextSubFolder**](oe-istorenamespace-getnextsubfolder.md)
</dt> </dl>

 

 





