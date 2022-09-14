---
title: MSAD_ReplNeighbor class
description: Represents the DS\_REPL\_NEIGHBOR structure, which contains the inbound replication state information for a particular naming context (NC) and source server pair.
ms.assetid: fdd3934b-a3f6-49ad-827b-077bcd21cf23
ms.tgt_platform: multiple
keywords:
- MSAD_ReplNeighbor class Active Directory
- MSAD_ReplNeighbor class Active Directory , described
topic_type:
- apiref
api_name:
- MSAD_ReplNeighbor
- MSAD_ReplNeighbor.NamingContextDN
- MSAD_ReplNeighbor.SourceDsaObjGuid
- MSAD_ReplNeighbor.NamingContextObjGuid
- MSAD_ReplNeighbor.SourceDsaDN
- MSAD_ReplNeighbor.SourceDsaAddress
- MSAD_ReplNeighbor.SourceDsaInvocationID
- MSAD_ReplNeighbor.AsyncIntersiteTransportDN
- MSAD_ReplNeighbor.AsyncIntersiteTransportObjGuid
- MSAD_ReplNeighbor.USNLastObjChangeSynced
- MSAD_ReplNeighbor.USNAttributeFilter
- MSAD_ReplNeighbor.TimeOfLastSyncSuccess
- MSAD_ReplNeighbor.TimeOfLastSyncAttempt
- MSAD_ReplNeighbor.LastSyncResult
- MSAD_ReplNeighbor.NumConsecutiveSyncFailures
- MSAD_ReplNeighbor.ReplicaFlags
- MSAD_ReplNeighbor.Writeable
- MSAD_ReplNeighbor.SyncOnStartup
- MSAD_ReplNeighbor.DoScheduledSyncs
- MSAD_ReplNeighbor.UseAsyncIntersiteTransport
- MSAD_ReplNeighbor.TwoWaySync
- MSAD_ReplNeighbor.FullSyncInProgress
- MSAD_ReplNeighbor.FullSyncNextPacket
- MSAD_ReplNeighbor.NeverSynced
- MSAD_ReplNeighbor.IgnoreChangeNotifications
- MSAD_ReplNeighbor.DisableScheduledSync
- MSAD_ReplNeighbor.CompressChanges
- MSAD_ReplNeighbor.NoChangeNotifications
- MSAD_ReplNeighbor.SourceDsaSite
- MSAD_ReplNeighbor.SourceDsaCN
- MSAD_ReplNeighbor.Domain
- MSAD_ReplNeighbor.IsDeletedSourceDsa
- MSAD_ReplNeighbor.ModifiedNumConsecutiveSyncFailures
api_location:
- replprov.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MSAD\_ReplNeighbor class

Represents the [**DS\_REPL\_NEIGHBOR**](/windows/desktop/api/Ntdsapi/ns-ntdsapi-ds_repl_neighborw) structure, which contains the inbound replication state information for a particular naming context (NC) and source server pair, as returned by the [**DsReplicaGetInfo**](/windows/desktop/api/Ntdsapi/nf-ntdsapi-dsreplicagetinfow) function.

## Syntax

``` syntax
[dynamic, provider("ReplProv1")]
class MSAD_ReplNeighbor
{
  String   NamingContextDN;
  String   SourceDsaObjGuid;
  String   NamingContextObjGuid;
  String   SourceDsaDN;
  String   SourceDsaAddress;
  String   SourceDsaInvocationID;
  String   AsyncIntersiteTransportDN;
  String   AsyncIntersiteTransportObjGuid;
  uint64   USNLastObjChangeSynced;
  uint64   USNAttributeFilter;
  datetime TimeOfLastSyncSuccess;
  datetime TimeOfLastSyncAttempt;
  uint32   LastSyncResult;
  uint32   NumConsecutiveSyncFailures;
  uint32   ReplicaFlags;
  boolean  Writeable = FALSE;
  boolean  SyncOnStartup = FALSE;
  boolean  DoScheduledSyncs = FALSE;
  boolean  UseAsyncIntersiteTransport = FALSE;
  boolean  TwoWaySync = FALSE;
  boolean  FullSyncInProgress = FALSE;
  boolean  FullSyncNextPacket = FALSE;
  boolean  NeverSynced = FALSE;
  boolean  IgnoreChangeNotifications = FALSE;
  boolean  DisableScheduledSync = FALSE;
  boolean  CompressChanges = FALSE;
  boolean  NoChangeNotifications = FALSE;
  String   SourceDsaSite;
  String   SourceDsaCN;
  String   Domain;
  boolean  IsDeletedSourceDsa = FALSE;
  uint32   ModifiedNumConsecutiveSyncFailures;
};
```

