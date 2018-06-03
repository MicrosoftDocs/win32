---
title: CreateOrModifyReplicationPipe method of the CIM\_StorageConfigurationService class
description: This method establishes a peer-to-peer connection identified by a NetworkPipe element and two ProtocolEndpoint elements created by the method provider.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 23e296c4-6a91-432c-aa30-d484ad3a42c0
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateOrModifyReplicationPipe method iSCSI Software Target API
- CreateOrModifyReplicationPipe method iSCSI Software Target API , CIM_StorageConfigurationService class
- CIM_StorageConfigurationService class iSCSI Software Target API , CreateOrModifyReplicationPipe method
topic_type:
- apiref
api_name:
- CIM_StorageConfigurationService.CreateOrModifyReplicationPipe
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateOrModifyReplicationPipe method of the CIM\_StorageConfigurationService class

This method establishes a peer-to-peer connection identified by a NetworkPipe element and two ProtocolEndpoint elements created by the method provider. The NetworkPipe is associated to a special peer-to-peer Network element. The provider will verify that two systems are capable of a peer relationship. If endpoints are assigned to the pipe, the same number of source and target endpoints must be supplied by the client to form a set of endpoint pairs. If ReplicationPipe is not supplied as an input parameter, a new pipe is created. If a pipe is supplied, a new set of endpoints is assigned to the existing pipe.

If Success (0) is returned, the function completed successfully.

A return value of Not Supported (1) indicates the method is not supported.

A return value of Busy (0x1000) indicates the method is not supported.

All other values indicate some type of error condition.

## Syntax


```mof
uint32 CreateOrModifyReplicationPipe(
  [in]      string                   PipeElementName,
  [in]      CIM_ComputerSystem   REF SourceSystem,
  [in]      CIM_ComputerSystem   REF TargetSystem,
  [in]      CIM_ProtocolEndpoint REF SourceEndpoint[],
  [in]      CIM_ProtocolEndpoint REF TargetEndpoint[],
  [in]      string                   Goal,
  [in, out] CIM_NetworkPipe      REF ReplicationPipe
);
```



## Parameters

<dl> <dt>

*PipeElementName* \[in\]
</dt> <dd>

A user-friendly name for the element created.

</dd> <dt>

*SourceSystem* \[in\]
</dt> <dd>

One of the two peer systems participating in the established peer-to-peer connection. If the provider supports uni-directional connections, this must identify the system hosting replica source elements.

</dd> <dt>

*TargetSystem* \[in\]
</dt> <dd>

One of the two peer systems participating in the established peer-to-peer connection. If the provider supports uni-directional connections, this must identify the system hosting replica target elements.

</dd> <dt>

*SourceEndpoint* \[in\]
</dt> <dd>

References to source system endpoints/ports assigned to the pipe. If a new pipe is created, this is the initial set of endpoints assigned. If an existing pipe is modified, this set replaces the previous set. The list must be null if a provider does not allow the client to manage port assignment.

</dd> <dt>

*TargetEndpoint* \[in\]
</dt> <dd>

References to target system endpoints/ports assigned to the pipe. If a new pipe is created, this is the initial set of endpoints assigned. If an existing pipe is modified, this set replaces the previous set. The list must be null if a provider does not allow the client to manage port assignment.

</dd> <dt>

*Goal* \[in\]
</dt> <dd>

The setting properties to be maintained for the peer-to-peer connection.

</dd> <dt>

*ReplicationPipe* \[in, out\]
</dt> <dd>

Reference to the created or modified NetworkPipe.

</dd> </dl>

## Return value

<dl> <dt>

**Success** (0)
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

**DMTF Reserved** (6 4095)
</dt> <dt>

**Busy** (4096)
</dt> <dt>

**Method Reserved** (4097 32767)
</dt> <dt>

**Vendor Specific** (32768 65535)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_StorageConfigurationService**](cim-storageconfigurationservice.md)
</dt> </dl>

 

 





