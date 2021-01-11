---
description: VSS allows many shadow copies to exist at once, but it only allows one shadow copy set creation to be in-progress between the call to IVssBackupComponents::StartSnapshotSet and the return from the call to IVssBackupComponents::DoSnapshotSet.
ms.assetid: 26657fc2-180f-4ebb-820c-2159e7fe7584
title: Error Handling in Shadow Copy Providers
ms.topic: article
ms.date: 05/31/2018
---

# Error Handling in Shadow Copy Providers

VSS allows many shadow copies to exist at once, but it only allows one shadow copy set creation to be in-progress between the call to [**IVssBackupComponents::StartSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-startsnapshotset) and the return from the call to [**IVssBackupComponents::DoSnapshotSet**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-dosnapshotset).

## No Partial Commit

If any provider fails a shadow copy on any volume or LUN in the shadow copy set, then the creation of the entire shadow copy set fails. This is by design. This design simplifies the behavioral issues associated with partial failure semantics and maintains a consistent point-in-time across all shadow copies in the set.

## Reporting Fault Conditions

If a provider error or fault condition occurs, the provider must log an error to the Application event log. This includes, but is not limited to, any provider-specific errors when creating or importing a Shadow Copy Set, or resource allocation failure for copy-on-write shadow copy after creation. This logging must not take place during the time the volumes in the shadow copy set are in a frozen state.

## Valid Provider Return Values

The following table lists the valid return codes for provider methods and their meanings.



| Value                                                                                                                                                                              | Description                                                                                                                                                                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="S_OK"></span><span id="s_ok"></span>S\_OK<br/>                                                                                                                     | The method was successful.<br/>                                                                                                                                                                                                                  |
| <span id="E_OUTOFMEMORY"></span><span id="e_outofmemory"></span>E\_OUTOFMEMORY<br/>                                                                                          | The provider is out of memory or other system resources.<br/>                                                                                                                                                                                    |
| <span id="E_INVALIDARG"></span><span id="e_invalidarg"></span>E\_INVALIDARG<br/>                                                                                             | One of the parameter values is not valid.<br/>                                                                                                                                                                                                   |
| <span id="E_ACCESSDENIED"></span><span id="e_accessdenied"></span>E\_ACCESSDENIED<br/>                                                                                       | A non-privileged client has tried to call into the provider.<br/>                                                                                                                                                                                |
| <span id="VSS_E_BAD_STATE"></span><span id="vss_e_bad_state"></span>VSS\_E\_BAD\_STATE<br/>                                                                                  | Either no provider supports the requested operation, or the operation cannot be performed on the object because the object is not in the correct state.<br/>                                                                                     |
| <span id="VSS_E_OBJECT_NOT_FOUND"></span><span id="vss_e_object_not_found"></span>VSS\_E\_OBJECT\_NOT\_FOUND<br/>                                                            | A parameter refers to an object that was not found (such as a shadow copy ID, shadow copy set ID, or volume.)<br/>                                                                                                                               |
| <span id="VSS_E_INSUFFICIENT_STORAGE"></span><span id="vss_e_insufficient_storage"></span>VSS\_E\_INSUFFICIENT\_STORAGE<br/>                                                 | The provider cannot perform the operation because there is not enough disk space.<br/>                                                                                                                                                           |
| <span id="VSS_E_VOLUME_NOT_SUPPORTED"></span><span id="vss_e_volume_not_supported"></span>VSS\_E\_VOLUME\_NOT\_SUPPORTED<br/>                                                | No provider on this computer supports the requested operation on the volume.<br/>                                                                                                                                                                |
| <span id="VSS_E_VOLUME_NOT_SUPPORTED_BY_PROVIDER"></span><span id="vss_e_volume_not_supported_by_provider"></span>VSS\_E\_VOLUME\_NOT\_SUPPORTED\_BY\_PROVIDER<br/>          | The provider does not support the volume.<br/>                                                                                                                                                                                                   |
| <span id="VSS_E_MAXIMUM_NUMBER_OF_SNAPSHOTS_REACHED"></span><span id="vss_e_maximum_number_of_snapshots_reached"></span>VSS\_E\_MAXIMUM\_NUMBER\_OF\_SNAPSHOTS\_REACHED<br/> | The provider has reached the maximum number of shadow copies that it can support.<br/>                                                                                                                                                           |
| <span id="VSS_E_PROVIDER_VETO"></span><span id="vss_e_provider_veto"></span>VSS\_E\_PROVIDER\_VETO<br/>                                                                      | The provider has encountered an internal run-time error that does not map to another return value. The provider must also write an event into the Application event log providing the user with information on how to resolve this problem.<br/> |
| <span id="VSS_E_CANNOT_REVERT_DISKID"></span><span id="vss_e_cannot_revert_diskid"></span>VSS\_E\_CANNOT\_REVERT\_DISKID<br/>                                                | The MBR signature or GPT ID for one or more disks could not be set to the requested value. Check the Application event log for more information.<br/>                                                                                            |



 

The provider should not attempt to return any other error codes.

If the provider returns an error code that is not expected (for example **S\_FALSE**, **E\_FAIL**, **E\_UNEXPECTED**, or **E\_ABORT**), VSS writes an event into the event log mentioning the provider and failed method and translates the error to **VSS\_E\_UNEXPECTED\_PROVIDER\_ERROR** before returning to the requester. This is not done for any returns from [**IVssProviderCreateSnapshotSet::AbortSnapshots**](/windows/desktop/api/VsProv/nf-vsprov-ivssprovidercreatesnapshotset-abortsnapshots) or [**IVssProviderNotifications::OnUnload**](/windows/desktop/api/VsProv/nf-vsprov-ivssprovidernotifications-onunload).

 

 




