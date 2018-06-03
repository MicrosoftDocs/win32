---
title: MSFT\_SMStorageSynchronized class
description: Represent the synchronization status of a storage object and its replicas.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a4fb53a8-cf24-4089-8649-77f2119108ee
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMStorageSynchronized class
- MSFT_SMStorageSynchronized class, described
topic_type:
- apiref
api_name:
- MSFT_SMStorageSynchronized
- MSFT_SMStorageSynchronized.WhenSynced
- MSFT_SMStorageSynchronized.SyncMaintained
- MSFT_SMStorageSynchronized.CopyState
- MSFT_SMStorageSynchronized.CopyStateDescription
- MSFT_SMStorageSynchronized.RequestedCopyState
- MSFT_SMStorageSynchronized.SyncType
- MSFT_SMStorageSynchronized.SyncTypeDescription
- MSFT_SMStorageSynchronized.Mode
- MSFT_SMStorageSynchronized.ModeDescription
- MSFT_SMStorageSynchronized.ProgressStatus
- MSFT_SMStorageSynchronized.ProgressStatusDescription
- MSFT_SMStorageSynchronized.PercentSynced
- MSFT_SMStorageSynchronized.WhenEstablished
- MSFT_SMStorageSynchronized.WhenSynchronized
- MSFT_SMStorageSynchronized.WhenActivated
- MSFT_SMStorageSynchronized.WhenDeactivated
- MSFT_SMStorageSynchronized.WhenSuspended
- MSFT_SMStorageSynchronized.CopyType
- MSFT_SMStorageSynchronized.CopyTypeDescription
- MSFT_SMStorageSynchronized.ReplicaType
- MSFT_SMStorageSynchronized.ReplicaTypeDescription
- MSFT_SMStorageSynchronized.SyncState
- MSFT_SMStorageSynchronized.SyncStateDescription
- MSFT_SMStorageSynchronized.CopyPriority
- MSFT_SMStorageSynchronized.CopyPriorityDescription
- MSFT_SMStorageSynchronized.CopyMethodology
- MSFT_SMStorageSynchronized.CopyMethodologyDescription
- MSFT_SMStorageSynchronized.RecoveryPointObjective
- MSFT_SMStorageSynchronized.SourceStorageVolume
- MSFT_SMStorageSynchronized.TargetStorageVolume
api_location:
- StorageService.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_SMStorageSynchronized class

Represent the synchronization status of a storage object and its replicas.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

**Windows Server 2012 R2 and Windows Server 2012:** This class does not inherit from [**MSFT\_SMStorageSynchronizedBase**](msft-smstoragesynchronizedbase.md) which is new for Windows Server 2016.

## Syntax

``` syntax
[Association, Dynamic, Provider("WMIStorage")]
class MSFT_SMStorageSynchronized : MSFT_SMStorageSynchronizedBase
{
  datetime                 WhenSynced;
  boolean                  SyncMaintained;
  uint16                   CopyState;
  string                   CopyStateDescription;
  uint16                   RequestedCopyState = 15;
  uint16                   SyncType;
  string                   SyncTypeDescription;
  uint16                   Mode;
  string                   ModeDescription;
  uint16                   ProgressStatus;
  string                   ProgressStatusDescription;
  uint16                   PercentSynced;
  datetime                 WhenEstablished;
  datetime                 WhenSynchronized;
  datetime                 WhenActivated;
  datetime                 WhenDeactivated;
  datetime                 WhenSuspended;
  uint16                   CopyType;
  string                   CopyTypeDescription;
  uint16                   ReplicaType;
  string                   ReplicaTypeDescription;
  uint16                   SyncState;
  string                   SyncStateDescription;
  uint16                   CopyPriority;
  string                   CopyPriorityDescription;
  uint16                   CopyMethodology;
  string                   CopyMethodologyDescription;
  UInt32                   RecoveryPointObjective;
  MSFT_SMStorageVolume REF SourceStorageVolume;
  MSFT_SMStorageVolume REF TargetStorageVolume;
};
```

## Members

The **MSFT\_SMStorageSynchronized** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMStorageSynchronized** class has these properties.

<dl> <dt>

**CopyMethodology**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The copy methodology used by the copy engine to create and maintain the target element.

The possible values are.

<dt>

<span id="Not_Specified"></span><span id="not_specified"></span><span id="NOT_SPECIFIED"></span>

