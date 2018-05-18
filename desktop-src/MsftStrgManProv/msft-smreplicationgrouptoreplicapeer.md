---
title: MSFT\_SMReplicationGroupToReplicaPeer class
description: Represents an association between a replication group and a replica peer.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '66e95abb-c1af-44e3-b56c-ed4de0367458'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SMReplicationGroupToReplicaPeer class", "MSFT_SMReplicationGroupToReplicaPeer class, described"]
topic_type:
- apiref
api_name:
- MSFT_SMReplicationGroupToReplicaPeer
- MSFT_SMReplicationGroupToReplicaPeer.WhenSynced
- MSFT_SMReplicationGroupToReplicaPeer.SyncMaintained
- MSFT_SMReplicationGroupToReplicaPeer.CopyState
- MSFT_SMReplicationGroupToReplicaPeer.CopyStateDescription
- MSFT_SMReplicationGroupToReplicaPeer.RequestedCopyState
- MSFT_SMReplicationGroupToReplicaPeer.SyncType
- MSFT_SMReplicationGroupToReplicaPeer.SyncTypeDescription
- MSFT_SMReplicationGroupToReplicaPeer.Mode
- MSFT_SMReplicationGroupToReplicaPeer.ModeDescription
- MSFT_SMReplicationGroupToReplicaPeer.ProgressStatus
- MSFT_SMReplicationGroupToReplicaPeer.ProgressStatusDescription
- MSFT_SMReplicationGroupToReplicaPeer.PercentSynced
- MSFT_SMReplicationGroupToReplicaPeer.WhenEstablished
- MSFT_SMReplicationGroupToReplicaPeer.WhenSynchronized
- MSFT_SMReplicationGroupToReplicaPeer.WhenActivated
- MSFT_SMReplicationGroupToReplicaPeer.WhenDeactivated
- MSFT_SMReplicationGroupToReplicaPeer.WhenSuspended
- MSFT_SMReplicationGroupToReplicaPeer.CopyType
- MSFT_SMReplicationGroupToReplicaPeer.CopyTypeDescription
- MSFT_SMReplicationGroupToReplicaPeer.RelationshipName
- MSFT_SMReplicationGroupToReplicaPeer.ConsistencyEnabled
- MSFT_SMReplicationGroupToReplicaPeer.ConsistencyType
- MSFT_SMReplicationGroupToReplicaPeer.ConsistencyState
- MSFT_SMReplicationGroupToReplicaPeer.ConsistencyStatus
- MSFT_SMReplicationGroupToReplicaPeer.Parent
- MSFT_SMReplicationGroupToReplicaPeer.Child
api_location:
- StorageService.dll
api_type:
- DllExport
---

# MSFT\_SMReplicationGroupToReplicaPeer class

