---
title: Adapter Workflow
description: This section describes the enrollment workflow from the perspective of the adapter plugins.
ms.assetid: 0392124A-78CF-49E3-A52A-1E2E3A100E2E
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Adapter Workflow

This section describes the enrollment workflow from the perspective of the adapter plugins.

In Windows 10, we ve implemented a V4 engine interface that provides 2 new engine adapter functions, [**EngineAdapterCreateKey**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_engine_create_key_fn?branch=master) and [**EngineAdapterIdentifyFeatureSetSecure**](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_engine_identify_feature_set_secure_fn?branch=master). These new functions allow support for secure biometrics using TPM 2.0. The following table shows the adapter-side enrollment workflow.



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
<td>[<strong>WinBioGetProperty(EXTENDED_ENGINE_INFO)</strong>](/windows/win32/Winbio/nf-winbio-winbiogetproperty?branch=master)</td>
<td>[<strong>EngineAdapterQueryExtendedInfo</strong>](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_engine_query_extended_info_fn?branch=master)</td>
</tr>
<tr class="odd">
<td>[<strong>WinBioEnrollBegin</strong>](/windows/win32/Winbio/nf-winbio-winbioenrollbegin?branch=master)</td>
<td><ol>
<li>[<strong>StorageAdapterQueryBySubject</strong>](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_query_by_subject_fn?branch=master)</li>
<li>[<strong>SensorAdapterClearContext</strong>](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_clear_context_fn?branch=master)</li>
<li>[<strong>EngineAdapterClearContext</strong>](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_engine_clear_context_fn?branch=master)</li>
<li>[<strong>StorageAdapterClearContext</strong>](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_clear_context_fn?branch=master)</li>
<li>[<strong>EngineAdapterCreateEnrollment</strong>](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_engine_create_enrollment_fn?branch=master)</li>
<li>[<strong>EngineAdapterSetEnrollmentParameters</strong>](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_engine_set_enrollment_parameters_fn?branch=master)</li>
</ol></td>
</tr>
<tr class="even">
<td>[<strong>WinBioEnrollCapture</strong>](/windows/win32/Winbio/nf-winbio-winbioenrollcapture?branch=master)</td>
<td><ol>
<li>[<strong>SensorAdapterStartCapture</strong>](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_start_capture_fn?branch=master)</li>
<li>[<strong>SensorAdapterFinishCapture</strong>](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_finish_capture_fn?branch=master)</li>
<li>[<strong>SensorAdapterPushDataToEngine</strong>](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_sensor_push_data_to_engine_fn?branch=master)<strong>[-&gt;</strong>[<strong>EngineAdapterAcceptSampleData</strong>](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_engine_accept_sample_data_fn?branch=master)]</li>
<li>If S_OK or WINBIO_I_MORE_DATA
<ol>
<li>[<strong>EngineAdapterUpdateEnrollment</strong>](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_engine_update_enrollment_fn?branch=master)</li>
<li>[Caller continues enrollment]</li>
</ol></li>
<li>Else if WINBIO_E_BAD_CAPTURE [Caller displays reject feedback, continues enrollment] <br/></li>
<li>Else if other ERROR
<ol>
<li>[<strong>EngineAdapterClearContext</strong>](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_engine_clear_context_fn?branch=master)</li>
<li>[<strong>StorageAdapterClearContext</strong>](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_clear_context_fn?branch=master)</li>
<li>[Bio service aborts enrollment]</li>
</ol></li>
</ol></td>
</tr>
<tr class="odd">
<td>[<strong>WinBioGetProperty (EXTENDED_ENROLLMENT_STATUS)</strong>](/windows/win32/Winbio/nf-winbio-winbiogetproperty?branch=master)</td>
<td>[<strong>EngineAdapterQueryExtendedEnrollmentStatus</strong>](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_engine_query_extended_enrollment_status_fn?branch=master)</td>
</tr>
<tr class="even">
<td>[<strong>WinBioEnrollCommit</strong>](/windows/win32/Winbio/nf-winbio-winbioenrollcommit?branch=master)</td>
<td><ol>
<li>[<strong>EngineAdapterCheckForDuplicate</strong>](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_engine_check_for_duplicate_fn?branch=master)</li>
<li>If REMOVABLE DATABASE
<ol>
<li>[<strong>EngineAdapterGetEnrollmentHash</strong>](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_engine_get_enrollment_hash_fn?branch=master)</li>
<li>[<strong>EngineAdapterCommitEnrollment</strong>](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_engine_commit_enrollment_fn?branch=master)</li>
</ol></li>
<li>Else[<strong>EngineAdapterCommitEnrollment</strong>](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_engine_commit_enrollment_fn?branch=master)<br/></li>
</ol></td>
</tr>
<tr class="odd">
<td>[<strong>WinBioEnrollDiscard</strong>](/windows/win32/Winbio/nf-winbio-winbioenrolldiscard?branch=master)</td>
<td><ol>
<li>[<strong>EngineAdapterDiscardEnrollment</strong>](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_engine_discard_enrollment_fn?branch=master)</li>
<li>[<strong>EngineAdapterClearContext</strong>](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_engine_clear_context_fn?branch=master)</li>
<li>[<strong>StorageAdapterClearContext</strong>](/windows/win32/Winbio_adapter/nc-winbio_adapter-pibio_storage_clear_context_fn?branch=master)</li>
</ol></td>
</tr>
</tbody>
</table>



 

 

 





