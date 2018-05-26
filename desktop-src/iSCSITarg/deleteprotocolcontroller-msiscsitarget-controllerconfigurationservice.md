---
title: DeleteProtocolController method of the MSISCSITARGET\_ControllerConfigurationService class
description: Deletes an instance of CIM\_ProtocolController and all associations in which this CIM\_ProtocolController is referenced.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 88efabb6-c93a-4ada-802c-49e5e5037d43
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DeleteProtocolController method iSCSI Software Target API
- DeleteProtocolController method iSCSI Software Target API , MSISCSITARGET_ControllerConfigurationService class
- MSISCSITARGET_ControllerConfigurationService class iSCSI Software Target API , DeleteProtocolController method
topic_type:
- apiref
api_name:
- MSISCSITARGET_ControllerConfigurationService.DeleteProtocolController
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DeleteProtocolController method of the MSISCSITARGET\_ControllerConfigurationService class

Deletes an instance of [**CIM\_ProtocolController**](https://msdn.microsoft.com/library/mt432251) and all associations in which this **CIM\_ProtocolController** is referenced.

This method overrides the method inherited from the **CIM\_ControllerConfigurationService** class.

## Syntax


```mof
uint32 DeleteProtocolController(
  [in] CIM_ProtocolController REF ProtocolController,
  [in] boolean                    DeleteChildrenProtocolControllers,
  [in] boolean                    DeleteUnits
);
```



## Parameters

<dl> <dt>

*ProtocolController* \[in\]
</dt> <dd>

Specifies the storage protocol controller to be deleted.

</dd> <dt>

*DeleteChildrenProtocolControllers* \[in\]
</dt> <dd>

If **True**, the Storage Management Initiative   Specification (SMI-S) provider will delete associated dependent protocol controllers.

</dd> <dt>

*DeleteUnits* \[in\]
</dt> <dd>

If **True**, the SMI-S provider will also delete the [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) instances associated with this [**CIM\_ProtocolController**](https://msdn.microsoft.com/library/mt432251) in a [**MSISCSITARGET\_ProtocolControllerForUnit**](msiscsitarget-protocolcontrollerforunit.md) instance.

If the *DeleteChildrenProtocolControllers* parameter is **True** the [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) objects associated with the deleted dependent protocol controllers will also be deleted.

> [!Note]  
> [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) instances will not be deleted as long as they are associated with any other protocol controllers.

 

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

**LogicalDevices Associated to Other ProtocolControllers Not Deleted** (4096)
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
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_ControllerConfigurationService**](msiscsitarget-controllerconfigurationservice.md)
</dt> <dt>

[**MSISCSITARGET\_ProtocolControllerForUnit**](msiscsitarget-protocolcontrollerforunit.md)
</dt> </dl>

 

 





