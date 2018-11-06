---
Description: Represents an association between a service access point (SAP) and a logical device that implements it.
ms.assetid: 40c8111a-d439-4c0f-805e-9c10d7182eb4
title: CIM_DeviceSAPImplementation class
ms.topic: article
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
- vmms.exe
---

# CIM\_DeviceSAPImplementation class

Represents an association between a service access point (SAP) and a logical device that implements it.

## Syntax

``` syntax
[Association, Abstract, Version("2.10.0"), UMLPackagePath("CIM::Core::Device"), AMENDMENT]
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

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

The logical device.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ServiceAccessPoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The SAP implemented by the logical device.

</dd> </dl>

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

 




