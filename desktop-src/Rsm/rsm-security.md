---
Description: RSM provides security for media pool and library objects.
ms.assetid: 9a0dd513-f8c0-454f-be3a-fbea7c865994
title: RSM Security
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RSM Security

\[[Removable Storage Manager](removable-storage-manager.md) is no longer available as of Windows 7 and Windows Server 2008 R2.\]

RSM provides security for media pool and library objects. Media pool security controls access to media, including physical media, sides, and logical media. When you use nested media pools, the security of the lowest-level media pool determines the security of the media objects. Library security controls access to physical library units, including drives, changers, slots, and insert or eject ports.

Applications can use the [**SetNtmsObjectSecurity**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-setntmsobjectsecurity) and [**GetNtmsObjectSecurity**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-getntmsobjectsecurity) functions to set and check security for an RSM object.

The tables in this topic identify the security requirements for the RSM functions. They use the following key:

<dl> U = NTMS\_USE\_ACCESS  
M = NTMS\_MODIFY\_ACCESS  
C = NTMS\_CONTROL\_ACCESS  
R = READ\_CONTROL  
W = WRITE\_DAC  
</dl>

The following table identifies the RSM functions and their security requirements.



<table>
<thead>
<tr class="header">
<th>Function</th>
<th>Media Pool</th>
<th>Library</th>
<th>Computer</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>AccessNtmsLibraryDoor</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-accessntmslibrarydoor)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>AddNtmsMediaType</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-addntmsmediatype)</td>

<td>M</td>

</tr>
<tr class="odd">
<td>[<strong>AllocateNtmsMedia</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-allocatentmsmedia)</td>
<td>C</td>


</tr>
<tr class="even">
<td>[<strong>CancelNtmsLibraryRequest</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-cancelntmslibraryrequest)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>CancelNtmsOperatorRequest</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-cancelntmsoperatorrequest)</td>


<td>C</td>
</tr>
<tr class="even">
<td>[<strong>ChangeNtmsMediaType</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-changentmsmediatype)</td>
<td>M</td>

<td>M</td>
</tr>
<tr class="odd">
<td>[<strong>CleanNtmsDrive</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-cleanntmsdrive)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>CreateNtmsMedia</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-createntmsmediaa)</td>
<td>M</td>

<td>M</td>
</tr>
<tr class="odd">
<td>[<strong>CreateNtmsMediaPool</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-createntmsmediapool)</td>
<td>C</td>


</tr>
<tr class="even">
<td>[<strong>DeallocateNtmsMedia</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-deallocatentmsmedia)</td>
<td>C</td>


</tr>
<tr class="odd">
<td>[<strong>DecommissionNtmsMedia</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-decommissionntmsmedia)</td>
<td>C</td>


</tr>
<tr class="even">
<td>[<strong>DeleteNtmsDrive</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-deletentmsdrive)</td>

<td>M</td>

</tr>
<tr class="odd">
<td>[<strong>DeleteNtmsLibrary</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-deletentmslibrary)</td>

<td>M</td>

</tr>
<tr class="even">
<td>[<strong>DeleteNtmsMedia</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-deletentmsmedia)</td>
<td>M</td>

<td>M</td>
</tr>
<tr class="odd">
<td>[<strong>DeleteNtmsMediaPool</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-deletentmsmediapool)</td>
<td>M</td>


</tr>
<tr class="even">
<td>[<strong>DeleteNtmsMediaType</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-deletentmsmediatype)</td>

<td>M</td>

</tr>
<tr class="odd">
<td>[<strong>DeleteNtmsRequests</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-deletentmsrequests)</td>


<td>M</td>
</tr>
<tr class="even">
<td>[<strong>DisableNtmsObject</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-disablentmsobject)</td>

<td>M</td>

</tr>
<tr class="odd">
<td>[<strong>DismountNtmsDrive</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-dismountntmsdrive)</td>

<td>M</td>

