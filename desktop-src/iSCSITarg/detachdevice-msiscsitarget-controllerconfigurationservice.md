---
title: DetachDevice method of the MSISCSITARGET\_ControllerConfigurationService class
description: Removes the CIM\_ProtocolControllerForDevice instance association between the specified CIM\_ProtocolController and CIM\_LogicalDevice instances.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '902f9fc5-c8a8-4f1d-992d-eb4aa3b695fb'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DetachDevice method iSCSI Software Target API", "DetachDevice method iSCSI Software Target API , MSISCSITARGET_ControllerConfigurationService class", "MSISCSITARGET_ControllerConfigurationService class iSCSI Software Target API , DetachDevice method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_ControllerConfigurationService.DetachDevice
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# DetachDevice method of the MSISCSITARGET\_ControllerConfigurationService class

Removes the **CIM\_ProtocolControllerForDevice** instance association between the specified [**CIM\_ProtocolController**](https://msdn.microsoft.com/library/mt432251) and [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) instances.

This method is inherited from the **CIM\_ControllerConfigurationService** class.

## Syntax


```mof
uint32 DetachDevice(
  [in] CIM_ProtocolController Ref ProtocolController,
  [in] CIM_LogicalDevice Ref      Device
);
```



## Parameters

<dl> <dt>

*ProtocolController* \[in\]
</dt> <dd>

Specifies the antecedent protocol controller instance.

> [!Note]  
> When the [**CIM\_ProtocolController**](https://msdn.microsoft.com/library/mt432251) instance is actively masking a device, that is, it is part of a **CIM\_AuthorizedTarget** association, the management instrumentation provider should update the hardware access configuration when this method is called.

 

</dd> <dt>

*Device* \[in\]
</dt> <dd>

Specifies the logical device instance to detach.

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

**DMTF Reserved** (6–4095)
</dt> <dt>

**LogicalDevice Instance not Associated with Controller** (4096)
</dt> <dt>

**Busy** (4097)
</dt> <dt>

**Method Reserved** (4098–32767)
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
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_ControllerConfigurationService**](msiscsitarget-controllerconfigurationservice.md)
</dt> <dt>

[**CIM\_ProtocolController**](https://msdn.microsoft.com/library/mt432251)
</dt> <dt>

[**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884)
</dt> </dl>

 

 





