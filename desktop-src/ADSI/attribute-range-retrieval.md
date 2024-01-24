---
title: Attribute Range Retrieval
description: A multi-valued attribute can have almost any number of values. In many cases, it may be advantageous, or even necessary, to limit the range of values that are retrieved by a query.
ms.assetid: 3a0eb764-fca9-4ca6-9991-b85f293961af
ms.tgt_platform: multiple
keywords:
- Attribute Range Retrieval ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Attribute Range Retrieval

A multi-valued attribute can have almost any number of values. In many cases, it may be advantageous, or even necessary, to limit the range of values that are retrieved by a query.

Range retrieval involves requesting a limited number of attribute values in a single query. The number of values requested must be less than, or equal to, the maximum number of values supported by the server. To reduce the number of times the query must contact the server, the number of values requested should be as close to this maximum as possible. To enable an application to work correctly with all Windows servers, a maximum number of 1000 should be used.

The range specifiers for a property query require the following form:


```C++
range=<low range>-<high range>
```



where "&lt;low range&gt;" is the zero-based index of the first property value to retrieve and "&lt;high range&gt;" is the zero-based index of the last property value to retrieve. Zero is used for "&lt;low range&gt;" to specify the first entry. The wildcard character (\*) can be used for "&lt;high range&gt;" to specify all remaining entries.

The following table lists examples of range specifiers.



| Example      | Description                                                                                   |
|--------------|-----------------------------------------------------------------------------------------------|
| range=0-\*   | Retrieve all property values. This is subject to limits imposed by the server.                |
| range=0-500  | Retrieve from 1st to 501st values inclusively.                                                |
| range=2-3    | Retrieve 3rd and 4th values.                                                                  |
| range=501-\* | Retrieve the 502nd and all remaining values. This is subject to limits imposed by the server. |



 

There are several different ways to retrieve a range of property values. The [**IADs.GetInfoEx**](/windows/desktop/api/Iads/nf-iads-iads-getinfoex) method can be used in either an automation language or C++. The **IADs.GetInfoEx** method is the preferred method of performing range retrieval. For more information about using **IADs.GetInfoEx** for range retrieval, see [Using IADs::GetInfoEx for Range Retrieval](using-iads--getinfoex-for-range-retrieval.md).

If an automation language is used, the ActiveX Directory Objects (ADO) can be used to retrieve a range of property values. For more information about using ADO for range retrieval, see [Using ADO for Range Retrieval](using-ado-for-range-retrieval.md).

If C++ is used, the [**IDirectorySearch**](/windows/desktop/api/Iads/nn-iads-idirectorysearch) and [**IDirectoryObject**](/windows/desktop/api/Iads/nn-iads-idirectoryobject) interfaces can be used to retrieve a range of property values. For more information about using **IDirectorySearch** and **IDirectoryObject** for range retrieval, see [Using IDirectorySearch and IDirectoryObject for Range Retrieval](using-idirectorysearch-and-idirectoryobject-for-range-retrieval.md).  This type of retrieval should be done on queries with a scope type of Base (ADS_SCOPE_BASE).

 

 




