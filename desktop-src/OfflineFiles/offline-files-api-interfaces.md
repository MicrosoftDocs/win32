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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Offline Files API Interfaces

The following interfaces are used with Offline Files.

> [!Note]  
> On Windows Server operating systems beginning with Windows Server 2008 R2, the Offline Files COM API and WMI provider are available only if the [Desktop Experience](http://go.microsoft.com/fwlink/p/?linkid=140788) feature is installed on the server.

 



| Interface                                                                      | Description                                                                                                                                                                                        |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IEnumOfflineFilesItems**](/windows/previous-versions/CscObj/nn-cscobj-ienumofflinefilesitems?branch=master)                       | Represents a collection of [**IOfflineFilesItem**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefilesitem?branch=master) interface pointers.                                                                                                      |
| [**IEnumOfflineFilesSettings**](/windows/previous-versions/CscObj/nn-cscobj-ienumofflinefilessettings?branch=master)                 | Enumerates setting objects associated with the Offline Files service.                                                                                                                              |
| [**IOfflineFilesCache**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefilescache?branch=master)                               | Used to manage the Offline Files cache.                                                                                                                                                            |
| [**IOfflineFilesChangeInfo**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefileschangeinfo?branch=master)                     | Represents the information associated with local changes made to an item while working offline.                                                                                                    |
| [**IOfflineFilesConnectionInfo**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefilesconnectioninfo?branch=master)             | Presents query and action capabilities associated with the online-offline behavior of Offline Files.                                                                                               |
| [**IOfflineFilesDirectoryItem**](/windows/previous-versions/CscObj/?branch=master)               | Represents a directory item in the Offline Files cache.                                                                                                                                            |
| [**IOfflineFilesDirtyInfo**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefilesdirtyinfo?branch=master)                       | Represents information about an unsynchronized ("dirty") file in the Offline Files cache.                                                                                                          |
| [**IOfflineFilesErrorInfo**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefileserrorinfo?branch=master)                       | Provides a text description and raw data block associated with an error.                                                                                                                           |
| [**IOfflineFilesEvents**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefilesevents?branch=master)                             | Used to report significant events associated with Offline Files.                                                                                                                                   |
| [**IOfflineFilesEvents2**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefilesevents2?branch=master)                           | Used to report additional events associated with Offline Files.                                                                                                                                    |
| [**IOfflineFilesEvents3**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefilesevents3?branch=master)                           | Used to report events associated with transparently cached items.                                                                                                                                  |
| [**IOfflineFilesEventsFilter**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefileseventsfilter?branch=master)                 | Provides a mechanism for recipients of published events to restrict the number of event instances they receive.                                                                                    |
| [**IOfflineFilesFileItem**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefilesfileitem?branch=master)                         | Represents a file item in the Offline Files cache.                                                                                                                                                 |
| [**IOfflineFilesFileSysInfo**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefilesfilesysinfo?branch=master)                   | Represents the standard information associated with a file system item in the Offline Files cache.                                                                                                 |
| [**IOfflineFilesGhostInfo**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefilesghostinfo?branch=master)                       | Represents the ghosting status of an item in the Offline Files cache.                                                                                                                              |
| [**IOfflineFilesItem**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefilesitem?branch=master)                                 | Represents a single item in the Offline Files cache.                                                                                                                                               |
| [**IOfflineFilesItemContainer**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefilesitemcontainer?branch=master)               | Used to access item enumeration functionality in the Offline Files cache.                                                                                                                          |
| [**IOfflineFilesItemFilter**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefilesitemfilter?branch=master)                     | Represents an instance of a filter to be applied to an enumeration.                                                                                                                                |
| [**IOfflineFilesPinInfo**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefilespininfo?branch=master)                           | Represents the pinned status of an item in the Offline Files cache.                                                                                                                                |
| [**IOfflineFilesPinInfo2**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefilespininfo2?branch=master)                         | Defines a method to determine whether an item in the Offline Files cache is partly pinned.                                                                                                         |
| [**IOfflineFilesProgress**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefilesprogress?branch=master)                         | Used to report progress back to callers of lengthy Offline Files operations.                                                                                                                       |
| [**IOfflineFilesServerItem**](/windows/previous-versions/CscObj/?branch=master)                     | Represents a server item in the Offline Files cache.                                                                                                                                               |
| [**IOfflineFilesSetting**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefilessetting?branch=master)                           | Represents a setting that controls the behavior the Offline Files service.                                                                                                                         |
| [**IOfflineFilesShareInfo**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefilesshareinfo?branch=master)                       | Presents share-specific information about cached items.                                                                                                                                            |
| [**IOfflineFilesShareItem**](/windows/previous-versions/CscObj/?branch=master)                       | Represents a share item in the Offline Files cache.                                                                                                                                                |
| [**IOfflineFilesSimpleProgress**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefilessimpleprogress?branch=master)             | Used to report progress back to callers of lengthy Offline Files operations.                                                                                                                       |
| [**IOfflineFilesSuspend**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefilessuspend?branch=master)                           | Suspends or releases a share root or directory tree in the Offline Files cache.                                                                                                                    |
| [**IOfflineFilesSuspendInfo**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefilessuspendinfo?branch=master)                   | Determines whether an item is suspended or not and, if so, if it is a suspended root or not.                                                                                                       |
| [**IOfflineFilesSyncConflictHandler**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefilessyncconflicthandler?branch=master)   | Used by a client calling the [**IOfflineFilesCache::Synchronize**](/windows/previous-versions/CscObj/nf-cscobj-iofflinefilescache-synchronize?branch=master) method to prescribe a conflict resolution strategy for sync conflicts as they are detected. |
| [**IOfflineFilesSyncErrorInfo**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefilessyncerrorinfo?branch=master)               | Supplied with the [**IOfflineFilesSyncProgress::SyncItemResult**](/windows/previous-versions/CscObj/nf-cscobj-iofflinefilessyncprogress-syncitemresult?branch=master) method to communicate details about the item that experienced a sync error.        |
| [**IOfflineFilesSyncErrorItemInfo**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefilessyncerroriteminfo?branch=master)       | Provides file attributes, time information, and file size for an item associated with a sync error.                                                                                                |
| [**IOfflineFilesSyncProgress**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefilessyncprogress?branch=master)                 | Used to report progress back to the caller during synchronization and synchronization-related operations.                                                                                          |
| [**IOfflineFilesTransparentCacheInfo**](/windows/previous-versions/CscObj/nn-cscobj-iofflinefilestransparentcacheinfo?branch=master) | Represents information associated with transparently cached items.                                                                                                                                 |



 

 

 



