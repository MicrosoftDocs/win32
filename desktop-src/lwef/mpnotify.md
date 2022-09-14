---
title: MPNOTIFY enumeration (MpClient.h)
description: Possible callback notifications.
ms.assetid: CCD0CD89-2C6E-453F-9437-E6ED87AD9F29
keywords:
- MPNOTIFY enumeration Legacy Windows Environment Features
- PMPNOTIFY enumeration pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPNOTIFY
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPNOTIFY enumeration

Possible callback notifications.

## Syntax


```C++
typedef enum tagMPNOTIFY { 
  MPNOTIFY_NONE,
  MPNOTIFY_CALL_START,
  MPNOTIFY_CALL_COMPLETE,
  MPNOTIFY_INTERNAL_FAILURE,
  MPNOTIFY_STATUS_SERVICE_START,
  MPNOTIFY_STATUS_SERVICE_RUNNING,
  MPNOTIFY_STATUS_SERVICE_STOP,
  MPNOTIFY_STATUS_COMPONENT,
  MPNOTIFY_STATUS_CHANGE,
  MPNOTIFY_STATUS_COMPONENT_CONFIGURATION,
  MPNOTIFY_STATUS_EXPIRATION_CHANGE,
  MPNOTIFY_STATUS_OFFLINE_SCAN_CHANGE,
  MPNOTIFY_SCAN_START,
  MPNOTIFY_SCAN_PAUSED,
  MPNOTIFY_SCAN_RESUMED,
  MPNOTIFY_SCAN_CANCEL,
  MPNOTIFY_SCAN_COMPLETE,
  MPNOTIFY_SCAN_PROGRESS,
  MPNOTIFY_SCAN_ERROR,
  MPNOTIFY_SCAN_INFECTED,
  MPNOTIFY_SCAN_MEMORYSTART,
  MPNOTIFY_SCAN_MEMORYCOMPLETE,
  MPNOTIFY_SCAN_SFC_BUILD_START,
  MPNOTIFY_SCAN_SFC_BUILD_COMPLETE,
  MPNOTIFY_SCAN_FASTPATH_START,
  MPNOTIFY_SCAN_FASTPATH_COMPLETE,
  MPNOTIFY_SCAN_FASTPATH_PROGRESS,
  MPNOTIFY_CLEAN_START,
  MPNOTIFY_CLEAN_COMPLETE,
  MPNOTIFY_CLEAN_RESTOREPOINT_START,
  MPNOTIFY_CLEAN_RESTOREPOINT_SUCCEEDED,
  MPNOTIFY_CLEAN_RESTOREPOINT_FAILED,
  MPNOTIFY_CLEAN_THREAT_START,
  MPNOTIFY_CLEAN_THREAT_SUCCEEDED,
  MPNOTIFY_CLEAN_THREAT_FAILED,
  MPNOTIFY_CLEAN_RESOURCE_SUCCEEDED,
  MPNOTIFY_CLEAN_RESOURCE_FAILED,
  MPNOTIFY_CLEAN_THREAT_COMPLETE,
  MPNOTIFY_PRECHECK_START,
  MPNOTIFY_PRECHECK_COMPLETE,
  MPNOTIFY_PRECHECK_RESOURCE_BLOCKED,
  MPNOTIFY_THREAT_DETECTED,
  MPNOTIFY_THREAT_MODIFIED,
  MPNOTIFY_THREAT_CLEAN_SUCCEEDED,
  MPNOTIFY_THREAT_CLEAN_FAILED,
  MPNOTIFY_THREAT_ABANDONED,
  MPNOTIFY_THREAT_CLEAN_EVENT_START,
  MPNOTIFY_THREAT_CLEAN_EVENT_COMPLETE,
  MPNOTIFY_SIGUPDATE_START,
  MPNOTIFY_SIGUPDATE_SEARCH_START,
  MPNOTIFY_SIGUPDATE_SEARCH_COMPLETE,
  MPNOTIFY_SIGUPDATE_SOFTWARE_UPDATE_AVAILABLE,
  MPNOTIFY_SIGUPDATE_DOWNLOAD_START,
  MPNOTIFY_SIGUPDATE_DOWNLOAD_PROGRESS,
  MPNOTIFY_SIGUPDATE_DOWNLOAD_COMPLETE,
  MPNOTIFY_SIGUPDATE_INSTALL_START,
  MPNOTIFY_SIGUPDATE_INSTALL_PROGRESS,
  MPNOTIFY_SIGUPDATE_INSTALL_COMPLETE,
  MPNOTIFY_SIGUPDATE_REBOOT_REQUIRED,
  MPNOTIFY_SIGUPDATE_REQUEST_PROCESSED,
  MPNOTIFY_SIGUPDATE_COMPLETE,
  MPNOTIFY_SAMPLE_START,
  MPNOTIFY_SAMPLE_COMPLETE,
  MPNOTIFY_SAMPLE_ITEM_START,
  MPNOTIFY_SAMPLE_ITEM_SUCCEEDED,
  MPNOTIFY_SAMPLE_ITEM_FAILED,
  MPNOTIFY_RESERVED_DATA,
  MPNOTIFY_FASTPATH_SIG_ADDED,
  MPNOTIFY_FASTPATH_SIG_REMOVED,
  MPNOTIFY_NIS_PRIVATE,
  MPNOTIFY_HEALTH_CHANGE,
  MPNOTIFY_HEALTH_RECOVERY,
  MPNOTIFY_HEALTH_START,
  MPNOTIFY_ENDOFLIFE_CHANGE,
  MPNOTIFY_MALWARETOAST_DATA
} MPNOTIFY, *PMPNOTIFY;
```



