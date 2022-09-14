---
title: Delivery Optimization Return Values
description: The below constants represent return values that Delivery Optimization generates and HTTP return values that Delivery Optimization captures.
ms.assetid: 68AC4581-C748-49AB-A588-15816E534756
ms.topic: article
ms.date: 05/31/2018
---

# Delivery Optimization Return Values

The below constants represent return values that Delivery Optimization generates and HTTP return values that Delivery Optimization captures. All other return values that you can receive are COM, RPC, or converted Windows return values (Delivery Optimization uses the [HRESULT_FROM_WIN32](/windows/win32/api/winerror/nf-winerror-hresult_from_win32) macro to convert the Windows return values to HRESULT values).

<dl> <dt>

<span id="DO_E_NO_SERVICE__0x80d01001_"></span><span id="do_e_no_service__0x80d01001_"></span><span id="DO_E_NO_SERVICE__0X80D01001_"></span>DO_E_NO_SERVICE (0x80d01001)
</dt> <dd>

Delivery Optimization was unable to provide the service.

</dd> <dt>

<span id="DO_E_DOWNLOAD_NO_PROGRESS__0x80d02002_"></span><span id="do_e_download_no_progress__0x80d02002_"></span><span id="DO_E_DOWNLOAD_NO_PROGRESS__0X80D02002_"></span>DO_E_DOWNLOAD_NO_PROGRESS (0x80d02002)
</dt> <dd>

Download of a file saw no progress within the defined period.

</dd> <dt>

<span id="DO_E_JOB_NOT_FOUND__0x80d02003_"></span><span id="do_e_job_not_found__0x80d02003_"></span><span id="DO_E_JOB_NOT_FOUND__0X80D02003_"></span>DO_E_JOB_NOT_FOUND (0x80d02003)
</dt> <dd>

Job was not found, expecting a job to be present.

</dd> <dt>

<span id="DO_E_JOB_EMPTY__0x80d02004_"></span><span id="do_e_job_empty__0x80d02004_"></span><span id="DO_E_JOB_EMPTY__0X80D02004_"></span>DO_E_JOB_EMPTY (0x80d02004)
</dt> <dd>

There was no file in the job, expecting at least one file.

</dd> <dt>

<span id="DO_E_LOCALPATH_NOT_SET__0x80d0200d_"></span><span id="do_e_localpath_not_set__0x80d0200d_"></span><span id="DO_E_LOCALPATH_NOT_SET__0X80D0200D_"></span>DO_E_LOCALPATH_NOT_SET (0x80d0200d)
</dt> <dd>

There is no local file path specified for this download.

</dd> <dt>

<span id="DO_E_FILE_NOT_AVAILABLE__0x80d02010_"></span><span id="do_e_file_not_available__0x80d02010_"></span><span id="DO_E_FILE_NOT_AVAILABLE__0X80D02010_"></span>DO_E_FILE_NOT_AVAILABLE (0x80d02010)
</dt> <dd>

No file is available because no URL generated an error.

</dd> <dt>

<span id="DO_E_UNKNOWN_PROPERTY_ID__0x80d02011_"></span><span id="do_e_unknown_property_id__0x80d02011_"></span><span id="DO_E_UNKNOWN_PROPERTY_ID__0X80D02011_"></span>DO_E_UNKNOWN_PROPERTY_ID (0x80d02011)
</dt> <dd>

SetProperty() or GetProperty() called with an unknown property ID.

</dd> <dt>

<span id="DO_E_READ_ONLY_PROPERTY__0x80d02012_"></span><span id="do_e_read_only_property__0x80d02012_"></span><span id="DO_E_READ_ONLY_PROPERTY__0X80D02012_"></span>DO_E_READ_ONLY_PROPERTY (0x80d02012)
</dt> <dd>

Unable to call SetProperty() on a read-only property.

</dd> <dt>

<span id="DO_E_INVALID_STATE__0x80d02013_"></span><span id="do_e_invalid_state__0x80d02013_"></span><span id="DO_E_INVALID_STATE__0X80D02013_"></span>DO_E_INVALID_STATE (0x80d02013)
</dt> <dd>

The requested action is not allowed in the current job state. The job might have been canceled or completed transferring.

</dd> <dt>

<span id="DO_E_ERROR_INFORMATION_UNAVAILABLE__0x80d02014_"></span><span id="do_e_error_information_unavailable__0x80d02014_"></span><span id="DO_E_ERROR_INFORMATION_UNAVAILABLE__0X80D02014_"></span>DO_E_ERROR_INFORMATION_UNAVAILABLE (0x80d02014)
</dt> <dd>

No errors have occurred.

</dd> <dt>

<span id="DO_E_NO_DOWNLOAD_EXTSETTINGS__0x80d03002_"></span><span id="do_e_no_download_extsettings__0x80d03002_"></span><span id="DO_E_NO_DOWNLOAD_EXTSETTINGS__0X80D03002_"></span>DO_E_NO_DOWNLOAD_EXTSETTINGS (0x80d03002)
</dt> <dd>

Download job not allowed due to user/admin settings.