## Members

The **MSAD\_ReplNeighbor** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSAD\_ReplNeighbor** class has these methods.



| Method                                                           | Description                                                                   |
|:-----------------------------------------------------------------|:------------------------------------------------------------------------------|
| [**SyncNamingContext**](syncnamingcontext-msad-replneighbor.md) | Synchronizes a destination naming context with one of its sources.<br/> |



 

### Properties

The **MSAD\_ReplNeighbor** class has these properties.

<dl> <dt>

**AsyncIntersiteTransportDN**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the X.500 path of the [**interSiteTransport**](/windows/desktop/ADSchema/c-intersitetransport) object that corresponds to the transport over which replication is performed. Set to **NULL** for RPC/IP replication.

</dd> <dt>

**AsyncIntersiteTransportObjGuid**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the GUID of the intersite transport object that corresponds to the **AsyncIntersiteTransportDN** property.

</dd> <dt>

**CompressChanges**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the value that indicates whether the **DS\_REPL\_NBR\_COMPRESS\_CHANGES** flag has been set in the **ReplicaFlags** property.

</dd> <dt>

**DisableScheduledSync**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the value that indicates whether the **DS\_REPL\_NBR\_DISABLE\_SCHEDULED\_SYNC** flag has been set in the **ReplicaFlags** property.

</dd> <dt>

**Domain**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the canonical name of the domain of the replicated NC.

</dd> <dt>

**DoScheduledSyncs**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the value that indicates whether the **DS\_REPL\_NBR\_DO\_SCHEDULED\_SYNCS** flag has been set in the **ReplicaFlags** property.

</dd> <dt>

**FullSyncInProgress**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the value that indicates whether the **DS\_REPL\_NBR\_FULL\_SYNC\_IN\_PROGRESS** flag has been set in the **ReplicaFlags** property.

</dd> <dt>

**FullSyncNextPacket**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the value that indicates whether the **DS\_REPL\_NBR\_FULL\_SYNC\_NEXT\_PACKET** flag has been set in the **ReplicaFlags** property.

</dd> <dt>

**IgnoreChangeNotifications**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the value that indicates whether the **DS\_REPL\_NBR\_IGNORE\_CHANGE\_NOTIFICATIONS** flag has been set in the **ReplicaFlags** property.

</dd> <dt>

**IsDeletedSourceDsa**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the value that indicates whether this connection represents a source DC that has been deleted. **TRUE** if this connection represents a source DC that has been deleted; otherwise, **FALSE**. By design, the DS will continue to replicate these connections for some time for some time after the source DC is deleted.

</dd> <dt>

**LastSyncResult**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the **HRESULT** error code for the last replication attempt.

</dd> <dt>

**ModifiedNumConsecutiveSyncFailures**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the number of consecutive failed replication attempts, not including the connections that are expected to fail. For example, if the **IsDeletedSourceDsa** property is set to **TRUE**, it is expected to fail.

</dd> <dt>

**NamingContextDN**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Gets the X.500 path for the NC that is replicated by this connection.

</dd> <dt>

**NamingContextObjGuid**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the GUID for the replicated NC.

</dd> <dt>

**NeverSynced**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the value that indicates whether the **DS\_REPL\_NBR\_NEVER\_SYNCED** flag has been set in the **ReplicaFlags** property.

