---
title: GetGroupType method of the MSCluster\_ResourceGroup class
description: Gets the group type for this resource group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd444f3a3-f64b-4ab5-a397-3003df21f020'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetGroupType method", "GetGroupType method, MSCluster_ResourceGroup class", "MSCluster_ResourceGroup class, GetGroupType method"]
topic_type:
- apiref
api_name:
- MSCluster_ResourceGroup.GetGroupType
api_location:
- ClusWMI.dll
api_type:
- COM
---

# GetGroupType method of the MSCluster\_ResourceGroup class

Gets the group type for this resource group.

## Syntax


```mof
uint32 GetGroupType();
```



## Parameters

This method has no parameters.

## Return value

This method returns one of the following values:

<dl> <dt>

**File Server**
</dt> <dd>

100

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **FileServer** before Windows Server 2012 R2 .

</dd> <dt>

**Print Server**
</dt> <dd>

101

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **PrintServer** before Windows Server 2012 R2 .

</dd> <dt>

**DHCP Server**
</dt> <dd>

102

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **DhcpServer** before Windows Server 2012 R2 .

</dd> <dt>

**DTC**
</dt> <dd>

103

</dd> <dt>

**Message Queuing**
</dt> <dd>

104

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **Msmq** before Windows Server 2012 R2 .

</dd> <dt>

**WINS Server**
</dt> <dd>

105

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **Wins** before Windows Server 2012 R2 .

</dd> <dt>

**DFS Namespace Server**
</dt> <dd>

106

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **StandAloneDfs** before Windows Server 2012 R2 .

</dd> <dt>

**Generic Application**
</dt> <dd>

107

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **GenericApplication** before Windows Server 2012 R2 .

</dd> <dt>

**Generic Service**
</dt> <dd>

108

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **GenericService** before Windows Server 2012 R2 .

</dd> <dt>

**Generic Script**
</dt> <dd>

109

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **GenericScript** before Windows Server 2012 R2 .

</dd> <dt>

**iSNS Cluster Resource**
</dt> <dd>

110

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **IScsiNameService** before Windows Server 2012 R2 .

</dd> <dt>

**Virtual Machine**
</dt> <dd>

111

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **Virtual Machine** before Windows Server 2012 R2 .

</dd> <dt>

**TS Session Broker**
</dt> <dd>

112

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This value is **TsSessionBroker** before Windows Server 2012 R2 .

</dd> <dt>

**iSCSI Target Server**
</dt> <dd>

113

</dd> <dt>

**Scale-Out File Server**
</dt> <dd>

114

</dd> <dt>

**Hyper-V Replica Broker**
</dt> <dd>

115

</dd> <dt>

**Unknown**
</dt> <dd>

9999

</dd> </dl>

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Namespace<br/>                | Root\\MSCluster<br/>                                                               |
| Header<br/>                   | <dl> <dt>Dvbsiparser.h</dt> </dl> |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl>   |



## See also

<dl> <dt>

[**MSCluster\_ResourceGroup**](mscluster-resourcegroup.md)
</dt> </dl>

 

 





