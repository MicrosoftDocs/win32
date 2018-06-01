---
Description: Extended OLE DB Properties
ms.assetid: 5da12d1a-7b54-4f2a-8fa7-cea9927238f3
title: Extended OLE DB Properties
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Extended OLE DB Properties

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Indexing Service defines a number of properties for use with the [**ICommand**](https://msdn.microsoft.com/windows/desktop/089427ad-5ba3-4613-b89e-8e86420ccc30) interface that can be used to customize queries. These properties are specific to Indexing Service and might not apply to other OLE DB providers.

These extended properties are set using OLE DB's [**ICommandProperties**](https://msdn.microsoft.com/windows/desktop/cfda4b13-b99f-4b66-ad2b-bd9584c8b3ef) interface. The properties must be set before a query is executed to have an effect on the query.

This section describes the following properties.

-   [**DBPROP\_CI\_CATALOG\_NAME**](dbprop-ci-catalog-name.md)
-   [**DBPROP\_CI\_INCLUDE\_SCOPES**](dbprop-ci-include-scopes.md)
-   [**DBPROP\_CI\_SCOPE\_FLAGS**](dbprop-ci-scope-flags.md)
-   [**DBPROP\_DEFERNONINDEXEDTRIMMING**](dbprop-defernonindexedtrimming.md)
-   [**DBPROP\_MACHINE**](dbprop-machine.md)
-   [**DBPROP\_USECONTENTINDEX**](dbprop-usecontentindex.md)
-   [**DBPROP\_USEEXTENDEDDBTYPES**](dbprop-useextendeddbtypes.md)

 

 