</tr>
<tr class="even">
<td>[<strong>DismountNtmsMedia</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-dismountntmsmedia)</td>
<td>U</td>
<td>U</td>

</tr>
<tr class="odd">
<td>[<strong>EjectNtmsCleaner</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-ejectntmscleaner)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>EjectNtmsMedia</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-ejectntmsmedia)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>EnableNtmsObject</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-enablentmsobject)</td>

<td>M</td>

</tr>
<tr class="even">
<td>[<strong>ExportNtmsDatabase</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-exportntmsdatabase)</td>


<td>C</td>
</tr>
<tr class="odd">
<td>[<strong>GetNtmsObjectAttribute</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-getntmsobjectattributea)<dl> NTMS_CHANGER<br />
NTMS_CHANGER_TYPE<br />
NTMS_COMPUTER<br />
NTMS_DRIVE<br />
NTMS_DRIVE_TYPE<br />
NTMS_IEDOOR<br />
NTMS_IEPORT<br />
NTMS_LIBRARY<br />
NTMS_LIBREQUEST<br />
NTMS_LOGICAL_MEDIA<br />
NTMS_MEDIA_POOL<br />
NTMS_MEDIA_TYPE<br />
NTMS_OPREQUEST<br />
NTMS_PARTITION<br />
NTMS_PHYSICAL_MEDIA<br />
NTMS_STORAGESLOT<br />
</dl></td>
<td><dl><br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
U<br />
U<br />
<br />
<br />
U<br />
U<br />
</dl></td>
<td><dl><br />
U<br />
<br />
<br />
U<br />
<br />
U<br />
U<br />
U<br />
U<br />
<br />
<br />
<br />
<br />
<br />
<br />
U<br />
</dl></td>
<td><dl><br />
<br />
U<br />
U<br />
<br />
U<br />
<br />
<br />
<br />
<br />
<br />
<br />
U<br />
U<br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>GetNtmsObjectInformation</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-getntmsobjectinformation)<dl> NTMS_CHANGER<br />
NTMS_CHANGER_TYPE<br />
NTMS_COMPUTER<br />
NTMS_DRIVE<br />
NTMS_DRIVE_TYPE<br />
NTMS_IEDOOR<br />
NTMS_IEPORT<br />
NTMS_LIBRARY<br />
NTMS_LIBREQUEST<br />
NTMS_LOGICAL_MEDIA<br />
NTMS_MEDIA_TYPE<br />
NTMS_OPREQUEST<br />
NTMS_PARTITION<br />
NTMS_PHYSICAL_MEDIA<br />
NTMS_STORAGESLOT<br />
</dl></td>
<td><dl><br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
U<br />
<br />
<br />
U<br />
U<br />
</dl></td>
<td><dl><br />
U<br />
<br />
<br />
U<br />
<br />
U<br />
U<br />
U<br />
U<br />
<br />
<br />
<br />
<br />
<br />
U<br />
</dl></td>
<td><dl><br />
<br />
U<br />
U<br />
<br />
U<br />
<br />
<br />
<br />
<br />
<br />
U<br />
U<br />
</dl></td>
</tr>
<tr class="odd">
<td>[<strong>GetNtmsObjectSecurity</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-getntmsobjectsecurity)<dl> NTMS_CHANGER<br />
NTMS_CHANGER_TYPE<br />
NTMS_COMPUTER<br />
NTMS_DRIVE<br />
NTMS_DRIVE_TYPE<br />
NTMS_IEDOOR<br />
NTMS_IEPORT<br />
NTMS_LIBRARY<br />
NTMS_LIBREQUEST<br />
NTMS_LOGICAL_MEDIA<br />
NTMS_MEDIA_POOL<br />
NTMS_MEDIA_TYPE<br />
NTMS_OPREQUEST<br />
NTMS_PARTITION<br />
NTMS_PHYSICAL_MEDIA<br />
NTMS_STORAGESLOT<br />
</dl></td>
<td><dl><br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
R<br />
R<br />
<br />
<br />
R<br />
R<br />
</dl></td>
<td><dl><br />
R<br />
<br />
<br />
R<br />
<br />
R<br />
R<br />
R<br />
R<br />
<br />
<br />
<br />
<br />
<br />
<br />
R<br />
</dl></td>
<td><dl><br />
<br />
R<br />
R<br />
<br />
R<br />
<br />
<br />
<br />
<br />
<br />
<br />
R<br />
R<br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>GetNtmsRequestOrder</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-getntmsrequestorder)</td>