<span id="Not_Specified"></span><span id="not_specified"></span><span id="NOT_SPECIFIED"></span>**Not Specified** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd></dd> <dt>

<span id="Implementation_decides"></span><span id="implementation_decides"></span><span id="IMPLEMENTATION_DECIDES"></span>

<span id="Implementation_decides"></span><span id="implementation_decides"></span><span id="IMPLEMENTATION_DECIDES"></span>**Implementation decides** (2)


</dt> <dd></dd> <dt>

<span id="Full_Copy"></span><span id="full_copy"></span><span id="FULL_COPY"></span>

<span id="Full_Copy"></span><span id="full_copy"></span><span id="FULL_COPY"></span>**Full Copy** (3)


</dt> <dd>

A full copy of the source object is generated.

</dd> <dt>

<span id="Incremental-Copy"></span><span id="incremental-copy"></span><span id="INCREMENTAL-COPY"></span>

<span id="Incremental-Copy"></span><span id="incremental-copy"></span><span id="INCREMENTAL-COPY"></span>**Incremental-Copy** (4)


</dt> <dd>

Only changed data from source element is copied to target element.

</dd> <dt>

<span id="Differential-Copy"></span><span id="differential-copy"></span><span id="DIFFERENTIAL-COPY"></span>

<span id="Differential-Copy"></span><span id="differential-copy"></span><span id="DIFFERENTIAL-COPY"></span>**Differential-Copy** (5)


</dt> <dd>

Only the new writes to source element are copied to the target element.

</dd> <dt>

<span id="Copy-On-Write"></span><span id="copy-on-write"></span><span id="COPY-ON-WRITE"></span>

<span id="Copy-On-Write"></span><span id="copy-on-write"></span><span id="COPY-ON-WRITE"></span>**Copy-On-Write** (6)


</dt> <dd>

Affected data is copied on the first write to the source or to the target elements.

</dd> <dt>

<span id="Copy-On-Access"></span><span id="copy-on-access"></span><span id="COPY-ON-ACCESS"></span>

<span id="Copy-On-Access"></span><span id="copy-on-access"></span><span id="COPY-ON-ACCESS"></span>**Copy-On-Access** (7)


</dt> <dd>

Affected data is copied on the first access to the source element.

</dd> <dt>

<span id="Delta-Update"></span><span id="delta-update"></span><span id="DELTA-UPDATE"></span>

<span id="Delta-Update"></span><span id="delta-update"></span><span id="DELTA-UPDATE"></span>**Delta-Update** (8)


</dt> <dd>

After the initial copy, only updates to the source are copied to the target.

</dd> <dt>

<span id="Snap-And-Clone"></span><span id="snap-and-clone"></span><span id="SNAP-AND-CLONE"></span>

<span id="Snap-And-Clone"></span><span id="snap-and-clone"></span><span id="SNAP-AND-CLONE"></span>**Snap-And-Clone** (9)


</dt> <dd>

A snapshot of the source element is created, then used as the source of the copy operation to the target element.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

Reserved

</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific**


</dt> <dd>

Reserved

</dd> </dl>

This property is inherited from [**MSFT\_SMStorageSynchronizedBase**](msft-smstoragesynchronizedbase.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMStorageSynchronizedBase**](msft-smstoragesynchronizedbase.md) .

</dd> <dt>

**CopyMethodologyDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the current value of the **CopyMethodology** property.

This property is inherited from [**MSFT\_SMStorageSynchronizedBase**](msft-smstoragesynchronizedbase.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMStorageSynchronizedBase**](msft-smstoragesynchronizedbase.md) .

</dd> <dt>

**CopyPriority**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

The priority of background copy engine I/O relative to host I/O operations during a sequential background copy operation.

The possible values are.

<dt>

<span id="Not_Managed"></span><span id="not_managed"></span><span id="NOT_MANAGED"></span>

**Not Managed** (0)


</dt> <dd></dd> <dt>

<span id="Low"></span><span id="low"></span><span id="LOW"></span>

**Low** (1)


</dt> <dd></dd> <dt>

<span id="Same"></span><span id="same"></span><span id="SAME"></span>

**Same** (2)


</dt> <dd></dd> <dt>

<span id="High"></span><span id="high"></span><span id="HIGH"></span>

**High** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 = *value* </dd> </dl>

This property is inherited from [**MSFT\_SMStorageSynchronizedBase**](msft-smstoragesynchronizedbase.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMStorageSynchronizedBase**](msft-smstoragesynchronizedbase.md) .

