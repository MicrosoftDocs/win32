---
Description: 'The following interfaces are used with Offline Files.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '9dea396f-ab71-4b2e-b5d3-776c16614f26'
ms.prod: 'windows-server-dev'
ms.technology: 'offline-files'
ms.tgt_platform: multiple
title: Offline Files API Interfaces
---

# Offline Files API Interfaces

The following interfaces are used with Offline Files.

> [!Note]  
> On Windows Server operating systems beginning with Windows Server 2008 R2, the Offline Files COM API and WMI provider are available only if the [Desktop Experience](http://go.microsoft.com/fwlink/p/?linkid=140788) feature is installed on the server.

 



| Interface                                                                      | Description                                                                                                                                                                                        |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IEnumOfflineFilesItems**](ienumofflinefilesitems.md)                       | Represents a collection of [**IOfflineFilesItem**](iofflinefilesitem.md) interface pointers.                                                                                                      |
| [**IEnumOfflineFilesSettings**](ienumofflinefilessettings.md)                 | Enumerates setting objects associated with the Offline Files service.                                                                                                                              |
| [**IOfflineFilesCache**](iofflinefilescache.md)                               | Used to manage the Offline Files cache.                                                                                                                                                            |
| [**IOfflineFilesChangeInfo**](iofflinefileschangeinfo.md)                     | Represents the information associated with local changes made to an item while working offline.                                                                                                    |
| [**IOfflineFilesConnectionInfo**](iofflinefilesconnectioninfo.md)             | Presents query and action capabilities associated with the online-offline behavior of Offline Files.                                                                                               |
| [**IOfflineFilesDirectoryItem**](iofflinefilesdirectoryitem.md)               | Represents a directory item in the Offline Files cache.                                                                                                                                            |
| [**IOfflineFilesDirtyInfo**](iofflinefilesdirtyinfo.md)                       | Represents information about an unsynchronized ("dirty") file in the Offline Files cache.                                                                                                          |
| [**IOfflineFilesErrorInfo**](iofflinefileserrorinfo.md)                       | Provides a text description and raw data block associated with an error.                                                                                                                           |
| [**IOfflineFilesEvents**](iofflinefilesevents.md)                             | Used to report significant events associated with Offline Files.                                                                                                                                   |
| [**IOfflineFilesEvents2**](iofflinefilesevents2.md)                           | Used to report additional events associated with Offline Files.                                                                                                                                    |
| [**IOfflineFilesEvents3**](iofflinefilesevents3.md)                           | Used to report events associated with transparently cached items.                                                                                                                                  |
| [**IOfflineFilesEventsFilter**](iofflinefileseventsfilter.md)                 | Provides a mechanism for recipients of published events to restrict the number of event instances they receive.                                                                                    |
| [**IOfflineFilesFileItem**](iofflinefilesfileitem.md)                         | Represents a file item in the Offline Files cache.                                                                                                                                                 |
| [**IOfflineFilesFileSysInfo**](iofflinefilesfilesysinfo.md)                   | Represents the standard information associated with a file system item in the Offline Files cache.                                                                                                 |
| [**IOfflineFilesGhostInfo**](iofflinefilesghostinfo.md)                       | Represents the ghosting status of an item in the Offline Files cache.                                                                                                                              |
| [**IOfflineFilesItem**](iofflinefilesitem.md)                                 | Represents a single item in the Offline Files cache.                                                                                                                                               |
| [**IOfflineFilesItemContainer**](iofflinefilesitemcontainer.md)               | Used to access item enumeration functionality in the Offline Files cache.                                                                                                                          |
| [**IOfflineFilesItemFilter**](iofflinefilesitemfilter.md)                     | Represents an instance of a filter to be applied to an enumeration.                                                                                                                                |
| [**IOfflineFilesPinInfo**](iofflinefilespininfo.md)                           | Represents the pinned status of an item in the Offline Files cache.                                                                                                                                |
| [**IOfflineFilesPinInfo2**](iofflinefilespininfo2.md)                         | Defines a method to determine whether an item in the Offline Files cache is partly pinned.                                                                                                         |
| [**IOfflineFilesProgress**](iofflinefilesprogress.md)                         | Used to report progress back to callers of lengthy Offline Files operations.                                                                                                                       |
| [**IOfflineFilesServerItem**](iofflinefilesserveritem.md)                     | Represents a server item in the Offline Files cache.                                                                                                                                               |
| [**IOfflineFilesSetting**](iofflinefilessetting.md)                           | Represents a setting that controls the behavior the Offline Files service.                                                                                                                         |
| [**IOfflineFilesShareInfo**](iofflinefilesshareinfo.md)                       | Presents share-specific information about cached items.                                                                                                                                            |
| [**IOfflineFilesShareItem**](iofflinefilesshareitem.md)                       | Represents a share item in the Offline Files cache.                                                                                                                                                |
| [**IOfflineFilesSimpleProgress**](iofflinefilessimpleprogress.md)             | Used to report progress back to callers of lengthy Offline Files operations.                                                                                                                       |
| [**IOfflineFilesSuspend**](iofflinefilessuspend.md)                           | Suspends or releases a share root or directory tree in the Offline Files cache.                                                                                                                    |
| [**IOfflineFilesSuspendInfo**](iofflinefilessuspendinfo.md)                   | Determines whether an item is suspended or not and, if so, if it is a suspended root or not.                                                                                                       |
| [**IOfflineFilesSyncConflictHandler**](iofflinefilessyncconflicthandler.md)   | Used by a client calling the [**IOfflineFilesCache::Synchronize**](iofflinefilescache-synchronize.md) method to prescribe a conflict resolution strategy for sync conflicts as they are detected. |
| [**IOfflineFilesSyncErrorInfo**](iofflinefilessyncerrorinfo.md)               | Supplied with the [**IOfflineFilesSyncProgress::SyncItemResult**](iofflinefilessyncprogress-syncitemresult.md) method to communicate details about the item that experienced a sync error.        |
| [**IOfflineFilesSyncErrorItemInfo**](iofflinefilessyncerroriteminfo.md)       | Provides file attributes, time information, and file size for an item associated with a sync error.                                                                                                |
| [**IOfflineFilesSyncProgress**](iofflinefilessyncprogress.md)                 | Used to report progress back to the caller during synchronization and synchronization-related operations.                                                                                          |
| [**IOfflineFilesTransparentCacheInfo**](iofflinefilestransparentcacheinfo.md) | Represents information associated with transparently cached items.                                                                                                                                 |



 

 

 