<td>C</td>
</tr>
<tr class="odd">
<td>[<strong>GetNtmsUIOptions</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-getntmsuioptionsa)<dl> NTMS_COMPUTER<br />
NTMS_LIBRARY<br />
</dl></td>

<td><dl><br />
<br />
U<br />
</dl></td>
<td><dl><br />
U<br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>IdentifyNtmsSlot</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-identifyntmsslot)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>ImportNtmsDatabase</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-importntmsdatabase)</td>


<td>C</td>
</tr>
<tr class="even">
<td>[<strong>InjectNtmsCleaner</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-injectntmscleaner)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>InjectNtmsMedia</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-injectntmsmedia)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>InventoryNtmsLibrary</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-inventoryntmslibrary)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>MountNtmsMedia</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-mountntmsmedia)</td>
<td>U</td>
<td>U</td>

</tr>
<tr class="even">
<td>[<strong>MoveToNtmsMediaPool</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-movetontmsmediapool)</td>
<td>C</td>


</tr>
<tr class="odd">
<td>[<strong>OpenNtmsNotification</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-openntmsnotification)</td>


<td>U</td>
</tr>
<tr class="even">
<td>[<strong>OpenNtmsSession</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-openntmssessiona)</td>


<td>U</td>
</tr>
<tr class="odd">
<td>[<strong>ReleaseNtmsCleanerSlot</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-releasentmscleanerslot)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>ReserveNtmsCleanerSlot</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-reserventmscleanerslot)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>SatisfyNtmsOperatorRequest</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-satisfyntmsoperatorrequest)</td>


<td>C</td>
</tr>
<tr class="even">
<td>[<strong>SetNtmsMediaComplete</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-setntmsmediacomplete)</td>
<td>C</td>


