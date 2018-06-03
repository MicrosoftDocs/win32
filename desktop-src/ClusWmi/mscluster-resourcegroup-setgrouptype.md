---
title: SetGroupType method of the MSCluster\_ResourceGroup class
description: This method is not supported starting with Windows Server 2012.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5d418ef0-9bb7-4a3a-aebd-74f9503a2fe8
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetGroupType method
- SetGroupType method, MSCluster_ResourceGroup class
- MSCluster_ResourceGroup class, SetGroupType method
topic_type:
- apiref
api_name:
- MSCluster_ResourceGroup.SetGroupType
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetGroupType method of the MSCluster\_ResourceGroup class

This method is not supported starting with Windows Server 2012.

**Windows Server 2008 R2 and Windows Server 2008:  **

Sets the group type for this resource group.

## Syntax


```mof
void SetGroupType(
  [in] uint32 GroupType
);
```



## Parameters

<dl> <dt>

*GroupType* \[in\]
</dt> <dd>

The type of this resource group. This parameter can be one of the following values.

<dt>

<span id="FileServer"></span><span id="fileserver"></span><span id="FILESERVER"></span>

**FileServer** (100)


</dt> <dd></dd> <dt>

<span id="PrintServer"></span><span id="printserver"></span><span id="PRINTSERVER"></span>

**PrintServer** (101)


</dt> <dd></dd> <dt>

<span id="DhcpServer"></span><span id="dhcpserver"></span><span id="DHCPSERVER"></span>

**DhcpServer** (102)


</dt> <dd></dd> <dt>

<span id="Dtc"></span><span id="dtc"></span><span id="DTC"></span>

**Dtc** (103)


</dt> <dd></dd> <dt>

<span id="Msmq"></span><span id="msmq"></span><span id="MSMQ"></span>

**Msmq** (104)


</dt> <dd></dd> <dt>

<span id="Wins"></span><span id="wins"></span><span id="WINS"></span>

**Wins** (105)


</dt> <dd></dd> <dt>

<span id="StandAloneDfs"></span><span id="standalonedfs"></span><span id="STANDALONEDFS"></span>

**StandAloneDfs** (106)


</dt> <dd></dd> <dt>

<span id="GenericApplication"></span><span id="genericapplication"></span><span id="GENERICAPPLICATION"></span>

**GenericApplication** (107)


</dt> <dd></dd> <dt>

<span id="GenericService"></span><span id="genericservice"></span><span id="GENERICSERVICE"></span>

**GenericService** (108)


</dt> <dd></dd> <dt>

<span id="GenericScript"></span><span id="genericscript"></span><span id="GENERICSCRIPT"></span>

**GenericScript** (109)


</dt> <dd></dd> <dt>

<span id="IScsiNameService"></span><span id="iscsinameservice"></span><span id="ISCSINAMESERVICE"></span>

**IScsiNameService** (110)


</dt> <dd></dd> <dt>

<span id="VirtualMachine"></span><span id="virtualmachine"></span><span id="VIRTUALMACHINE"></span>

**VirtualMachine** (111)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (9999)


</dt> <dd></dd> </dl> </dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_ResourceGroup**](mscluster-resourcegroup.md)
</dt> </dl>

 

 





