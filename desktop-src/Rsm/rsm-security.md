---
Description: RSM provides security for media pool and library objects.
ms.assetid: 9a0dd513-f8c0-454f-be3a-fbea7c865994
title: RSM Security
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RSM Security

\[[Removable Storage Manager](removable-storage-manager.md) is no longer available as of Windows 7 and Windows Server 2008 R2.\]

RSM provides security for media pool and library objects. Media pool security controls access to media, including physical media, sides, and logical media. When you use nested media pools, the security of the lowest-level media pool determines the security of the media objects. Library security controls access to physical library units, including drives, changers, slots, and insert or eject ports.

Applications can use the [**SetNtmsObjectSecurity**](/windows/win32/Ntmsapi/nf-ntmsapi-setntmsobjectsecurity?branch=master) and [**GetNtmsObjectSecurity**](/windows/win32/Ntmsapi/nf-ntmsapi-getntmsobjectsecurity?branch=master) functions to set and check security for an RSM object.

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
<td>[<strong>AccessNtmsLibraryDoor</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-accessntmslibrarydoor?branch=master)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>AddNtmsMediaType</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-addntmsmediatype?branch=master)</td>

<td>M</td>

</tr>
<tr class="odd">
<td>[<strong>AllocateNtmsMedia</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-allocatentmsmedia?branch=master)</td>
<td>C</td>


</tr>
<tr class="even">
<td>[<strong>CancelNtmsLibraryRequest</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-cancelntmslibraryrequest?branch=master)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>CancelNtmsOperatorRequest</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-cancelntmsoperatorrequest?branch=master)</td>


<td>C</td>
</tr>
<tr class="even">
<td>[<strong>ChangeNtmsMediaType</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-changentmsmediatype?branch=master)</td>
<td>M</td>

<td>M</td>
</tr>
<tr class="odd">
<td>[<strong>CleanNtmsDrive</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-cleanntmsdrive?branch=master)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>CreateNtmsMedia</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-createntmsmediaa?branch=master)</td>
<td>M</td>

<td>M</td>
</tr>
<tr class="odd">
<td>[<strong>CreateNtmsMediaPool</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-createntmsmediapool?branch=master)</td>
<td>C</td>


</tr>
<tr class="even">
<td>[<strong>DeallocateNtmsMedia</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-deallocatentmsmedia?branch=master)</td>
<td>C</td>


</tr>
<tr class="odd">
<td>[<strong>DecommissionNtmsMedia</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-decommissionntmsmedia?branch=master)</td>
<td>C</td>


</tr>
<tr class="even">
<td>[<strong>DeleteNtmsDrive</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-deletentmsdrive?branch=master)</td>

<td>M</td>

</tr>
<tr class="odd">
<td>[<strong>DeleteNtmsLibrary</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-deletentmslibrary?branch=master)</td>

<td>M</td>

</tr>
<tr class="even">
<td>[<strong>DeleteNtmsMedia</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-deletentmsmedia?branch=master)</td>
<td>M</td>

<td>M</td>
</tr>
<tr class="odd">
<td>[<strong>DeleteNtmsMediaPool</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-deletentmsmediapool?branch=master)</td>
<td>M</td>


</tr>
<tr class="even">
<td>[<strong>DeleteNtmsMediaType</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-deletentmsmediatype?branch=master)</td>

<td>M</td>

</tr>
<tr class="odd">
<td>[<strong>DeleteNtmsRequests</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-deletentmsrequests?branch=master)</td>


<td>M</td>
</tr>
<tr class="even">
<td>[<strong>DisableNtmsObject</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-disablentmsobject?branch=master)</td>

<td>M</td>

</tr>
<tr class="odd">
<td>[<strong>DismountNtmsDrive</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-dismountntmsdrive?branch=master)</td>

<td>M</td>

</tr>
<tr class="even">
<td>[<strong>DismountNtmsMedia</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-dismountntmsmedia?branch=master)</td>
<td>U</td>
<td>U</td>

</tr>
<tr class="odd">
<td>[<strong>EjectNtmsCleaner</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-ejectntmscleaner?branch=master)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>EjectNtmsMedia</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-ejectntmsmedia?branch=master)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>EnableNtmsObject</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-enablentmsobject?branch=master)</td>

<td>M</td>

</tr>
<tr class="even">
<td>[<strong>ExportNtmsDatabase</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-exportntmsdatabase?branch=master)</td>


