---
description: The following administrative functions enable a network provider to take network-specific action to display and manipulate network-specific directories, in other words, directories mapped to non-Windows protocols.
ms.assetid: df2f1bd6-5257-46e4-a4d4-ad2f5c0a1517
title: Administrative Functions
ms.topic: article
ms.date: 05/31/2018
---

# Administrative Functions

The following administrative functions enable a network provider to take network-specific action to display and manipulate network-specific directories, in other words, directories mapped to non-Windows protocols.



| Function                                         | Description                                                                                                                                                   |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**NPGetDirectoryType**](/windows/desktop/api/Npapi/nf-npapi-npgetdirectorytype) | Called by File Manager to determine the type of a network directory.                                                                                          |
| [**NPDirectoryNotify**](/windows/desktop/api/Npapi/nf-npapi-npdirectorynotify)   | Called by File Manager to notify the network provider of directory operations. This function can be used to perform special behavior for certain directories. |



 

 

 



