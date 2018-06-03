---
title: Adapter Workflow
description: This section describes the enrollment workflow from the perspective of the adapter plugins.
ms.assetid: 0392124A-78CF-49E3-A52A-1E2E3A100E2E
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Adapter Workflow

This section describes the enrollment workflow from the perspective of the adapter plugins.

In Windows 10, we ve implemented a V4 engine interface that provides 2 new engine adapter functions, [**EngineAdapterCreateKey**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_create_key_fn) and [**EngineAdapterIdentifyFeatureSetSecure**](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_identify_feature_set_secure_fn). These new functions allow support for secure biometrics using TPM 2.0. The following table shows the adapter-side enrollment workflow.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Client API</td>
<td>Adapter Methods</td>
</tr>
<tr class="even">
<td>[<strong>WinBioGetProperty(EXTENDED_ENGINE_INFO)</strong>](/windows/desktop/api/Winbio/nf-winbio-winbiogetproperty)</td>
<td>[<strong>EngineAdapterQueryExtendedInfo</strong>](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_query_extended_info_fn)</td>
</tr>
<tr class="odd">
<td>[<strong>WinBioEnrollBegin</strong>](/windows/desktop/api/Winbio/nf-winbio-winbioenrollbegin)</td>
<td><ol>
<li>[<strong>StorageAdapterQueryBySubject</strong>](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_query_by_subject_fn)</li>
<li>[<strong>SensorAdapterClearContext</strong>](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_clear_context_fn)</li>
<li>[<strong>EngineAdapterClearContext</strong>](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_clear_context_fn)</li>
<li>[<strong>StorageAdapterClearContext</strong>](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_clear_context_fn)</li>
<li>[<strong>EngineAdapterCreateEnrollment</strong>](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_create_enrollment_fn)</li>
<li>[<strong>EngineAdapterSetEnrollmentParameters</strong>](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_set_enrollment_parameters_fn)</li>
</ol></td>
</tr>
<tr class="even">
<td>[<strong>WinBioEnrollCapture</strong>](/windows/desktop/api/Winbio/nf-winbio-winbioenrollcapture)</td>
<td><ol>
<li>[<strong>SensorAdapterStartCapture</strong>](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_start_capture_fn)</li>
<li>[<strong>SensorAdapterFinishCapture</strong>](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_finish_capture_fn)</li>
<li>[<strong>SensorAdapterPushDataToEngine</strong>](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_sensor_push_data_to_engine_fn)<strong>[-&gt;</strong>[<strong>EngineAdapterAcceptSampleData</strong>](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_accept_sample_data_fn)]</li>
<li>If S_OK or WINBIO_I_MORE_DATA
<ol>
<li>[<strong>EngineAdapterUpdateEnrollment</strong>](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_update_enrollment_fn)</li>
<li>[Caller continues enrollment]</li>
</ol></li>
<li>Else if WINBIO_E_BAD_CAPTURE [Caller displays reject feedback, continues enrollment] <br/></li>
<li>Else if other ERROR
<ol>
<li>[<strong>EngineAdapterClearContext</strong>](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_clear_context_fn)</li>
<li>[<strong>StorageAdapterClearContext</strong>](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_clear_context_fn)</li>
<li>[Bio service aborts enrollment]</li>
</ol></li>
</ol></td>
</tr>
<tr class="odd">
<td>[<strong>WinBioGetProperty (EXTENDED_ENROLLMENT_STATUS)</strong>](/windows/desktop/api/Winbio/nf-winbio-winbiogetproperty)</td>
<td>[<strong>EngineAdapterQueryExtendedEnrollmentStatus</strong>](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_query_extended_enrollment_status_fn)</td>
</tr>
<tr class="even">
<td>[<strong>WinBioEnrollCommit</strong>](/windows/desktop/api/Winbio/nf-winbio-winbioenrollcommit)</td>
<td><ol>
<li>[<strong>EngineAdapterCheckForDuplicate</strong>](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_check_for_duplicate_fn)</li>
<li>If REMOVABLE DATABASE
<ol>
<li>[<strong>EngineAdapterGetEnrollmentHash</strong>](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_get_enrollment_hash_fn)</li>
<li>[<strong>EngineAdapterCommitEnrollment</strong>](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_commit_enrollment_fn)</li>
</ol></li>
<li>Else[<strong>EngineAdapterCommitEnrollment</strong>](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_commit_enrollment_fn)<br/></li>
</ol></td>
</tr>
<tr class="odd">
<td>[<strong>WinBioEnrollDiscard</strong>](/windows/desktop/api/Winbio/nf-winbio-winbioenrolldiscard)</td>
<td><ol>
<li>[<strong>EngineAdapterDiscardEnrollment</strong>](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_discard_enrollment_fn)</li>
<li>[<strong>EngineAdapterClearContext</strong>](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_engine_clear_context_fn)</li>
<li>[<strong>StorageAdapterClearContext</strong>](/windows/desktop/api/Winbio_adapter/nc-winbio_adapter-pibio_storage_clear_context_fn)</li>
</ol></td>
</tr>
</tbody>
</table>



 

 

 





