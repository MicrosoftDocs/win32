---
title: ScsiScan method of the CIM\_StorageConfigurationService class
description: This method requests that the system rescan SCSI devices for changes in their configuration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b55c9563-9368-48f7-8ed9-3716a7d4c085'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ScsiScan method iSCSI Software Target API", "ScsiScan method iSCSI Software Target API , CIM_StorageConfigurationService class", "CIM_StorageConfigurationService class iSCSI Software Target API , ScsiScan method"]
topic_type:
- apiref
api_name:
- CIM_StorageConfigurationService.ScsiScan
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# ScsiScan method of the CIM\_StorageConfigurationService class

This method requests that the system rescan SCSI devices for changes in their configuration. If called on a general-purpose host, the changes are reflected in the list of devices available to applications (for example, the UNIX 'device tree'. This method may also be used on a storage appliance to force rescanning of attached SCSI devices.

This operation can be disruptive; optional parameters allow the caller to limit the scan to a single or set of SCSI device elements. All parameters are optional; if parameters other Job are passed in as null, a full scan is invoked.

## Syntax


```mof
uint32 ScsiScan(
  [in, out] CIM_ConcreteJob          REF Job,
  [in]      uint16                       ConnectionType,
  [in]      string                       OtherConnectionType,
  [in]      CIM_SCSIProtocolEndpoint REF Initiators[],
  [in]      string                       Targets[],
  [in, out] string                       LogicalUnits[]
);
```



## Parameters

<dl> <dt>

*Job* \[in, out\]
</dt> <dd>

Reference to the job (may be null if job completed).

</dd> <dt>

*ConnectionType* \[in\]
</dt> <dd>

The type of connection, constrains the scan to initiator ports of this type. Only used if the Initiators parameter is null.

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Fibre_Channel"></span><span id="fibre_channel"></span><span id="FIBRE_CHANNEL"></span>

**Fibre Channel** (2)


</dt> <dd></dd> <dt>

<span id="Parallel_SCSI"></span><span id="parallel_scsi"></span><span id="PARALLEL_SCSI"></span>

**Parallel SCSI** (3)


</dt> <dd></dd> <dt>

<span id="SSA"></span><span id="ssa"></span>

**SSA** (4)


</dt> <dd></dd> <dt>

<span id="IEEE_1394"></span><span id="ieee_1394"></span>

**IEEE 1394** (5)


</dt> <dd></dd> <dt>

<span id="RDMA"></span><span id="rdma"></span>

**RDMA** (6)


</dt> <dd></dd> <dt>

<span id="iSCSI"></span><span id="iscsi"></span><span id="ISCSI"></span>

**iSCSI** (7)


</dt> <dd></dd> <dt>

<span id="SAS"></span><span id="sas"></span>

**SAS** (8)


</dt> <dd></dd> <dt>

<span id="ADT"></span><span id="adt"></span>

**ADT** (9)


</dt> <dd></dd> </dl> </dd> <dt>

*OtherConnectionType* \[in\]
</dt> <dd>

The connection type, if the ConnectionType parameter is "Other".

</dd> <dt>

*Initiators* \[in\]
</dt> <dd>

A list of references to initiators. Scanning will be limited to SCSI targets attached to these initiators. If this parameter is null and connection is specified, all initiators of that connection type are scanned. If this parameter and ConnectionType are null, all targets on all system initiators are probed.

</dd> <dt>

*Targets* \[in\]
</dt> <dd>

A list of names or numbers for targets. These should be formatted to match the appropriate connection type, For example, PortWWNs would be specified for Fibre Channel targets.

</dd> <dt>

*LogicalUnits* \[in, out\]
</dt> <dd>

A list of SCSI logical unit numbers representing logical units hosted on the targets specified in the Targets argument.

</dd> </dl>

## Return value

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unknown** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**DMTF Reserved** (6–4095)
</dt> <dt>

**Invalid connection type** (4096)
</dt> <dt>

**Invalid Initiator** (4097)
</dt> <dt>

**No matching target found** (4098)
</dt> <dt>

**No matching LUs found** (4099)
</dt> <dt>

**Prohibited by name binding configuration** (4100)
</dt> <dt>

**DMTF Reserved** (4101–32767)
</dt> <dt>

**Vendor Specific** (32768–65535)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_StorageConfigurationService**](cim-storageconfigurationservice.md)
</dt> </dl>

 

 