</dd> <dt>

**CopyPriorityDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the current value of the **CopyPriority** property.

This property is inherited from [**MSFT\_SMStorageSynchronizedBase**](msft-smstoragesynchronizedbase.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMStorageSynchronizedBase**](msft-smstoragesynchronizedbase.md) .

</dd> <dt>

**CopyState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

Indicates the state of the replication activity.

The possible values are:

<dt>

<span id="Initialized"></span><span id="initialized"></span><span id="INITIALIZED"></span>

**Initialized** (2)


</dt> <dd></dd> <dt>

<span id="Unsynchronized"></span><span id="unsynchronized"></span><span id="UNSYNCHRONIZED"></span>

**Unsynchronized** (3)


</dt> <dd></dd> <dt>

<span id="Synchronized"></span><span id="synchronized"></span><span id="SYNCHRONIZED"></span>

**Synchronized** (4)


</dt> <dd></dd> <dt>

<span id="Broken"></span><span id="broken"></span><span id="BROKEN"></span>

**Broken** (5)


</dt> <dd></dd> <dt>

<span id="Fractured"></span><span id="fractured"></span><span id="FRACTURED"></span>

**Fractured** (6)


</dt> <dd></dd> <dt>

<span id="Split"></span><span id="split"></span><span id="SPLIT"></span>

**Split** (7)


</dt> <dd></dd> <dt>

<span id="Inactive"></span><span id="inactive"></span><span id="INACTIVE"></span>

**Inactive** (8)


</dt> <dd></dd> <dt>

<span id="Suspended"></span><span id="suspended"></span><span id="SUSPENDED"></span>

**Suspended** (9)


</dt> <dd></dd> <dt>

<span id="Failedover"></span><span id="failedover"></span><span id="FAILEDOVER"></span>

**Failedover** (10)


</dt> <dd></dd> <dt>

<span id="Prepared"></span><span id="prepared"></span><span id="PREPARED"></span>

**Prepared** (11)


</dt> <dd></dd> <dt>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>

**Aborted** (12)


</dt> <dd></dd> <dt>

<span id="Skewed"></span><span id="skewed"></span><span id="SKEWED"></span>

**Skewed** (13)


</dt> <dd></dd> <dt>

<span id="Mixed"></span><span id="mixed"></span><span id="MIXED"></span>

**Mixed** (14)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (15)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>16 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl>

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md) .

</dd> <dt>

**CopyStateDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the **CopyState** property value.

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md) .

</dd> <dt>

**CopyType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The replication policy of the association.

The possible values are:

<dt>

<span id="Async"></span><span id="async"></span><span id="ASYNC"></span>

**Async** (2)


</dt> <dd></dd> <dt>

<span id="Sync"></span><span id="sync"></span><span id="SYNC"></span>

**Sync** (3)


</dt> <dd></dd> <dt>

<span id="UnSyncAssoc"></span><span id="unsyncassoc"></span><span id="UNSYNCASSOC"></span>

**UnSyncAssoc** (4)


</dt> <dd></dd> <dt>

<span id="UnSyncUnAssoc"></span><span id="unsyncunassoc"></span><span id="UNSYNCUNASSOC"></span>

**UnSyncUnAssoc** (5)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>6 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 ...</dd> </dl>

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md) .

</dd> <dt>

**CopyTypeDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the **CopyType** value.

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md) .

</dd> <dt>

**Mode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

The update mode of the target elements. If the value is set to **NULL**, the implementation will provide the update mode.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Synchronous"></span><span id="synchronous"></span><span id="SYNCHRONOUS"></span>

**Synchronous** (2)


</dt> <dd></dd> <dt>

<span id="Asynchronous"></span><span id="asynchronous"></span><span id="ASYNCHRONOUS"></span>

**Asynchronous** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl>

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md) .

</dd> <dt>

**ModeDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the **Mode** value.

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md) .

</dd> <dt>

**PercentSynced**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

The percent of synchronization work that is complete. This value must be set to **NULL** if the implementation is not capable of providing this information.

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md) .

</dd> <dt>

**ProgressStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

Indicates the status of the replication activity for the association.

The possible values are:

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>

**Completed** (2)


</dt> <dd></dd> <dt>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>

**Dormant** (3)


</dt> <dd></dd> <dt>

<span id="Initializing"></span><span id="initializing"></span><span id="INITIALIZING"></span>

**Initializing** (4)


