---
description: An association between a service access point (SAP) and how it is implemented.
ms.assetid: 7fd1bafd-2890-4972-812e-23f50e62afe7
title: CIM\_DeviceSAPImplementation class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_DeviceSAPImplementation
- CIM_DeviceSAPImplementation.Antecedent
- CIM_DeviceSAPImplementation.Dependent
api_type: 
- DllExport
api_location: 
- netTCPIP.dll
ROBOTS: INDEX,FOLLOW
---

# CIM\_DeviceSAPImplementation class

An association between a service access point (SAP) and how it is implemented.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, UMLPackagePath("CIM::Core::Device"), Version("2.10.0"), AMENDMENT]
class CIM_DeviceSAPImplementation : CIM_Dependency
{
  CIM_LogicalDevice      REF Antecedent;
  CIM_ServiceAccessPoint REF Dependent;
};
```

## Members

The **CIM\_DeviceSAPImplementation** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_DeviceSAPImplementation** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalDevice**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**Override**](/windows/win32/wmisdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

A [**CIM\_LogicalDevice**](cim-logicaldevice.md) describing the logical device.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ServiceAccessPoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**Override**](/windows/win32/wmisdk/standard-qualifiers) ("Dependent")
</dt> </dl>

A [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md) describing the service access point implemented using the logical device.

</dd> </dl>

## Remarks

The cardinality of this association is many-to-many. A SAP can be provided by more than one logical device, operating in conjunction. And, any Device can provide more than one SAP. When many logical devices are associated with a single SAP, it is assumed that these elements operate in conjunction to provide the access point. If different implementations of a SAP exist, each of these implementations would result in individual instantiations of the service access point object. These individual instantiations would then have associations to the unique implementations.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\standardcimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTCPIP.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTCPIP.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

