---
Description: 'This topic identifies what is new or changed in Offline Files in Windows 7 and Windows Server 2008 R2.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'B0EB30FF-6480-4D4B-90BF-15B38CE7CE21'
ms.prod: 'windows-server-dev'
ms.technology: 'offline-files'
ms.tgt_platform: multiple
title: 'What's New in Offline Files, in Windows 7 and Windows Server 2008 R2'
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# What's New in Offline Files, in Windows 7 and Windows Server 2008 R2

This topic identifies what is new or changed in Offline Files in Windows 7 and Windows Server 2008 R2.

## Windows 7 and Windows Server 2008 R2

On Windows Server operating systems beginning with Windows Server 2008 R2, the Offline Files COM API and WMI provider are available only if the [Desktop Experience](http://go.microsoft.com/fwlink/p/?linkid=140788) feature is installed on the server.

Windows 7 and Windows Server 2008 R2 added the following interfaces:

-   [**IOfflineFilesEvents3**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilesevents3)
-   [**IOfflineFilesTransparentCacheInfo**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilestransparentcacheinfo)

Windows 7 and Windows Server 2008 R2 changed the following enumerations:

-   [**OFFLINEFILES\_CONNECT\_STATE**](/previous-versions/windows/desktop/api/CscObj/ne-cscobj-tagofflinefiles_connect_state)
-   [**OFFLINEFILES\_EVENTS**](/previous-versions/windows/desktop/api/CscObj/ne-cscobj-tagofflinefiles_events)

Windows 7 with Service Pack 1 (SP1) and Windows Server 2008 R2 with SP1 added the following interface:

-   [**IOfflineFilesCache2**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilescache2)

Windows 7 with SP1 and Windows Server 2008 R2 with SP1 added the following WMI method:

-   [**Win32\_OfflineFilesCache::RenameItemEx**](win32-offlinefilescache-renameitemex.md)

 

 



