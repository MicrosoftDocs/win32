---
title: ISearchDesktop ExecuteSQLQuery method
description: Takes a pointer to a string that contains a Structured Query Language (SQL) query and its attributes and returns a pointer to the return set.
ms.assetid: df3f473b-0bee-4035-abf8-dbe5249ef0ed
keywords:
- ExecuteSQLQuery method Legacy Windows Environment Features
- ExecuteSQLQuery method Legacy Windows Environment Features , ISearchDesktop interface
- ISearchDesktop interface Legacy Windows Environment Features , ExecuteSQLQuery method
topic_type:
- apiref
api_name:
- ISearchDesktop.ExecuteSQLQuery
api_type:
- COM
ms.topic: article
ms.date: 05/31/2018
api_location: 
---

# ISearchDesktop::ExecuteSQLQuery method

\[Windows Search 2.x is available for use in the operating system specified in the Requirements section. It might be altered or unavailable in later versions. Use the [Windows Search API](https://docs.microsoft.com/windows/desktop/search/-search-reference-entry-page) instead.\]

Takes a pointer to a string that contains a Structured Query Language (SQL) query and its attributes and returns a pointer to the return set.

## Syntax


```C++
HRESULT ExecuteSQLQuery(
  [in]  LPCWSTR *pdwAttributes,
  [in]  LPCWSTR pwszURL,
  [out] ppidUrl *ppidUrl
);
```



## Parameters

<dl> <dt>

*pdwAttributes* \[in\]
</dt> <dd>

Type: **LPCWSTR\***

A string that contains the other attributes for the query.

</dd> <dt>

*pwszURL* \[in\]
</dt> <dd>

Type: **LPCWSTR**

A string that contains the SQL query.

</dd> <dt>

*ppidUrl* \[out\]
</dt> <dd>

Type: **ppidUrl\***

When this method returns successfully, contains a pointer to the returned recordset.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

 

 