Represents an association between a replication group and a replica peer.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("WMIStorage"), AMENDMENT]
class MSFT_SMReplicationGroupToReplicaPeer : MSFT_SMGroupSynchronizedBase
{
  datetime                    WhenSynced;
  boolean                     SyncMaintained;
  uint16                      CopyState;
  string                      CopyStateDescription;
  uint16                      RequestedCopyState = 15;
  uint16                      SyncType;
  string                      SyncTypeDescription;
  uint16                      Mode;
  string                      ModeDescription;
  uint16                      ProgressStatus;
  string                      ProgressStatusDescription;
  uint16                      PercentSynced;
  datetime                    WhenEstablished;
  datetime                    WhenSynchronized;
  datetime                    WhenActivated;
  datetime                    WhenDeactivated;
  datetime                    WhenSuspended;
  uint16                      CopyType;
  string                      CopyTypeDescription;
  string                      RelationshipName;
  boolean                     ConsistencyEnabled = FALSE;
  uint16                      ConsistencyType;
  uint16                      ConsistencyState = 2;
  uint16                      ConsistencyStatus;
  MSFT_SMReplicationGroup REF Parent;
  MSFT_SMReplicaPeer      REF Child;
};
```

## Members

The **MSFT\_SMReplicationGroupToReplicaPeer** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMReplicationGroupToReplicaPeer** class has these properties.

<dl> <dt>

**Child**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_SMReplicaPeer**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The [**MSFT\_SMReplicaPeer**](msft-smreplicapeer.md) object that represents the replica peer in the association.

</dd> <dt>

**ConsistencyEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Set to true if consistency is enabled.

This property is inherited from [**MSFT\_SMGroupSynchronizedBase**](msft-smgroupsynchronizedbase.md).

</dd> <dt>

**ConsistencyState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the current state of consistency.

This property is inherited from [**MSFT\_SMGroupSynchronizedBase**](msft-smgroupsynchronizedbase.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (2)


</dt> <dd></dd> <dt>

<span id="Consistent"></span><span id="consistent"></span><span id="CONSISTENT"></span>

**Consistent** (3)


</dt> <dd></dd> <dt>

<span id="Inconsistent"></span><span id="inconsistent"></span><span id="INCONSISTENT"></span>

**Inconsistent** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**ConsistencyStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the current status of consistency. Consistency may have been disabled or is experiencing an error condition.

This property is inherited from [**MSFT\_SMGroupSynchronizedBase**](msft-smgroupsynchronizedbase.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>

**Completed** (2)


</dt> <dd></dd> <dt>

<span id="Consistency-in-progress"></span><span id="consistency-in-progress"></span><span id="CONSISTENCY-IN-PROGRESS"></span>

**Consistency-in-progress** (3)


</dt> <dd></dd> <dt>

<span id="Consistency_disabled"></span><span id="consistency_disabled"></span><span id="CONSISTENCY_DISABLED"></span>

**Consistency disabled** (4)


</dt> <dd></dd> <dt>

<span id="Consistency-error"></span><span id="consistency-error"></span><span id="CONSISTENCY-ERROR"></span>

**Consistency-error** (5)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>6–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**ConsistencyType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the consistency type used by the source and its associated target group.

This property is inherited from [**MSFT\_SMGroupSynchronizedBase**](msft-smgroupsynchronizedbase.md).

<dt>

<span id="Sequentially_Consistent"></span><span id="sequentially_consistent"></span><span id="SEQUENTIALLY_CONSISTENT"></span>

**Sequentially Consistent** (2)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>3–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl>

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

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

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


</dt> <dd>16–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**CopyStateDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the **CopyState** property value.

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

</dd> <dt>

**CopyType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The replication policy of the association.

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

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


</dt> <dd>6–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–...</dd> </dl>

</dd> <dt>

**CopyTypeDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the **CopyType** value.

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

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

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

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


</dt> <dd>4–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**ModeDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the **Mode** value.

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

</dd> <dt>

**Parent**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_SMReplicationGroup**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The [**MSFT\_SMReplicationGroup**](msft-smreplicationgroup.md) object that represents the replication group in the association.

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

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

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


</dt> <dd>22–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–...</dd> </dl>

</dd> <dt>

**ProgressStatusDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the **ProgressStatus** value.

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

</dd> <dt>

**RelationshipName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A unique identifier for the relationship.

This property is inherited from [**MSFT\_SMGroupSynchronizedBase**](msft-smgroupsynchronizedbase.md).

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

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

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


</dt> <dd>16–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**SyncMaintained**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if the synchronization between the elements is maintained; otherwise, **False**.

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

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

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

The possible values are:

<dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>0–5</dd> <dt>

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


</dt> <dd>9–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–...</dd> </dl>

</dd> <dt>

**SyncTypeDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the **SyncType** property value.

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

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

</dd> <dt>

**WhenSynced**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A **datetime** value that indicates when the elements were synchronized.

This property is inherited from [**MSFT\_SMSynchronizedBase**](msft-smsynchronizedbase.md).

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

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMGroupSynchronizedBase**](msft-smgroupsynchronizedbase.md)
</dt> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





