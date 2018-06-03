---
title: CIM\_StorageSynchronized class
description: Indicates that two Storage objects were replicated at the specified point in time. If the CopyType property is set to 'Sync' ( 3), then synchronization of the Storage objects is preserved.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b0aed98e-8c08-45cf-8d77-339eee82d378
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_StorageSynchronized class iSCSI Software Target API
- CIM_StorageSynchronized class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- CIM_StorageSynchronized
- CIM_StorageSynchronized.WhenSynced
- CIM_StorageSynchronized.SyncMaintained
- CIM_StorageSynchronized.CopyState
- CIM_StorageSynchronized.Mode
- CIM_StorageSynchronized.PercentSynced
- CIM_StorageSynchronized.ProgressStatus
- CIM_StorageSynchronized.RequestedCopyState
- CIM_StorageSynchronized.SyncType
- CIM_StorageSynchronized.WhenActivated
- CIM_StorageSynchronized.WhenDeactivated
- CIM_StorageSynchronized.WhenEstablished
- CIM_StorageSynchronized.WhenSuspended
- CIM_StorageSynchronized.WhenSynchronized
- CIM_StorageSynchronized.CopyRecoveryMode
- CIM_StorageSynchronized.FailedCopyStopsHostIO
- CIM_StorageSynchronized.SystemElement
- CIM_StorageSynchronized.SyncedElement
- CIM_StorageSynchronized.CopyType
- CIM_StorageSynchronized.ReplicaType
- CIM_StorageSynchronized.SyncState
- CIM_StorageSynchronized.CopyPriority
- CIM_StorageSynchronized.CopyMethodology
- CIM_StorageSynchronized.UndiscoveredElement
- CIM_StorageSynchronized.ReadOnly
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CIM\_StorageSynchronized class