<td>C</td>
</tr>
<tr class="odd">
<td>[<strong>GetNtmsObjectAttribute</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-getntmsobjectattributea?branch=master)<dl> NTMS_CHANGER<br />
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
<td>[<strong>GetNtmsObjectInformation</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-getntmsobjectinformation?branch=master)<dl> NTMS_CHANGER<br />
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
<td>[<strong>GetNtmsObjectSecurity</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-getntmsobjectsecurity?branch=master)<dl> NTMS_CHANGER<br />
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
<td>[<strong>GetNtmsRequestOrder</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-getntmsrequestorder?branch=master)</td>


<td>C</td>
</tr>
<tr class="odd">
<td>[<strong>GetNtmsUIOptions</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-getntmsuioptionsa?branch=master)<dl> NTMS_COMPUTER<br />
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
<td>[<strong>IdentifyNtmsSlot</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-identifyntmsslot?branch=master)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>ImportNtmsDatabase</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-importntmsdatabase?branch=master)</td>


<td>C</td>
</tr>
<tr class="even">
<td>[<strong>InjectNtmsCleaner</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-injectntmscleaner?branch=master)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>InjectNtmsMedia</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-injectntmsmedia?branch=master)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>InventoryNtmsLibrary</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-inventoryntmslibrary?branch=master)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>MountNtmsMedia</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-mountntmsmedia?branch=master)</td>
<td>U</td>
<td>U</td>

</tr>
<tr class="even">
<td>[<strong>MoveToNtmsMediaPool</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-movetontmsmediapool?branch=master)</td>
<td>C</td>


</tr>
<tr class="odd">
<td>[<strong>OpenNtmsNotification</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-openntmsnotification?branch=master)</td>


<td>U</td>
</tr>
<tr class="even">
<td>[<strong>OpenNtmsSession</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-openntmssessiona?branch=master)</td>


<td>U</td>
</tr>
<tr class="odd">
<td>[<strong>ReleaseNtmsCleanerSlot</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-releasentmscleanerslot?branch=master)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>ReserveNtmsCleanerSlot</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-reserventmscleanerslot?branch=master)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>SatisfyNtmsOperatorRequest</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-satisfyntmsoperatorrequest?branch=master)</td>


<td>C</td>
</tr>
<tr class="even">
<td>[<strong>SetNtmsMediaComplete</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-setntmsmediacomplete?branch=master)</td>
<td>C</td>


</tr>
<tr class="odd">
<td>[<strong>SetNtmsObjectAttribute</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-setntmsobjectattributea?branch=master)<dl> NTMS_CHANGER<br />
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
<td>[<strong>SetNtmsObjectInformation</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-setntmsobjectinformation?branch=master)<dl> NTMS_CHANGER<br />
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
<td>[<strong>SetNtmsObjectSecurity</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-setntmsobjectsecurity?branch=master)<dl> NTMS_CHANGER<br />
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
<td>[<strong>SetNtmsRequestOrder</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-setntmsrequestorder?branch=master)</td>


<td>C</td>
</tr>
<tr class="odd">
<td>[<strong>SetNtmsUIOptions</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-setntmsuioptionsa?branch=master)<dl> NTMS_COMPUTER<br />
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
<td>[<strong>SubmitNtmsOperatorRequest</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-submitntmsoperatorrequesta?branch=master)<dl> NTMS_OPREQ_CLEANER<br />
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
<td>[<strong>SwapNtmsMedia</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-swapntmsmedia?branch=master)</td>
<td>M</td>


</tr>
<tr class="even">
<td>[<strong>UpdateNtmsOmidInfo</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-updatentmsomidinfo?branch=master)</td>

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
<td>[<strong>AccessNtmsLibraryDoor</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-accessntmslibrarydoor?branch=master)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>AddNtmsMediaType</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-addntmsmediatype?branch=master)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>AllocateNtmsMedia</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-allocatentmsmedia?branch=master)</td>
<td>M</td>


</tr>
<tr class="even">
<td>[<strong>CancelNtmsLibraryRequest</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-cancelntmslibraryrequest?branch=master)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>CancelNtmsOperatorRequest</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-cancelntmsoperatorrequest?branch=master)</td>


<td>C</td>
</tr>
<tr class="even">
<td>[<strong>ChangeNtmsMediaType</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-changentmsmediatype?branch=master)</td>
<td>M</td>


</tr>
<tr class="odd">
<td>[<strong>CleanNtmsDrive</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-cleanntmsdrive?branch=master)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>CreateNtmsMedia</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-createntmsmediaa?branch=master)</td>
<td>C</td>
<td>M</td>

</tr>
<tr class="odd">
<td>[<strong>CreateNtmsMediaPool</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-createntmsmediapool?branch=master)</td>
<td>M</td>


