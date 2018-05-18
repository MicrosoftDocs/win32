---
title: Win32\_ODBCSourceAttribute class
description: The Win32\_ODBCSourceAttribute class represents the information regarding an ODBC source and the attributes that must be set for installation.
ms.assetid: 'f6d5a4f5-7e3c-4f13-8688-125412c42af2'
keywords: ["Win32_ODBCSourceAttribute class", "Win32_ODBCSourceAttribute class, described"]
topic_type:
- apiref
api_name:
- Win32_ODBCSourceAttribute
- Win32_ODBCSourceAttribute.Attribute
- Win32_ODBCSourceAttribute.Caption
- Win32_ODBCSourceAttribute.DataSource
- Win32_ODBCSourceAttribute.Description
- Win32_ODBCSourceAttribute.SettingID
- Win32_ODBCSourceAttribute.Value
api_location:
- Msiprov.dll
api_type:
- DllExport
---

# Win32\_ODBCSourceAttribute class

The **Win32\_ODBCSourceAttribute** class represents the information regarding an ODBC source and the attributes that must be set for installation.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_ODBCSourceAttribute : CIM_Setting
{
  string Attribute;
  string Caption;
  string DataSource;
  string Description;
  string SettingID;
  string Value;
};
```

## Members

The **Win32\_ODBCSourceAttribute** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ODBCSourceAttribute** class has these properties.

<dl> <dt>

**Attribute**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Name of the data source attribute.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Short textual description of the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object.

</dd> <dt>

**DataSource**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Token name for the data source within its package to which this attribute applies.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Description of the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object.

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

Value for this data source attribute.

</dd> </dl>

## Remarks

The **Win32\_ODBCSourceAttribute** class is derived from [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461).

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

 

 





