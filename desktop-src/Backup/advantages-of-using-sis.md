---
title: Advantages of Using SIS
description: The advantages of using SIS and the SIS backup architecture are the following.
ms.assetid: c72a14a1-92ae-4875-ae73-e277ed2b0c0d
keywords:
- single-instance store (SIS) Backup , advantages
ms.topic: article
ms.date: 05/31/2018
---

# Advantages of Using SIS

The advantages of using SIS and the SIS backup architecture are the following:

-   The connections between the SIS links and the backing files are automatically maintained by the SIS architecture as your backup applications call the SIS backup API functions.
-   The contents of the SIS reparse points are opaque to your backup and restore applications, ensuring that upgrades to the SIS internals will not require a change in the SIS API or your backup and restore applications that call SIS API functions. You need only recompile your application with a new version of the SIS DLL, named Sisbkup.dll.
-   Because SIS is implemented as a file system filter driver, it constantly tracks the connections between the SIS links and the backing files. When the files are backed up and restored, SIS backup ensures that only one instance of the backing file will be backed up and restored, regardless of the number of SIS links that point to it.

 

 