</dd> <dt>

**NoChangeNotifications**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the value that indicates whether the **DS\_REPL\_NBR\_NO\_CHANGE\_NOTIFICATIONS** flag has been set in the **ReplicaFlags** property.

</dd> <dt>

**NumConsecutiveSyncFailures**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the number of consecutive failed replication attempts.

</dd> <dt>

**ReplicaFlags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the set of flags that specify attributes and options for the replication data. This property can be zero or a combination of one or more of the following flags.

<dt>

<span id="DS_REPL_NBR_WRITEABLE"></span><span id="ds_repl_nbr_writeable"></span>

<span id="DS_REPL_NBR_WRITEABLE"></span><span id="ds_repl_nbr_writeable"></span>**DS\_REPL\_NBR\_WRITEABLE** (16 (0x10))


</dt> <dd>

The local copy of the naming context is writable.

</dd> <dt>

<span id="DS_REPL_NBR_SYNC_ON_STARTUP"></span><span id="ds_repl_nbr_sync_on_startup"></span>

<span id="DS_REPL_NBR_SYNC_ON_STARTUP"></span><span id="ds_repl_nbr_sync_on_startup"></span>**DS\_REPL\_NBR\_SYNC\_ON\_STARTUP** (32 (0x20))


</dt> <dd>

Replication of this naming context from this source is attempted when the destination server is booted. This flag usually only applies to intra-site neighbors.

</dd> <dt>

<span id="DS_REPL_NBR_DO_SCHEDULED_SYNCS"></span><span id="ds_repl_nbr_do_scheduled_syncs"></span>

<span id="DS_REPL_NBR_DO_SCHEDULED_SYNCS"></span><span id="ds_repl_nbr_do_scheduled_syncs"></span>**DS\_REPL\_NBR\_DO\_SCHEDULED\_SYNCS** (64 (0x40))


</dt> <dd>

Perform replication on a schedule. This flag is usually set unless the schedule for this naming context or source is "never", that is, the empty schedule.

</dd> <dt>

<span id="DS_REPL_NBR_USE_ASYNC_INTERSITE_TRANSPORT"></span><span id="ds_repl_nbr_use_async_intersite_transport"></span>

<span id="DS_REPL_NBR_USE_ASYNC_INTERSITE_TRANSPORT"></span><span id="ds_repl_nbr_use_async_intersite_transport"></span>**DS\_REPL\_NBR\_USE\_ASYNC\_INTERSITE\_TRANSPORT** (128 (0x80))


</dt> <dd>

Perform replication indirectly through the Inter-Site Messaging Service. This flag is set only when replicating over SMTP. This flag is not set when replicating over inter-site RPC/IP.

</dd> <dt>

<span id="DS_REPL_NBR_TWO_WAY_SYNC"></span><span id="ds_repl_nbr_two_way_sync"></span>

<span id="DS_REPL_NBR_TWO_WAY_SYNC"></span><span id="ds_repl_nbr_two_way_sync"></span>**DS\_REPL\_NBR\_TWO\_WAY\_SYNC** (512 (0x200))


</dt> <dd>

If set, indicates that when inbound replication is complete, the destination server must tell the source server to synchronize in the reverse direction. This feature is used in dial-up scenarios where only one of the two servers can initiate a dial-up connection. For example, this option could be used in a corporate headquarters and branch office, where the branch office connects to the corporate headquarters over the Internet by means of a dial-up ISP connection.

</dd> <dt>

<span id="DS_REPL_NBR_RETURN_OBJECT_PARENTS"></span><span id="ds_repl_nbr_return_object_parents"></span>

<span id="DS_REPL_NBR_RETURN_OBJECT_PARENTS"></span><span id="ds_repl_nbr_return_object_parents"></span>**DS\_REPL\_NBR\_RETURN\_OBJECT\_PARENTS** (2048 (0x800))


</dt> <dd>

