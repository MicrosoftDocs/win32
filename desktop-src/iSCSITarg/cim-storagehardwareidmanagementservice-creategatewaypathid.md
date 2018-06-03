---
title: CreateGatewayPathID method of the CIM\_StorageHardwareIDManagementService class
description: This method creates a CIM\_GatewayPathID and the association CIM\_ConcreteDependency between this service and the new GatewayPathID.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d968616a-0ffa-43c2-b533-2da18fbb1340
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateGatewayPathID method iSCSI Software Target API
- CreateGatewayPathID method iSCSI Software Target API , CIM_StorageHardwareIDManagementService class
- CIM_StorageHardwareIDManagementService class iSCSI Software Target API , CreateGatewayPathID method
topic_type:
- apiref
api_name:
- CIM_StorageHardwareIDManagementService.CreateGatewayPathID
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateGatewayPathID method of the CIM\_StorageHardwareIDManagementService class

This method creates a CIM\_GatewayPathID and the association CIM\_ConcreteDependency between this service and the new GatewayPathID.

## Syntax


```mof
uint32 CreateGatewayPathID(
  [in]  string                ElementName,
  [in]  string                StorageID,
  [in]  uint16                IDType,
  [in]  string                OtherIDType,
  [in]  string                GatewayID,
  [in]  uint16                GatewayIDType,
  [in]  string                OtherGatewayIDType,
  [out] CIM_GatewayPathID REF NewGatewayPathID
);
```



## Parameters

<dl> <dt>

*ElementName* \[in\]
</dt> <dd>

The ElementName of the new StorageHardwareID instance.

</dd> <dt>

*StorageID* \[in\]
</dt> <dd>

StorageID is the value used by the SecurityService to represent Identity - in this case, a hardware worldwide unique name.

</dd> <dt>

*IDType* \[in\]
</dt> <dd>

The type of the StorageID property. iSCSI IDs may use one of three iSCSI formats - iqn, eui, or naa. This three letter format is the name prefix; so a single iSCSI type is provided here, the prefix can be used to further refine the format.

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="PortWWN"></span><span id="portwwn"></span><span id="PORTWWN"></span>

**PortWWN** (2)


</dt> <dd></dd> <dt>

<span id="NodeWWN"></span><span id="nodewwn"></span><span id="NODEWWN"></span>

**NodeWWN** (3)


</dt> <dd></dd> <dt>

<span id="Hostname"></span><span id="hostname"></span><span id="HOSTNAME"></span>

**Hostname** (4)


</dt> <dd></dd> <dt>

<span id="iSCSI_Name"></span><span id="iscsi_name"></span><span id="ISCSI_NAME"></span>

**iSCSI Name** (5)


</dt> <dd></dd> </dl> </dd> <dt>

*OtherIDType* \[in\]
</dt> <dd>

The type of the storage ID, when IDType is "Other".

</dd> <dt>

*GatewayID* \[in\]
</dt> <dd>

GatewayID is the value used by the SecurityService to represent identity of a Gateway element.

</dd> <dt>

*GatewayIDType* \[in\]
</dt> <dd>

The type of the GatewayID property. iSCSI IDs may use one of three iSCSI formats - iqn, eui, or naa. This three letter format is the name prefix; so a single iSCSI type is provided here, the prefix can be used to further refine the format.

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="PortWWN"></span><span id="portwwn"></span><span id="PORTWWN"></span>

**PortWWN** (2)


</dt> <dd></dd> <dt>

<span id="NodeWWN"></span><span id="nodewwn"></span><span id="NODEWWN"></span>

**NodeWWN** (3)


</dt> <dd></dd> <dt>

<span id="Hostname"></span><span id="hostname"></span><span id="HOSTNAME"></span>

**Hostname** (4)


</dt> <dd></dd> <dt>

<span id="iSCSI_Name"></span><span id="iscsi_name"></span><span id="ISCSI_NAME"></span>

**iSCSI Name** (5)


</dt> <dd></dd> </dl> </dd> <dt>

*OtherGatewayIDType* \[in\]
</dt> <dd>

The type of the storage ID, when GatewayIDType is "Other".

</dd> <dt>

*NewGatewayPathID* \[out\]
</dt> <dd>

REF to the new GatewayPathID instance.

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

**ID already created** (4096)
</dt> <dt>

**Hardware implementation does not support specified IDType** (4097)
</dt> <dt>

**GatewayPathID already created** (4099)
</dt> <dt>

**Hardware implementation does not support specified GatewayIDType** (4100)
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
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_StorageHardwareIDManagementService**](cim-storagehardwareidmanagementservice.md)
</dt> </dl>

 

 





