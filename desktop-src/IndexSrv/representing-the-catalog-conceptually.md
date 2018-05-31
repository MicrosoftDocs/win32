---
title: Representing the Catalog Conceptually
description: Representing the Catalog Conceptually
ms.assetid: 3a358862-1422-40cc-a265-7f33c9c3051a
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Representing the Catalog Conceptually

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The result of indexing is a catalog that conceptually consists of a logical "table" of properties with the text or value and locale stored in columns of the table. A text-type property entry also has a location in the document stored with the text and locale. Each row of the table corresponds to a separate document in the scope of the catalog. The following table shows how the results for the example document from the topic [Property Filtering](property-filtering.md) would appear as a row in the table. (The following table does not show columns for the locale or the location in the document.)



| Document Name         | Contents                                                                                                                                     | Chapter                                                                      |                                    | DocTitle                | Book                    |              |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|------------------------------------|-------------------------|-------------------------|--------------|
|                       | *Text-Type Properties*<br/>                                                                                                            |                                                                              | *Value-Type Properties*<br/> |                         |                         |              |
|  <br/>          |  <br/>                                                                                                                                 |  <br/>                                                                 |  <br/>                       |  <br/>            |  <br/>            |  <br/> |
| stormy.xyz<br/> | detective<br/> exclaimed<br/> fini<br/> minutes<br/> room<br/> silent<br/> small<br/>  <br/> | A Scream<br/> Confessions<br/> The Knife<br/>  <br/> |  <br/>                       | Stormy Night<br/> | Stormy Night<br/> |  <br/> |
|  <br/>          |  <br/>                                                                                                                                 |  <br/>                                                                 |  <br/>                       |  <br/>            |  <br/>            |  <br/> |



 

It is important to note that entries for the value-type properties are single-valued and correspond to the last-set value of each property. Entries in the text-type properties can be, and usually are, multi-valued. Note that in this context, vectors and arrays (data types **VT\_VECTOR** and **VT\_ARRAY**) are considered to be single-valued quantities.

 

 