</tr>
<tr class="odd">
<td>[<strong>SetNtmsObjectAttribute</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-setntmsobjectattributea)<dl> NTMS_CHANGER<br />
NTMS_CHANGER_TYPE<br />
NTMS_COMPUTER<br />
NTMS_DRIVE<br />
NTMS_DRIVE_TYPE<br />
NTMS_IEDOOR<br />
NTMS_IEPORT<br />
NTMS_LIBRARY<br />
NTMS_LIBREQUEST<br />
NTMS_LOGICAL_MEDIA<br />
NTMS_MEDIA_POOL<br />
NTMS_MEDIA_TYPE<br />
NTMS_OPREQUEST<br />
NTMS_PARTITION<br />
NTMS_PHYSICAL_MEDIA<br />
NTMS_STORAGESLOT<br />
</dl></td>
<td><dl><br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
M<br />
M<br />
<br />
<br />
M<br />
M<br />
</dl></td>
<td><dl><br />
M<br />
<br />
<br />
M<br />
<br />
M<br />
M<br />
M<br />
M<br />
<br />
<br />
<br />
<br />
<br />
<br />
M<br />
</dl></td>
<td><dl><br />
<br />
M<br />
M<br />
<br />
M<br />
<br />
<br />
<br />
<br />
<br />
<br />
M<br />
M<br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>SetNtmsObjectInformation</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-setntmsobjectinformation)<dl> NTMS_CHANGER<br />
NTMS_CHANGER_TYPE<br />
NTMS_COMPUTER<br />
NTMS_DRIVE<br />
NTMS_DRIVE_TYPE<br />
NTMS_IEDOOR<br />
NTMS_IEPORT<br />
NTMS_LIBRARY<br />
NTMS_LIBREQUEST<br />
NTMS_LOGICAL_MEDIA<br />
NTMS_MEDIA_POOL<br />
NTMS_MEDIA_TYPE<br />
NTMS_OPREQUEST<br />
NTMS_PARTITION<br />
NTMS_PHYSICAL_MEDIA<br />
NTMS_STORAGESLOT<br />
</dl></td>
<td><dl><br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
M<br />
M<br />
<br />
<br />
M<br />
M<br />
</dl></td>
<td><dl><br />
M<br />
<br />
<br />
M<br />
<br />
M<br />
M<br />
C<br />
M<br />
<br />
<br />
<br />
<br />
<br />
<br />
M<br />
</dl></td>
<td><dl><br />
<br />
M<br />
M<br />
<br />
M<br />
<br />
<br />
<br />
<br />
<br />
<br />
M<br />
M<br />
</dl></td>
</tr>
<tr class="odd">
<td>[<strong>SetNtmsObjectSecurity</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-setntmsobjectsecurity)<dl> NTMS_CHANGER<br />
NTMS_CHANGER_TYPE<br />
NTMS_COMPUTER<br />
NTMS_DRIVE<br />
NTMS_DRIVE_TYPE<br />
NTMS_IEDOOR<br />
NTMS_IEPORT<br />
NTMS_LIBRARY<br />
NTMS_LIBREQUEST<br />
NTMS_LOGICAL_MEDIA<br />
NTMS_MEDIA_POOL<br />
NTMS_MEDIA_TYPE<br />
NTMS_OPREQUEST<br />
NTMS_PARTITION<br />
NTMS_PHYSICAL_MEDIA<br />
NTMS_STORAGESLOT<br />
</dl></td>
<td><dl><br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
W<br />
W<br />
<br />
<br />
W<br />
W<br />
</dl></td>
<td><dl><br />
W<br />
<br />
<br />
W<br />
<br />
W<br />
W<br />
W<br />
W<br />
<br />
<br />
<br />
<br />
<br />
<br />
W<br />
</dl></td>
<td><dl><br />
<br />
W<br />
W<br />
<br />
W<br />
<br />
<br />
<br />
<br />
<br />
<br />
W<br />
W<br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>SetNtmsRequestOrder</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-setntmsrequestorder)</td>


<td>C</td>
</tr>
<tr class="odd">
<td>[<strong>SetNtmsUIOptions</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-setntmsuioptionsa)<dl> NTMS_COMPUTER<br />
NTMS_LIBRARY<br />
</dl></td>

<td><dl><br />
<br />
U&amp;M<br />
</dl></td>
<td><dl><br />
U&amp;M<br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>SubmitNtmsOperatorRequest</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-submitntmsoperatorrequesta)<dl> NTMS_OPREQ_CLEANER<br />
NTMS_OPREQ_DEVICESERVICE<br />
NTMS_OPREQ_MESSAGE<br />
NTMS_OPREQ_MOVEMEDIA<br />
NTMS_OPREQ_NEWMEDIA<br />
</dl></td>
<td><dl><br />
<br />
<br />
<br />
C<br />
C<br />
</dl></td>
<td><dl><br />
C<br />
C<br />
<br />
<br />
<br />
</dl></td>
<td><dl><br />
<br />
<br />
U<br />
<br />
<br />
</dl></td>
</tr>
<tr class="odd">
<td>[<strong>SwapNtmsMedia</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-swapntmsmedia)</td>
<td>M</td>


</tr>
<tr class="even">
<td>[<strong>UpdateNtmsOmidInfo</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-updatentmsomidinfo)</td>

<td>C</td>

</tr>
</tbody>
</table>



 

**Windows XP:** The following table identifies the RSM functions and their security requirements.



<table>
<thead>
<tr class="header">
<th>Function</th>
<th>Media Pool</th>
<th>Library</th>
<th>Computer</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>AccessNtmsLibraryDoor</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-accessntmslibrarydoor)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>AddNtmsMediaType</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-addntmsmediatype)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>AllocateNtmsMedia</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-allocatentmsmedia)</td>
<td>M</td>


