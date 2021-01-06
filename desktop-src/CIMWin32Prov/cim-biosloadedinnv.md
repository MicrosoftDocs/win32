---
description: The CIM\_BIOSLoadedInNV class associates a BIOS element and the non-volatile storage in which it is loaded.
ms.assetid: 11641616-e11d-49ff-bfe4-f95fe27f00b8
ms.tgt_platform: multiple
title: CIM_BIOSLoadedInNV class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_BIOSLoadedInNV
- CIM_BIOSLoadedInNV.Dependent
- CIM_BIOSLoadedInNV.Antecedent
- CIM_BIOSLoadedInNV.EndingAddress
- CIM_BIOSLoadedInNV.StartingAddress
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_BIOSLoadedInNV class

The **CIM\_BIOSLoadedInNV** class associates a BIOS element and the non-volatile storage in which it is loaded.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{524ED194-DB35-11d2-85FC-0000F8102E5F}"), AMENDMENT]
class CIM_BIOSLoadedInNV : CIM_Dependency
{
  CIM_BIOSElement        REF Dependent;
  CIM_NonVolatileStorage REF Antecedent;
  uint64                     EndingAddress;
  uint64                     StartingAddress;
};
```

## Members

The **CIM\_BIOSLoadedInNV** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_BIOSLoadedInNV** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_NonVolatileStorage**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

A [**CIM\_NonVolatileStorage**](cim-nonvolatilestorage.md) that describes the non-volatile storage.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_BIOSElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent")
</dt> </dl>

A [**CIM\_BIOSElement**](cim-bioselement.md) that describes the BIOS stored in the non-volatile extent.

</dd> <dt>

**EndingAddress**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Ending address where the BIOS is located in non-volatile storage.

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

</dd> <dt>

**StartingAddress**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Starting address where the BIOS is located in non-volatile storage.

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

</dd> </dl>

## Remarks

The **CIM\_BIOSLoadedInNV** class is derived from [**CIM\_Dependency**](cim-dependency.md).

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

 

