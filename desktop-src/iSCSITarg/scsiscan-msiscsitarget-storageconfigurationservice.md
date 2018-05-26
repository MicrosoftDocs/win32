---
title: ScsiScan method of the MSISCSITARGET\_StorageConfigurationService class
description: Requests the system to re-scan SCSI devices for changes in their configuration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 64a18224-81e4-4621-af21-781fae613413
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ScsiScan method iSCSI Software Target API
- ScsiScan method iSCSI Software Target API , MSISCSITARGET_StorageConfigurationService class
- MSISCSITARGET_StorageConfigurationService class iSCSI Software Target API , ScsiScan method
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageConfigurationService.ScsiScan
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ScsiScan method of the MSISCSITARGET\_StorageConfigurationService class

Requests the system to re-scan SCSI devices for changes in their configuration. This operation can be disruptive; optional parameters enable the caller to limit the scan to a subset of the available SCSI device elements.

This method is inherited from the **CIM\_StorageConfigurationService** class.

## Syntax


```mof
uint32 ScsiScan(
  [in, out] CIM_ConcreteJob Ref          Job,
  [in]      uint16                       ConnectionType,
  [in]      string                       OtherConnectionType,
  [in]      CIM_SCSIProtocolEndpoint Ref Initiators[],
  [in]      string                       Targets[],
  [in, out] string                       LogicalUnits[]
);
```



## Parameters

<dl> <dt>

*Job* \[in, out\]
</dt> <dd>

Contains a reference to the job, if a job is created and not completed.

</dd> <dt>

*ConnectionType* \[in\]
</dt> <dd>

Specifies the type of connection. If specified, the scan is constrained to initiator ports of this type. This parameter is only used if the *Initiators* parameter is **NULL**.

The values for this parameter correspond to the [**MSISCSITARGET\_iSCSIProtocolEndpoint**](msiscsitarget-iscsiprotocolendpoint.md).**ConnectionType** property.

The possible values are.

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

Describes the connection type, if the *ConnectionType* parameter is set to **Other**.

</dd> <dt>

*Initiators* \[in\]
</dt> <dd>

Specifies a list of initiator endpoints to scan. If specified, the scan is limited to SCSI targets that are attached to the specified endpoints. If **NULL** and the *ConnectionType* parameter is specified, all initiators of that connection type are scanned. If the *Initiators* and *ConnectionType* parameters are **NULL**, all targets on all system initiators are scanned.

</dd> <dt>

*Targets* \[in\]
</dt> <dd>

Specifies a list of names or numbers for targets. Entries must be formatted appropriately for the connection type.

</dd> <dt>

*LogicalUnits* \[in, out\]
</dt> <dd>

Specifies a list of SCSI logical unit numbers. Each logical unit is hosted on the targets that are specified in the *Targets* parameter.

</dd> </dl>

## Return value

This method returns one of the following values.

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

**DMTF Reserved** (6 4095)
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

**Method Reserved** (4101 32767)
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
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_StorageConfigurationService**](msiscsitarget-storageconfigurationservice.md)
</dt> <dt>

[**MSISCSITARGET\_iSCSIProtocolEndpoint**](msiscsitarget-iscsiprotocolendpoint.md)
</dt> </dl>

 

 





