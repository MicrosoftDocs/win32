---
title: CreateOrModifyReplicationPipe method of the MSISCSITARGET\_StorageConfigurationService class
description: Establishes a peer-to-peer connection that is represented by a CIM\_NetworkPipe element and two CIM\_ProtocolEndpoint elements.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9d849f98-0c9b-48eb-8439-3ebe3cba922b
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateOrModifyReplicationPipe method iSCSI Software Target API
- CreateOrModifyReplicationPipe method iSCSI Software Target API , MSISCSITARGET_StorageConfigurationService class
- MSISCSITARGET_StorageConfigurationService class iSCSI Software Target API , CreateOrModifyReplicationPipe method
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageConfigurationService.CreateOrModifyReplicationPipe
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateOrModifyReplicationPipe method of the MSISCSITARGET\_StorageConfigurationService class

Establishes a peer-to-peer connection that is represented by a **CIM\_NetworkPipe** element and two [**CIM\_ProtocolEndpoint**](https://msdn.microsoft.com/library/cc136899) elements. A return value of **Busy** (0x1000) indicates that the method is not supported.

This method is inherited from the **CIM\_StorageConfigurationService** class.

## Syntax


```mof
uint32 CreateOrModifyReplicationPipe(
  [in]      string                   PipeElementName,
  [in]      CIM_ComputerSystem Ref   SourceSystem,
  [in]      CIM_ComputerSystem Ref   TargetSystem,
  [in]      CIM_ProtocolEndpoint Ref SourceEndpoint[],
  [in]      CIM_ProtocolEndpoint Ref TargetEndpoint[],
  [in]      string                   Goal,
  [in, out] CIM_NetworkPipe Ref      ReplicationPipe
);
```



## Parameters

<dl> <dt>

*PipeElementName* \[in\]
</dt> <dd>

Specifies a user-friendly name for the element to be created.

</dd> <dt>

*SourceSystem* \[in\]
</dt> <dd>

Specifies one of the two peer systems that participate in the peer-to-peer connection. If the provider supports uni-directional connections, this property must identify the system that hosts the source elements.

</dd> <dt>

*TargetSystem* \[in\]
</dt> <dd>

Specifies one of the two peer systems that participate in the peer-to-peer connection. If the provider supports uni-directional connections, this property must identify the system that hosts the target elements.

</dd> <dt>

*SourceEndpoint* \[in\]
</dt> <dd>

Specifies the source system endpoints to be assigned to the pipe. Must be **NULL**, if a provider does not enable the client to manage port assignments. If an existing pipe is modified, this set of endpoints replaces the previous set. If this parameter is not **NULL**, it must contain the same number of endpoints as the *TargetEndpoint* parameter so that the two parameters specify a set of endpoint pairs.

</dd> <dt>

*TargetEndpoint* \[in\]
</dt> <dd>

Specifies the target system endpoints to be assigned to the pipe. Must be **NULL**, if a provider does not enable the client to manage port assignments. If an existing pipe is modified, this set of endpoints replaces the previous set. If this parameter is not **NULL**, it must contain the same number of endpoints as the *SourceEndpoint* parameter so that the two parameters specify a set of endpoint pairs.

</dd> <dt>

*Goal* \[in\]
</dt> <dd>

Specifies the characteristics, qualities of service, and goals for the peer-to-peer connection, in the form of a string representation of a [**CIM\_SettingData**](https://msdn.microsoft.com/library/cc136911) instance.

</dd> <dt>

*ReplicationPipe* \[in, out\]
</dt> <dd>

On input, optionally specifies an existing network pipe to modify. The specified protocol endpoints replaces any existing endpoints in the specified pipe. If **NULL**, a new network pipe is created with the specified protocol endpoints.

On return, contains a reference to the created or modified network pipe.

</dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

**Job Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unspecified Error** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**DMTF Reserved** (6 0x0FFF)
</dt> <dt>

**Busy** (0x1000)
</dt> <dt>

**Method Reserved** (0x1001 0x7FFF)
</dt> <dt>

**Vendor Specific** (0x8000 0xFFFF)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_StorageConfigurationService**](msiscsitarget-storageconfigurationservice.md)
</dt> <dt>

[**CIM\_ProtocolEndpoint**](https://msdn.microsoft.com/library/cc136899)
</dt> <dt>

[**CIM\_SettingData**](https://msdn.microsoft.com/library/cc136911)
</dt> </dl>

 

 