Indicates that two Storage objects were replicated at the specified point in time. If the CopyType property is set to 'Sync' (=3), then synchronization of the Storage objects is preserved.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Experimental, Version("2.29.0"), UMLPackagePath("CIM::Device::StorageServices")]
class CIM_StorageSynchronized : CIM_Synchronized
{
  datetime               WhenSynced;
  boolean                SyncMaintained;
  uint16                 CopyState;
  uint16                 Mode;
  uint16                 PercentSynced;
  uint16                 ProgressStatus;
  uint16                 RequestedCopyState = 15;
  uint16                 SyncType;
  datetime               WhenActivated;
  datetime               WhenDeactivated;
  datetime               WhenEstablished;
  datetime               WhenSuspended;
  datetime               WhenSynchronized;
  uint16                 CopyRecoveryMode;
  boolean                FailedCopyStopsHostIO = FALSE;
  CIM_ManagedElement REF SystemElement;
  CIM_ManagedElement REF SyncedElement;
  uint16                 CopyType;
  uint16                 ReplicaType;
  uint16                 SyncState;
  uint16                 CopyPriority;
  uint16                 CopyMethodology;
  uint16                 UndiscoveredElement;
  uint16                 ReadOnly;
};
```

## Members

The **CIM\_StorageSynchronized** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_StorageSynchronized** class has these properties.

<dl> <dt>

**CopyMethodology**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

CopyMethodology specifies what copy methodology the service uses to create and/or maintain the target element.

Values are:

Not Specified: The method of maintaining the copy is not specified.

Full Copy: This indicates that a full copy of the source object is (or will be) generated .

Incremental-Copy: Only changed data from source element is copied to target element.

Differential-Copy: Only the new writes to source element are copied to the target element.

Copy-On-Write: Affected data is copied on the first write to the source or to the target elements.

Copy-On-Access: Affected data is copied on the first access to the source element.

Delta-Update: Difference based replication where after the initial copy, only updates to source are copied to target.

Snap-And-Clone: The service creates a snapshot of the source element first, then uses the the snapshot as the source of the copy operation to the target element.

<dt>

<span id="Not_Specified"></span><span id="not_specified"></span><span id="NOT_SPECIFIED"></span>

**Not Specified** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Implementation_decides"></span><span id="implementation_decides"></span><span id="IMPLEMENTATION_DECIDES"></span>

**Implementation decides** (2)


</dt> <dd></dd> <dt>

<span id="Full_Copy"></span><span id="full_copy"></span><span id="FULL_COPY"></span>

**Full Copy** (3)


</dt> <dd></dd> <dt>

<span id="Incremental-Copy"></span><span id="incremental-copy"></span><span id="INCREMENTAL-COPY"></span>

**Incremental-Copy** (4)


</dt> <dd></dd> <dt>

<span id="Differential-Copy"></span><span id="differential-copy"></span><span id="DIFFERENTIAL-COPY"></span>

**Differential-Copy** (5)


</dt> <dd></dd> <dt>

<span id="Copy-On-Write"></span><span id="copy-on-write"></span><span id="COPY-ON-WRITE"></span>

**Copy-On-Write** (6)


</dt> <dd></dd> <dt>

<span id="Copy-On-Access"></span><span id="copy-on-access"></span><span id="COPY-ON-ACCESS"></span>

**Copy-On-Access** (7)


</dt> <dd></dd> <dt>

<span id="Delta-Update"></span><span id="delta-update"></span><span id="DELTA-UPDATE"></span>

**Delta-Update** (8)


</dt> <dd></dd> <dt>

<span id="Snap-And-Clone"></span><span id="snap-and-clone"></span><span id="SNAP-AND-CLONE"></span>

**Snap-And-Clone** (9)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>10 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**CopyPriority**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

CopyPriority allows the priority of background copy engine I/O to be managed relative to host I/O operations during a sequential background copy operation.

Values are: Low: copy engine I/O lower priority than host I/O. Same: copy engine I/O has the same priority as host I/O. High: copy engine I/O has higher priority than host I/O. Urgent: copy operation to be performed as soon as possible, regardless of the host I/O requests.

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

<span id="Urgent"></span><span id="urgent"></span><span id="URGENT"></span>

**Urgent** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**CopyRecoveryMode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

Describes whether the copy operation continues after a broken link is restored.

Automatic: copy operation resumes automatically.

Manual: CopyState is set to Suspended after the link is restored. It is required to issue the Resume operation to continue.

This property is inherited from [**CIM\_Synchronized**](cim-synchronized.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Automatic"></span><span id="automatic"></span><span id="AUTOMATIC"></span>

**Automatic** (2)


</dt> <dd></dd> <dt>

<span id="Manual"></span><span id="manual"></span><span id="MANUAL"></span>

**Manual** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**CopyState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

CopyState describes the state of the association with respect to Replication activity. Values are:

Initialized: The link to enable replication is established and source/replica elements are associated, but the data flow has not started.

Unsynchronized: Not all the source element data has been copied to the target element.

Synchronized: For the Mirror, Snapshot, or Clone replication, the target represents a copy of the source.

Broken: The relationship is non-functional due to errors in the source, the target, the path between the two or space constraints.

Fractured: Target is split from the source.

Split: The target element was gracefully (or systematically) split from its source element -- consistency is guaranteed.

Inactive: Data flow has stopped, writes to source element will not be sent to target element.

Suspended: Data flow between the source and target elements has stopped. Writes to source element are held until the association is Resumed.

Failedover: Reads and writes to/from the target element. Source element is not reachable.

Prepared: Initialization is completed, the data flow has started, however, the data flow has not started.

Aborted: The copy operation is aborted with the Abort operation. Use the Resync Replica operation to restart the copy operation.

Skewed: The target has been modified and is no longer synchronized with the source element or the point-in-time view.

Mixed: Applies to the CopyState of GroupSynchronized. It indicates the StorageSynchronized associations of the elements in the groups have different CopyState values.

Partitioned: State of replication relationship can not be determined, for example, due to a connection problem.

Invalid: The array is unable to determine the state of the replication relationship, for example, after the connection is restored; however, either source or target elements have an unknown status.

This property is inherited from [**CIM\_Synchronized**](cim-synchronized.md).

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

<span id="Partitioned"></span><span id="partitioned"></span><span id="PARTITIONED"></span>

**Partitioned** (16)


</dt> <dd></dd> <dt>

<span id="Invalid"></span><span id="invalid"></span><span id="INVALID"></span>

**Invalid** (17)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>18 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**CopyType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

CopyType describes the Replication Policy. Values are:

Async: create and maintain an asynchronous copy of the source.

Sync: create and maintain a synchronized copy of the source.

UnSyncAssoc: create an unsynchronized copy and maintain an association to the source.

UnSyncUnAssoc: create an unsynchronized copy with a temporary association that is deleted upon completion of the copy operation.

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


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**FailedCopyStopsHostIO**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

If true, the storage array tells host to stop sending data to source element if copying to a remote element fails.

This property is inherited from [**CIM\_Synchronized**](cim-synchronized.md).

</dd> <dt>

**Mode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

Mode describes whether the target elements will be updated synchronously or asynchronously. If NULL, implementaton decides the mode.

This property is inherited from [**CIM\_Synchronized**](cim-synchronized.md).

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

</dd> <dt>

**PercentSynced**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

Specifies the percent of the work completed to reach synchronization. Must be set to NULL if implementation is not capable of providing this information.

This property is inherited from [**CIM\_Synchronized**](cim-synchronized.md).

</dd> <dt>

**ProgressStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

ProgressStatus describes the status of the association with respect to Replication activity. Values are: Completed: The request is completed. Data flow is idle.

Dormant: Indicates that the data flow is inactive suspended or quiesced.

Initializing: In the process of establishing source/replica association and the data flow has not started.

Preparing: preparation-in-progress.

Synchronizing: sync-in-progress.

Resyncing: resync-in-progess.

Restoring: restore-in-progress.

Fracturing: fracture-in-progress.

Splitting: split-in-progress.

Failing over: in the process of switching source and target.

Failing back: Undoing the result of failover.

Detaching: detach-in-progress.

Aborting: abort-in-progress.

Mixed: Applies to groups with element pairs with different statuses. Generally, the individual statuses need to be examined.Suspending: The copy operation is in the process of being suspended.

Requires fracture: The requested operation has completed, however, the synchronization relationship needs to be fractured before further copy operations can be issued.

Requires resync: The requested operation has completed, however, the synchronization relationship needs to be resynced before further copy operations can be issued.

Requires activate: The requested operation has completed, however, the synchronization relationship needs to be activated before further copy operations can be issued.

Pending: The flow of data has stopped momentarily due to limited bandwidth or busy system.

This property is inherited from [**CIM\_Synchronized**](cim-synchronized.md).

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


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**ReadOnly**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

This property specifies whether the source, the target, or both elements are "read only" to the host.SystemElement: The source element.

SyncedElement: The target element.

Both: Both the source and the target elements.are read only to the host.

<dt>

<span id="SystemElement"></span><span id="systemelement"></span><span id="SYSTEMELEMENT"></span>

**SystemElement** (2)


</dt> <dd></dd> <dt>

<span id="SyncedElement"></span><span id="syncedelement"></span><span id="SYNCEDELEMENT"></span>

**SyncedElement** (3)


</dt> <dd></dd> <dt>

<span id="Both"></span><span id="both"></span><span id="BOTH"></span>

**Both** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**ReplicaType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

ReplicaType provides information on how the Replica is being maintained. Values are:

Full Copy: This indicates that a full copy of the source object is (or will be) generated .

Before Delta: This indicates that the source object will be maintained as a delta data from the replica.

After Delta: This indicates that the replica will be maintained as delta data from the source object.

Log: This indicates that the replica object is being maintained as a log of changes to the source.

Not Specified: The method of maintaining the copy is not specified.

<dt>

<span id="Not_Specified"></span><span id="not_specified"></span><span id="NOT_SPECIFIED"></span>

**Not Specified** (0)


</dt> <dd></dd> <dt>

<span id="Full_Copy"></span><span id="full_copy"></span><span id="FULL_COPY"></span>

**Full Copy** (2)


</dt> <dd></dd> <dt>

<span id="Before_Delta"></span><span id="before_delta"></span><span id="BEFORE_DELTA"></span>

**Before Delta** (3)


</dt> <dd></dd> <dt>

<span id="After_Delta"></span><span id="after_delta"></span><span id="AFTER_DELTA"></span>

**After Delta** (4)


</dt> <dd></dd> <dt>

<span id="Log"></span><span id="log"></span><span id="LOG"></span>

**Log** (5)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>6 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**RequestedCopyState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Synchronized.CopyState")
</dt> </dl>

RequestedCopyState is an integer enumeration that indicates the last requested or desired state for the association. The actual state of the association is represented by CopyState. Note that when CopyState reaches the requested state, this property will be set to 'Not Applicable.

This property is inherited from [**CIM\_Synchronized**](cim-synchronized.md).

</dd> <dt>

**SyncedElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("SyncedElement")
</dt> </dl>

SyncedElement represents the Storage that is the target of the replication.

</dd> <dt>

**SyncMaintained**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Boolean indicating whether synchronization is maintained.

This property is inherited from [**CIM\_Synchronized**](cim-synchronized.md).

</dd> <dt>

**SyncState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

SyncState describes the state of the association with respect to Replication activity. Values are:

Initialized: The link to enable replication is established.

and source/replica elements are associated, but the Copy engine has not started.

PrepareInProgress: Preparation for Replication is in progress and the Copy engine has started.

Prepared: All necessary preparation has completed.

ResyncInProgress: Synchronization or Resynchronization is in progress.

This may be the initial 'copy' or subsequent changes being copied.

Synchronized: An Async or Sync replication is currently synchronized. When this value is set, SyncMaintained will be true.

FractureInProgress: An operation to fracture an Async or Sync replication is in progress.

Fractured: An Async or Sync replication is fractured.

QuiesceInProgress: A quiesce operation is in progress.

Quiesced: The replication has been quiesced and is ready for a change.

RestoreInProgress: An operation is in progress to copy the Synced object to the System object.

Idle: The 'normal' state for an UnSyncAssoc replica.

Frozen: All blocks copied from source to an UnSyncAssoc replica and the copy engine is stopped.

CopyInProgress: A deferred background copy operation is in progress to copy the source to the replica target for an UnSyncAssoc association.

Broken: The relationship is non-functional due to errors in the source, the target, the path between the two or space constraints.

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


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**SyncType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

SyncType describes the intended outcome of the replication.Values are:

Mirror: create and maintain a copy of the source.

Snapshot: create a PIT, virtual copy of the source.

Clone: create a PIT, full copy the source.

This property is inherited from [**CIM\_Synchronized**](cim-synchronized.md).

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


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**SystemElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("SystemElement")
</dt> </dl>

SystemElement represents the Storage that is the source of the replication.

</dd> <dt>

**UndiscoveredElement**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

This property specifies whether the source, the target, or both elements involved in a copy operation are undiscovered. An element is considered undiscovered if its object model is not known to the service performing the copy operation. The values are:

SystemElement: The source element.

SyncedElement: The target element.

Both: Both the source and the target elements. If both the source and the target elements are discovered, the value of this property shall be NULL.

<dt>

<span id="SystemElement"></span><span id="systemelement"></span><span id="SYSTEMELEMENT"></span>

**SystemElement** (2)


</dt> <dd></dd> <dt>

<span id="SyncedElement"></span><span id="syncedelement"></span><span id="SYNCEDELEMENT"></span>

**SyncedElement** (3)


</dt> <dd></dd> <dt>

<span id="Both"></span><span id="both"></span><span id="BOTH"></span>

**Both** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**WhenActivated**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

Specifies when point-in-time was taken or when the replication association is activated, reactivated, resumed or restablished. Must be set to NULL if implementation is not capable of providing this information. A value of 0 indicates the information is not known.

This property is inherited from [**CIM\_Synchronized**](cim-synchronized.md).

</dd> <dt>

**WhenDeactivated**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

Specifies when the association was deactivated. A deactivated association is reactivated.Must be set to NULL if implementation is not capable of providing this information. A value of 0 indicates the information is not known.

This property is inherited from [**CIM\_Synchronized**](cim-synchronized.md).

</dd> <dt>

**WhenEstablished**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

Specifies when the association was established. Must be set to NULL if implementation is not capable of providing this information. A value of 0 indicates the information is not known.

This property is inherited from [**CIM\_Synchronized**](cim-synchronized.md).

</dd> <dt>

**WhenSuspended**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

Specifies when the association was suspended. A suspended association is resumed.Must be set to NULL if implementation is not capable of providing this information. A value of 0 indicates the information is not known.

This property is inherited from [**CIM\_Synchronized**](cim-synchronized.md).

</dd> <dt>

**WhenSynced**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The point in time that the Elements were synchronized.

This property is inherited from [**CIM\_Synchronized**](cim-synchronized.md).

</dd> <dt>

**WhenSynchronized**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

Specifies when the CopyState has a value of Synchronized. Must be set to NULL if implementation is not capable of providing this information. A value of 0 indicates the information is not known.

This property is inherited from [**CIM\_Synchronized**](cim-synchronized.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Synchronized**](cim-synchronized.md)
</dt> </dl>

 

 





