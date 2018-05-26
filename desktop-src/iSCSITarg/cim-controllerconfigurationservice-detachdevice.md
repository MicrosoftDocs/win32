---
title: DetachDevice method of the CIM\_ControllerConfigurationService class
description: This method removes the ProtocolControllerForDevice association subclass between the ProtocolController and a LogicalDevice, such as a StorageVolume or a MediaAccessDevice.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d6b1e3b3-3173-4f84-b0e4-511055dcdcc1
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DetachDevice method iSCSI Software Target API
- DetachDevice method iSCSI Software Target API , CIM_ControllerConfigurationService class
- CIM_ControllerConfigurationService class iSCSI Software Target API , DetachDevice method
topic_type:
- apiref
api_name:
- CIM_ControllerConfigurationService.DetachDevice
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DetachDevice method of the CIM\_ControllerConfigurationService class

This method removes the ProtocolControllerForDevice association subclass between the ProtocolController and a LogicalDevice, such as a StorageVolume or a MediaAccessDevice. When the ProtocolController is actively masking a device (i.e. is part of an AuthorizedTarget association, the management instrumentation provider should update the hardware access configuration when DetachDevice is called.

## Syntax


```mof
uint32 DetachDevice(
  [in] CIM_ProtocolController REF ProtocolController,
  [in] CIM_LogicalDevice      REF Device
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

The LogicalDevice instance to detach.

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

**LogicalDevice Instance not Associated with Controller** (4096)
</dt> <dt>

**Busy** (4097)
</dt> <dt>

**Method Reserved** (4098 32767)
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

 

 





