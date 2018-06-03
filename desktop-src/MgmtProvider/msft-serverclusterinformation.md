---
title: MSFT\_ServerClusterInformation class
description: Represents the cluster attribute of the managed node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9578844b-5ba1-4735-9f2a-280b0726047b
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_ServerClusterInformation class
- MSFT_ServerClusterInformation class, described
topic_type:
- apiref
api_name:
- MSFT_ServerClusterInformation
- MSFT_ServerClusterInformation.Name
- MSFT_ServerClusterInformation.ObjectType
- MSFT_ServerClusterInformation.GroupType
api_location:
- MgmtProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_ServerClusterInformation class

Represents the cluster attribute of the managed node.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("mgmtprovider"), AMENDMENT]
class MSFT_ServerClusterInformation
{
  string Name;
  uint8  ObjectType;
  sint32 GroupType;
};
```

## Members

The **MSFT\_ServerClusterInformation** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_ServerClusterInformation** class has these properties.

<dl> <dt>

**GroupType**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The group type of the cluster object.

<dt>

<span id="Core_Cluster"></span><span id="core_cluster"></span><span id="CORE_CLUSTER"></span>

**Core Cluster** (1)


</dt> <dd></dd> <dt>

<span id="Available_Storage"></span><span id="available_storage"></span><span id="AVAILABLE_STORAGE"></span>

**Available Storage** (2)


</dt> <dd></dd> <dt>

<span id="Temporary"></span><span id="temporary"></span><span id="TEMPORARY"></span>

**Temporary** (3)


</dt> <dd></dd> <dt>

<span id="Shared_Volume"></span><span id="shared_volume"></span><span id="SHARED_VOLUME"></span>

**Shared Volume** (4)


</dt> <dd></dd> <dt>

<span id="Pool"></span><span id="pool"></span><span id="POOL"></span>

**Pool** (5)


</dt> <dd></dd> <dt>

<span id="File_Server"></span><span id="file_server"></span><span id="FILE_SERVER"></span>

**File Server** (100)


</dt> <dd></dd> <dt>

<span id="Print_Server"></span><span id="print_server"></span><span id="PRINT_SERVER"></span>

**Print Server** (101)


</dt> <dd></dd> <dt>

<span id="Dhcp_Server"></span><span id="dhcp_server"></span><span id="DHCP_SERVER"></span>

**Dhcp Server** (102)


</dt> <dd></dd> <dt>

<span id="Distributed_Transaction_Controller"></span><span id="distributed_transaction_controller"></span><span id="DISTRIBUTED_TRANSACTION_CONTROLLER"></span>

**Distributed Transaction Controller** (103)


</dt> <dd></dd> <dt>

<span id="Microsoft_Message_Queue"></span><span id="microsoft_message_queue"></span><span id="MICROSOFT_MESSAGE_QUEUE"></span>

**Microsoft Message Queue** (104)


</dt> <dd></dd> <dt>

<span id="Wins_Server"></span><span id="wins_server"></span><span id="WINS_SERVER"></span>

**Wins Server** (105)


</dt> <dd></dd> <dt>

<span id="Standalone_Dfs"></span><span id="standalone_dfs"></span><span id="STANDALONE_DFS"></span>

**Standalone Dfs** (106)


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

<span id="iSns_Server"></span><span id="isns_server"></span><span id="ISNS_SERVER"></span>

**iSns Server** (110)


</dt> <dd></dd> <dt>

<span id="Virtual_Machine"></span><span id="virtual_machine"></span><span id="VIRTUAL_MACHINE"></span>

**Virtual Machine** (111)


</dt> <dd></dd> <dt>

<span id="Ts_Session_Broker"></span><span id="ts_session_broker"></span><span id="TS_SESSION_BROKER"></span>

**Ts Session Broker** (112)


</dt> <dd></dd> <dt>

<span id="iScsi_Target_Server"></span><span id="iscsi_target_server"></span><span id="ISCSI_TARGET_SERVER"></span>

**iScsi Target Server** (113)


</dt> <dd></dd> <dt>

<span id="Scale-out_File_Server"></span><span id="scale-out_file_server"></span><span id="SCALE-OUT_FILE_SERVER"></span>

**Scale-out File Server** (114)


</dt> <dd></dd> <dt>

<span id="Hyper-V_Replica_Broker"></span><span id="hyper-v_replica_broker"></span><span id="HYPER-V_REPLICA_BROKER"></span>

**Hyper-V Replica Broker** (115)


</dt> <dd></dd> <dt>

<span id="Task_Scheduler"></span><span id="task_scheduler"></span><span id="TASK_SCHEDULER"></span>

**Task Scheduler** (116)


</dt> <dd></dd> <dt>

<span id="Update_Agent"></span><span id="update_agent"></span><span id="UPDATE_AGENT"></span>

**Update Agent** (117)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (9999)


</dt> <dd></dd> </dl>

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the cluster.

<dt>

0
</dt> <dd>

Standalone

</dd> <dt>

1
</dt> <dd>

Node

</dd> <dt>

2
</dt> <dd>

Cluster name object

</dd> <dt>

3
</dt> <dd>

Client access point

</dd> <dt>

4
</dt> <dd>

Distributed network name

</dd> </dl>

</dd> <dt>

**ObjectType**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of cluster object type.

<dt>

<span id="Standalone"></span><span id="standalone"></span><span id="STANDALONE"></span>

<span id="Standalone"></span><span id="standalone"></span><span id="STANDALONE"></span>**Standalone** (0)


</dt> <dd></dd> <dt>

<span id="Node"></span><span id="node"></span><span id="NODE"></span>

<span id="Node"></span><span id="node"></span><span id="NODE"></span>**Node** (1)


</dt> <dd>

Core Cluster

</dd> <dt>

<span id="Cluster_Name_Object"></span><span id="cluster_name_object"></span><span id="CLUSTER_NAME_OBJECT"></span>

<span id="Cluster_Name_Object"></span><span id="cluster_name_object"></span><span id="CLUSTER_NAME_OBJECT"></span>**Cluster Name Object** (2)


</dt> <dd>

Available Storage

</dd> <dt>

<span id="Client_Access_Point"></span><span id="client_access_point"></span><span id="CLIENT_ACCESS_POINT"></span>

<span id="Client_Access_Point"></span><span id="client_access_point"></span><span id="CLIENT_ACCESS_POINT"></span>**Client Access Point** (3)


</dt> <dd>

Temporary

</dd> <dt>

<span id="Distributed_Network_Name"></span><span id="distributed_network_name"></span><span id="DISTRIBUTED_NETWORK_NAME"></span>

<span id="Distributed_Network_Name"></span><span id="distributed_network_name"></span><span id="DISTRIBUTED_NETWORK_NAME"></span>**Distributed Network Name** (4)


</dt> <dd>

Shared Volume

</dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\Windows\\ServerManager<br/>                                                     |
| MOF<br/>                      | <dl> <dt>MgmtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MgmtProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**GetServerInventory method of MSFT\_ServerManagerTasks**](getserverinventory-msft-servermanagertasks.md)
</dt> </dl>

 

 





