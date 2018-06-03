---
title: ICatalogRead GetLinkedAsset method
description: method GetLinkedAsset - returns a data stream containing the requested asset.
ms.assetid: f25ae42a-9287-4c24-beef-db124d22d7bc
keywords:
- GetLinkedAsset method HelpAPI
- GetLinkedAsset method HelpAPI , ICatalogRead interface
- ICatalogRead interface HelpAPI , GetLinkedAsset method
topic_type:
- apiref
api_name:
- ICatalogRead.GetLinkedAsset
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ICatalogRead::GetLinkedAsset method

method GetLinkedAsset - returns a data stream containing the requested asset. Asset is identified by its package name and file path within the package within the currently open catalog

## Syntax


```C++
HRESULT GetLinkedAsset(
  [in]          ICatalog *Catalog,
  [in]          BSTR     packageName,
  [in]          BSTR     path,
  [in]          BSTR     locale,
  [out, retval] IUnknown **pRetVal
);
```



## Parameters

<dl> <dt>

*Catalog* \[in\]
</dt> <dd></dd> <dt>

*packageName* \[in\]
</dt> <dd></dd> <dt>

*path* \[in\]
</dt> <dd></dd> <dt>

*locale* \[in\]
</dt> <dd></dd> <dt>

*pRetVal* \[out, retval\]
</dt> <dd></dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



## See also

<dl> <dt>

[**ICatalogRead**](icatalogread.md)
</dt> </dl>

 

 





