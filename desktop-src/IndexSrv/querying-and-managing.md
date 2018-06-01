---
title: Querying and Managing
description: Querying-related processing occurs when an application submits a request in one of the supported query languages.
ms.assetid: 581bb9b2-e48a-4b59-b14a-1a87748b68e9
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Querying and Managing

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Querying-related processing occurs when an application submits a request in one of the supported query languages. Queries execute based on several entries in the Windows registry. You can manage querying by adjusting the registry entries, selecting the catalogs and scopes, providing locale-specific word breakers and noise-word lists, and directly controlling the state of the [Querying component](querying-component.md).

The following diagram illustrates how the task of managing Indexing Service integrates with the querying process.

![](images/ixarch02.png)

In the diagram, rectangles represent sources and sinks of Indexing Service data, and the ellipse represents a group of Indexing Service processes. A shaded rectangle denotes a Windows data source or sink used by Indexing Service. The solid lines indicate the flow of data in the direction of the arrows. A dotted line indicates a control functionality between processes.

An end user of Indexing Service usually manages querying through the MMC. An application or script can programmatically manage querying using the methods and properties of the Indexing Service [Admin Helper](https://www.bing.com/search?q=Admin Helper) automation objects ([AdminIndexServer](iadminindexserver.md), [CatAdm](icatadm.md), and [ScopeAdm](iscopeadm.md)). These programming elements provide read/write access to Indexing Service [Registry entries](registry-entries.md), provide properties and methods for manipulating catalogs and scopes, and provide methods for changing the state of the [Querying component](querying-component.md). Also, the [ISAPI extensions](https://www.bing.com/search?q=ISAPI extensions) for Indexing Service provide programmatic control of Indexing Service using Internet Data Administration (.ida) files.

 

 




