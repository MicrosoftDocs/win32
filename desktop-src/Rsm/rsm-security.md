---
Description: 'RSM provides security for media pool and library objects.'
ms.assetid: '9a0dd513-f8c0-454f-be3a-fbea7c865994'
title: RSM Security
---

# RSM Security

\[[Removable Storage Manager](removable-storage-manager.md) is no longer available as of Windows 7 and Windows Server 2008 R2.\]

RSM provides security for media pool and library objects. Media pool security controls access to media, including physical media, sides, and logical media. When you use nested media pools, the security of the lowest-level media pool determines the security of the media objects. Library security controls access to physical library units, including drives, changers, slots, and insert or eject ports.

Applications can use the [**SetNtmsObjectSecurity**](setntmsobjectsecurity.md) and [**GetNtmsObjectSecurity**](getntmsobjectsecurity.md) functions to set and check security for an RSM object.

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
<td>[<strong>AccessNtmsLibraryDoor</strong>](accessntmslibrarydoor.md)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>AddNtmsMediaType</strong>](addntmsmediatype.md)</td>

<td>M</td>

</tr>
<tr class="odd">
<td>[<strong>AllocateNtmsMedia</strong>](allocatentmsmedia.md)</td>
<td>C</td>


</tr>
<tr class="even">
<td>[<strong>CancelNtmsLibraryRequest</strong>](cancelntmslibraryrequest.md)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>CancelNtmsOperatorRequest</strong>](cancelntmsoperatorrequest.md)</td>


<td>C</td>
</tr>
<tr class="even">
<td>[<strong>ChangeNtmsMediaType</strong>](changentmsmediatype.md)</td>
<td>M</td>

<td>M</td>
</tr>
<tr class="odd">
<td>[<strong>CleanNtmsDrive</strong>](cleanntmsdrive.md)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>CreateNtmsMedia</strong>](createntmsmedia.md)</td>
<td>M</td>

<td>M</td>
</tr>
<tr class="odd">
<td>[<strong>CreateNtmsMediaPool</strong>](createntmsmediapool.md)</td>
<td>C</td>


</tr>
<tr class="even">
<td>[<strong>DeallocateNtmsMedia</strong>](deallocatentmsmedia.md)</td>
<td>C</td>


</tr>
<tr class="odd">
<td>[<strong>DecommissionNtmsMedia</strong>](decommissionntmsmedia.md)</td>
<td>C</td>


</tr>
<tr class="even">
<td>[<strong>DeleteNtmsDrive</strong>](deletentmsdrive.md)</td>

<td>M</td>

</tr>
<tr class="odd">
<td>[<strong>DeleteNtmsLibrary</strong>](deletentmslibrary.md)</td>

<td>M</td>

</tr>
<tr class="even">
<td>[<strong>DeleteNtmsMedia</strong>](deletentmsmedia.md)</td>
<td>M</td>

<td>M</td>
</tr>
<tr class="odd">
<td>[<strong>DeleteNtmsMediaPool</strong>](deletentmsmediapool.md)</td>
<td>M</td>


</tr>
<tr class="even">
<td>[<strong>DeleteNtmsMediaType</strong>](deletentmsmediatype.md)</td>

<td>M</td>

</tr>
<tr class="odd">
<td>[<strong>DeleteNtmsRequests</strong>](deletentmsrequests.md)</td>


<td>M</td>
</tr>
<tr class="even">
<td>[<strong>DisableNtmsObject</strong>](disablentmsobject.md)</td>

<td>M</td>

</tr>
<tr class="odd">
<td>[<strong>DismountNtmsDrive</strong>](dismountntmsdrive.md)</td>

<td>M</td>

</tr>
<tr class="even">
<td>[<strong>DismountNtmsMedia</strong>](dismountntmsmedia.md)</td>
<td>U</td>
<td>U</td>

</tr>
<tr class="odd">
<td>[<strong>EjectNtmsCleaner</strong>](ejectntmscleaner.md)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>EjectNtmsMedia</strong>](ejectntmsmedia.md)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>EnableNtmsObject</strong>](enablentmsobject.md)</td>

<td>M</td>

</tr>
<tr class="even">
<td>[<strong>ExportNtmsDatabase</strong>](exportntmsdatabase.md)</td>


