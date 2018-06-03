---
title: Adding Property Sheet Pages
description: When an administrator pulls up a property sheet for the object you are extending, Failover Cluster Administrator calls your implementation of IWEExtendPropertySheet CreatePropertySheetPages.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bb48bdc1-a520-4fcc-943b-520f0c1d52ae
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- property sheets Failover Cluster
- property sheets Failover Cluster ,adding pages
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Adding Property Sheet Pages

\[Support for Failover Cluster Administrator extension DLLs was removed in Windows Server 2008.\]

When an administrator pulls up a property sheet for the object you are extending, [Failover Cluster Administrator](cluster-administrator.md) calls your implementation of [**IWEExtendPropertySheet::CreatePropertySheetPages**](/previous-versions/windows/desktop/api/cluadmex/nf-cluadmex-iweextendpropertysheet-createpropertysheetpages). Your implementation should:

1.  Create the property sheet pages to be added to the property sheet.
2.  Call the Cluster Administrator information interfaces as needed. See [Using the Information Interfaces](using-the-information-interfaces.md).
3.  Call [**IWCPropertySheetCallback::AddPropertySheetPage**](/previous-versions/windows/desktop/api/cluadmex/nf-cluadmex-iwcpropertysheetcallback-addpropertysheetpage) for each page to be added.

 

 




