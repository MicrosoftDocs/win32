---
title: MSFTSMNET\_DeviceSAPImplementation class
description: Associates a service access point (SAP) with the device that implements it.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 010243a8-6231-4c29-b307-92aae1728df3
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFTSMNET_DeviceSAPImplementation class iSCSI Software Target API
- MSFTSMNET_DeviceSAPImplementation class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- MSFTSMNET_DeviceSAPImplementation
- MSFTSMNET_DeviceSAPImplementation.Antecedent
- MSFTSMNET_DeviceSAPImplementation.Dependent
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFTSMNET\_DeviceSAPImplementation class

Associates a service access point (SAP) with the device that implements it. This association is a many-to-many association. An SAP can be provided by multiple logical devices that operate in conjunction. Any device can provide more than one SAP.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MSiSCSITargetProv"), Association, Version("1.0.0")]
class MSFTSMNET_DeviceSAPImplementation : CIM_DeviceSAPImplementation
{
  CIM_LogicalDevice      REF Antecedent;
  CIM_ServiceAccessPoint REF Dependent;
};
```

## Members

The **MSFTSMNET\_DeviceSAPImplementation** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFTSMNET\_DeviceSAPImplementation** class has these properties.

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

 

 





