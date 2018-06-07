---
title: Processing a Result Set
description: A result set is returned as a series of rows.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: e0949c1c-a31a-440a-ae10-2934ffeb7128
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Processing a Result Set

A result set is returned as a series of rows. Each row may or may not contain a given attribute. With the OLE DB provider, the result set appears similar to a normal SQL result set. If you use ADO for the query, the [ADODB.Recordset](http://go.microsoft.com/fwlink/p/?linkid=83859) object is used for traversing the result set. [**IDirectorySearch**](/windows/desktop/api/Iads/nn-iads-idirectorysearch) (available only from languages that support vtable bindings) contains members for moving the row cursor and checking property values in a given row. Alternatively, you can use [**IDirectoryObject**](/windows/desktop/api/Iads/nn-iads-idirectoryobject) to get and set properties.

 

 