## Constants

<dl> <dt>

<span id="MPNOTIFY_NONE"></span><span id="mpnotify_none"></span>**MPNOTIFY\_NONE**
</dt> <dd></dd> <dt>

<span id="MPNOTIFY_CALL_START"></span><span id="mpnotify_call_start"></span>**MPNOTIFY\_CALL\_START**
</dt> <dd>

Notification call start.

</dd> <dt>

<span id="MPNOTIFY_CALL_COMPLETE"></span><span id="mpnotify_call_complete"></span>**MPNOTIFY\_CALL\_COMPLETE**
</dt> <dd>

Notification call completed.

</dd> <dt>

<span id="MPNOTIFY_INTERNAL_FAILURE"></span><span id="mpnotify_internal_failure"></span>**MPNOTIFY\_INTERNAL\_FAILURE**
</dt> <dd>

Generic internal failure.

</dd> <dt>

<span id="MPNOTIFY_STATUS_SERVICE_START"></span><span id="mpnotify_status_service_start"></span>**MPNOTIFY\_STATUS\_SERVICE\_START**
</dt> <dd>

Malware protection service has started.

</dd> <dt>

<span id="MPNOTIFY_STATUS_SERVICE_RUNNING"></span><span id="mpnotify_status_service_running"></span>**MPNOTIFY\_STATUS\_SERVICE\_RUNNING**
</dt> <dd>

Malware protection service is running.

</dd> <dt>

<span id="MPNOTIFY_STATUS_SERVICE_STOP"></span><span id="mpnotify_status_service_stop"></span>**MPNOTIFY\_STATUS\_SERVICE\_STOP**
</dt> <dd>

Malware protection service has stopped.

</dd> <dt>

<span id="MPNOTIFY_STATUS_COMPONENT"></span><span id="mpnotify_status_component"></span>**MPNOTIFY\_STATUS\_COMPONENT**
</dt> <dd>

Particular component enable/disable status.

</dd> <dt>

<span id="MPNOTIFY_STATUS_CHANGE"></span><span id="mpnotify_status_change"></span>**MPNOTIFY\_STATUS\_CHANGE**
</dt> <dd>

Overall product status has changed. Call [**MpManagerStatusQueryEx**](mpmanagerstatusqueryex.md) to obtain the current status.

