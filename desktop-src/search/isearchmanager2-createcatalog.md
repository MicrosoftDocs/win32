---
description: Creates a new custom catalog in the Windows Search indexer and returns a reference to it.
ms.assetid: 2ADC48B8-87A2-4527-9AA8-9B0BA3A12462
title: ISearchManager2::CreateCatalog method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISearchManager2.CreateCatalog
api_type: 
- COM
api_location: 
- searchapi.h
---

# ISearchManager2::CreateCatalog method

Creates a new custom catalog in the Windows Search indexer and returns a reference to it.

## Syntax


```C++
HRESULT CreateCatalog(
  [in]  LPCWSTR               pszCatalog,
  [out] ISearchCatalogManager **ppCatalogManager
);
```



## Parameters

<dl> <dt>

*pszCatalog* \[in\]
</dt> <dd>

Type: **[**LPCWSTR**](../winprog/windows-data-types.md)**

Name of catalog to create. Can be any name selected by the caller, must contain only standard alphanumeric characters and underscore.

</dd> <dt>

*ppCatalogManager* \[out\]
</dt> <dd>

Type: **[**ISearchCatalogManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcatalogmanager)\*\***

On success a reference to the created catalog is returned as an [**ISearchCatalogManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcatalogmanager) interface pointer. The Release() must be called on this interface after the calling application has finished using it.

</dd> </dl>

## Return value

Type: **HRESULT**

HRESULT indicating status of operation:



| Return code                                                                             | Description                                                                                 |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | Catalog did not previously exist and was created. Reference to catalog returned.<br/> |
| <dl> <dt>**S\_FALSE**</dt> </dl> | Catalog previously existed, reference to catalog returned.<br/>                       |



 

FAILED HRESULT: Failure creating catalog or invalid arguments passed.

## Remarks

Called to create a new catalog in the Windows Search indexer. After creation, the methods on the returned [**ISearchCatalog**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcatalogmanager) manager can be used to add locations to be indexed, monitor indexing process, and construct queries to send to the indexer and get results. See the “Managing the Index” documentation for more info: https://msdn.microsoft.com/library/bb266516(VS.85).aspx

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>           |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**ISearchManager2**](/windows/desktop/api/searchapi/nn-searchapi-isearchmanager2)
</dt> </dl>

 

 
