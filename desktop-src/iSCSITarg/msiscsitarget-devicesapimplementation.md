---
title: MSISCSITARGET\_DeviceSAPImplementation class
description: Describes an association between one or more Service Access Points (SAP)s and the logical devices that implement them.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5202b818-72b4-414c-a4f4-862d862afdb3
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSISCSITARGET_DeviceSAPImplementation class iSCSI Software Target API
- MSISCSITARGET_DeviceSAPImplementation class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- MSISCSITARGET_DeviceSAPImplementation
- MSISCSITARGET_DeviceSAPImplementation.Antecedent
- MSISCSITARGET_DeviceSAPImplementation.Dependent
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSISCSITARGET\_DeviceSAPImplementation class

Describes an association between one or more Service Access Points (SAP)s and the logical devices that implement them.

This association can define many-to-many relationships between [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884) and [**CIM\_ServiceAccessPoint**](https://msdn.microsoft.com/library/aa388447) instances.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MSiSCSITargetProv"), Association, Version("1.0.0")]
class MSISCSITARGET_DeviceSAPImplementation : CIM_DeviceSAPImplementation
{
  CIM_LogicalDevice      REF Antecedent;
  CIM_ServiceAccessPoint REF Dependent;
};
```

## Members

The **MSISCSITARGET\_DeviceSAPImplementation** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSISCSITARGET\_DeviceSAPImplementation** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalDevice**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The LogicalDevice.

This property is inherited from [**CIM\_DeviceSAPImplementation**](cim-devicesapimplementation.md).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ServiceAccessPoint**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ServiceAccessPoint implemented using the LogicalDevice.

This property is inherited from [**CIM\_DeviceSAPImplementation**](cim-devicesapimplementation.md).

</dd> </dl>

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

[**CIM\_DeviceSAPImplementation**](cim-devicesapimplementation.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> </dl>

 

 





