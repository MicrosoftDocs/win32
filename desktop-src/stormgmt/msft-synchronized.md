---
title: MSFT\_Synchronized class
description: Synchronized status of a storage object and its snapshots, clones, or mirrors.
ms.assetid: '460FAAB4-9DB2-4B02-9E2B-07791E93E728'
keywords: ["MSFT_Synchronized class Windows Storage Management API", "MSFT_Synchronized class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_Synchronized
- MSFT_Synchronized.SyncTime
- MSFT_Synchronized.SyncMaintained
- MSFT_Synchronized.CopyState
- MSFT_Synchronized.RequestedCopyState
- MSFT_Synchronized.SyncType
- MSFT_Synchronized.SyncMode
- MSFT_Synchronized.ProgressStatus
- MSFT_Synchronized.PercentSynced
- MSFT_Synchronized.CopyType
- MSFT_Synchronized.ReplicaType
- MSFT_Synchronized.SyncState
- MSFT_Synchronized.CopyPriority
- MSFT_Synchronized.CopyMethodology
- MSFT_Synchronized.RecoveryPointObjective
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_Synchronized class

Synchronized status of a storage object and its snapshots, clones, or mirrors.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_Synchronized
{
  DateTime SyncTime;
  Boolean  SyncMaintained;
  UInt16   CopyState;
  UInt16   RequestedCopyState;
  UInt16   SyncType;
  UInt16   SyncMode;
  UInt16   ProgressStatus;
  UInt16   PercentSynced;
  UInt16   CopyType;
  UInt16   ReplicaType;
  UInt16   SyncState;
  UInt16   CopyPriority;
  UInt16   CopyMethodology;
  UInt16   RecoveryPointObjective[];
};
```

## Members

The **MSFT\_Synchronized** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_Synchronized** class has these properties.

<dl> <dt>

**CopyMethodology**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the copy methodology that the copy engine uses to create and/or maintain the target element.



| Value                                                                                                                                                                                                                                                                                   | Meaning                                                                                                                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Not_Specified"></span><span id="not_specified"></span><span id="NOT_SPECIFIED"></span><dl> <dt>**Not Specified**</dt> <dt>0</dt> </dl>                                     | The method of maintaining the copy is not specified.<br/>                                                                                          |
| <span id="Other"></span><span id="other"></span><span id="OTHER"></span><dl> <dt>**Other**</dt> <dt>1</dt> </dl>                                                                     |                                                                                                                                                          |
| <span id="Implementation_decides"></span><span id="implementation_decides"></span><span id="IMPLEMENTATION_DECIDES"></span><dl> <dt>**Implementation decides**</dt> <dt>2</dt> </dl> |                                                                                                                                                          |
| <span id="Full_Copy"></span><span id="full_copy"></span><span id="FULL_COPY"></span><dl> <dt>**Full Copy**</dt> <dt>3</dt> </dl>                                                     | A full copy of the source object is (or will be) generated.<br/>                                                                                   |
| <span id="Incremental_Copy"></span><span id="incremental_copy"></span><span id="INCREMENTAL_COPY"></span><dl> <dt>**Incremental Copy**</dt> <dt>4</dt> </dl>                         | Only changed data from the source element is copied to the target element.<br/>                                                                    |
| <span id="Differential_Copy"></span><span id="differential_copy"></span><span id="DIFFERENTIAL_COPY"></span><dl> <dt>**Differential Copy**</dt> <dt>5</dt> </dl>                     | Only the new writes to the source element are copied to the target element.<br/>                                                                   |
| <span id="Copy_On_Write"></span><span id="copy_on_write"></span><span id="COPY_ON_WRITE"></span><dl> <dt>**Copy On Write**</dt> <dt>6</dt> </dl>                                     | Affected data is copied on the first write to the source or to the target elements.<br/>                                                           |
| <span id="Copy_On_Access"></span><span id="copy_on_access"></span><span id="COPY_ON_ACCESS"></span><dl> <dt>**Copy On Access**</dt> <dt>7</dt> </dl>                                 | Affected data is copied on the first access to the source element.<br/>                                                                            |
| <span id="Delta_Update"></span><span id="delta_update"></span><span id="DELTA_UPDATE"></span><dl> <dt>**Delta Update**</dt> <dt>8</dt> </dl>                                         | Difference-based replication where, after the initial copy, only updates to the source are copied to the target.<br/>                              |
| <span id="Snap_And______Clone"></span><span id="snap_and______clone"></span><span id="SNAP_AND______CLONE"></span><dl> <dt>**Snap And Clone**</dt> <dt>9</dt> </dl>                  | The service creates a snapshot of the source element first, then uses the snapshot as the source of the copy operation to the target element.<br/> |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span><dl> <dt>**Microsoft Reserved**</dt> <dt>..</dt> </dl>                |                                                                                                                                                          |
| <span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span><dl> <dt>**Vendor Specific**</dt> <dt>0x8000..</dt> </dl>                      |                                                                                                                                                          |



 

</dd> <dt>

**CopyPriority**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Allows the priority of background copy engine I/O to be managed relative to host I/O operations during a sequential background copy operation.



| Value                                                                                                                                                                                                                                                                    | Meaning                                                       |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <span id="Not_Managed"></span><span id="not_managed"></span><span id="NOT_MANAGED"></span><dl> <dt>**Not Managed**</dt> <dt>0</dt> </dl>                              |                                                               |
| <span id="Low"></span><span id="low"></span><span id="LOW"></span><dl> <dt>**Low**</dt> <dt>1</dt> </dl>                                                              | Copy engine I/O has lower priority than host I/O.<br/>  |
| <span id="Same"></span><span id="same"></span><span id="SAME"></span><dl> <dt>**Same**</dt> <dt>2</dt> </dl>                                                          | Copy engine I/O has the same priority as host I/O.<br/> |
| <span id="High"></span><span id="high"></span><span id="HIGH"></span><dl> <dt>**High**</dt> <dt>3</dt> </dl>                                                          | copy engine I/O has higher priority as host I/O.<br/>   |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span><dl> <dt>**Microsoft Reserved**</dt> <dt>..</dt> </dl> |                                                               |
| <span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span><dl> <dt>**Vendor Specific**</dt> <dt>0x8000..</dt> </dl>       |                                                               |



 

</dd> <dt>

**CopyState**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes the state of the association with respect to replication activity.



| Value                                                                                                                                                                                                                                                                    | Meaning                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Initialized"></span><span id="initialized"></span><span id="INITIALIZED"></span><dl> <dt>**Initialized**</dt> <dt>2</dt> </dl>                              | The link to enable replication is established, and source and replica elements are associated, but the copy operation has not started.<br/>                                       |
| <span id="Unsynchronized"></span><span id="unsynchronized"></span><span id="UNSYNCHRONIZED"></span><dl> <dt>**Unsynchronized**</dt> <dt>3</dt> </dl>                  | Not all the source element data has been copied to the target element.<br/>                                                                                                       |
| <span id="Synchronized"></span><span id="synchronized"></span><span id="SYNCHRONIZED"></span><dl> <dt>**Synchronized**</dt> <dt>4</dt> </dl>                          | For mirror, snapshot, or clone replication, the target represents a copy of the source.<br/>                                                                                      |
| <span id="Broken"></span><span id="broken"></span><span id="BROKEN"></span><dl> <dt>**Broken**</dt> <dt>5</dt> </dl>                                                  | The relationship is non-functional due to errors in the source, the target, the path between the two, or space constraints.<br/>                                                  |
| <span id="Fractured"></span><span id="fractured"></span><span id="FRACTURED"></span><dl> <dt>**Fractured**</dt> <dt>6</dt> </dl>                                      | The target is split from the source.<br/>                                                                                                                                         |
| <span id="Split"></span><span id="split"></span><span id="SPLIT"></span><dl> <dt>**Split**</dt> <dt>7</dt> </dl>                                                      | The target element was gracefully (or systematically) split from its source element. Consistency is guaranteed.<br/>                                                              |
| <span id="Inactive"></span><span id="inactive"></span><span id="INACTIVE"></span><dl> <dt>**Inactive**</dt> <dt>8</dt> </dl>                                          | The copy operation has stopped. Writes to the source element will not be sent to target element.<br/>                                                                             |
| <span id="Suspended"></span><span id="suspended"></span><span id="SUSPENDED"></span><dl> <dt>**Suspended**</dt> <dt>9</dt> </dl>                                      | Data flow between the source and target elements has stopped. Writes to the source element are held until the association is resumed.<br/>                                        |
| <span id="Failedover"></span><span id="failedover"></span><span id="FAILEDOVER"></span><dl> <dt>**Failedover**</dt> <dt>10</dt> </dl>                                 | Reads and writes to and from the target element have failed. The source element is not reachable.<br/>                                                                            |
| <span id="Prepared"></span><span id="prepared"></span><span id="PREPARED"></span><dl> <dt>**Prepared**</dt> <dt>11</dt> </dl>                                         | Initialization has completed and the copy operation started. However, the data flow has not started.<br/>                                                                         |
| <span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span><dl> <dt>**Aborted**</dt> <dt>12</dt> </dl>                                             | The copy operation is aborted with the Abort operation. Use the Resync Replica operation to restart the copy operation.<br/>                                                      |
| <span id="Skewed"></span><span id="skewed"></span><span id="SKEWED"></span><dl> <dt>**Skewed**</dt> <dt>13</dt> </dl>                                                 | The target has been modified and is no longer synchronized with the source element or the point-in-time view.<br/>                                                                |
| <span id="Mixed"></span><span id="mixed"></span><span id="MIXED"></span><dl> <dt>**Mixed**</dt> <dt>14</dt> </dl>                                                     | Applies to the *CopyState* of *GroupSynchronized*. It indicates that the *StorageSynchronized* associations of the elements in the groups have different *CopyState* values.<br/> |
| <span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span><dl> <dt>**Not Applicable**</dt> <dt>15</dt> </dl>                 | The target does not have a replication state.<br/>                                                                                                                                |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span><dl> <dt>**Microsoft Reserved**</dt> <dt>..</dt> </dl> | This value is reserved for system use.<br/>                                                                                                                                       |
| <span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span><dl> <dt>**Vendor Specific**</dt> <dt>0x8000..</dt> </dl>       | These values are reserved for vendors.<br/>                                                                                                                                       |



 

</dd> <dt>

**CopyType**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes the replication policy.



| Value                                                                                                                                                                                                                                                                    | Meaning                                                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| <span id="Async"></span><span id="async"></span><span id="ASYNC"></span><dl> <dt>**Async**</dt> <dt>2</dt> </dl>                                                      | Create and maintain an asynchronous copy of the source.<br/>                                                           |
| <span id="Sync"></span><span id="sync"></span><span id="SYNC"></span><dl> <dt>**Sync**</dt> <dt>3</dt> </dl>                                                          | Create and maintain a synchronized copy of the source.<br/>                                                            |
| <span id="UnSyncAssoc"></span><span id="unsyncassoc"></span><span id="UNSYNCASSOC"></span><dl> <dt>**UnSyncAssoc**</dt> <dt>4</dt> </dl>                              | Create an unsynchronized copy and maintain an association to the source.<br/>                                          |
| <span id="UnSyncUnAssoc"></span><span id="unsyncunassoc"></span><span id="UNSYNCUNASSOC"></span><dl> <dt>**UnSyncUnAssoc**</dt> <dt>5</dt> </dl>                      | Create an unsynchronized copy with a temporary association that is deleted upon completion of the copy operation.<br/> |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span><dl> <dt>**Microsoft Reserved**</dt> <dt>..</dt> </dl> |                                                                                                                              |
| <span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span><dl> <dt>**Vendor Specific**</dt> <dt>0x8000..</dt> </dl>       |                                                                                                                              |



 

</dd> <dt>

**PercentSynced**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the percent of the work completed to reach synchronization. Must be set to **NULL** if the implementation is not capable of providing this information.

</dd> <dt>

**ProgressStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes the status of the association with respect to replication activity.



| Value                                                                                                                                                                                                                                                                    | Meaning                                                                                                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                              |                                                                                                                                                                 |
| <span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span><dl> <dt>**Completed**</dt> <dt>2</dt> </dl>                                      | The request is completed. Copy operation is idle.<br/>                                                                                                    |
| <span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span><dl> <dt>**Dormant**</dt> <dt>3</dt> </dl>                                              | The copy operation is inactive, suspended, or quiesced.<br/>                                                                                              |
| <span id="Initializing"></span><span id="initializing"></span><span id="INITIALIZING"></span><dl> <dt>**Initializing**</dt> <dt>4</dt> </dl>                          | In the process of establishing the source/replica association. The copy operation has not started.<br/>                                                   |
| <span id="Preparing"></span><span id="preparing"></span><span id="PREPARING"></span><dl> <dt>**Preparing**</dt> <dt>5</dt> </dl>                                      | Preparation is in progress.<br/>                                                                                                                          |
| <span id="Synchronizing"></span><span id="synchronizing"></span><span id="SYNCHRONIZING"></span><dl> <dt>**Synchronizing**</dt> <dt>6</dt> </dl>                      | Sync is in progress.<br/>                                                                                                                                 |
| <span id="Resyncing"></span><span id="resyncing"></span><span id="RESYNCING"></span><dl> <dt>**Resyncing**</dt> <dt>7</dt> </dl>                                      | Resync is in progress.<br/>                                                                                                                               |
| <span id="Restoring"></span><span id="restoring"></span><span id="RESTORING"></span><dl> <dt>**Restoring**</dt> <dt>8</dt> </dl>                                      | Restore is in progress.<br/>                                                                                                                              |
| <span id="Fracturing"></span><span id="fracturing"></span><span id="FRACTURING"></span><dl> <dt>**Fracturing**</dt> <dt>9</dt> </dl>                                  | Fracture is in progress.<br/>                                                                                                                             |
| <span id="Splitting"></span><span id="splitting"></span><span id="SPLITTING"></span><dl> <dt>**Splitting**</dt> <dt>10</dt> </dl>                                     | Split is in progress.<br/>                                                                                                                                |
| <span id="Failing_over"></span><span id="failing_over"></span><span id="FAILING_OVER"></span><dl> <dt>**Failing over**</dt> <dt>11</dt> </dl>                         | In the process of switching source and target.<br/>                                                                                                       |
| <span id="Failing_back"></span><span id="failing_back"></span><span id="FAILING_BACK"></span><dl> <dt>**Failing back**</dt> <dt>12</dt> </dl>                         | Undoing the result of failover.<br/>                                                                                                                      |
| <span id="Detaching"></span><span id="detaching"></span><span id="DETACHING"></span><dl> <dt>**Detaching**</dt> <dt>13</dt> </dl>                                     | Detach in progress.<br/>                                                                                                                                  |
| <span id="Aborting"></span><span id="aborting"></span><span id="ABORTING"></span><dl> <dt>**Aborting**</dt> <dt>14</dt> </dl>                                         | Abort in progress.<br/>                                                                                                                                   |
| <span id="Mixed"></span><span id="mixed"></span><span id="MIXED"></span><dl> <dt>**Mixed**</dt> <dt>15</dt> </dl>                                                     | Applies to groups with element pairs with different statuses. Generally, the individual statuses need to be examined.<br/>                                |
| <span id="Suspending"></span><span id="suspending"></span><span id="SUSPENDING"></span><dl> <dt>**Suspending**</dt> <dt>16</dt> </dl>                                 | The copy operation is in the process of being suspended.<br/>                                                                                             |
| <span id="Requires_fracture"></span><span id="requires_fracture"></span><span id="REQUIRES_FRACTURE"></span><dl> <dt>**Requires fracture**</dt> <dt>17</dt> </dl>     | The requested operation has completed. However, the synchronization relationship needs to be fractured before further copy operations can be issued.<br/> |
| <span id="Requires_resync"></span><span id="requires_resync"></span><span id="REQUIRES_RESYNC"></span><dl> <dt>**Requires resync**</dt> <dt>18</dt> </dl>             | The requested operation has completed. However, the synchronization relationship needs to be resynced before further copy operations can be issued.<br/>  |
| <span id="Requires_activate"></span><span id="requires_activate"></span><span id="REQUIRES_ACTIVATE"></span><dl> <dt>**Requires activate**</dt> <dt>19</dt> </dl>     | The requested operation has completed. However, the synchronization relationship needs to be activated before further copy operations can be issued.<br/> |
| <span id="Pending"></span><span id="pending"></span><span id="PENDING"></span><dl> <dt>**Pending**</dt> <dt>20</dt> </dl>                                             | The flow of data has stopped momentarily due to limited bandwidth or a busy system.<br/>                                                                  |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span><dl> <dt>**Microsoft Reserved**</dt> <dt>..</dt> </dl> |                                                                                                                                                                 |
| <span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span><dl> <dt>**Vendor Specific**</dt> <dt>0x8000..</dt> </dl>       |                                                                                                                                                                 |



 

</dd> <dt>

**RecoveryPointObjective**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the maximum interval in which data might be lost. For synchronous copy operations, *RecoveryPointObjective* is 0. For asynchronous copy operations *RecoveryPointObjective* represents the interval since the most recent transmission of data to the target element.

</dd> <dt>

**ReplicaType**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides information on how the replica is being maintained.



| Value                                                                                                                                                                                                                                                                    | Meaning                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| <span id="Not_Specified"></span><span id="not_specified"></span><span id="NOT_SPECIFIED"></span><dl> <dt>**Not Specified**</dt> <dt>0</dt> </dl>                      | The method of maintaining the copy is not specified.<br/>                      |
| <span id="Full_Copy"></span><span id="full_copy"></span><span id="FULL_COPY"></span><dl> <dt>**Full Copy**</dt> <dt>2</dt> </dl>                                      | A full copy of the source object is (or will be) generated.<br/>               |
| <span id="Before_Delta"></span><span id="before_delta"></span><span id="BEFORE_DELTA"></span><dl> <dt>**Before Delta**</dt> <dt>3</dt> </dl>                          | The source object will be maintained as a delta data from the replica.<br/>    |
| <span id="After_Delta"></span><span id="after_delta"></span><span id="AFTER_DELTA"></span><dl> <dt>**After Delta**</dt> <dt>4</dt> </dl>                              | The replica will be maintained as delta data from the source object.<br/>      |
| <span id="Log"></span><span id="log"></span><span id="LOG"></span><dl> <dt>**Log**</dt> <dt>5</dt> </dl>                                                              | The replica object is being maintained as a log of changes to the source.<br/> |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span><dl> <dt>**Microsoft Reserved**</dt> <dt>..</dt> </dl> |                                                                                      |
| <span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span><dl> <dt>**Vendor Specific**</dt> <dt>0x8000..</dt> </dl>       |                                                                                      |



 

</dd> <dt>

**RequestedCopyState**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An integer enumeration that indicates the last requested or desired state for the association. The actual state of the association is represented by *CopyState*. Note that when *CopyState* reaches the requested state, his property will be set to "Not Applicable".

</dd> <dt>

**SyncMaintained**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether synchronization is maintained.

</dd> <dt>

**SyncMode**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes whether the target elements will be updated synchronously or asynchronously. If **NULL**, the implementation decides the mode.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Synchronous"></span><span id="synchronous"></span><span id="SYNCHRONOUS"></span>**Synchronous** (2)
</dt> <dt>

<span id="Asynchronous"></span><span id="asynchronous"></span><span id="ASYNCHRONOUS"></span>**Asynchronous** (3)
</dt> <dt>

<span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span>**Microsoft Reserved** (..)
</dt> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific** (32768..65535)
</dt> </dl>

</dd> <dt>

**SyncState**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes the state of the association with respect to replication activity.



| Value                                                                                                                                                                                                                                                                           | Meaning                                                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Initialized"></span><span id="initialized"></span><span id="INITIALIZED"></span><dl> <dt>**Initialized**</dt> <dt>2</dt> </dl>                                     | The link to enable replication is established and source/replica elements are associated, but the copy engine has not started.<br/>   |
| <span id="PrepareInProgress"></span><span id="prepareinprogress"></span><span id="PREPAREINPROGRESS"></span><dl> <dt>**PrepareInProgress**</dt> <dt>3</dt> </dl>             | Preparation for replication is in progress and the copy engine has started.<br/>                                                      |
| <span id="Prepared"></span><span id="prepared"></span><span id="PREPARED"></span><dl> <dt>**Prepared**</dt> <dt>4</dt> </dl>                                                 | All necessary preparation has completed.<br/>                                                                                         |
| <span id="ResyncInProgress"></span><span id="resyncinprogress"></span><span id="RESYNCINPROGRESS"></span><dl> <dt>**ResyncInProgress**</dt> <dt>5</dt> </dl>                 | Synchronization or resynchronization is in progress. This may be the initial copy or subsequent changes being copied.<br/>            |
| <span id="Synchronized"></span><span id="synchronized"></span><span id="SYNCHRONIZED"></span><dl> <dt>**Synchronized**</dt> <dt>6</dt> </dl>                                 | An async or sync replication is currently synchronized. When this value is set, *SyncMaintained* will be true.<br/>                   |
| <span id="Fracture_In_Progress"></span><span id="fracture_in_progress"></span><span id="FRACTURE_IN_PROGRESS"></span><dl> <dt>**Fracture In Progress**</dt> <dt>7</dt> </dl> | An operation to fracture an async or sync replication is in progress.<br/>                                                            |
| <span id="QuiesceInProgress"></span><span id="quiesceinprogress"></span><span id="QUIESCEINPROGRESS"></span><dl> <dt>**QuiesceInProgress**</dt> <dt>8</dt> </dl>             | A quiesce operation is in progress.<br/>                                                                                              |
| <span id="Quiesced"></span><span id="quiesced"></span><span id="QUIESCED"></span><dl> <dt>**Quiesced**</dt> <dt>9</dt> </dl>                                                 | The replication has been quiesced and is ready for a change.<br/>                                                                     |
| <span id="Restore_In_Progress"></span><span id="restore_in_progress"></span><span id="RESTORE_IN_PROGRESS"></span><dl> <dt>**Restore In Progress**</dt> <dt>10</dt> </dl>    | Operation is in progress to copy the synced object to the system object.<br/>                                                         |
| <span id="Idle"></span><span id="idle"></span><span id="IDLE"></span><dl> <dt>**Idle**</dt> <dt>11</dt> </dl>                                                                | The normal state for an **UnSyncAssoc** replica.<br/>                                                                                 |
| <span id="Broken"></span><span id="broken"></span><span id="BROKEN"></span><dl> <dt>**Broken**</dt> <dt>12</dt> </dl>                                                        | The relationship is non-functional due to errors in the source, the target, the path between the two, or space constraints.<br/>      |
| <span id="Fractured"></span><span id="fractured"></span><span id="FRACTURED"></span><dl> <dt>**Fractured**</dt> <dt>13</dt> </dl>                                            | An async or sync replication is fractured.<br/>                                                                                       |
| <span id="Frozen"></span><span id="frozen"></span><span id="FROZEN"></span><dl> <dt>**Frozen**</dt> <dt>14</dt> </dl>                                                        | All blocks are copied from the source to an **UnSyncAssoc** replica, and the copy engine is stopped.<br/>                             |
| <span id="Copy_In_Progress"></span><span id="copy_in_progress"></span><span id="COPY_IN_PROGRESS"></span><dl> <dt>**Copy In Progress**</dt> <dt>15</dt> </dl>                | A deferred background copy operation is in progress to copy the source to the replica target for an **UnSyncAssoc** association.<br/> |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span><dl> <dt>**Microsoft Reserved**</dt> <dt>..</dt> </dl>        |                                                                                                                                             |
| <span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span><dl> <dt>**Vendor Specific**</dt> <dt>0x8000..</dt> </dl>              |                                                                                                                                             |



 

</dd> <dt>

**SyncTime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The point in time that the virtual disks were synchronized.

</dd> <dt>

**SyncType**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Describes the intended outcome of the replication.



| Value                                                                                                                                                                                                                                                                    | Meaning                                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span><dl> <dt>**Microsoft Reserved**</dt> <dt>..</dt> </dl> |                                                                |
| <span id="Mirror"></span><span id="mirror"></span><span id="MIRROR"></span><dl> <dt>**Mirror**</dt> <dt>6</dt> </dl>                                                  | Create and maintain a copy of the source.<br/>           |
| <span id="Snapshot"></span><span id="snapshot"></span><span id="SNAPSHOT"></span><dl> <dt>**Snapshot**</dt> <dt>7</dt> </dl>                                          | Create a point-in-time, virtual copy of the source.<br/> |
| <span id="Clone"></span><span id="clone"></span><span id="CLONE"></span><dl> <dt>**Clone**</dt> <dt>8</dt> </dl>                                                      | Create a point-in-time, full copy the source.<br/>       |
| <span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span><dl> <dt>**Microsoft Reserved**</dt> <dt>..</dt> </dl> |                                                                |
| <span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span><dl> <dt>**Vendor Specific**</dt> <dt>0x8000..</dt> </dl>       |                                                                |



 

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



 

 





