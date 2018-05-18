---
Description: 'The state transition model in a shadow copy provider is simplified by the serialization of shadow copy creation from the time that IVssBackupComponents::StartSnapshotSet is called until the call to IVssBackupComponents::DoSnapshotSet returns.'
ms.assetid: '5dbf0fb3-53cb-4532-9a8f-bd955afe16c4'
title: State Transitions in Shadow Copy Providers
---

# State Transitions in Shadow Copy Providers

The state transition model in a shadow copy provider is simplified by the serialization of shadow copy creation from the time that [**IVssBackupComponents::StartSnapshotSet**](ivssbackupcomponents-startsnapshotset.md) is called until the call to [**IVssBackupComponents::DoSnapshotSet**](ivssbackupcomponents-dosnapshotset.md) returns. If another requester tries to create a shadow copy during this time, the call to **StartSnapshotSet** will fail with error **VSS\_E\_SNAPSHOT\_SET\_IN\_PROGRESS**, indicating that the second requester should wait and try again.

VSS will only call [**IVssProviderCreateSnapshotSet::AbortSnapshots**](ivssprovidercreatesnapshotset-abortsnapshots.md) after the requester has called [**DoSnapshotSet**](ivssbackupcomponents-dosnapshotset.md), even if the shadow copy fails or is aborted before this point. This means that a provider will not receive a call to **AbortSnapshots** until after [**IVssProviderCreateSnapshotSet::EndPrepareSnapshots**](ivssprovidercreatesnapshotset-endpreparesnapshots.md) has been called. If a shadow copy is aborted or fails before this point, the provider is not given any indication until a new shadow copy is started. For this reason, the provider must be prepared to handle an out-of-sequence call to [**IVssHardwareSnapshotProvider::BeginPrepareSnapshot**](ivsshardwaresnapshotprovider-beginpreparesnapshot.md) at any point. This out-of-sequence call represents the start of a new shadow copy sequence and will have a new shadow copy set ID.

 

 