<td>C</td>
</tr>
<tr class="odd">
<td>[<strong>GetNtmsObjectAttribute</strong>](getntmsobjectattribute.md)<dl> NTMS_CHANGER<br />
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
<td>[<strong>GetNtmsObjectInformation</strong>](getntmsobjectinformation.md)<dl> NTMS_CHANGER<br />
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
<td>[<strong>GetNtmsObjectSecurity</strong>](getntmsobjectsecurity.md)<dl> NTMS_CHANGER<br />
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
<td>[<strong>GetNtmsRequestOrder</strong>](getntmsrequestorder.md)</td>


<td>C</td>
</tr>
<tr class="odd">
<td>[<strong>GetNtmsUIOptions</strong>](getntmsuioptions.md)<dl> NTMS_COMPUTER<br />
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
<td>[<strong>IdentifyNtmsSlot</strong>](identifyntmsslot.md)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>ImportNtmsDatabase</strong>](importntmsdatabase.md)</td>


<td>C</td>
</tr>
<tr class="even">
<td>[<strong>InjectNtmsCleaner</strong>](injectntmscleaner.md)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>InjectNtmsMedia</strong>](injectntmsmedia.md)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>InventoryNtmsLibrary</strong>](inventoryntmslibrary.md)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>MountNtmsMedia</strong>](mountntmsmedia.md)</td>
<td>U</td>
<td>U</td>

</tr>
<tr class="even">
<td>[<strong>MoveToNtmsMediaPool</strong>](movetontmsmediapool.md)</td>
<td>C</td>


</tr>
<tr class="odd">
<td>[<strong>OpenNtmsNotification</strong>](openntmsnotification.md)</td>


<td>U</td>
</tr>
<tr class="even">
<td>[<strong>OpenNtmsSession</strong>](openntmssession.md)</td>


<td>U</td>
</tr>
<tr class="odd">
<td>[<strong>ReleaseNtmsCleanerSlot</strong>](releasentmscleanerslot.md)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>ReserveNtmsCleanerSlot</strong>](reserventmscleanerslot.md)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>SatisfyNtmsOperatorRequest</strong>](satisfyntmsoperatorrequest.md)</td>


<td>C</td>
</tr>
<tr class="even">
<td>[<strong>SetNtmsMediaComplete</strong>](setntmsmediacomplete.md)</td>
<td>C</td>


</tr>
<tr class="odd">
<td>[<strong>SetNtmsObjectAttribute</strong>](setntmsobjectattribute.md)<dl> NTMS_CHANGER<br />
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
<td>[<strong>SetNtmsObjectInformation</strong>](setntmsobjectinformation.md)<dl> NTMS_CHANGER<br />
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
<td>[<strong>SetNtmsObjectSecurity</strong>](setntmsobjectsecurity.md)<dl> NTMS_CHANGER<br />
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
<td>[<strong>SetNtmsRequestOrder</strong>](setntmsrequestorder.md)</td>


<td>C</td>
</tr>
<tr class="odd">
<td>[<strong>SetNtmsUIOptions</strong>](setntmsuioptions.md)<dl> NTMS_COMPUTER<br />
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
<td>[<strong>SubmitNtmsOperatorRequest</strong>](submitntmsoperatorrequest.md)<dl> NTMS_OPREQ_CLEANER<br />
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
<td>[<strong>SwapNtmsMedia</strong>](swapntmsmedia.md)</td>
<td>M</td>


</tr>
<tr class="even">
<td>[<strong>UpdateNtmsOmidInfo</strong>](updatentmsomidinfo.md)</td>

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
<td>[<strong>AccessNtmsLibraryDoor</strong>](accessntmslibrarydoor.md)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>AddNtmsMediaType</strong>](addntmsmediatype.md)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>AllocateNtmsMedia</strong>](allocatentmsmedia.md)</td>
<td>M</td>


</tr>
<tr class="even">
<td>[<strong>CancelNtmsLibraryRequest</strong>](cancelntmslibraryrequest.md)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>CancelNtmsOperatorRequest</strong>](cancelntmsoperatorrequest.md)</td>


<td>C</td>
</tr>
<tr class="even">
<td>[<strong>ChangeNtmsMediaType</strong>](changentmsmediatype.md)</td>
<td>M</td>


</tr>
<tr class="odd">
<td>[<strong>CleanNtmsDrive</strong>](cleanntmsdrive.md)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>CreateNtmsMedia</strong>](createntmsmedia.md)</td>
<td>C</td>
<td>M</td>

</tr>
<tr class="odd">
<td>[<strong>CreateNtmsMediaPool</strong>](createntmsmediapool.md)</td>
<td>M</td>


