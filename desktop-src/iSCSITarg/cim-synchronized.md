---
title: CIM\_Synchronized class
description: Indicates that two ManagedElements were aligned or made to be equivalent at the specified point in time.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '43e2e891-692d-49f1-abb3-cca422504b8c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_Synchronized class iSCSI Software Target API", "CIM_Synchronized class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- CIM_Synchronized
- CIM_Synchronized.SystemElement
- CIM_Synchronized.SyncedElement
- CIM_Synchronized.WhenSynced
- CIM_Synchronized.SyncMaintained
- CIM_Synchronized.CopyState
- CIM_Synchronized.Mode
- CIM_Synchronized.PercentSynced
- CIM_Synchronized.ProgressStatus
- CIM_Synchronized.RequestedCopyState
- CIM_Synchronized.SyncType
- CIM_Synchronized.WhenActivated
- CIM_Synchronized.WhenDeactivated
- CIM_Synchronized.WhenEstablished
- CIM_Synchronized.WhenSuspended
- CIM_Synchronized.WhenSynchronized
- CIM_Synchronized.CopyRecoveryMode
- CIM_Synchronized.FailedCopyStopsHostIO
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# CIM\_Synchronized class

Indicates that two ManagedElements were aligned or made to be equivalent at the specified point in time. If the Boolean property SyncMaintained is true, then synchronization of the Elements is preserved. Both like and unlike objects can be synchronized. For example, two WatchDog timers can be aligned, or the contents of a LogicalFile can be synchronized with the contents of a StorageExtent.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Version("2.28.0"), UMLPackagePath("CIM::Core::CoreElements")]
class CIM_Synchronized
{
  CIM_ManagedElement REF SystemElement;
  CIM_ManagedElement REF SyncedElement;
  datetime               WhenSynced;
  boolean                SyncMaintained;
  uint16                 CopyState;
  uint16                 Mode;
  uint16                 PercentSynced;
  uint16                 ProgressStatus;
  uint16                 RequestedCopyState = 15;
  uint16                 SyncType;
  datetime               WhenActivated;
  datetime               WhenDeactivated;
  datetime               WhenEstablished;
  datetime               WhenSuspended;
  datetime               WhenSynchronized;
  uint16                 CopyRecoveryMode;
  boolean                FailedCopyStopsHostIO = FALSE;
};
```

## Members

The **CIM\_Synchronized** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_Synchronized** class has these properties.

<dl> <dt>

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


</dt> <dd>4–32767</dd> <dt>

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


</dt> <dd>18–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl>

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

**PercentSynced**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Experimental**](https://msdn.microsoft.com/library/aa392729)
</dt> </dl>

Specifies the percent of the work completed to reach synchronization. Must be set to NULL if implementation is not capable of providing this information.

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


</dt> <dd>32768–65535</dd> </dl>

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

</dd> <dt>

**SyncedElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

SyncedElement represents another ManagedElement that is synchronized with the entity referenced as SystemElement.

</dd> <dt>

**SyncMaintained**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Boolean indicating whether synchronization is maintained.

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


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**SystemElement**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

SystemElement represents one ManagedElement that is synchronized with the entity referenced as SyncedElement.

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

</dd> <dt>

**WhenSynced**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The point in time that the Elements were synchronized.

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

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



 

 





