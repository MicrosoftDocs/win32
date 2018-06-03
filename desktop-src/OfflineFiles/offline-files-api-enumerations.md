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
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Offline Files API Enumerations

The following enumerations are used with Offline Files.



| Enumeration                                                                         | Description                                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**OFFLINEFILES\_CACHING\_MODE**](/previous-versions/windows/desktop/api/CscObj/ne-cscobj-tagofflinefiles_caching_mode)                    | Describes the caching mode used in methods such as [**IOfflineFilesCache::IsPathCacheable**](/previous-versions/windows/desktop/api/CscObj/nf-cscobj-iofflinefilescache-ispathcacheable) and [**IOfflineFilesShareInfo::GetShareCachingMode**](/previous-versions/windows/desktop/api/CscObj/nf-cscobj-iofflinefilesshareinfo-getsharecachingmode). |
| [**OFFLINEFILES\_COMPARE**](/previous-versions/windows/desktop/api/CscObj/ne-cscobj-tagofflinefiles_compare)                               | Specifies the type of comparison to perform in the [**IOfflineFilesItemFilter::GetTimeFilter**](/previous-versions/windows/desktop/api/CscObj/nf-cscobj-iofflinefilesitemfilter-gettimefilter) method.                                                                                          |
| [**OFFLINEFILES\_CONNECT\_STATE**](/previous-versions/windows/desktop/api/CscObj/ne-cscobj-tagofflinefiles_connect_state)                  | Describes the connection state of an item in the Offline Files cache.                                                                                                                                                                       |
| [**OFFLINEFILES\_EVENTS**](/previous-versions/windows/desktop/api/CscObj/ne-cscobj-tagofflinefiles_events)                                 | Event identifier codes describing events to be received or excluded by an event sink.                                                                                                                                                       |
| [**OFFLINEFILES\_ITEM\_COPY**](/previous-versions/windows/desktop/api/CscObj/ne-cscobj-tagofflinefiles_item_copy)                          | Specifies whether the local, remote, or original copy of an item is being queried.                                                                                                                                                          |
| [**OFFLINEFILES\_ITEM\_TIME**](/previous-versions/windows/desktop/api/CscObj/ne-cscobj-tagofflinefiles_item_time)                          | Specifies which time value associated with the cache item is to be used.                                                                                                                                                                    |
| [**OFFLINEFILES\_ITEM\_TYPE**](/previous-versions/windows/desktop/api/CscObj/ne-cscobj-tagofflinefiles_item_type)                          | Identifies the type of an item in the Offline Files cache.                                                                                                                                                                                  |
| [**OFFLINEFILES\_OFFLINE\_REASON**](/previous-versions/windows/desktop/api/CscObj/ne-cscobj-tagofflinefiles_offline_reason)                | Indicates the reason why an item is offline.                                                                                                                                                                                                |
| [**OFFLINEFILES\_OP\_RESPONSE**](/previous-versions/windows/desktop/api/CscObj/ne-cscobj-tagofflinefiles_op_response)                      | Specifies whether to continue, retry, or stop processing items.                                                                                                                                                                             |
| [**OFFLINEFILES\_PATHFILTER\_MATCH**](/previous-versions/windows/desktop/api/CscObj/ne-cscobj-tagofflinefiles_pathfilter_match)            | Specifies how closely an event must match a filter.                                                                                                                                                                                         |
| [**OFFLINEFILES\_SETTING\_VALUE\_TYPE**](/previous-versions/windows/desktop/api/CscObj/ne-cscobj-tagofflinefiles_setting_value_type)       | Identifies the data type returned by the [**IOfflineFilesSetting::GetValueType**](/previous-versions/windows/desktop/api/CscObj/nf-cscobj-iofflinefilessetting-getvaluetype) method.                                                                                                            |
| [**OFFLINEFILES\_SYNC\_CONFLICT\_RESOLVE**](/previous-versions/windows/desktop/api/CscObj/ne-cscobj-tagofflinefiles_sync_conflict_resolve) | Identifies the conflict resolution code returned by the [**IOfflineFilesSyncConflictHandler::ResolveConflict**](/previous-versions/windows/desktop/api/CscObj/nf-cscobj-iofflinefilessyncconflicthandler-resolveconflict) method.                                                               |
| [**OFFLINEFILES\_SYNC\_OPERATION**](/previous-versions/windows/desktop/api/CscObj/ne-cscobj-tagofflinefiles_sync_operation)                | Indicates the type of sync operation that was being performed when a sync error was encountered.                                                                                                                                            |
| [**OFFLINEFILES\_SYNC\_STATE**](/previous-versions/windows/desktop/api/CscObj/ne-cscobj-tagofflinefiles_sync_state)                        | Describes the state of an Offline Files item in conflict.                                                                                                                                                                                   |



 

 

 