</tr>
<tr class="even">
<td>[<strong>DeallocateNtmsMedia</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-deallocatentmsmedia?branch=master)</td>
<td>M</td>


</tr>
<tr class="odd">
<td>[<strong>DecommissionNtmsMedia</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-decommissionntmsmedia?branch=master)</td>
<td>M</td>


</tr>
<tr class="even">
<td>[<strong>DeleteNtmsDrive</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-deletentmsdrive?branch=master)</td>

<td>M</td>

</tr>
<tr class="odd">
<td>[<strong>DeleteNtmsLibrary</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-deletentmslibrary?branch=master)</td>

<td>M</td>

</tr>
<tr class="even">
<td>[<strong>DeleteNtmsMedia</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-deletentmsmedia?branch=master)</td>
<td>M</td>


</tr>
<tr class="odd">
<td>[<strong>DeleteNtmsMediaPool</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-deletentmsmediapool?branch=master)</td>
<td>C</td>


</tr>
<tr class="even">
<td>[<strong>DeleteNtmsMediaType</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-deletentmsmediatype?branch=master)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>DeleteNtmsRequests</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-deletentmsrequests?branch=master)</td>


<td>C</td>
</tr>
<tr class="even">
<td>[<strong>DisableNtmsObject</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-disablentmsobject?branch=master)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>DismountNtmsDrive</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-dismountntmsdrive?branch=master)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>DismountNtmsMedia</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-dismountntmsmedia?branch=master)</td>
<td>U</td>
<td>U</td>

</tr>
<tr class="odd">
<td>[<strong>EjectNtmsCleaner</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-ejectntmscleaner?branch=master)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>EjectNtmsMedia</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-ejectntmsmedia?branch=master)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>EnableNtmsObject</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-enablentmsobject?branch=master)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>ExportNtmsDatabase</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-exportntmsdatabase?branch=master)</td>


<td>C</td>
</tr>
<tr class="odd">
<td>[<strong>GetNtmsObjectInformation</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-getntmsobjectinformation?branch=master)<dl> NTMS_CHANGER<br />
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
<td>[<strong>GetNtmsUIOptions</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-getntmsuioptionsa?branch=master)<dl> NTMS_COMPUTER<br />
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
<td>[<strong>IdentifyNtmsSlot</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-identifyntmsslot?branch=master)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>ImportNtmsDatabase</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-importntmsdatabase?branch=master)</td>


<td>C</td>
</tr>
<tr class="odd">
<td>[<strong>InjectNtmsCleaner</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-injectntmscleaner?branch=master)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>InjectNtmsMedia</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-injectntmsmedia?branch=master)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>InventoryNtmsLibrary</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-inventoryntmslibrary?branch=master)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>MountNtmsMedia</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-mountntmsmedia?branch=master)</td>
<td>U</td>
<td>U</td>

</tr>
<tr class="odd">
<td>[<strong>MoveToNtmsMediaPool</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-movetontmsmediapool?branch=master)</td>
<td>M</td>


</tr>
<tr class="even">
<td>[<strong>OpenNtmsSession</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-openntmssessiona?branch=master)</td>


<td>U</td>
</tr>
<tr class="odd">
<td>[<strong>ReleaseNtmsCleanerSlot</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-releasentmscleanerslot?branch=master)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>ReserveNtmsCleanerSlot</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-reserventmscleanerslot?branch=master)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>SatisfyNtmsOperatorRequest</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-satisfyntmsoperatorrequest?branch=master)</td>


<td>C</td>
</tr>
<tr class="even">
<td>[<strong>SetNtmsMediaComplete</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-setntmsmediacomplete?branch=master)</td>
<td>M</td>


</tr>
<tr class="odd">
<td>[<strong>SetNtmsObjectInformation</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-setntmsobjectinformation?branch=master)<dl> NTMS_LOGICAL_MEDIA<br />
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
<td>[<strong>SetNtmsObjectSecurity</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-setntmsobjectsecurity?branch=master)<dl> NTMS_CHANGER<br />
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
<td>[<strong>SetNtmsUIOptions</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-setntmsuioptionsa?branch=master)<dl> NTMS_COMPUTER<br />
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
<td>[<strong>SwapNtmsMedia</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-swapntmsmedia?branch=master)</td>
<td>M</td>


</tr>
<tr class="odd">
<td>[<strong>UpdateNtmsOmidInfo</strong>](/windows/win32/Ntmsapi/nf-ntmsapi-updatentmsomidinfo?branch=master)</td>

<td>C</td>

</tr>
</tbody>
</table>



 

 

 