</dt> <dd></dd> <dt>

<span id="Preparing"></span><span id="preparing"></span><span id="PREPARING"></span>

**Preparing** (5)


</dt> <dd></dd> <dt>

<span id="Synchronizing"></span><span id="synchronizing"></span><span id="SYNCHRONIZING"></span>

**Synchronizing** (6)


</dt> <dd></dd> <dt>

<span id="Resyncing"></span><span id="resyncing"></span><span id="RESYNCING"></span>

**Resyncing** (7)


</dt> <dd></dd> <dt>

<span id="Restoring"></span><span id="restoring"></span><span id="RESTORING"></span>

**Restoring** (8)


</dt> <dd></dd> <dt>

<span id="Fracturing"></span><span id="fracturing"></span><span id="FRACTURING"></span>

**Fracturing** (9)


</dt> <dd></dd> <dt>

<span id="Splitting"></span><span id="splitting"></span><span id="SPLITTING"></span>

**Splitting** (10)


</dt> <dd></dd> <dt>

<span id="Failing_over"></span><span id="failing_over"></span><span id="FAILING_OVER"></span>

**Failing over** (11)


</dt> <dd></dd> <dt>

<span id="Failing_back"></span><span id="failing_back"></span><span id="FAILING_BACK"></span>

**Failing back** (12)


</dt> <dd></dd> <dt>

<span id="Aborting"></span><span id="aborting"></span><span id="ABORTING"></span>

**Aborting** (13)


</dt> <dd></dd> <dt>

<span id="Mixed"></span><span id="mixed"></span><span id="MIXED"></span>

**Mixed** (14)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (15)


</dt> <dd></dd> <dt>

<span id="Suspending"></span><span id="suspending"></span><span id="SUSPENDING"></span>

**Suspending** (16)


</dt> <dd></dd> <dt>

<span id="Requires_fracture"></span><span id="requires_fracture"></span><span id="REQUIRES_FRACTURE"></span>

**Requires fracture** (17)


</dt> <dd></dd> <dt>

<span id="Requires_resync"></span><span id="requires_resync"></span><span id="REQUIRES_RESYNC"></span>

**Requires resync** (18)


</dt> <dd></dd> <dt>

<span id="Requires_activate"></span><span id="requires_activate"></span><span id="REQUIRES_ACTIVATE"></span>

**Requires activate** (19)


</dt> <dd></dd> <dt>

<span id="Pending"></span><span id="pending"></span><span id="PENDING"></span>

**Pending** (20)


</dt> <dd></dd> <dt>

<span id="Detaching"></span><span id="detaching"></span><span id="DETACHING"></span>

**Detaching** (21)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>22 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 ...</dd> </dl>

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md) .

</dd> <dt>

**ProgressStatusDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the **ProgressStatus** value.

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md) .

</dd> <dt>

**RecoveryPointObjective**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the maximum interval in which data from copy operations might be lost. For synchronous copy operations, this interval is "0". For asynchronous copy operations, this parameter represents the interval since the most recent transmission of data to the target element.

This property is inherited from [**MSFT\_SMStorageSynchronizedBase**](msft-smstoragesynchronizedbase.md).

**Windows Server 2012 R2 and Windows Server 2012:** Not supported.

</dd> <dt>

**ReplicaType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of replica for the storage object.

The possible values are.

<dt>

<span id="Not_Specified"></span><span id="not_specified"></span><span id="NOT_SPECIFIED"></span>

<span id="Not_Specified"></span><span id="not_specified"></span><span id="NOT_SPECIFIED"></span>**Not Specified** (0)


</dt> <dd></dd> <dt>

<span id="Full_Copy"></span><span id="full_copy"></span><span id="FULL_COPY"></span>

<span id="Full_Copy"></span><span id="full_copy"></span><span id="FULL_COPY"></span>**Full Copy** (2)


</dt> <dd>

A full copy of the source object is generated.

</dd> <dt>

<span id="Before_Delta"></span><span id="before_delta"></span><span id="BEFORE_DELTA"></span>

<span id="Before_Delta"></span><span id="before_delta"></span><span id="BEFORE_DELTA"></span>**Before Delta** (3)


</dt> <dd>

The source object is maintained as a delta data from the replica.

</dd> <dt>

<span id="After_Delta"></span><span id="after_delta"></span><span id="AFTER_DELTA"></span>

<span id="After_Delta"></span><span id="after_delta"></span><span id="AFTER_DELTA"></span>**After Delta** (4)


