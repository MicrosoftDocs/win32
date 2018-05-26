---
Description: The following enumerations are used with Offline Files.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 89f2d683-5f94-4728-bd86-074c1ef8fe13
ms.prod: windows-server-dev
ms.technology: offline-files
ms.tgt_platform: multiple
title: Offline Files API Enumerations
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Offline Files API Enumerations

The following enumerations are used with Offline Files.



| Enumeration                                                                         | Description                                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**OFFLINEFILES\_CACHING\_MODE**](/windows/previous-versions/CscObj/ne-cscobj-tagofflinefiles_caching_mode?branch=master)                    | Describes the caching mode used in methods such as [**IOfflineFilesCache::IsPathCacheable**](/windows/previous-versions/CscObj/nf-cscobj-iofflinefilescache-ispathcacheable?branch=master) and [**IOfflineFilesShareInfo::GetShareCachingMode**](/windows/previous-versions/CscObj/nf-cscobj-iofflinefilesshareinfo-getsharecachingmode?branch=master). |
| [**OFFLINEFILES\_COMPARE**](/windows/previous-versions/CscObj/ne-cscobj-tagofflinefiles_compare?branch=master)                               | Specifies the type of comparison to perform in the [**IOfflineFilesItemFilter::GetTimeFilter**](/windows/previous-versions/CscObj/nf-cscobj-iofflinefilesitemfilter-gettimefilter?branch=master) method.                                                                                          |
| [**OFFLINEFILES\_CONNECT\_STATE**](/windows/previous-versions/CscObj/ne-cscobj-tagofflinefiles_connect_state?branch=master)                  | Describes the connection state of an item in the Offline Files cache.                                                                                                                                                                       |
| [**OFFLINEFILES\_EVENTS**](/windows/previous-versions/CscObj/ne-cscobj-tagofflinefiles_events?branch=master)                                 | Event identifier codes describing events to be received or excluded by an event sink.                                                                                                                                                       |
| [**OFFLINEFILES\_ITEM\_COPY**](/windows/previous-versions/CscObj/ne-cscobj-tagofflinefiles_item_copy?branch=master)                          | Specifies whether the local, remote, or original copy of an item is being queried.                                                                                                                                                          |
| [**OFFLINEFILES\_ITEM\_TIME**](/windows/previous-versions/CscObj/ne-cscobj-tagofflinefiles_item_time?branch=master)                          | Specifies which time value associated with the cache item is to be used.                                                                                                                                                                    |
| [**OFFLINEFILES\_ITEM\_TYPE**](/windows/previous-versions/CscObj/ne-cscobj-tagofflinefiles_item_type?branch=master)                          | Identifies the type of an item in the Offline Files cache.                                                                                                                                                                                  |
| [**OFFLINEFILES\_OFFLINE\_REASON**](/windows/previous-versions/CscObj/ne-cscobj-tagofflinefiles_offline_reason?branch=master)                | Indicates the reason why an item is offline.                                                                                                                                                                                                |
| [**OFFLINEFILES\_OP\_RESPONSE**](/windows/previous-versions/CscObj/ne-cscobj-tagofflinefiles_op_response?branch=master)                      | Specifies whether to continue, retry, or stop processing items.                                                                                                                                                                             |
| [**OFFLINEFILES\_PATHFILTER\_MATCH**](/windows/previous-versions/CscObj/ne-cscobj-tagofflinefiles_pathfilter_match?branch=master)            | Specifies how closely an event must match a filter.                                                                                                                                                                                         |
| [**OFFLINEFILES\_SETTING\_VALUE\_TYPE**](/windows/previous-versions/CscObj/ne-cscobj-tagofflinefiles_setting_value_type?branch=master)       | Identifies the data type returned by the [**IOfflineFilesSetting::GetValueType**](/windows/previous-versions/CscObj/nf-cscobj-iofflinefilessetting-getvaluetype?branch=master) method.                                                                                                            |
| [**OFFLINEFILES\_SYNC\_CONFLICT\_RESOLVE**](/windows/previous-versions/CscObj/ne-cscobj-tagofflinefiles_sync_conflict_resolve?branch=master) | Identifies the conflict resolution code returned by the [**IOfflineFilesSyncConflictHandler::ResolveConflict**](/windows/previous-versions/CscObj/nf-cscobj-iofflinefilessyncconflicthandler-resolveconflict?branch=master) method.                                                               |
| [**OFFLINEFILES\_SYNC\_OPERATION**](/windows/previous-versions/CscObj/ne-cscobj-tagofflinefiles_sync_operation?branch=master)                | Indicates the type of sync operation that was being performed when a sync error was encountered.                                                                                                                                            |
| [**OFFLINEFILES\_SYNC\_STATE**](/windows/previous-versions/CscObj/ne-cscobj-tagofflinefiles_sync_state?branch=master)                        | Describes the state of an Offline Files item in conflict.                                                                                                                                                                                   |



 

 

 