</dd> <dt>

<span id="DO_E_BLOCKED_BY_COST_TRANSFER_POLICY__0x80d03801_"></span><span id="do_e_blocked_by_cost_transfer_policy__0x80d03801_"></span><span id="DO_E_BLOCKED_BY_COST_TRANSFER_POLICY__0X80D03801_"></span>DO_E_BLOCKED_BY_COST_TRANSFER_POLICY (0x80d03801)
</dt> <dd>

Delivery Optimization paused the job due to cost policy restrictions.

</dd> <dt>

<span id="DO_E_BLOCKED_BY_CELLULAR_POLICY__0x80d03803_"></span><span id="do_e_blocked_by_cellular_policy__0x80d03803_"></span><span id="DO_E_BLOCKED_BY_CELLULAR_POLICY__0X80D03803_"></span>DO_E_BLOCKED_BY_CELLULAR_POLICY (0x80d03803)
</dt> <dd>

Delivery Optimization paused the job due to detection of cellular network and policy restrictions.

</dd> <dt>

<span id="DO_E_BLOCKED_BY_POWER_STATE__0x80d03804_"></span><span id="do_e_blocked_by_power_state__0x80d03804_"></span><span id="DO_E_BLOCKED_BY_POWER_STATE__0X80D03804_"></span>DO_E_BLOCKED_BY_POWER_STATE (0x80d03804)
</dt> <dd>

Delivery Optimization paused the job due to detection of power state change into non-AC mode.

</dd> <dt>

<span id="DO_E_BLOCKED_BY_NO_NETWORK__0x80d03805_"></span><span id="do_e_blocked_by_no_network__0x80d03805_"></span><span id="DO_E_BLOCKED_BY_NO_NETWORK__0X80D03805_"></span>DO_E_BLOCKED_BY_NO_NETWORK (0x80d03805)
</dt> <dd>

Delivery Optimization paused the job due to loss of network connectivity.

</dd> <dt>

<span id="DO_E_BLOCKED_BY_VPN_POLICY__0x80d03807_"></span><span id="do_e_blocked_by_vpn_policy__0x80d03807_"></span><span id="DO_E_BLOCKED_BY_VPN_POLICY__0X80D03807_"></span>DO_E_BLOCKED_BY_VPN_POLICY (0x80d03807)
</dt> <dd>

Delivery Optimization paused the completed job due to detection of VPN network.

</dd> <dt>

<span id="DO_E_BLOCKED_BY_CRITICAL_MEMORY_USAGE__0x80d03808_"></span><span id="do_e_blocked_by_critical_memory_usage__0x80d03808_"></span><span id="DO_E_BLOCKED_BY_CRITICAL_MEMORY_USAGE__0X80D03808_"></span>DO_E_BLOCKED_BY_CRITICAL_MEMORY_USAGE (0x80d03808)
</dt> <dd>

Delivery Optimization paused the completed job due to detection of critical memory usage on the system.

</dd> <dt>

<span id="DO_E_HTTP_BLOCKSIZE_MISMATCH__0x80d05001_"></span><span id="do_e_http_blocksize_mismatch__0x80d05001_"></span><span id="DO_E_HTTP_BLOCKSIZE_MISMATCH__0X80D05001_"></span>DO_E_HTTP_BLOCKSIZE_MISMATCH (0x80d05001)
</dt> <dd>

HTTP server returned a response with data size not equal to what was requested.

</dd> <dt>

<span id="DO_E_INVALID_RANGE__0x80d05010_"></span><span id="do_e_invalid_range__0x80d05010_"></span><span id="DO_E_INVALID_RANGE__0X80D05010_"></span>DO_E_INVALID_RANGE (0x80d05010)
</dt> <dd>

The specified byte range is invalid.

</dd> <dt>

<span id="DO_E_INSUFFICIENT_RANGE_SUPPORT__0x80d05011_"></span><span id="do_e_insufficient_range_support__0x80d05011_"></span><span id="DO_E_INSUFFICIENT_RANGE_SUPPORT__0X80D05011_"></span>DO_E_INSUFFICIENT_RANGE_SUPPORT (0x80d05011)
</dt> <dd>

The server does not support the necessary HTTP protocol. Delivery Optimization requires that the server support the Range protocol header.

</dd> <dt>

<span id="DO_E_OVERLAPPING_RANGES__0x80d05012_"></span><span id="do_e_overlapping_ranges__0x80d05012_"></span><span id="DO_E_OVERLAPPING_RANGES__0X80D05012_"></span>DO_E_OVERLAPPING_RANGES (0x80d05012)
</dt> <dd>

The list of byte ranges contains some overlapping ranges, which are not supported.

</dd> <dt>

<span id="DO_E_FATAL_CORE_ERROR__0x80d06802_"></span><span id="do_e_fatal_core_error__0x80d06802_"></span><span id="DO_E_FATAL_CORE_ERROR__0X80D06802_"></span>DO_E_FATAL_CORE_ERROR (0x80d06802)
</dt> <dd>

Fatal error encountered in core.

</dd> </dl>

 

 