</dd> <dt>

<span id="MPNOTIFY_STATUS_COMPONENT_CONFIGURATION"></span><span id="mpnotify_status_component_configuration"></span>**MPNOTIFY\_STATUS\_COMPONENT\_CONFIGURATION**
</dt> <dd>

A particular component has changed configuration.

</dd> <dt>

<span id="MPNOTIFY_STATUS_EXPIRATION_CHANGE"></span><span id="mpnotify_status_expiration_change"></span>**MPNOTIFY\_STATUS\_EXPIRATION\_CHANGE**
</dt> <dd>

Product expiration status has changed.

</dd> <dt>

<span id="MPNOTIFY_STATUS_OFFLINE_SCAN_CHANGE"></span><span id="mpnotify_status_offline_scan_change"></span>**MPNOTIFY\_STATUS\_OFFLINE\_SCAN\_CHANGE**
</dt> <dd>

Offline scan required state changed.

</dd> <dt>

<span id="MPNOTIFY_SCAN_START"></span><span id="mpnotify_scan_start"></span>**MPNOTIFY\_SCAN\_START**
</dt> <dd>

Scan started.

</dd> <dt>

<span id="MPNOTIFY_SCAN_PAUSED"></span><span id="mpnotify_scan_paused"></span>**MPNOTIFY\_SCAN\_PAUSED**
</dt> <dd>

Scan paused.

</dd> <dt>

<span id="MPNOTIFY_SCAN_RESUMED"></span><span id="mpnotify_scan_resumed"></span>**MPNOTIFY\_SCAN\_RESUMED**
</dt> <dd>

scan resumed.

</dd> <dt>

<span id="MPNOTIFY_SCAN_CANCEL"></span><span id="mpnotify_scan_cancel"></span>**MPNOTIFY\_SCAN\_CANCEL**
</dt> <dd>

Scan cancelled.

</dd> <dt>

<span id="MPNOTIFY_SCAN_COMPLETE"></span><span id="mpnotify_scan_complete"></span>**MPNOTIFY\_SCAN\_COMPLETE**
</dt> <dd>

Scan completed.

</dd> <dt>

<span id="MPNOTIFY_SCAN_PROGRESS"></span><span id="mpnotify_scan_progress"></span>**MPNOTIFY\_SCAN\_PROGRESS**
</dt> <dd>

Progress notification for the specific resource being scanned.

</dd> <dt>

<span id="MPNOTIFY_SCAN_ERROR"></span><span id="mpnotify_scan_error"></span>**MPNOTIFY\_SCAN\_ERROR**
</dt> <dd>

Failure to scan a particular resource. Scan will still continue.

</dd> <dt>

<span id="MPNOTIFY_SCAN_INFECTED"></span><span id="mpnotify_scan_infected"></span>**MPNOTIFY\_SCAN\_INFECTED**
</dt> <dd>

Scan found an infected resource.

</dd> <dt>

<span id="MPNOTIFY_SCAN_MEMORYSTART"></span><span id="mpnotify_scan_memorystart"></span>**MPNOTIFY\_SCAN\_MEMORYSTART**
</dt> <dd>

Scan progress to notify memory scan portion of the system scan has started.

</dd> <dt>

<span id="MPNOTIFY_SCAN_MEMORYCOMPLETE"></span><span id="mpnotify_scan_memorycomplete"></span>**MPNOTIFY\_SCAN\_MEMORYCOMPLETE**
</dt> <dd>

Scan progress to notify memory scan portion of the system scan has completed.

</dd> <dt>

<span id="MPNOTIFY_SCAN_SFC_BUILD_START"></span><span id="mpnotify_scan_sfc_build_start"></span>**MPNOTIFY\_SCAN\_SFC\_BUILD\_START**
</dt> <dd>

Scan progress to notify sfc build portion has started.

</dd> <dt>

<span id="MPNOTIFY_SCAN_SFC_BUILD_COMPLETE"></span><span id="mpnotify_scan_sfc_build_complete"></span>**MPNOTIFY\_SCAN\_SFC\_BUILD\_COMPLETE**
</dt> <dd>

