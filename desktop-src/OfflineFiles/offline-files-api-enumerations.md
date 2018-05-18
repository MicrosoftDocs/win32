---
Description: 'The following enumerations are used with Offline Files.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '89f2d683-5f94-4728-bd86-074c1ef8fe13'
ms.prod: 'windows-server-dev'
ms.technology: 'offline-files'
ms.tgt_platform: multiple
title: Offline Files API Enumerations
---

# Offline Files API Enumerations

The following enumerations are used with Offline Files.



| Enumeration                                                                         | Description                                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**OFFLINEFILES\_CACHING\_MODE**](offlinefiles-caching-mode.md)                    | Describes the caching mode used in methods such as [**IOfflineFilesCache::IsPathCacheable**](iofflinefilescache-ispathcacheable.md) and [**IOfflineFilesShareInfo::GetShareCachingMode**](iofflinefilesshareinfo-getsharecachingmode.md). |
| [**OFFLINEFILES\_COMPARE**](offlinefiles-compare.md)                               | Specifies the type of comparison to perform in the [**IOfflineFilesItemFilter::GetTimeFilter**](iofflinefilesitemfilter-gettimefilter.md) method.                                                                                          |
| [**OFFLINEFILES\_CONNECT\_STATE**](offlinefiles-connect-state.md)                  | Describes the connection state of an item in the Offline Files cache.                                                                                                                                                                       |
| [**OFFLINEFILES\_EVENTS**](offlinefiles-events.md)                                 | Event identifier codes describing events to be received or excluded by an event sink.                                                                                                                                                       |
| [**OFFLINEFILES\_ITEM\_COPY**](offlinefiles-item-copy.md)                          | Specifies whether the local, remote, or original copy of an item is being queried.                                                                                                                                                          |
| [**OFFLINEFILES\_ITEM\_TIME**](offlinefiles-item-time.md)                          | Specifies which time value associated with the cache item is to be used.                                                                                                                                                                    |
| [**OFFLINEFILES\_ITEM\_TYPE**](offlinefiles-item-type.md)                          | Identifies the type of an item in the Offline Files cache.                                                                                                                                                                                  |
| [**OFFLINEFILES\_OFFLINE\_REASON**](offlinefiles-offline-reason.md)                | Indicates the reason why an item is offline.                                                                                                                                                                                                |
| [**OFFLINEFILES\_OP\_RESPONSE**](offlinefiles-op-response.md)                      | Specifies whether to continue, retry, or stop processing items.                                                                                                                                                                             |
| [**OFFLINEFILES\_PATHFILTER\_MATCH**](offlinefiles-pathfilter-match.md)            | Specifies how closely an event must match a filter.                                                                                                                                                                                         |
| [**OFFLINEFILES\_SETTING\_VALUE\_TYPE**](offlinefiles-setting-value-type.md)       | Identifies the data type returned by the [**IOfflineFilesSetting::GetValueType**](iofflinefilessetting-getvaluetype.md) method.                                                                                                            |
| [**OFFLINEFILES\_SYNC\_CONFLICT\_RESOLVE**](offlinefiles-sync-conflict-resolve.md) | Identifies the conflict resolution code returned by the [**IOfflineFilesSyncConflictHandler::ResolveConflict**](iofflinefilessyncconflicthandler-resolveconflict.md) method.                                                               |
| [**OFFLINEFILES\_SYNC\_OPERATION**](offlinefiles-sync-operation.md)                | Indicates the type of sync operation that was being performed when a sync error was encountered.                                                                                                                                            |
| [**OFFLINEFILES\_SYNC\_STATE**](offlinefiles-sync-state.md)                        | Describes the state of an Offline Files item in conflict.                                                                                                                                                                                   |



 

 

 



