---
title: AttachDevice method of the MSISCSITARGET\_ControllerConfigurationService class
description: Associates a CIM\_LogicalDevice subclass, such as CIM\_StorageVolume to the referenced CIM\_ProtocolController. The association is persisted as an instance of the CIM\_ProtocolControllerForUnit class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 266efc79-acda-4785-a6e5-3d1eda74f99d
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AttachDevice method iSCSI Software Target API
- AttachDevice method iSCSI Software Target API , MSISCSITARGET_ControllerConfigurationService class
- MSISCSITARGET_ControllerConfigurationService class iSCSI Software Target API , AttachDevice method
topic_type:
- apiref
api_name:
- MSISCSITARGET_ControllerConfigurationService.AttachDevice
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AttachDevice method of the MSISCSITARGET\_ControllerConfigurationService class

Associates a [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) subclass, such as **CIM\_StorageVolume** to the referenced [**CIM\_ProtocolController**](https://msdn.microsoft.com/library/mt432251). The association is persisted as an instance of the [**CIM\_ProtocolControllerForUnit**](https://msdn.microsoft.com/library/mt432253) class.

This method is inherited from the **CIM\_ControllerConfigurationService** class.

## Syntax


```mof
uint32 AttachDevice(
  [in]      CIM_ProtocolController Ref ProtocolController,
  [in]      CIM_LogicalDevice Ref      Device,
  [in, out] string                     DeviceNumber
);
```



## Parameters

<dl> <dt>

*ProtocolController* \[in\]
</dt> <dd>

Specifies the antecedent protocol controller instance.

</dd> <dt>

*Device* \[in\]
</dt> <dd>

Specifies the logical device instance to attach.

</dd> <dt>

*DeviceNumber* \[in, out\]
</dt> <dd>

Specifies the number assigned to the **CIM\_ProtocolControllerForUnit.DeviceNumber** property if client assigned numbers are supported by the hardware. Hardware support is indicated by the **CIM\_ProtocolControllerMaskingCapabilities.ClientSelectableDeviceNumbers** property.

> \[!Important\]  
> The management instrumentation provider must verify that the logical unit numbers specified using the *DeviceNumber* parameter are unique for the protocol controller.

 

</dd> </dl>

## Return value

This method returns one of the following values.

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
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_ControllerConfigurationService**](msiscsitarget-controllerconfigurationservice.md)
</dt> <dt>

[**MSISCSITARGET\_ProtocolControllerForUnit**](msiscsitarget-protocolcontrollerforunit.md)
</dt> <dt>

[**MSISCSITARGET\_ProtocolControllerMaskingCapabilities**](msiscsitarget-protocolcontrollermaskingcapabilities.md)
</dt> <dt>

[**MSISCSITARGET\_AuthorizedTarget**](msiscsitarget-authorizedtarget.md)
</dt> </dl>

 

 





