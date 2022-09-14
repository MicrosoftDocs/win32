---
title: Query Interfaces
description: Three types of ADSI interfaces can be used to perform directory searches. The application environment and other requirements may indicate which interface is used.
ms.assetid: 42843e02-b685-492e-9046-aea460e84584
ms.tgt_platform: multiple
keywords:
- Query Interfaces ADSI
- Queries ADSI , Query Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Query Interfaces

Three types of ADSI interfaces can be used to perform directory searches. The application environment and other requirements may indicate which interface is used.

-   [**IDirectorySearch**](/windows/desktop/api/Iads/nn-iads-idirectorysearch). **IDirectorySearch** is a basic COM interface only available to C/C++ programmers. For more information, see [Searching With the IDirectorySearch Interface](searching-with-idirectorysearch.md).
-   ADO. The ActiveX Data Object (ADO) interfaces are Automation interfaces that use OLE DB. Use ADO for queries within applications that rely on Automation. These include Visual Basic applications, Active Server Pages, and so on. For more information, see [Searching with ActiveX Data Objects](searching-with-activex-data-objects-ado.md).
-   OLE DB. OLE DB is a set of C/C++ interfaces used to query databases. By supporting these interfaces, ADSI providers can implement advanced OLE DB features, such as distributed queries with other OLE DB providers. For more information, see [Searching with OLE DB](searching-with-ole-db.md).

 

 




