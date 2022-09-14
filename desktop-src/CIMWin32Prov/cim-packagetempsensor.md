---
description: The CIM\_PackageTempSensor association represents the relationship in which a temperature sensor is often installed in a package, such as a chassis or a rack, to monitor the package's environment.
ms.assetid: 79f2c4d1-5e1a-4c5f-9ef4-0c8bc3926a13
ms.tgt_platform: multiple
title: CIM_PackageTempSensor class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_PackageTempSensor
- CIM_PackageTempSensor.Dependent
- CIM_PackageTempSensor.Antecedent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_PackageTempSensor class

The **CIM\_PackageTempSensor** association represents the relationship in which a temperature sensor is often installed in a package, such as a chassis or a rack, to monitor the package's environment.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, Aggregation, UUID("{FAF76B8F-798C-11D2-AAD1-006008C78BC7}"), AMENDMENT]
class CIM_PackageTempSensor : CIM_Dependency
{
  CIM_PhysicalPackage   REF Dependent;
  CIM_TemperatureSensor REF Antecedent;
};
```

## Members

The **CIM\_PackageTempSensor** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_PackageTempSensor** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_TemperatureSensor**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

A [**CIM\_TemperatureSensor**](cim-temperaturesensor.md) describing the temperature sensor for the package.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_PhysicalPackage**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent")
</dt> </dl>

A [**CIM\_PhysicalPackage**](cim-physicalpackage.md) describing the physical package whose environment is monitored.

</dd> </dl>

## Remarks

**CIM\_PackageTempSensor** is derived from [**CIM\_Dependency**](cim-dependency.md).

WMI does not implement this class.

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

