---
title: Win32\_Property class
description: The Win32\_Property WMI class contains the property names and values for all defined properties in the installation. Properties with Null values are not present in the table.
ms.assetid: 'f5ca9981-a32e-4a9c-9175-dcab3c395e95'
keywords: ["Win32_Property class", "Win32_Property class, described"]
topic_type:
- apiref
api_name:
- Win32_Property
- Win32_Property.Caption
- Win32_Property.Description
- Win32_Property.ProductCode
- Win32_Property.Property
- Win32_Property.SettingID
- Win32_Property.Value
api_location:
- Msiprov.dll
api_type:
- DllExport
---

# Win32\_Property class

The **Win32\_Property** [WMI class](https://msdn.microsoft.com/library/aa393244) contains the property names and values for all defined properties in the installation. Properties with Null values are not present in the table.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_Property : Win32_MSIResource
{
  string Caption;
  string Description;
  string ProductCode;
  string Property;
  string SettingID;
  string Value;
};
```

## Members

The **Win32\_Property** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_Property** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Short textual description of the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Description of the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object.

</dd> <dt>

**ProductCode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Product code for the product of which this property is a part.

</dd> <dt>

**Property**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Name of the property.

</dd> <dt>

**SettingID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifier by which the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object is known.

</dd> <dt>

**Value**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Value of the property.

</dd> </dl>

## Remarks

The **Win32\_Property** class is derived from [**Win32\_MSIResource**](win32-msiresource.md).

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                         |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>Msi.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>Msiprov.dll</dt> </dl> |



## See also

<dl> <dt>

[Installed Applications Classes](https://msdn.microsoft.com/library/aa390887)
</dt> </dl>

 

 





