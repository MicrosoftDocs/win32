---
title: Msvm\_DeviceSAPImplementation class
description: An association between a service access point (SAP) and how it is implemented.
ms.assetid: 6944ecd4-6618-4ef7-9f4a-b6d6bff7aab9
keywords:
- Msvm_DeviceSAPImplementation class Hyper-V
- Msvm_DeviceSAPImplementation class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_DeviceSAPImplementation
- Msvm_DeviceSAPImplementation.Antecedent
- Msvm_DeviceSAPImplementation.Dependent
api_location:
- Root\Virtualization
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Msvm\_DeviceSAPImplementation class

An association between a service access point (SAP) and how it is implemented. The cardinality of this association is many-to-many. A SAP can be provided by more than one logical device, operating in conjunction. Any device can provide more than one SAP. When many logical devices are associated with a single SAP, it is assumed that these elements operate in conjunction to provide the access point. If different implementations of a SAP exist, each of these implementations would result in individual instantiations of the SAP object. These individual instantiations would then have associations to the unique implementations.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_DeviceSAPImplementation : CIM_DeviceSAPImplementation
{
  CIM_LogicalDevice      REF Antecedent;
  CIM_ServiceAccessPoint REF Dependent;
};
```

## Members

The **Msvm\_DeviceSAPImplementation** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_DeviceSAPImplementation** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_LogicalDevice**](cim-logicaldevice.md)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The logical device.

This property is inherited from [**CIM\_DeviceSAPImplementation**](cim-devicesapimplementation.md).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The service access point implemented using the logical device.

This property is inherited from [**CIM\_DeviceSAPImplementation**](cim-devicesapimplementation.md).

</dd> </dl>

## Remarks

Access to the **Msvm\_DeviceSAPImplementation** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Examples

See [Querying Networking Objects](querying-networking-objects.md).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_DeviceSAPImplementation**](cim-devicesapimplementation.md)
</dt> <dt>

[**CIM\_DeviceSAPImplementation**](https://msdn.microsoft.com/library/aa387245)
</dt> <dt>

[Networking Classes](networking-classes.md)
</dt> </dl>

 

 





