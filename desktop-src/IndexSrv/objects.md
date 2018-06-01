---
title: Objects
description: Indexing Service provides three categories of objects.
ms.assetid: 434d8b9a-03a8-4e91-b6ff-c692f77b342d
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Objects

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Indexing Service provides three categories of objects. The first two categories are used in scripting languages, such as Microsoft Visual Basic, Scripting Edition (VBScript) and Microsoft JScript, or any programming language that supports automation, to automate and manage Indexing Service. The third category of objects is used by language resources, such as word breakers and stemmers.

Indexing Service provides the following categories of objects:

-   [Indexing Service Administration Automation Objects](#indexing-service-administration-automation-objects)
-   [Indexing Service Query Automation Objects](#indexing-service-query-automation-objects)
-   [Indexing Service Language Resource Objects](#indexing-service-language-resource-objects)

### Indexing Service Administration Automation Objects

The Indexing Service Administration Automation Objects contained in Ciodm.dll provide ways to manage Indexing Service.



| Object name          | Interface                                      | Description                                                                                                                  |
|----------------------|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| **AdminIndexServer** | [**IAdminIndexServer**](iadminindexserver.md) | Manages Indexing Service. Allows access to all the functionality provided by the Microsoft Management Console (MMC) snap-in. |
| **CatAdm**           | [**ICatAdm**](icatadm.md)                     | Manages the collection of scopes for a catalog.                                                                              |
| **ScopeAdm**         | [**IScopeAdm**](iscopeadm.md)                 | Manages an individual scope.                                                                                                 |



 

Indexing Service can be administered in two ways:

-   Manually, by using the Indexing Service Management snap-in, which is accessible by clicking the right-mouse button on the **My Computer** icon on the desktop. **Manage** opens the **Computer Management** console. Choose **Server Applications and Services\\Indexing Service** on **Local** computer.
-   Programmatically, by writing applications or scripts to administer Indexing Service components with the Indexing Service Administration Automation Objects.

Examples showing how Indexing Service components can be managed using the administration, catalog, and scope objects that can be found in the mssdk\\samples\\internet\\index\\VBAdmin sample code.

### Indexing Service Query Automation Objects

The Indexing Service Query Automation Objects in Ixsso.dll give script writers control over creating and managing queries and the resultant record sets. Originally designed to integrate Indexing Service with Active Server Pages (ASP) on the web server, these objects can also be used by client-side scripts, server-side scripts , Microsoft Windows Script Host (CScript.exe, WScript.exe), and any automation-enabled language.

These objects include:



| Object name | Interface                          | Description                                                          |
|-------------|------------------------------------|----------------------------------------------------------------------|
| **Query**   | [**IixssoQuery**](iixssoquery.md) | Manages the query definition and result-set creation and navigation. |
| **Utility** | [**IixssoUtil**](iixssoutil.md)   | Helpful utilities for managing the queries and result sets.          |



 

Examples showing how queries can be created with these objects can be found in the Platform Software Development Kit (SDK) mssdk\\samples\\internet\\index\\vbquery directory.

### Indexing Service Language Resource Objects

The Indexing Service Language Resource Objects defined in uuid.lib are used by language resource components, such as word breakers and stemmers, during the creation and querying of an index.

These objects are described in the following table.



| Object name      | Interface                              | Description                       |
|------------------|----------------------------------------|-----------------------------------|
| **PhraseSink**   | [**IPhraseSink**](/windows/desktop/api/Indexsrv/nn-indexsrv-iphrasesink)     | Phrase sink used by word breakers |
| **WordFormSink** | [**IWordFormSink**](https://www.bing.com/search?q=**IWordFormSink**) | Stem sink used by stemmers        |
| **WordSink**     | [**IWordSink**](https://www.bing.com/search?q=**IWordSink**)iix      | Word sink used by word breakers   |



 

For an example of how these objects are used in querying and creating an index, see the language resources sample.

 

 




