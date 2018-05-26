---
title: Win32\_ODBCAttribute class
description: Instances of the Win32\_ODBCAttribute WMI class represent attributes that are set for an ODBC driver.
ms.assetid: 26b49bbe-dba6-40d9-bb7b-fbeba185a9b1
keywords:
- Win32_ODBCAttribute class
- Win32_ODBCAttribute class, described
topic_type:
- apiref
api_name:
- Win32_ODBCAttribute
- Win32_ODBCAttribute.Attribute
- Win32_ODBCAttribute.Caption
- Win32_ODBCAttribute.Description
- Win32_ODBCAttribute.Driver
- Win32_ODBCAttribute.SettingID
- Win32_ODBCAttribute.Value
api_location:
- Msiprov.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Win32\_ODBCAttribute class

Instances of the **Win32\_ODBCAttribute** [WMI class](https://msdn.microsoft.com/library/aa393244) represent attributes that are set for an ODBC driver.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_ODBCAttribute : CIM_Setting
{
  string Attribute;
  string Caption;
  string Description;
  string Driver;
  string SettingID;
  string Value;
};
```

## Members

The **Win32\_ODBCAttribute** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ODBCAttribute** class has these properties.

<dl> <dt>

**Attribute**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Name of the ODBC attribute.

</dd> <dt>

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

**Driver**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

ODBC driver to which this attribute applies.

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

Value for this attribute.

</dd> </dl>

## Remarks

The **Win32\_ODBCAttribute** class is derived from [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461).

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                         |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>Msi.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>Msiprov.dll</dt> </dl> |



## See also

<dl> <dt>

[Installed Applications Classes](https://msdn.microsoft.com/library/aa390887)
</dt> </dl>

 

 





