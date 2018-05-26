---
title: AttachDevice method of the CIM\_ControllerConfigurationService class
description: This method associates a LogicalDevice subclass (specifically a StorageVolume or MediaAccessDevice subclass) to the referenced ProtocolController.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9e37af6f-6781-48db-9754-4c34ef6e46a5
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AttachDevice method iSCSI Software Target API
- AttachDevice method iSCSI Software Target API , CIM_ControllerConfigurationService class
- CIM_ControllerConfigurationService class iSCSI Software Target API , AttachDevice method
topic_type:
- apiref
api_name:
- CIM_ControllerConfigurationService.AttachDevice
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AttachDevice method of the CIM\_ControllerConfigurationService class

This method associates a LogicalDevice subclass (specifically a StorageVolume or MediaAccessDevice subclass) to the referenced ProtocolController. The association is persisted as an instance of ProtocolControllerForUnit. The management instrumentation provider must verify that the logical unit numbers (defined using the DeviceNumber input parameter) are unique for the ProtocolController. When the Protocol Controller is actively masking a device (i.e. is part of an AuthorizedTarget association), the provider should update the access configuration in the underlying hardware as appropriate.

## Syntax


```mof
uint32 AttachDevice(
  [in]      CIM_ProtocolController REF ProtocolController,
  [in]      CIM_LogicalDevice      REF Device,
  [in, out] string                     DeviceNumber
);
```



## Parameters

<dl> <dt>

*ProtocolController* \[in\]
</dt> <dd>

The ProtocolController instance.

</dd> <dt>

*Device* \[in\]
</dt> <dd>

The LogicalDevice instance to attach.

</dd> <dt>

*DeviceNumber* \[in, out\]
</dt> <dd>

The number assigned to ProtocolControllerForUnit.DeviceNumber (if supported by the hardware). Hardware support is indicated by ProtocolControllerMaskingCapabilities.ClientSelectableDeviceNumbers). If the hardware does not support setting the number, but the DeviceNumber has not been established in an existing ProtocolControllerForDevice subclass, then this parameter's value will be used. If the DeviceNumber has been established, then the current number will be reused.

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

**Invalid LogicalDevice Instance** (4096)
</dt> <dt>

**Device Number Conflict** (4097)
</dt> <dt>

**DeviceNumber Parameter Must Be Provided** (4098)
</dt> <dt>

**Hardware Implementation Requires Null DeviceNumber** (4099)
</dt> <dt>

**Busy** (4100)
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

[**CIM\_ControllerConfigurationService**](cim-controllerconfigurationservice.md)
</dt> </dl>

 

 