</tr>
<tr class="even">
<td>[<strong>CancelNtmsLibraryRequest</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-cancelntmslibraryrequest)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>CancelNtmsOperatorRequest</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-cancelntmsoperatorrequest)</td>


<td>C</td>
</tr>
<tr class="even">
<td>[<strong>ChangeNtmsMediaType</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-changentmsmediatype)</td>
<td>M</td>


</tr>
<tr class="odd">
<td>[<strong>CleanNtmsDrive</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-cleanntmsdrive)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>CreateNtmsMedia</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-createntmsmediaa)</td>
<td>C</td>
<td>M</td>

</tr>
<tr class="odd">
<td>[<strong>CreateNtmsMediaPool</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-createntmsmediapool)</td>
<td>M</td>


</tr>
<tr class="even">
<td>[<strong>DeallocateNtmsMedia</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-deallocatentmsmedia)</td>
<td>M</td>


</tr>
<tr class="odd">
<td>[<strong>DecommissionNtmsMedia</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-decommissionntmsmedia)</td>
<td>M</td>


</tr>
<tr class="even">
<td>[<strong>DeleteNtmsDrive</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-deletentmsdrive)</td>

<td>M</td>

</tr>
<tr class="odd">
<td>[<strong>DeleteNtmsLibrary</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-deletentmslibrary)</td>

<td>M</td>

</tr>
<tr class="even">
<td>[<strong>DeleteNtmsMedia</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-deletentmsmedia)</td>
<td>M</td>


</tr>
<tr class="odd">
<td>[<strong>DeleteNtmsMediaPool</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-deletentmsmediapool)</td>
<td>C</td>


</tr>
<tr class="even">
<td>[<strong>DeleteNtmsMediaType</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-deletentmsmediatype)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>DeleteNtmsRequests</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-deletentmsrequests)</td>


<td>C</td>
</tr>
<tr class="even">
<td>[<strong>DisableNtmsObject</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-disablentmsobject)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>DismountNtmsDrive</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-dismountntmsdrive)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>DismountNtmsMedia</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-dismountntmsmedia)</td>
<td>U</td>
<td>U</td>

</tr>
<tr class="odd">
<td>[<strong>EjectNtmsCleaner</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-ejectntmscleaner)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>EjectNtmsMedia</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-ejectntmsmedia)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>EnableNtmsObject</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-enablentmsobject)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>ExportNtmsDatabase</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-exportntmsdatabase)</td>


<td>C</td>
</tr>
<tr class="odd">
<td>[<strong>GetNtmsObjectInformation</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-getntmsobjectinformation)<dl> NTMS_CHANGER<br />
NTMS_CHANGER_TYPE<br />
NTMS_COMPUTER<br />
NTMS_DRIVE<br />
NTMS_DRIVE_TYPE<br />
NTMS_IEDOOR<br />
NTMS_IEPORT<br />
NTMS_LIBRARY<br />
NTMS_LIBREQUEST<br />
NTMS_LOGICAL_MEDIA<br />
NTMS_MEDIA_TYPE<br />
NTMS_OPREQUEST<br />
NTMS_PARTITION<br />
NTMS_PHYSICAL_MEDIA<br />
NTMS_STORAGESLOT<br />
</dl></td>
<td><dl><br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
C<br />
<br />
<br />
C<br />
C<br />
</dl></td>
<td><dl><br />
C<br />
<br />
<br />
C<br />
<br />
C<br />
C<br />
C<br />
M<br />
<br />
<br />
<br />
<br />
<br />
C<br />
</dl></td>
<td><dl><br />
<br />
M<br />
M<br />
<br />
M<br />
<br />
<br />
<br />
<br />
<br />
M<br />
M<br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>GetNtmsUIOptions</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-getntmsuioptionsa)<dl> NTMS_COMPUTER<br />
NTMS_LIBRARY<br />
</dl></td>

