---
title: DeleteProtocolController method of the MSISCSITARGET\_ControllerConfigurationService class
description: The method deletes an instance of ProtocolController and all associations in which this ProtocolController is referenced.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9822ef89-d8bf-4a74-b316-8544a581c155
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
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DeleteProtocolController method of the MSISCSITARGET\_ControllerConfigurationService class

The method deletes an instance of ProtocolController and all associations in which this ProtocolController is referenced.

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

The ProtocolController to be deleted.

</dd> <dt>

*DeleteChildrenProtocolControllers* \[in\]
</dt> <dd>

If true, the management instrumentation provider will also delete 'child' ProtocolControllers (i.e., those defined as Dependent references in instances of AssociatedProtocolController where this ProtocolController is the Antecedent reference). Also, all direct associations involving the 'child' ProtocolControllers will be removed.

</dd> <dt>

*DeleteUnits* \[in\]
</dt> <dd>

If true, the management instrumentation provider will also delete LogicalDevice instances associated via ProtocolControllerForUnit, to this ProtocolController and its children. (Note that 'child' controllers will only be affected if the DeleteChildrenProtocolControllers input parameter is TRUE). LogicalDevice instances are only deleted if there are NO remaining ProtocolControllerForUnit associations, to other ProtocolControllers.

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
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_ControllerConfigurationService**](msiscsitarget-controllerconfigurationservice.md)
</dt> </dl>

 

 