</tr>
<tr class="even">
<td>[<strong>DeallocateNtmsMedia</strong>](deallocatentmsmedia.md)</td>
<td>M</td>


</tr>
<tr class="odd">
<td>[<strong>DecommissionNtmsMedia</strong>](decommissionntmsmedia.md)</td>
<td>M</td>


</tr>
<tr class="even">
<td>[<strong>DeleteNtmsDrive</strong>](deletentmsdrive.md)</td>

<td>M</td>

</tr>
<tr class="odd">
<td>[<strong>DeleteNtmsLibrary</strong>](deletentmslibrary.md)</td>

<td>M</td>

</tr>
<tr class="even">
<td>[<strong>DeleteNtmsMedia</strong>](deletentmsmedia.md)</td>
<td>M</td>


</tr>
<tr class="odd">
<td>[<strong>DeleteNtmsMediaPool</strong>](deletentmsmediapool.md)</td>
<td>C</td>


</tr>
<tr class="even">
<td>[<strong>DeleteNtmsMediaType</strong>](deletentmsmediatype.md)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>DeleteNtmsRequests</strong>](deletentmsrequests.md)</td>


<td>C</td>
</tr>
<tr class="even">
<td>[<strong>DisableNtmsObject</strong>](disablentmsobject.md)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>DismountNtmsDrive</strong>](dismountntmsdrive.md)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>DismountNtmsMedia</strong>](dismountntmsmedia.md)</td>
<td>U</td>
<td>U</td>

</tr>
<tr class="odd">
<td>[<strong>EjectNtmsCleaner</strong>](ejectntmscleaner.md)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>EjectNtmsMedia</strong>](ejectntmsmedia.md)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>EnableNtmsObject</strong>](enablentmsobject.md)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>ExportNtmsDatabase</strong>](exportntmsdatabase.md)</td>


<td>C</td>
</tr>
<tr class="odd">
<td>[<strong>GetNtmsObjectInformation</strong>](getntmsobjectinformation.md)<dl> NTMS_CHANGER<br />
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
<td>[<strong>GetNtmsUIOptions</strong>](getntmsuioptions.md)<dl> NTMS_COMPUTER<br />
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
<td>[<strong>IdentifyNtmsSlot</strong>](identifyntmsslot.md)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>ImportNtmsDatabase</strong>](importntmsdatabase.md)</td>


<td>C</td>
</tr>
<tr class="odd">
<td>[<strong>InjectNtmsCleaner</strong>](injectntmscleaner.md)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>InjectNtmsMedia</strong>](injectntmsmedia.md)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>InventoryNtmsLibrary</strong>](inventoryntmslibrary.md)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>MountNtmsMedia</strong>](mountntmsmedia.md)</td>
<td>U</td>
<td>U</td>

</tr>
<tr class="odd">
<td>[<strong>MoveToNtmsMediaPool</strong>](movetontmsmediapool.md)</td>
<td>M</td>


</tr>
<tr class="even">
<td>[<strong>OpenNtmsSession</strong>](openntmssession.md)</td>


<td>U</td>
</tr>
<tr class="odd">
<td>[<strong>ReleaseNtmsCleanerSlot</strong>](releasentmscleanerslot.md)</td>

<td>C</td>

</tr>
<tr class="even">
<td>[<strong>ReserveNtmsCleanerSlot</strong>](reserventmscleanerslot.md)</td>

<td>C</td>

</tr>
<tr class="odd">
<td>[<strong>SatisfyNtmsOperatorRequest</strong>](satisfyntmsoperatorrequest.md)</td>


<td>C</td>
</tr>
<tr class="even">
<td>[<strong>SetNtmsMediaComplete</strong>](setntmsmediacomplete.md)</td>
<td>M</td>


</tr>
<tr class="odd">
<td>[<strong>SetNtmsObjectInformation</strong>](setntmsobjectinformation.md)<dl> NTMS_LOGICAL_MEDIA<br />
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
<td>[<strong>SetNtmsObjectSecurity</strong>](setntmsobjectsecurity.md)<dl> NTMS_CHANGER<br />
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
<td>[<strong>SetNtmsUIOptions</strong>](setntmsuioptions.md)<dl> NTMS_COMPUTER<br />
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
<td>[<strong>SwapNtmsMedia</strong>](swapntmsmedia.md)</td>
<td>M</td>


</tr>
<tr class="odd">
<td>[<strong>UpdateNtmsOmidInfo</strong>](updatentmsomidinfo.md)</td>

<td>C</td>

</tr>
</tbody>
</table>



 

 

 