Scan progress to notify sfc build portion has completed.

</dd> <dt>

<span id="MPNOTIFY_SCAN_FASTPATH_START"></span><span id="mpnotify_scan_fastpath_start"></span>**MPNOTIFY\_SCAN\_FASTPATH\_START**
</dt> <dd>

Scan fastpath spynet has begun.

</dd> <dt>

<span id="MPNOTIFY_SCAN_FASTPATH_COMPLETE"></span><span id="mpnotify_scan_fastpath_complete"></span>**MPNOTIFY\_SCAN\_FASTPATH\_COMPLETE**
</dt> <dd>

Scan fastpath spynet has ended.

</dd> <dt>

<span id="MPNOTIFY_SCAN_FASTPATH_PROGRESS"></span><span id="mpnotify_scan_fastpath_progress"></span>**MPNOTIFY\_SCAN\_FASTPATH\_PROGRESS**
</dt> <dd>

Progress notification for fastpath rescans, used internally and converted to **MPNOTIFY\_SCAN\_PROGRESS** for external.

</dd> <dt>

<span id="MPNOTIFY_CLEAN_START"></span><span id="mpnotify_clean_start"></span>**MPNOTIFY\_CLEAN\_START**
</dt> <dd>

Cleaning started.

</dd> <dt>

<span id="MPNOTIFY_CLEAN_COMPLETE"></span><span id="mpnotify_clean_complete"></span>**MPNOTIFY\_CLEAN\_COMPLETE**
</dt> <dd>

Cleaning completed.

</dd> <dt>

<span id="MPNOTIFY_CLEAN_RESTOREPOINT_START"></span><span id="mpnotify_clean_restorepoint_start"></span>**MPNOTIFY\_CLEAN\_RESTOREPOINT\_START**
</dt> <dd>

Started to create a system restore point.

</dd> <dt>

<span id="MPNOTIFY_CLEAN_RESTOREPOINT_SUCCEEDED"></span><span id="mpnotify_clean_restorepoint_succeeded"></span>**MPNOTIFY\_CLEAN\_RESTOREPOINT\_SUCCEEDED**
</dt> <dd>

System restore point successfully created.

</dd> <dt>

<span id="MPNOTIFY_CLEAN_RESTOREPOINT_FAILED"></span><span id="mpnotify_clean_restorepoint_failed"></span>**MPNOTIFY\_CLEAN\_RESTOREPOINT\_FAILED**
</dt> <dd>

System restore point creation failed.

</dd> <dt>

<span id="MPNOTIFY_CLEAN_THREAT_START"></span><span id="mpnotify_clean_threat_start"></span>**MPNOTIFY\_CLEAN\_THREAT\_START**
</dt> <dd>

Cleaning is started for a particular threat.

</dd> <dt>

<span id="MPNOTIFY_CLEAN_THREAT_SUCCEEDED"></span><span id="mpnotify_clean_threat_succeeded"></span>**MPNOTIFY\_CLEAN\_THREAT\_SUCCEEDED**
</dt> <dd>

Cleaning is succeeded for a particular threat.

</dd> <dt>

<span id="MPNOTIFY_CLEAN_THREAT_FAILED"></span><span id="mpnotify_clean_threat_failed"></span>**MPNOTIFY\_CLEAN\_THREAT\_FAILED**
</dt> <dd>

Cleaning has failed for a particular threat. **ERROR\_MP\_THREAT\_NOT\_FOUND** error code indicates that the threat was not found (and was not a failure to clean).

</dd> <dt>

<span id="MPNOTIFY_CLEAN_RESOURCE_SUCCEEDED"></span><span id="mpnotify_clean_resource_succeeded"></span>**MPNOTIFY\_CLEAN\_RESOURCE\_SUCCEEDED**
</dt> <dd>

Cleaning is succeeded for a particular resource.

</dd> <dt>

