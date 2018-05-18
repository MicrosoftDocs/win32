---
title: CreateGatewayPathID method of the MSISCSITARGET\_StorageHardwareIDManagementService class
description: Creates a CIM\_GatewayPathID instance and the MSISCSITARGET\_ConcreteDependency association between the new instance and the MSISCSITARGET\_StorageHardwareIDManagementService service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '10862354-2fe9-4933-ad57-df9007131d63'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateGatewayPathID method iSCSI Software Target API", "CreateGatewayPathID method iSCSI Software Target API , MSISCSITARGET_StorageHardwareIDManagementService class", "MSISCSITARGET_StorageHardwareIDManagementService class iSCSI Software Target API , CreateGatewayPathID method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageHardwareIDManagementService.CreateGatewayPathID
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# CreateGatewayPathID method of the MSISCSITARGET\_StorageHardwareIDManagementService class

Creates a **CIM\_GatewayPathID** instance and the [**MSISCSITARGET\_ConcreteDependency**](msiscsitarget-concretedependency.md) association between the new instance and the [**MSISCSITARGET\_StorageHardwareIDManagementService**](msiscsitarget-storagehardwareidmanagementservice.md) service.

This method is inherited from the **CIM\_StorageHardwareIDManagementService** class.

## Syntax


```mof
uint32 CreateGatewayPathID(
  [in]  string                ElementName,
  [in]  string                StorageID,
  [in]  uint16                IDType,
  [in]  string                OtherIDType,
  [in]  string                GatewayID,
  [in]  uint16                GatewayIDType,
  [in]  string                OtherGatewayIDType,
  [out] CIM_GatewayPathID Ref NewGatewayPathID
);
```



## Parameters

<dl> <dt>

*ElementName* \[in\]
</dt> <dd>

Specifies the **ElementName** property of the new instance.

</dd> <dt>

*StorageID* \[in\]
</dt> <dd>

Specifies the unique hardware ID of the new instance.

</dd> <dt>

*IDType* \[in\]
</dt> <dd>

Specifies the type of the *StorageID* parameter.

> [!Note]  
> An **iSCSI Name** can be in any one of three iSCSI formats, IQN, EUI, or NAA.

 

Possible values are.

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


</dt> <dd></dd> <dt>

<span id="SwitchWWN"></span><span id="switchwwn"></span><span id="SWITCHWWN"></span>

**SwitchWWN** (6)


</dt> <dd></dd> </dl> </dd> <dt>

*OtherIDType* \[in\]
</dt> <dd>

Specifies the type of the *StorageID* parameter when the *IDType* parameter is **Other**.

</dd> <dt>

*GatewayID* \[in\]
</dt> <dd>

Specifies the unique gateway ID of the new instance.

</dd> <dt>

*GatewayIDType* \[in\]
</dt> <dd>

Specifies the type of the *GatewayID* parameter.

> [!Note]  
> An **iSCSI Name** can be in any one of three iSCSI formats, IQN, EUI, or NAA.

 

Possible values are.

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


</dt> <dd></dd> <dt>

<span id="SwitchWWN"></span><span id="switchwwn"></span><span id="SWITCHWWN"></span>

**SwitchWWN** (6)


</dt> <dd></dd> </dl> </dd> <dt>

*OtherGatewayIDType* \[in\]
</dt> <dd>

Specifies the type of the *GatewayID* parameter when the *GatewayIDType* parameter is **Other**.

</dd> <dt>

*NewGatewayPathID* \[out\]
</dt> <dd>

On return, contains a reference to the new **CIM\_GatewayPathID** instance.

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

**DMTF Reserved** (6–0x0FFF)
</dt> <dt>

**ID already created** (0x1000)
</dt> <dt>

**Hardware implementation does not support specified IDType** (0x1001)
</dt> <dt>

**GatewayPathID already created** (0x1003)
</dt> <dt>

**Hardware implementation does not support specified GatewayIDType** (0x1004)
</dt> <dt>

**Method Reserved** (0x1005–0x7FFF)
</dt> <dt>

**Vendor Specific** (0x8000–0xFFFF)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_StorageHardwareIDManagementService**](msiscsitarget-storagehardwareidmanagementservice.md)
</dt> </dl>

 

 





