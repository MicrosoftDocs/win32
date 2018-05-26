---
title: CI\_STATE\_\ Constants
description: Reflects the state of the current activities of Indexing Service, including merges, scans, and performance indicators on the computer running the service.
ms.assetid: c951a3bf-16d3-4f69-8485-c3d62a4fdd17
topic_type:
- apiref
api_name:
- CI_STATE_ANNEALING_MERGE
- CI_STATE_BATTERY_POWER
- CI_STATE_CONTENT_SCAN_REQUIRED
- CI_STATE_HIGH_IO
- CI_STATE_INDEX_MIGRATION_MERGE
- CI_STATE_LOW_MEMORY
- CI_STATE_MASTER_MERGE
- CI_STATE_MASTER_MERGE_PAUSED
- CI_STATE_READ_ONLY
- CI_STATE_READING_USNS
- CI_STATE_RECOVERING
- CI_STATE_SCANNING
- CI_STATE_SHADOW_MERGE
- CI_STATE_STARTING
- CI_STATE_USER_ACTIVE
api_location:
- Ntquery.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CI\_STATE\_\* Constants

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Reflects the state of the current activities of Indexing Service, including merges, scans, and performance indicators on the computer running the service.



| Constant/value                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                        |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CI_STATE_ANNEALING_MERGE"></span><span id="ci_state_annealing_merge"></span><dl> <dt>**CI\_STATE\_ANNEALING\_MERGE**</dt> <dt>0x8</dt> </dl>                     | An annealing merge is in process.<br/>                                                                                                                                                                                                                                                                       |
| <span id="CI_STATE_BATTERY_POWER"></span><span id="ci_state_battery_power"></span><dl> <dt>**CI\_STATE\_BATTERY\_POWER**</dt> <dt>0x800</dt> </dl>                         | The service is paused to conserve battery lifetime. The threshold for entering this state depends on the value of the [**MinWordlistBattery**](minwordlistbattery.md) registry entry. <br/>                                                                                                                 |
| <span id="CI_STATE_CONTENT_SCAN_REQUIRED"></span><span id="ci_state_content_scan_required"></span><dl> <dt>**CI\_STATE\_CONTENT\_SCAN\_REQUIRED**</dt> <dt>0x4</dt> </dl>  | Some documents in the index have changed and Indexing Service needs to determine which have been added, changed, or deleted.<br/>                                                                                                                                                                            |
| <span id="CI_STATE_HIGH_IO"></span><span id="ci_state_high_io"></span><dl> <dt>**CI\_STATE\_HIGH\_IO**</dt> <dt>0x100</dt> </dl>                                           | The level of input/output (I/O) activity on the computer running Indexing Service is relatively high. The threshold for entering this state depends on the value of the [**MaxWordlistIo**](maxwordlistio.md) registry entry. In this state, indexing is paused, but queries continue to be accepted. <br/> |
| <span id="CI_STATE_INDEX_MIGRATION_MERGE"></span><span id="ci_state_index_migration_merge"></span><dl> <dt>**CI\_STATE\_INDEX\_MIGRATION\_MERGE**</dt> <dt>0x40</dt> </dl> | The catalog is in the process of being merged for the purpose of migrating the catalog.<br/>                                                                                                                                                                                                                 |
| <span id="CI_STATE_LOW_MEMORY"></span><span id="ci_state_low_memory"></span><dl> <dt>**CI\_STATE\_LOW\_MEMORY**</dt> <dt>0x80</dt> </dl>                                   | Most of the virtual memory of the computer running Indexing Service is in use. The threshold for entering this state depends on the value of the [**MinWordlistMemory**](minwordlistmemory.md) registry entry. In this state, indexing is paused, but queries continue to be accepted.<br/>                 |
| <span id="CI_STATE_MASTER_MERGE"></span><span id="ci_state_master_merge"></span><dl> <dt>**CI\_STATE\_MASTER\_MERGE**</dt> <dt>0x2</dt> </dl>                              | A master merge is in process. <br/>                                                                                                                                                                                                                                                                          |
| <span id="CI_STATE_MASTER_MERGE_PAUSED"></span><span id="ci_state_master_merge_paused"></span><dl> <dt>**CI\_STATE\_MASTER\_MERGE\_PAUSED**</dt> <dt>0x200</dt> </dl>      | The master merge that was in progress has been paused.<br/>                                                                                                                                                                                                                                                  |
| <span id="CI_STATE_READ_ONLY"></span><span id="ci_state_read_only"></span><dl> <dt>**CI\_STATE\_READ\_ONLY**</dt> <dt>0x400</dt> </dl>                                     | The service has been manually paused.<br/>                                                                                                                                                                                                                                                                   |
| <span id="CI_STATE_READING_USNS"></span><span id="ci_state_reading_usns"></span><dl> <dt>**CI\_STATE\_READING\_USNS**</dt> <dt>0x4000</dt> </dl>                           | The service has not read the USN journal from one or more volumes being indexed. The index might not be up to date.<br/>                                                                                                                                                                                     |
| <span id="CI_STATE_RECOVERING"></span><span id="ci_state_recovering"></span><dl> <dt>**CI\_STATE\_RECOVERING**</dt> <dt>0x20</dt> </dl>                                    | The service is starting from the last saved state and is in the process of recovering.<br/>                                                                                                                                                                                                                  |
| <span id="CI_STATE_SCANNING"></span><span id="ci_state_scanning"></span><dl> <dt>**CI\_STATE\_SCANNING**</dt> <dt>0x10</dt> </dl>                                          | A scan is in process.<br/>                                                                                                                                                                                                                                                                                   |
| <span id="CI_STATE_SHADOW_MERGE"></span><span id="ci_state_shadow_merge"></span><dl> <dt>**CI\_STATE\_SHADOW\_MERGE**</dt> <dt>0x1</dt> </dl>                              | A shadow merge is in process. <br/>                                                                                                                                                                                                                                                                          |
| <span id="CI_STATE_STARTING"></span><span id="ci_state_starting"></span><dl> <dt>**CI\_STATE\_STARTING**</dt> <dt>0x2000</dt> </dl>                                        | The service is starting. Queries can be run, but scanning and notification have not been enabled yet.<br/>                                                                                                                                                                                                   |
| <span id="CI_STATE_USER_ACTIVE"></span><span id="ci_state_user_active"></span><dl> <dt>**CI\_STATE\_USER\_ACTIVE**</dt> <dt>0x1000</dt> </dl>                              | The service is paused due to high activity by the user (keyboard or mouse). The threshold for entering this state depends on the value of the [**WordlistUserIdle**](wordlistuseridle.md) registry entry. In this state, indexing is paused, but queries are still accepted. <br/>                          |



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| Header<br/>                   | <dl> <dt>Ntquery.h</dt> </dl> |



## See also

<dl> <dt>

[**CIState**](/windows/win32/Ntquery/nf-ntquery-cistate?branch=master)
</dt> <dt>

[**CI\_STATE**](/windows/win32/Ntquery/ns-ntquery-_ci_state?branch=master)
</dt> </dl>

 

 