<span id="MPNOTIFY_CLEAN_RESOURCE_FAILED"></span><span id="mpnotify_clean_resource_failed"></span>**MPNOTIFY\_CLEAN\_RESOURCE\_FAILED**
</dt> <dd>

Cleaning has failed for a particular resource.

</dd> <dt>

<span id="MPNOTIFY_CLEAN_THREAT_COMPLETE"></span><span id="mpnotify_clean_threat_complete"></span>**MPNOTIFY\_CLEAN\_THREAT\_COMPLETE**
</dt> <dd>

Cleaning has completed for a particular threat.

</dd> <dt>

<span id="MPNOTIFY_PRECHECK_START"></span><span id="mpnotify_precheck_start"></span>**MPNOTIFY\_PRECHECK\_START**
</dt> <dd>

Clean precheck started.

</dd> <dt>

<span id="MPNOTIFY_PRECHECK_COMPLETE"></span><span id="mpnotify_precheck_complete"></span>**MPNOTIFY\_PRECHECK\_COMPLETE**
</dt> <dd>

Clean precheck completed.

</dd> <dt>

<span id="MPNOTIFY_PRECHECK_RESOURCE_BLOCKED"></span><span id="mpnotify_precheck_resource_blocked"></span>**MPNOTIFY\_PRECHECK\_RESOURCE\_BLOCKED**
</dt> <dd>

Clean precheck detected blocked resource.

</dd> <dt>

<span id="MPNOTIFY_THREAT_DETECTED"></span><span id="mpnotify_threat_detected"></span>**MPNOTIFY\_THREAT\_DETECTED**
</dt> <dd>

New threat detected in system.

</dd> <dt>

<span id="MPNOTIFY_THREAT_MODIFIED"></span><span id="mpnotify_threat_modified"></span>**MPNOTIFY\_THREAT\_MODIFIED**
</dt> <dd>

Threat information modified. For example, a new resource was added.

</dd> <dt>

<span id="MPNOTIFY_THREAT_CLEAN_SUCCEEDED"></span><span id="mpnotify_threat_clean_succeeded"></span>**MPNOTIFY\_THREAT\_CLEAN\_SUCCEEDED**
</dt> <dd>

Cleaning action succeeded for a threat.

</dd> <dt>

<span id="MPNOTIFY_THREAT_CLEAN_FAILED"></span><span id="mpnotify_threat_clean_failed"></span>**MPNOTIFY\_THREAT\_CLEAN\_FAILED**
</dt> <dd>

Cleaning action failed for a threat. **ERROR\_MP\_THREAT\_NOT\_FOUND** error code indicates that the threat was not found (and was not a failure to clean).

</dd> <dt>

<span id="MPNOTIFY_THREAT_ABANDONED"></span><span id="mpnotify_threat_abandoned"></span>**MPNOTIFY\_THREAT\_ABANDONED**
</dt> <dd>

No remediation occurred before the service was stopped.

</dd> <dt>

<span id="MPNOTIFY_THREAT_CLEAN_EVENT_START"></span><span id="mpnotify_threat_clean_event_start"></span>**MPNOTIFY\_THREAT\_CLEAN\_EVENT\_START**
</dt> <dd>

A cleaning action has been started.

</dd> <dt>

<span id="MPNOTIFY_THREAT_CLEAN_EVENT_COMPLETE"></span><span id="mpnotify_threat_clean_event_complete"></span>**MPNOTIFY\_THREAT\_CLEAN\_EVENT\_COMPLETE**
</dt> <dd>

A cleaning action has ended.

</dd> <dt>

<span id="MPNOTIFY_SIGUPDATE_START"></span><span id="mpnotify_sigupdate_start"></span>**MPNOTIFY\_SIGUPDATE\_START**
</dt> <dd>

Signature update started.

</dd> <dt>

<span id="MPNOTIFY_SIGUPDATE_SEARCH_START"></span><span id="mpnotify_sigupdate_search_start"></span>**MPNOTIFY\_SIGUPDATE\_SEARCH\_START**
</dt> <dd>