</dt> <dd>

The replica is maintained as delta data from the source object.

</dd> <dt>

<span id="Log"></span><span id="log"></span><span id="LOG"></span>

<span id="Log"></span><span id="log"></span><span id="LOG"></span>**Log** (5)


</dt> <dd>

The replica object is maintained as a log of changes to the source.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

Reserved.

</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific**


</dt> <dd>

Reserved.

</dd> </dl>

This property is inherited from [**MSFT\_SMStorageSynchronizedBase**](msft-smstoragesynchronizedbase.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMStorageSynchronizedBase**](msft-smstoragesynchronizedbase.md) .

</dd> <dt>

**ReplicaTypeDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the current value of the **ReplicaType** property.

This property is inherited from [**MSFT\_SMStorageSynchronizedBase**](msft-smstoragesynchronizedbase.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMStorageSynchronizedBase**](msft-smstoragesynchronizedbase.md) .

</dd> <dt>

**RequestedCopyState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("SNIA\_Synchronized.CopyState")
</dt> </dl>

Indicates the last requested or desired state of replication activity for the association. When the **CopyState** value matches the requested state, **RequestedCopyState** will be set to "Not Applicable".

The possible values are:

<dt>

<span id="Initialized"></span><span id="initialized"></span><span id="INITIALIZED"></span>

**Initialized** (2)


</dt> <dd></dd> <dt>

<span id="Unsynchronized"></span><span id="unsynchronized"></span><span id="UNSYNCHRONIZED"></span>

**Unsynchronized** (3)


</dt> <dd></dd> <dt>

<span id="Synchronized"></span><span id="synchronized"></span><span id="SYNCHRONIZED"></span>

**Synchronized** (4)


</dt> <dd></dd> <dt>

<span id="Broken"></span><span id="broken"></span><span id="BROKEN"></span>

**Broken** (5)


</dt> <dd></dd> <dt>

<span id="Fractured"></span><span id="fractured"></span><span id="FRACTURED"></span>

**Fractured** (6)


</dt> <dd></dd> <dt>

<span id="Split"></span><span id="split"></span><span id="SPLIT"></span>

**Split** (7)


</dt> <dd></dd> <dt>

<span id="Inactive"></span><span id="inactive"></span><span id="INACTIVE"></span>

**Inactive** (8)


</dt> <dd></dd> <dt>

<span id="Suspended"></span><span id="suspended"></span><span id="SUSPENDED"></span>

**Suspended** (9)


</dt> <dd></dd> <dt>

<span id="Failedover"></span><span id="failedover"></span><span id="FAILEDOVER"></span>

**Failedover** (10)


</dt> <dd></dd> <dt>

<span id="Prepared"></span><span id="prepared"></span><span id="PREPARED"></span>

**Prepared** (11)


</dt> <dd></dd> <dt>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>

**Aborted** (12)


</dt> <dd></dd> <dt>

<span id="Skewed"></span><span id="skewed"></span><span id="SKEWED"></span>

**Skewed** (13)


</dt> <dd></dd> <dt>

<span id="Mixed"></span><span id="mixed"></span><span id="MIXED"></span>

**Mixed** (14)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (15)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>16 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl>

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md) .

</dd> <dt>

**SourceStorageVolume**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMStorageVolume**](msft-smstoragevolume.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the source volume.

</dd> <dt>

**SyncMaintained**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if the synchronization between the elements is maintained; otherwise, **False**.

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md) .

</dd> <dt>

**SyncState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The state of replication activity for the storage object.

The possible values are.

<dt>

<span id="Initialized"></span><span id="initialized"></span><span id="INITIALIZED"></span>

**Initialized** (2)


</dt> <dd></dd> <dt>

<span id="PrepareInProgress"></span><span id="prepareinprogress"></span><span id="PREPAREINPROGRESS"></span>

**PrepareInProgress** (3)


</dt> <dd></dd> <dt>

<span id="Prepared"></span><span id="prepared"></span><span id="PREPARED"></span>

**Prepared** (4)


</dt> <dd></dd> <dt>

<span id="ResyncInProgress"></span><span id="resyncinprogress"></span><span id="RESYNCINPROGRESS"></span>

**ResyncInProgress** (5)


</dt> <dd></dd> <dt>

<span id="Synchronized"></span><span id="synchronized"></span><span id="SYNCHRONIZED"></span>

**Synchronized** (6)