This neighbor is in a state where it returns parent objects before children objects. It goes into this state after it receives a child object before its parent.

</dd> <dt>

<span id="DS_REPL_NBR_FULL_SYNC_IN_PROGRESS"></span><span id="ds_repl_nbr_full_sync_in_progress"></span>

<span id="DS_REPL_NBR_FULL_SYNC_IN_PROGRESS"></span><span id="ds_repl_nbr_full_sync_in_progress"></span>**DS\_REPL\_NBR\_FULL\_SYNC\_IN\_PROGRESS** (65536 (0x10000))


</dt> <dd>

The destination server is performing a full synchronization from the source server. Full synchronizations do not use vectors that create updates (such as [**DS\_REPL\_CURSORS**](/windows/desktop/api/Ntdsapi/ns-ntdsapi-ds_repl_cursors)) for filtering updates. Full synchronizations are not used as a part of the default replication protocol.

</dd> <dt>

<span id="DS_REPL_NBR_FULL_SYNC_NEXT_PACKET"></span><span id="ds_repl_nbr_full_sync_next_packet"></span>

<span id="DS_REPL_NBR_FULL_SYNC_NEXT_PACKET"></span><span id="ds_repl_nbr_full_sync_next_packet"></span>**DS\_REPL\_NBR\_FULL\_SYNC\_NEXT\_PACKET** (131072 (0x20000))


</dt> <dd>

The last packet from the source indicated a modification of an object that the destination server has not yet created. The next packet to be requested instructs the source server to put all attributes of the modified object into the packet.

</dd> <dt>

<span id="DS_REPL_NBR_NEVER_SYNCED"></span><span id="ds_repl_nbr_never_synced"></span>

<span id="DS_REPL_NBR_NEVER_SYNCED"></span><span id="ds_repl_nbr_never_synced"></span>**DS\_REPL\_NBR\_NEVER\_SYNCED** (2097152 (0x200000))


</dt> <dd>

A synchronization has never been successfully completed from this source.

</dd> <dt>

<span id="DS_REPL_NBR_PREEMPTED"></span><span id="ds_repl_nbr_preempted"></span>

<span id="DS_REPL_NBR_PREEMPTED"></span><span id="ds_repl_nbr_preempted"></span>**DS\_REPL\_NBR\_PREEMPTED** (16777216 (0x1000000))


</dt> <dd>

The replication engine has temporarily stopped processing this neighbor in order to service another higher-priority neighbor, either for this partition or for another partition. The replication engine will resume processing this neighbor after the higher-priority work is completed.

</dd> <dt>

<span id="DS_REPL_NBR_IGNORE_CHANGE_NOTIFICATIONS"></span><span id="ds_repl_nbr_ignore_change_notifications"></span>

<span id="DS_REPL_NBR_IGNORE_CHANGE_NOTIFICATIONS"></span><span id="ds_repl_nbr_ignore_change_notifications"></span>**DS\_REPL\_NBR\_IGNORE\_CHANGE\_NOTIFICATIONS** (67108864 (0x4000000))


</dt> <dd>

This neighbor is set to disable notification-based synchronizations. Within a site, domain controllers synchronize with each other based on notifications when changes occur. This setting prevents this neighbor from performing synchronizations that are triggered by notifications. The neighbor will still do synchronizations based on its schedule, or in response to manually requested synchronizations.

</dd> <dt>

<span id="DS_REPL_NBR_DISABLE_SCHEDULED_SYNC"></span><span id="ds_repl_nbr_disable_scheduled_sync"></span>

<span id="DS_REPL_NBR_DISABLE_SCHEDULED_SYNC"></span><span id="ds_repl_nbr_disable_scheduled_sync"></span>**DS\_REPL\_NBR\_DISABLE\_SCHEDULED\_SYNC** (134217728 (0x8000000))


</dt> <dd>

This neighbor is set to not perform synchronizations based on its schedule. The only way this neighbor will perform synchronizations is in response to change notifications or to manually requested synchronizations.

