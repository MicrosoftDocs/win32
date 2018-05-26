---
title: Support for Queries
description: By implementing the IDirectorySearch interface, ADSI providers gain access to a subset of OLE DB read-only features.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 73ebed18-0e56-4902-a229-3b03f9be1cf6
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Support for Queries ADSI
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Support for Queries

By implementing the [**IDirectorySearch**](/windows/win32/Iads/nn-iads-idirectorysearch?branch=master) interface, ADSI providers gain access to a subset of OLE DB read-only features.

The ADSI implementation of the methods of [**IDirectorySearch**](/windows/win32/Iads/nn-iads-idirectorysearch?branch=master) itself uses the OLE DB interfaces described in ADSI Version 1.0, including the following list of COM objects:

-   Data Source Object (the directory service), supporting **IDBInitialize**, **IDBCreateSession**, **IDBProperties**, and **IPersist**.
-   DBSessions Object, supporting **IOpenRowSet**, **ISessionProperties**, and **ICreateCommand**.
-   Command Object, supporting **ICommand**, **IAccessor**, **IColumnsInfo**, **ICommandProperties**, **ICommandText**, and **IConvertType**.
-   Rowset Object, supporting **IAccessor**, **IColumnsInfo**, **IConvertType**, **IRowset**, and **IRowsetInfo**.

For more information about OLE DB, see the OLE DB Programmer's Reference in the Platform Software Development Kit (SDK).

 

 




