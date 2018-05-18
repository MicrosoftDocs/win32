---
title: Adapter Workflow
description: This section describes the enrollment workflow from the perspective of the adapter plugins.
ms.assetid: '0392124A-78CF-49E3-A52A-1E2E3A100E2E'
---

# Adapter Workflow

This section describes the enrollment workflow from the perspective of the adapter plugins.

In Windows 10, we’ve implemented a V4 engine interface that provides 2 new engine adapter functions, [**EngineAdapterCreateKey**](engineadaptercreatekey.md) and [**EngineAdapterIdentifyFeatureSetSecure**](engineadapteridentifyfeaturesetsecure.md). These new functions allow support for secure biometrics using TPM 2.0. The following table shows the adapter-side enrollment workflow.



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
<td>[<strong>WinBioGetProperty(EXTENDED_ENGINE_INFO)</strong>](winbiogetproperty.md)</td>
<td>[<strong>EngineAdapterQueryExtendedInfo</strong>](engineadapterqueryextendedinfo.md)</td>
</tr>
<tr class="odd">
<td>[<strong>WinBioEnrollBegin</strong>](winbioenrollbegin.md)</td>
<td><ol>
<li>[<strong>StorageAdapterQueryBySubject</strong>](storageadapterquerybysubject.md)</li>
<li>[<strong>SensorAdapterClearContext</strong>](sensoradapterclearcontext.md)</li>
<li>[<strong>EngineAdapterClearContext</strong>](engineadapterclearcontext.md)</li>
<li>[<strong>StorageAdapterClearContext</strong>](storageadapterclearcontext.md)</li>
<li>[<strong>EngineAdapterCreateEnrollment</strong>](engineadaptercreateenrollment.md)</li>
<li>[<strong>EngineAdapterSetEnrollmentParameters</strong>](engineadaptersetenrollmentparameters.md)</li>
</ol></td>
</tr>
<tr class="even">
<td>[<strong>WinBioEnrollCapture</strong>](winbioenrollcapture.md)</td>
<td><ol>
<li>[<strong>SensorAdapterStartCapture</strong>](sensoradapterstartcapture.md)</li>
<li>[<strong>SensorAdapterFinishCapture</strong>](sensoradapterfinishcapture.md)</li>
<li>[<strong>SensorAdapterPushDataToEngine</strong>](sensoradapterpushdatatoengine.md)<strong>[-&gt;</strong>[<strong>EngineAdapterAcceptSampleData</strong>](engineadapteracceptsampledata.md)]</li>
<li>If S_OK or WINBIO_I_MORE_DATA
<ol>
<li>[<strong>EngineAdapterUpdateEnrollment</strong>](engineadapterupdateenrollment.md)</li>
<li>[Caller continues enrollment]</li>
</ol></li>
<li>Else if WINBIO_E_BAD_CAPTURE [Caller displays reject feedback, continues enrollment] <br/></li>
<li>Else if other ERROR
<ol>
<li>[<strong>EngineAdapterClearContext</strong>](engineadapterclearcontext.md)</li>
<li>[<strong>StorageAdapterClearContext</strong>](storageadapterclearcontext.md)</li>
<li>[Bio service aborts enrollment]</li>
</ol></li>
</ol></td>
</tr>
<tr class="odd">
<td>[<strong>WinBioGetProperty (EXTENDED_ENROLLMENT_STATUS)</strong>](winbiogetproperty.md)</td>
<td>[<strong>EngineAdapterQueryExtendedEnrollmentStatus</strong>](engineadapterqueryextendedenrollmentstatus.md)</td>
</tr>
<tr class="even">
<td>[<strong>WinBioEnrollCommit</strong>](winbioenrollcommit.md)</td>
<td><ol>
<li>[<strong>EngineAdapterCheckForDuplicate</strong>](engineadaptercheckforduplicate.md)</li>
<li>If REMOVABLE DATABASE
<ol>
<li>[<strong>EngineAdapterGetEnrollmentHash</strong>](engineadaptergetenrollmenthash.md)</li>
<li>[<strong>EngineAdapterCommitEnrollment</strong>](engineadaptercommitenrollment.md)</li>
</ol></li>
<li>Else[<strong>EngineAdapterCommitEnrollment</strong>](engineadaptercommitenrollment.md)<br/></li>
</ol></td>
</tr>
<tr class="odd">
<td>[<strong>WinBioEnrollDiscard</strong>](winbioenrolldiscard.md)</td>
<td><ol>
<li>[<strong>EngineAdapterDiscardEnrollment</strong>](engineadapterdiscardenrollment.md)</li>
<li>[<strong>EngineAdapterClearContext</strong>](engineadapterclearcontext.md)</li>
<li>[<strong>StorageAdapterClearContext</strong>](storageadapterclearcontext.md)</li>
</ol></td>
</tr>
</tbody>
</table>



 

 

 





