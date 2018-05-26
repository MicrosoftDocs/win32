---
title: DBPROP\_USECONTENTINDEX
description: DBPROP\_USECONTENTINDEX
ms.assetid: f9ce6ed6-1943-4cf7-ac10-887985b0dd1e
keywords:
- DBPROP_USECONTENTINDEX
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DBPROP\_USECONTENTINDEX

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The DBPROP\_USECONTENTINDEX property controls the use of the index when processing queries.

### Summary



|                  |                         |
|------------------|-------------------------|
| **Property Set** | DBPROPSET\_QUERYEXT     |
| **Property ID**  | DBPROP\_USECONTENTINDEX |
| **Value Type**   | DBTYPE\_BOOL            |
| **Default**      | VARIANT\_FALSE          |



 

### Remarks

If the value is VARIANT\_TRUE, the index is always used to resolve the query, even if the index is not up to date. If the value is VARIANT\_FALSE and the index is not up to date, the query engine may enumerate the file system to process the query.

This setting affects property value queries such as "@size &gt; 1000".

Enumerating the file system can be disk-intensive and slow.

Content queries always use the index and never enumerate, regardless of the setting of this property.

Certain types of queries require DBPROP\_USECONTENTINDEX to be VARIANT\_FALSE to return results, for example "\#filename \*.dl\*". These queries require enumeration and cannot use the index even if the index is up to date.

This property corresponds to the *CiForceUseCi* variable in the [Internet Data Query Files](internet-data-query-files.md) of Indexing Service.

This property corresponds to the *AllowEnumeration* variable in the [**Query**](iixssoquery.md) object of Indexing Service .

 

 