</dd> <dt>

<span id="DS_REPL_NBR_COMPRESS_CHANGES"></span><span id="ds_repl_nbr_compress_changes"></span>

<span id="DS_REPL_NBR_COMPRESS_CHANGES"></span><span id="ds_repl_nbr_compress_changes"></span>**DS\_REPL\_NBR\_COMPRESS\_CHANGES** (268435456 (0x10000000))


</dt> <dd>

Changes received from this source are to be compressed. Compression usually occurs only if the source server is in a different site.

</dd> <dt>

<span id="DS_REPL_NBR_NO_CHANGE_NOTIFICATIONS"></span><span id="ds_repl_nbr_no_change_notifications"></span>

<span id="DS_REPL_NBR_NO_CHANGE_NOTIFICATIONS"></span><span id="ds_repl_nbr_no_change_notifications"></span>**DS\_REPL\_NBR\_NO\_CHANGE\_NOTIFICATIONS** (536870912 (0x20000000))


</dt> <dd>

No change notifications should be received from this source. Usually set only if the source server is in a different site.

</dd> <dt>

<span id="DS_REPL_NBR_PARTIAL_ATTRIBUTE_SET"></span><span id="ds_repl_nbr_partial_attribute_set"></span>

<span id="DS_REPL_NBR_PARTIAL_ATTRIBUTE_SET"></span><span id="ds_repl_nbr_partial_attribute_set"></span>**DS\_REPL\_NBR\_PARTIAL\_ATTRIBUTE\_SET** (1073741824 (0x40000000))


</dt> <dd>

This neighbor is in a state where it is rebuilding the contents of this replica because of a change in the partial attribute set.

</dd> </dl>

</dd> <dt>

**SourceDsaAddress**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the DNS address of the source DC.

> [!Note]  
> This string contains a modified GUID, not the commonly used canonical DNS name.

 

</dd> <dt>

**SourceDsaCN**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the object path component for the DSA that represents the source DC. This string is often similar to the computer name but is not always identical.

</dd> <dt>

**SourceDsaDN**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the X.500 path for the DSA that represents the source DC.

</dd> <dt>

**SourceDsaInvocationID**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the invocation ID that was used by the source server as of the last replication.

</dd> <dt>

**SourceDsaObjGuid**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Gets the GUID for the directory service agent (DSA) that represents the source domain controller (DC).

</dd> <dt>

**SourceDsaSite**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the site that contains the source DC.

</dd> <dt>

**SyncOnStartup**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the value that indicates whether the **DS\_REPL\_NBR\_SYNC\_ON\_STARTUP** flag has been set in the **ReplicaFlags** property.

</dd> <dt>

**TimeOfLastSyncAttempt**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the timestamp for the last replication attempt.

</dd> <dt>

**TimeOfLastSyncSuccess**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the timestamp for the last successful replication attempt.

</dd> <dt>

**TwoWaySync**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the value that indicates whether the **DS\_REPL\_NBR\_TWO\_WAY\_SYNC** flag has been set in the **ReplicaFlags** property.

</dd> <dt>

**UseAsyncIntersiteTransport**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the value that indicates whether the **DS\_REPL\_NBR\_USE\_ASYNC\_INTERSITE\_TRANSPORT** flag has been set in the **ReplicaFlags** property.

</dd> <dt>

**USNAttributeFilter**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the **USNLastObjChangeSynced** property value at the end of the last successful completed replication cycle. Zero if there were no successfully completed replication cycles.

</dd> <dt>

**USNLastObjChangeSynced**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the [**unchanged**](/windows/desktop/ADSchema/a-usnchanged) attribute value of the last object update that was received.

</dd> <dt>

**Writeable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the value that indicates whether the **DS\_REPL\_NBR\_WRITEABLE** flag has been set in the **ReplicaFlags** property.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftActiveDirectory<br/>                                               |
| MOF<br/>                      | <dl> <dt>Replprov.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Replprov.dll</dt> </dl> |



 