</dt> <dd></dd> <dt>

<span id="Fracture_In_Progress"></span><span id="fracture_in_progress"></span><span id="FRACTURE_IN_PROGRESS"></span>

**Fracture In Progress** (7)


</dt> <dd></dd> <dt>

<span id="QuiesceInProgress"></span><span id="quiesceinprogress"></span><span id="QUIESCEINPROGRESS"></span>

**QuiesceInProgress** (8)


</dt> <dd></dd> <dt>

<span id="Quiesced"></span><span id="quiesced"></span><span id="QUIESCED"></span>

**Quiesced** (9)


</dt> <dd></dd> <dt>

<span id="Restore_In_Progresss"></span><span id="restore_in_progresss"></span><span id="RESTORE_IN_PROGRESSS"></span>

**Restore In Progresss** (10)


</dt> <dd></dd> <dt>

<span id="Idle"></span><span id="idle"></span><span id="IDLE"></span>

**Idle** (11)


</dt> <dd></dd> <dt>

<span id="Broken"></span><span id="broken"></span><span id="BROKEN"></span>

**Broken** (12)


</dt> <dd></dd> <dt>

<span id="Fractured"></span><span id="fractured"></span><span id="FRACTURED"></span>

**Fractured** (13)


</dt> <dd></dd> <dt>

<span id="Frozen"></span><span id="frozen"></span><span id="FROZEN"></span>

**Frozen** (14)


</dt> <dd></dd> <dt>

<span id="Copy_In_Progress"></span><span id="copy_in_progress"></span><span id="COPY_IN_PROGRESS"></span>

**Copy In Progress** (15)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>16 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 = *value* </dd> </dl>

This property is inherited from [**MSFT\_SMStorageSynchronizedBase**](msft-smstoragesynchronizedbase.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMStorageSynchronizedBase**](msft-smstoragesynchronizedbase.md) .

</dd> <dt>

**SyncStateDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the current value of the **SyncState** property.

This property is inherited from [**MSFT\_SMStorageSynchronizedBase**](msft-smstoragesynchronizedbase.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMStorageSynchronizedBase**](msft-smstoragesynchronizedbase.md) .

</dd> <dt>

**SyncType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

The intended outcome of the replication operation.

The possible values are:

<dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>0 5</dd> <dt>

<span id="Mirror"></span><span id="mirror"></span><span id="MIRROR"></span>

**Mirror** (6)


</dt> <dd></dd> <dt>

<span id="Snapshot"></span><span id="snapshot"></span><span id="SNAPSHOT"></span>

**Snapshot** (7)


</dt> <dd></dd> <dt>

<span id="Clone"></span><span id="clone"></span><span id="CLONE"></span>

**Clone** (8)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>9 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 ...</dd> </dl>

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md) .

</dd> <dt>

**SyncTypeDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the **SyncType** property value.

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md) .

</dd> <dt>

**TargetStorageVolume**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_SMStorageVolume**](msft-smstoragevolume.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to the object that represents the target volume.

</dd> <dt>

**WhenActivated**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

A **datetime** value that indicates when the association was activated. This value must be set to **NULL** if the implementation is not capable of providing this information. A value of "0" indicates the information is unknown.

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md) .

</dd> <dt>

**WhenDeactivated**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

A **datetime** value that indicates when the association was deactivated. This value must be set to **NULL** if the implementation is not capable of providing this information. A value of "0" indicates the information is unknown.

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md) .

</dd> <dt>

**WhenEstablished**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

A **datetime** value that indicates when the association was established. This value must be set to **NULL** if the implementation is not capable of providing this information. A value of "0" indicates the information is unknown.

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md) .

</dd> <dt>

**WhenSuspended**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

A **datetime** value that indicates when the association was suspended. This value must be set to **NULL** if the implementation is not capable of providing this information. A value of "0" indicates the information is unknown.

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md) .

</dd> <dt>

**WhenSynced**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A **datetime** value that indicates when the elements were synchronized.

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md) .

</dd> <dt>

**WhenSynchronized**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

A **datetime** value that indicates when the **CopyState** property is set to "Synchronized". This value must be set to **NULL** if the implementation is not capable of providing this information. A value of "0" indicates the information is unknown.

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

**Windows Server 2012 R2 and Windows Server 2012:** This property is present, but is not inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md) .

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMStorageSynchronizedBase**](msft-smstoragesynchronizedbase.md)
</dt> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