Search for updates started.

</dd> <dt>

<span id="MPNOTIFY_SIGUPDATE_SEARCH_COMPLETE"></span><span id="mpnotify_sigupdate_search_complete"></span>**MPNOTIFY\_SIGUPDATE\_SEARCH\_COMPLETE**
</dt> <dd>

Search for updates completed.

</dd> <dt>

<span id="MPNOTIFY_SIGUPDATE_SOFTWARE_UPDATE_AVAILABLE"></span><span id="mpnotify_sigupdate_software_update_available"></span>**MPNOTIFY\_SIGUPDATE\_SOFTWARE\_UPDATE\_AVAILABLE**
</dt> <dd>

Software update available.

</dd> <dt>

<span id="MPNOTIFY_SIGUPDATE_DOWNLOAD_START"></span><span id="mpnotify_sigupdate_download_start"></span>**MPNOTIFY\_SIGUPDATE\_DOWNLOAD\_START**
</dt> <dd>

Download started.

</dd> <dt>

<span id="MPNOTIFY_SIGUPDATE_DOWNLOAD_PROGRESS"></span><span id="mpnotify_sigupdate_download_progress"></span>**MPNOTIFY\_SIGUPDATE\_DOWNLOAD\_PROGRESS**
</dt> <dd>

Download in progress. Callback data contains progress.

</dd> <dt>

<span id="MPNOTIFY_SIGUPDATE_DOWNLOAD_COMPLETE"></span><span id="mpnotify_sigupdate_download_complete"></span>**MPNOTIFY\_SIGUPDATE\_DOWNLOAD\_COMPLETE**
</dt> <dd>

Download completed.

</dd> <dt>

<span id="MPNOTIFY_SIGUPDATE_INSTALL_START"></span><span id="mpnotify_sigupdate_install_start"></span>**MPNOTIFY\_SIGUPDATE\_INSTALL\_START**
</dt> <dd>

Installation started.

</dd> <dt>

<span id="MPNOTIFY_SIGUPDATE_INSTALL_PROGRESS"></span><span id="mpnotify_sigupdate_install_progress"></span>**MPNOTIFY\_SIGUPDATE\_INSTALL\_PROGRESS**
</dt> <dd>

Installation in progress. Callback data contains progress.

</dd> <dt>

<span id="MPNOTIFY_SIGUPDATE_INSTALL_COMPLETE"></span><span id="mpnotify_sigupdate_install_complete"></span>**MPNOTIFY\_SIGUPDATE\_INSTALL\_COMPLETE**
</dt> <dd>

Installation complete.

</dd> <dt>

<span id="MPNOTIFY_SIGUPDATE_REBOOT_REQUIRED"></span><span id="mpnotify_sigupdate_reboot_required"></span>**MPNOTIFY\_SIGUPDATE\_REBOOT\_REQUIRED**
</dt> <dd>

Update requires reboot.

</dd> <dt>

<span id="MPNOTIFY_SIGUPDATE_REQUEST_PROCESSED"></span><span id="mpnotify_sigupdate_request_processed"></span>**MPNOTIFY\_SIGUPDATE\_REQUEST\_PROCESSED**
</dt> <dd>

Service processed a signature update request. Failure or success is indicated by **hResult** in the callback data.

</dd> <dt>

<span id="MPNOTIFY_SIGUPDATE_COMPLETE"></span><span id="mpnotify_sigupdate_complete"></span>**MPNOTIFY\_SIGUPDATE\_COMPLETE**
</dt> <dd>

Update complete. **S\_FALSE** status indicates that no updates were needed.

</dd> <dt>

<span id="MPNOTIFY_SAMPLE_START"></span><span id="mpnotify_sample_start"></span>**MPNOTIFY\_SAMPLE\_START**
</dt> <dd>

Sample submission started.

</dd> <dt>