<td><dl><br />
<br />
U<br />
</dl></td>
<td><dl><br />
U<br />
</dl></td>
</tr>
<tr class="odd">
<td>[<strong>IdentifyNtmsSlot</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-identifyntmsslot)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>ImportNtmsDatabase</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-importntmsdatabase)</td>


<td>C</td>
</tr>
<tr class="odd">
<td>[<strong>InjectNtmsCleaner</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-injectntmscleaner)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>InjectNtmsMedia</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-injectntmsmedia)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>InventoryNtmsLibrary</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-inventoryntmslibrary)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>MountNtmsMedia</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-mountntmsmedia)</td>
<td>U</td>
<td>U</td>

</tr>
<tr class="odd">
<td>[<strong>MoveToNtmsMediaPool</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-movetontmsmediapool)</td>
<td>M</td>


</tr>
<tr class="even">
<td>[<strong>OpenNtmsSession</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-openntmssessiona)</td>


<td>U</td>
</tr>
<tr class="odd">
<td>[<strong>ReleaseNtmsCleanerSlot</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-releasentmscleanerslot)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>ReserveNtmsCleanerSlot</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-reserventmscleanerslot)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>SatisfyNtmsOperatorRequest</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-satisfyntmsoperatorrequest)</td>


<td>C</td>
</tr>
<tr class="even">
<td>[<strong>SetNtmsMediaComplete</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-setntmsmediacomplete)</td>
<td>M</td>


</tr>
<tr class="odd">
<td>[<strong>SetNtmsObjectInformation</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-setntmsobjectinformation)<dl> NTMS_LOGICAL_MEDIA<br />
NTMS_MEDIA_POOL<br />
NTMS_PARTITION<br />
NTMS_STORAGESLOT<br />
</dl></td>
<td><dl><br />
C<br />
C<br />
C<br />
</dl></td>
<td><dl><br />
<br />
<br />
<br />
C<br />
</dl></td>

</tr>
<tr class="even">
<td>[<strong>SetNtmsObjectSecurity</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-setntmsobjectsecurity)<dl> NTMS_CHANGER<br />
NTMS_CHANGER_TYPE<br />
NTMS_COMPUTER<br />
NTMS_DRIVE<br />
NTMS_DRIVE_TYPE<br />
NTMS_IEDOOR<br />
NTMS_IEPORT<br />
NTMS_LIBRARY<br />
NTMS_LIBREQUEST<br />
NTMS_LOGICAL_MEDIA<br />
NTMS_MEDIA_POOL<br />
NTMS_MEDIA_TYPE<br />
NTMS_OPREQUEST<br />
NTMS_PARTITION<br />
NTMS_PHYSICAL_MEDIA<br />
NTMS_STORAGESLOT<br />
</dl></td>
<td><dl><br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
W<br />
W<br />
<br />
<br />
W<br />
W<br />
</dl></td>
<td><dl><br />
W<br />
<br />
<br />
W<br />
<br />
W<br />
W<br />
W<br />
W<br />
<br />
<br />
<br />
<br />
<br />
<br />
W<br />
</dl></td>
<td><dl><br />
<br />
W<br />
W<br />
<br />
W<br />
<br />
<br />
<br />
<br />
<br />
<br />
W<br />
W<br />
</dl></td>
</tr>
<tr class="odd">
<td>[<strong>SetNtmsUIOptions</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-setntmsuioptionsa)<dl> NTMS_COMPUTER<br />
NTMS_LIBRARY<br />
</dl></td>

<td><dl><br />
<br />
U&amp;M<br />
</dl></td>
<td><dl><br />
U&amp;M<br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>SwapNtmsMedia</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-swapntmsmedia)</td>
<td>M</td>


</tr>
<tr class="odd">
<td>[<strong>UpdateNtmsOmidInfo</strong>](/windows/desktop/api/Ntmsapi/nf-ntmsapi-updatentmsomidinfo)</td>

<td>C</td>

</tr>
</tbody>
</table>



 

 

 



