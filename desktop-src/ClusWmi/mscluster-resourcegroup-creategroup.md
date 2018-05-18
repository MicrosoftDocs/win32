---
title: CreateGroup method of the MSCluster\_ResourceGroup class
description: Creates a group and brings it online.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '02910650-1e1a-4046-8e31-ee639132bb28'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateGroup method", "CreateGroup method, MSCluster_ResourceGroup class", "MSCluster_ResourceGroup class, CreateGroup method"]
topic_type:
- apiref
api_name:
- MSCluster_ResourceGroup.CreateGroup
api_location:
- ClusWMI.dll
api_type:
- COM
---

# CreateGroup method of the MSCluster\_ResourceGroup class

Creates a [group](https://msdn.microsoft.com/library/aa369645) and brings it [*online*](https://msdn.microsoft.com/library/aa371781#-wolf-online-gly).

## Syntax


```mof
void CreateGroup(
  [in]      string GroupName,
  [in]      uint32 GroupType,
  [in, out] string Id
);
```



## Parameters

<dl> <dt>

*GroupName* \[in\]
</dt> <dd>

The new group name.

</dd> <dt>

*GroupType* \[in\]
</dt> <dd>

The resource group type.

<dt>

<span id="File_Server"></span><span id="file_server"></span><span id="FILE_SERVER"></span>

**File Server** (100)


</dt> <dd></dd> <dt>

<span id="Print_Server"></span><span id="print_server"></span><span id="PRINT_SERVER"></span>

**Print Server** (101)


</dt> <dd></dd> <dt>

<span id="DHCP_Server"></span><span id="dhcp_server"></span><span id="DHCP_SERVER"></span>

**DHCP Server** (102)


</dt> <dd></dd> <dt>

<span id="DTC"></span><span id="dtc"></span>

**DTC** (103)


</dt> <dd></dd> <dt>

<span id="Message_Queuing"></span><span id="message_queuing"></span><span id="MESSAGE_QUEUING"></span>

**Message Queuing** (104)


</dt> <dd></dd> <dt>

<span id="WINS_Server"></span><span id="wins_server"></span><span id="WINS_SERVER"></span>

**WINS Server** (105)


</dt> <dd></dd> <dt>

<span id="DFS_Namespace_Server"></span><span id="dfs_namespace_server"></span><span id="DFS_NAMESPACE_SERVER"></span>

**DFS Namespace Server** (106)


</dt> <dd></dd> <dt>

<span id="Generic_Application"></span><span id="generic_application"></span><span id="GENERIC_APPLICATION"></span>

**Generic Application** (107)


</dt> <dd></dd> <dt>

<span id="Generic_Service"></span><span id="generic_service"></span><span id="GENERIC_SERVICE"></span>

**Generic Service** (108)


</dt> <dd></dd> <dt>

<span id="Generic_Script"></span><span id="generic_script"></span><span id="GENERIC_SCRIPT"></span>

**Generic Script** (109)


</dt> <dd></dd> <dt>

<span id="iSNS_Cluster_Resource"></span><span id="isns_cluster_resource"></span><span id="ISNS_CLUSTER_RESOURCE"></span>

**iSNS Cluster Resource** (110)


</dt> <dd></dd> <dt>

<span id="Virtual_Machine"></span><span id="virtual_machine"></span><span id="VIRTUAL_MACHINE"></span>

**Virtual Machine** (111)


</dt> <dd></dd> <dt>

<span id="TS_Session_Broker"></span><span id="ts_session_broker"></span><span id="TS_SESSION_BROKER"></span>

**TS Session Broker** (112)


</dt> <dd></dd> <dt>

<span id="iSCSI_Target_Server"></span><span id="iscsi_target_server"></span><span id="ISCSI_TARGET_SERVER"></span>

**iSCSI Target Server** (113)


</dt> <dd></dd> <dt>

<span id="Scale-Out_File_Server"></span><span id="scale-out_file_server"></span><span id="SCALE-OUT_FILE_SERVER"></span>

**Scale-Out File Server** (114)


</dt> <dd></dd> <dt>

<span id="Hyper-V_Replica_Broker"></span><span id="hyper-v_replica_broker"></span><span id="HYPER-V_REPLICA_BROKER"></span>

**Hyper-V Replica Broker** (115)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (9999)


</dt> <dd></dd> </dl>

**Windows Server 2008 R2 and Windows Server 2008:  **

This parameter is not supported before Windows Server 2012.

</dd> <dt>

*Id* \[in, out\]
</dt> <dd>

Id of the resource group.

**Windows Server 2008 R2 and Windows Server 2008:  **

This parameter is not supported before Windows Server 2012.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_ResourceGroup**](mscluster-resourcegroup.md)
</dt> <dt>

[**DeleteGroup Method of the MSCluster\_ResourceGroup Class**](mscluster-resourcegroup-deletegroup.md)
</dt> </dl>

 

 