<span id="MPNOTIFY_SAMPLE_COMPLETE"></span><span id="mpnotify_sample_complete"></span>**MPNOTIFY\_SAMPLE\_COMPLETE**
</dt> <dd>

Sample submission completed.

</dd> <dt>

<span id="MPNOTIFY_SAMPLE_ITEM_START"></span><span id="mpnotify_sample_item_start"></span>**MPNOTIFY\_SAMPLE\_ITEM\_START**
</dt> <dd>

Specific sample item submission started. Sample item index is available in [**MPSAMPLE\_DATA**](mpsample-data.md).

</dd> <dt>

<span id="MPNOTIFY_SAMPLE_ITEM_SUCCEEDED"></span><span id="mpnotify_sample_item_succeeded"></span>**MPNOTIFY\_SAMPLE\_ITEM\_SUCCEEDED**
</dt> <dd>

Specific sample item submission succeeded.

</dd> <dt>

<span id="MPNOTIFY_SAMPLE_ITEM_FAILED"></span><span id="mpnotify_sample_item_failed"></span>**MPNOTIFY\_SAMPLE\_ITEM\_FAILED**
</dt> <dd>

Specific sample item submission failed. Error code is available in [**MPCALLBACK\_DATA**](mpcallback-data.md).

</dd> <dt>

<span id="MPNOTIFY_RESERVED_DATA"></span><span id="mpnotify_reserved_data"></span>**MPNOTIFY\_RESERVED\_DATA**
</dt> <dd>

Internal reserved data.

</dd> <dt>

<span id="MPNOTIFY_FASTPATH_SIG_ADDED"></span><span id="mpnotify_fastpath_sig_added"></span>**MPNOTIFY\_FASTPATH\_SIG\_ADDED**
</dt> <dd>

A Fastpath signature has either added or disabled a signature.

</dd> <dt>

<span id="MPNOTIFY_FASTPATH_SIG_REMOVED"></span><span id="mpnotify_fastpath_sig_removed"></span>**MPNOTIFY\_FASTPATH\_SIG\_REMOVED**
</dt> <dd>

A FastPath signature has been removed.

</dd> <dt>

<span id="MPNOTIFY_NIS_PRIVATE"></span><span id="mpnotify_nis_private"></span>**MPNOTIFY\_NIS\_PRIVATE**
</dt> <dd>

NIS private notifcations. No partners should register for this.

</dd> <dt>

<span id="MPNOTIFY_HEALTH_CHANGE"></span><span id="mpnotify_health_change"></span>**MPNOTIFY\_HEALTH\_CHANGE**
</dt> <dd>

The AM service has entered a new state.

</dd> <dt>

<span id="MPNOTIFY_HEALTH_RECOVERY"></span><span id="mpnotify_health_recovery"></span>**MPNOTIFY\_HEALTH\_RECOVERY**
</dt> <dd>

The AM service has recovered from a state.

</dd> <dt>

<span id="MPNOTIFY_HEALTH_START"></span><span id="mpnotify_health_start"></span>**MPNOTIFY\_HEALTH\_START**
</dt> <dd>

The AM service has initialized the health of the system.

</dd> <dt>

<span id="MPNOTIFY_ENDOFLIFE_CHANGE"></span><span id="mpnotify_endoflife_change"></span>**MPNOTIFY\_ENDOFLIFE\_CHANGE**
</dt> <dd>

The "End Of Life" expiry dates for the AM service have changed.

</dd> <dt>

<span id="MPNOTIFY_MALWARETOAST_DATA"></span><span id="mpnotify_malwaretoast_data"></span>**MPNOTIFY\_MALWARETOAST\_DATA**
</dt> <dd>

The AM service has encountered malware that might have caused critical settings change in the machine.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



## See also

<dl> <dt>

[**MpManagerStatusQueryEx**](mpmanagerstatusqueryex.md)
</dt> <dt>

[**MPCALLBACK\_DATA**](mpcallback-data.md)
</dt> <dt>

[**MPSAMPLE\_DATA**](mpsample-data.md)
</dt> </dl>

 

 





