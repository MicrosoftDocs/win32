---
title: MSFT\_WvrAdminTasks class
description: Used to administer a Storage Replica.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '73955d80-1092-4343-93da-b7691c266fac'
ms.prod: 'windows-server-dev'
ms.technology:
- 'storage-replica'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_WvrAdminTasks class", "MSFT_WvrAdminTasks class, described"]
---

# MSFT\_WvrAdminTasks class

Used to administer a Storage Replica.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("wvrcimprov"), AMENDMENT]
class MSFT_WvrAdminTasks
{
};
```

## Members

The **MSFT\_WvrAdminTasks** class has these types of members:

-   [Methods](#methods)

### Methods

The **MSFT\_WvrAdminTasks** class has these methods.



| Method                                                                                                  | Description                                                                                                                                                                                                                       |
|:--------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ActivateReplicaSet**](msft-wvradmintasks-activatereplicaset.md)                                     | Assigns replica set IDs and partitions to replication.<br/>                                                                                                                                                                 |
| [**ClearMetadataAll**](msft-wvradmintasks-clearmetadataall.md)                                         | Removes orphaned Storage Replica metadata from the registry, partition, and system volume information folder.<br/>                                                                                                          |
| [**ClearMetadataForReplicationGroup**](msft-wvradmintasks-clearmetadataforreplicationgroup.md)         | Removes orphaned Storage Replica metadata from the partition, and system volume information folder for a replication group. This operation may result in the restart of the specified computer.<br/>                        |
| [**CompareReplicationVector**](msft-wvradmintasks-comparereplicationvector.md)                         | Determines whether a destination replication group can connect to a source replication group.<br/>                                                                                                                          |
| [**CreatePartnership**](msft-wvradmintasks-createpartnership.md)                                       | Creates a replication partnership between two existing replication groups.<br/>                                                                                                                                             |
| [**CreateStretchPartnership**](msft-wvradmintasks-createstretchpartnership.md)                         | Creates a replication partnership between two existing replication groups.<br/>                                                                                                                                             |
| [**CreateStretchTopology**](msft-wvradmintasks-createstretchtopology.md)                               | Creates replication groups and a new replication partnership.<br/>                                                                                                                                                          |
| [**CreateTopology**](msft-wvradmintasks-createtopology.md)                                             | Creates replication groups and a new replication partnership.<br/>                                                                                                                                                          |
| [**DeactivateReplicaSet**](msft-wvradmintasks-deactivatereplicaset.md)                                 | Removes a partition from replication.<br/>                                                                                                                                                                                  |
| [**ExchangeReplicationGroupId**](msft-wvradmintasks-exchangereplicationgroupid.md)                     | Exchanges the replication group ID between source and destination replication groups.<br/>                                                                                                                                  |
| [**GetGroup**](msft-wvradmintasks-getgroup.md)                                                         | Retrieves a replication group.<br/>                                                                                                                                                                                         |
| [**GetGroupFromPartnership**](msft-wvradmintasks-getgroupfrompartnership.md)                           | Retrieves a replication group.<br/>                                                                                                                                                                                         |
| [**GetNetworkConstraint**](msft-wvradmintasks-getnetworkconstraint.md)                                 | Retrieves a replication network constraint for the partnership.<br/>                                                                                                                                                        |
| [**GetPartnership**](msft-wvradmintasks-getpartnership.md)                                             | Retrieves a replication partnership.<br/>                                                                                                                                                                                   |
| [**GetPartnershipFromGroup**](msft-wvradmintasks-getpartnershipfromgroup.md)                           | Retrieves a replication partnership.<br/>                                                                                                                                                                                   |
| [**GetSrAccess**](msft-wvradmintasks-getsraccess.md)                                                   | TBD<br/>                                                                                                                                                                                                                    |
| [**GetSrUserAccess**](msft-wvradmintasks-getsruseraccess.md)                                           | Returns users that have all capabilities required for them to manage Storage Replica on a given computer.<br/>                                                                                                              |
| [**GetStretchPartnership**](msft-wvradmintasks-getstretchpartnership.md)                               | Retrieves a replication partnership.<br/>                                                                                                                                                                                   |
| [**GrantSrAccess**](msft-wvradmintasks-grantsraccess.md)                                               | TBD<br/>                                                                                                                                                                                                                    |
| [**GrantSrUserAccess**](msft-wvradmintasks-grantsruseraccess.md)                                       | Grants the user all capabilities required to manage Storage Replica on a given computer.<br/>                                                                                                                               |
| [**NewSrGroup**](msft-wvradmintasks-newsrgroup.md)                                                     | Creates a replication group.<br/>                                                                                                                                                                                           |
| [**PairRemoteSubsystem**](msft-wvradmintasks-pairremotesubsystem.md)                                   | Pairing two computers or clusters for replication.<br/>                                                                                                                                                                     |
| [**ProvisionPartitionsAdd**](msft-wvradmintasks-provisionpartitionsadd.md)                             | Adds partition IDs to the partition database.<br/>                                                                                                                                                                          |
| [**ProvisionPartitionsRemove**](msft-wvradmintasks-provisionpartitionsremove.md)                       | Removes partition IDs from the partition database.<br/>                                                                                                                                                                     |
| [**QueryCounterInstance**](msft-wvradmintasks-querycounterinstance.md)                                 | Queries partition related performance counter information.<br/>                                                                                                                                                             |
| [**QueryPartitionInfo**](msft-wvradmintasks-querypartitioninfo.md)                                     | Queries the partition related information.<br/>                                                                                                                                                                             |
| [**QueryReplicaSet**](msft-wvradmintasks-queryreplicaset.md)                                           | Returns replica set information for a given replication group.<br/>                                                                                                                                                         |
| [**QueryReplicationPartners**](msft-wvradmintasks-queryreplicationpartners.md)                         | Returns the partners of a replication group.<br/>                                                                                                                                                                           |
| [**RemoveNetworkConstraint**](msft-wvradmintasks-removenetworkconstraint.md)                           | Removes an existing replication network constraint for the partnership.<br/>                                                                                                                                                |
| [**RemovePartnership**](msft-wvradmintasks-removepartnership.md)                                       | Removes an existing replication partnership.<br/>                                                                                                                                                                           |
| [**RemoveSrGroup**](msft-wvradmintasks-removesrgroup.md)                                               | Removes a replication group.<br/>                                                                                                                                                                                           |
| [**RemoveStretchPartnership**](msft-wvradmintasks-removestretchpartnership.md)                         | Removes an existing replication partnership.<br/>                                                                                                                                                                           |
| [**RemoveTopology**](msft-wvradmintasks-removetopology.md)                                             | Removes an existing replication partnership and its associated replication groups.<br/>                                                                                                                                     |
| [**RevokeSrAccess**](msft-wvradmintasks-revokesraccess.md)                                             | TBD<br/>                                                                                                                                                                                                                    |
| [**RevokeSrUserAccess**](msft-wvradmintasks-revokesruseraccess.md)                                     | Revokes capabilities required for the user to manage Storage Replica on a given computer.<br/>                                                                                                                              |
| [**SetGroupAddVolumes**](msft-wvradmintasks-setgroupaddvolumes.md)                                     | Adds volumes to an existing replication group.<br/>                                                                                                                                                                         |
| [**SetGroupModifyConfig**](msft-wvradmintasks-setgroupmodifyconfig.md)                                 | Modifies settings on an existing replication group.<br/>                                                                                                                                                                    |
| [**SetGroupRemoveVolumes**](msft-wvradmintasks-setgroupremovevolumes.md)                               | Removes volumes from an existing replication group.<br/>                                                                                                                                                                    |
| [**SetNetworkConstraint**](msft-wvradmintasks-setnetworkconstraint.md)                                 | Creates a new replication network constraint for the partnership.<br/>                                                                                                                                                      |
| [**SetPartnershipAddVolumes**](msft-wvradmintasks-setpartnershipaddvolumes.md)                         | Adds source and destination volumes to replication groups in an existing partnership.<br/>                                                                                                                                  |
| [**SetPartnershipModifyPartnership**](msft-wvradmintasks-setpartnershipmodifypartnership.md)           | Changes the RPO or log size settings to replication groups in an existing partnership.<br/>                                                                                                                                 |
| [**SetPartnershipSetSourcePartnership**](msft-wvradmintasks-setpartnershipsetsourcepartnership.md)     | Changes the source and destination replication direction between two replication groups.<br/>                                                                                                                               |
| [**SetSecondaryReplicationGroup**](msft-wvradmintasks-setsecondaryreplicationgroup.md)                 | Assigns a source to a destination replication group.<br/>                                                                                                                                                                   |
| [**SmapiAddMember**](msft-wvradmintasks-smapiaddmember.md)                                             | TBD<br/>                                                                                                                                                                                                                    |
| [**SmapiGetPairCluster**](msft-wvradmintasks-smapigetpaircluster.md)                                   | TBD<br/>                                                                                                                                                                                                                    |
| [**SmapiPairCluster**](msft-wvradmintasks-smapipaircluster.md)                                         | TBD<br/>                                                                                                                                                                                                                    |
| [**SmapiQueryPartnerGroupStatus**](msft-wvradmintasks-smapiquerypartnergroupstatus.md)                 | TBD<br/>                                                                                                                                                                                                                    |
| [**SmapiQueryPartnerPartitions**](msft-wvradmintasks-smapiquerypartnerpartitions.md)                   | Retrieves the partner partition information for this replication group.<br/>                                                                                                                                                |
| [**SmapiQueryReplicatedPartitions**](msft-wvradmintasks-smapiqueryreplicatedpartitions.md)             | TBD<br/>                                                                                                                                                                                                                    |
| [**SmapiRemoveMember**](msft-wvradmintasks-smapiremovemember.md)                                       | TBD<br/>                                                                                                                                                                                                                    |
| [**SmapiUnpairCluster**](msft-wvradmintasks-smapiunpaircluster.md)                                     | TBD<br/>                                                                                                                                                                                                                    |
| [**SuspendGroup**](msft-wvradmintasks-suspendgroup.md)                                                 | Pauses replication for a replication group.<br/>                                                                                                                                                                            |
| [**SyncGroup**](msft-wvradmintasks-syncgroup.md)                                                       | Starts or resumes replication for a replication group.<br/>                                                                                                                                                                 |
| [**UnpairRemoteSubsystem**](msft-wvradmintasks-unpairremotesubsystem.md)                               | Unpairing two computers or clusters from replication.<br/>                                                                                                                                                                  |
| [**VerifyReplicablePartition**](msft-wvradmintasks-verifyreplicablepartition.md)                       | Determines whether a partition can be replicated.<br/>                                                                                                                                                                      |
| [**WvrAddReplica**](msft-wvradmintasks-wvraddreplica.md)                                               | Adds a volume to an existing replication group.<br/>                                                                                                                                                                        |
| [**WvrAddReplicaById**](msft-wvradmintasks-wvraddreplicabyid.md)                                       | Adds a volume to an existing replication group and assigns a replica set ID to the volume.<br/>                                                                                                                             |
| [**WvrAddReplicaSet**](msft-wvradmintasks-wvraddreplicaset.md)                                         | TBD<br/>                                                                                                                                                                                                                    |
| [**WvrAddVolumePartnerStretchById**](msft-wvradmintasks-wvraddvolumepartnerstretchbyid.md)             | TBD<br/>                                                                                                                                                                                                                    |
| [**WvrCheckIfGroupsLogVolumeMatchVolume**](msft-wvradmintasks-wvrcheckifgroupslogvolumematchvolume.md) | Perform a remote cim call to check whether given replication group log volume matches with the volume which is to be removed from a group<br/>                                                                              |
| [**WvrClearOrphanedClusterResources**](msft-wvradmintasks-wvrclearorphanedclusterresources.md)         | Removes orphaned Storage Replica cluster resources.<br/>                                                                                                                                                                    |
| [**WvrClearOrphanedLogs**](msft-wvradmintasks-wvrclearorphanedlogs.md)                                 | Removes orphaned Storage Replica metadata from the Storage Replica log container for a replication group. If no ReplicationGroupName is specified the operation will be performed at a machine level.<br/>                  |
| [**WvrClearOrphanedPartitionDbRecord**](msft-wvradmintasks-wvrclearorphanedpartitiondbrecord.md)       | Removes orphaned Storage Replica metadata from the Storage Replica partition database.<br/>                                                                                                                                 |
| [**WvrCreateReplicationGroup**](msft-wvradmintasks-wvrcreatereplicationgroup.md)                       | Creates a new replication group.<br/>                                                                                                                                                                                       |
| [**WvrCreateReplicationPartnership**](msft-wvradmintasks-wvrcreatereplicationpartnership.md)           | Creates a new replication partnership between existing replication groups.<br/>                                                                                                                                             |
| [**WvrDeleteReplicationGroup**](msft-wvradmintasks-wvrdeletereplicationgroup.md)                       | Deletes a replication group.<br/>                                                                                                                                                                                           |
| [**WvrGetOrphanedPartitionDbRecords**](msft-wvradmintasks-wvrgetorphanedpartitiondbrecords.md)         | Retrieves a list of orphaned Storage Replica metadata from the Storage Replica partition database for a replication group. If no ReplicationGroupName is specified the operation will be performed at a machine level.<br/> |
| [**WvrGetUserAccess**](msft-wvradmintasks-wvrgetuseraccess.md)                                         | Performs a CIM call to obtain list of users that have permissions to manage Storage Replica.<br/>                                                                                                                           |
| [**WvrGrantUserAccess**](msft-wvradmintasks-wvrgrantuseraccess.md)                                     | Performs a CIM call to grant the user permissions to manage Storage Replica.<br/>                                                                                                                                           |
| [**WvrInitializeReplicationGroup**](msft-wvradmintasks-wvrinitializereplicationgroup.md)               | This routine initializes a newly provisioned replication group.<br/>                                                                                                                                                        |
| [**WvrModifyReplicationGroup**](msft-wvradmintasks-wvrmodifyreplicationgroup.md)                       | Modifies the settings in a replication group.<br/>                                                                                                                                                                          |
| [**WvrQueryClusterId**](msft-wvradmintasks-wvrqueryclusterid.md)                                       | TBD<br/>                                                                                                                                                                                                                    |
| [**WvrQueryReplicationGroupInfo**](msft-wvradmintasks-wvrqueryreplicationgroupinfo.md)                 | This routine queries metadata of a replication group.<br/>                                                                                                                                                                  |
| [**WvrRemoveNetworkConstraint**](msft-wvradmintasks-wvrremovenetworkconstraint.md)                     | Performs a CIM call to Remove Network Constraint from a partnership.<br/>                                                                                                                                                   |
| [**WvrRemoveReplica**](msft-wvradmintasks-wvrremovereplica.md)                                         | Removes a volume from an existing replication group.<br/>                                                                                                                                                                   |
| [**WvrRemoveReplicaById**](msft-wvradmintasks-wvrremovereplicabyid.md)                                 | Removes a partition from an existing replication group.<br/>                                                                                                                                                                |
| [**WvrRemoveReplicaSet**](msft-wvradmintasks-wvrremovereplicaset.md)                                   | TBD<br/>                                                                                                                                                                                                                    |
| [**WvrRemoveReplicationPartnership**](msft-wvradmintasks-wvrremovereplicationpartnership.md)           | Removes an existing replication partnership.<br/>                                                                                                                                                                           |
| [**WvrRemoveVolumePartnerStretch**](msft-wvradmintasks-wvrremovevolumepartnerstretch.md)               | TBD<br/>                                                                                                                                                                                                                    |
| [**WvrResumeReplicationGroup**](msft-wvradmintasks-wvrresumereplicationgroup.md)                       | Resumes all network and storage I/O for all replicas in a suspended replication group.<br/>                                                                                                                                 |
| [**WvrRevokeUserAccess**](msft-wvradmintasks-wvrrevokeuseraccess.md)                                   | Performs a CIM call to revoke the user permissions to manage StorageReplica.<br/>                                                                                                                                           |
| [**WvrSetNetworkConstraint**](msft-wvradmintasks-wvrsetnetworkconstraint.md)                           | Performs a CIM call to Set new Network Constraint for a partnership.<br/>                                                                                                                                                   |
| [**WvrSetPrimaryReplicationGroup**](msft-wvradmintasks-wvrsetprimaryreplicationgroup.md)               | TBD<br/>                                                                                                                                                                                                                    |
| [**WvrSuspendReplicationGroup**](msft-wvradmintasks-wvrsuspendreplicationgroup.md)                     | Suspends all network and storage I/O for all volumes in a replication group.<br/>                                                                                                                                           |



 

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>WVRCimProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WvrCimProv.dll</dt> </dl> |



 

 





