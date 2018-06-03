---
Description: The following interfaces are used with Offline Files.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9dea396f-ab71-4b2e-b5d3-776c16614f26
ms.prod: windows-server-dev
ms.technology: offline-files
ms.tgt_platform: multiple
title: Offline Files API Interfaces
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Offline Files API Interfaces

The following interfaces are used with Offline Files.

> [!Note]  
> On Windows Server operating systems beginning with Windows Server 2008 R2, the Offline Files COM API and WMI provider are available only if the [Desktop Experience](http://go.microsoft.com/fwlink/p/?linkid=140788) feature is installed on the server.

 



| Interface                                                                      | Description                                                                                                                                                                                        |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IEnumOfflineFilesItems**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-ienumofflinefilesitems)                       | Represents a collection of [**IOfflineFilesItem**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilesitem) interface pointers.                                                                                                      |
| [**IEnumOfflineFilesSettings**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-ienumofflinefilessettings)                 | Enumerates setting objects associated with the Offline Files service.                                                                                                                              |
| [**IOfflineFilesCache**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilescache)                               | Used to manage the Offline Files cache.                                                                                                                                                            |
| [**IOfflineFilesChangeInfo**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefileschangeinfo)                     | Represents the information associated with local changes made to an item while working offline.                                                                                                    |
| [**IOfflineFilesConnectionInfo**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilesconnectioninfo)             | Presents query and action capabilities associated with the online-offline behavior of Offline Files.                                                                                               |
| [**IOfflineFilesDirectoryItem**](/previous-versions/windows/desktop/api/CscObj/)               | Represents a directory item in the Offline Files cache.                                                                                                                                            |
| [**IOfflineFilesDirtyInfo**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilesdirtyinfo)                       | Represents information about an unsynchronized ("dirty") file in the Offline Files cache.                                                                                                          |
| [**IOfflineFilesErrorInfo**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefileserrorinfo)                       | Provides a text description and raw data block associated with an error.                                                                                                                           |
| [**IOfflineFilesEvents**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilesevents)                             | Used to report significant events associated with Offline Files.                                                                                                                                   |
| [**IOfflineFilesEvents2**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilesevents2)                           | Used to report additional events associated with Offline Files.                                                                                                                                    |
| [**IOfflineFilesEvents3**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilesevents3)                           | Used to report events associated with transparently cached items.                                                                                                                                  |
| [**IOfflineFilesEventsFilter**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefileseventsfilter)                 | Provides a mechanism for recipients of published events to restrict the number of event instances they receive.                                                                                    |
| [**IOfflineFilesFileItem**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilesfileitem)                         | Represents a file item in the Offline Files cache.                                                                                                                                                 |
| [**IOfflineFilesFileSysInfo**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilesfilesysinfo)                   | Represents the standard information associated with a file system item in the Offline Files cache.                                                                                                 |
| [**IOfflineFilesGhostInfo**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilesghostinfo)                       | Represents the ghosting status of an item in the Offline Files cache.                                                                                                                              |
| [**IOfflineFilesItem**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilesitem)                                 | Represents a single item in the Offline Files cache.                                                                                                                                               |
| [**IOfflineFilesItemContainer**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilesitemcontainer)               | Used to access item enumeration functionality in the Offline Files cache.                                                                                                                          |
| [**IOfflineFilesItemFilter**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilesitemfilter)                     | Represents an instance of a filter to be applied to an enumeration.                                                                                                                                |
| [**IOfflineFilesPinInfo**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilespininfo)                           | Represents the pinned status of an item in the Offline Files cache.                                                                                                                                |
| [**IOfflineFilesPinInfo2**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilespininfo2)                         | Defines a method to determine whether an item in the Offline Files cache is partly pinned.                                                                                                         |
| [**IOfflineFilesProgress**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilesprogress)                         | Used to report progress back to callers of lengthy Offline Files operations.                                                                                                                       |
| [**IOfflineFilesServerItem**](/previous-versions/windows/desktop/api/CscObj/)                     | Represents a server item in the Offline Files cache.                                                                                                                                               |
| [**IOfflineFilesSetting**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilessetting)                           | Represents a setting that controls the behavior the Offline Files service.                                                                                                                         |
| [**IOfflineFilesShareInfo**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilesshareinfo)                       | Presents share-specific information about cached items.                                                                                                                                            |
| [**IOfflineFilesShareItem**](/previous-versions/windows/desktop/api/CscObj/)                       | Represents a share item in the Offline Files cache.                                                                                                                                                |
| [**IOfflineFilesSimpleProgress**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilessimpleprogress)             | Used to report progress back to callers of lengthy Offline Files operations.                                                                                                                       |
| [**IOfflineFilesSuspend**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilessuspend)                           | Suspends or releases a share root or directory tree in the Offline Files cache.                                                                                                                    |
| [**IOfflineFilesSuspendInfo**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilessuspendinfo)                   | Determines whether an item is suspended or not and, if so, if it is a suspended root or not.                                                                                                       |
| [**IOfflineFilesSyncConflictHandler**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilessyncconflicthandler)   | Used by a client calling the [**IOfflineFilesCache::Synchronize**](/previous-versions/windows/desktop/api/CscObj/nf-cscobj-iofflinefilescache-synchronize) method to prescribe a conflict resolution strategy for sync conflicts as they are detected. |
| [**IOfflineFilesSyncErrorInfo**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilessyncerrorinfo)               | Supplied with the [**IOfflineFilesSyncProgress::SyncItemResult**](/previous-versions/windows/desktop/api/CscObj/nf-cscobj-iofflinefilessyncprogress-syncitemresult) method to communicate details about the item that experienced a sync error.        |
| [**IOfflineFilesSyncErrorItemInfo**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilessyncerroriteminfo)       | Provides file attributes, time information, and file size for an item associated with a sync error.                                                                                                |
| [**IOfflineFilesSyncProgress**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilessyncprogress)                 | Used to report progress back to the caller during synchronization and synchronization-related operations.                                                                                          |
| [**IOfflineFilesTransparentCacheInfo**](/previous-versions/windows/desktop/api/CscObj/nn-cscobj-iofflinefilestransparentcacheinfo) | Represents information associated with transparently cached items.                                                                                                                                 |



 

 

 



