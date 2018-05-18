---
title: Win32\_Binary class
description: The Win32\_Binary WMI class represents binary information (such as bitmaps, icons, executable files, and so on) that are used by an installation.
ms.assetid: '04294329-07f8-495a-8132-a1b0a324e28a'
keywords: ["Win32_Binary class", "Win32_Binary class, described"]
topic_type:
- apiref
api_name:
- Win32_Binary
- Win32_Binary.Caption
- Win32_Binary.Data
- Win32_Binary.Description
- Win32_Binary.Name
- Win32_Binary.ProductCode
- Win32_Binary.SettingID
api_location:
- Msiprov.dll
api_type:
- DllExport
---

# Win32\_Binary class

The **Win32\_Binary** [WMI class](https://msdn.microsoft.com/library/aa393244) represents binary information (such as bitmaps, icons, executable files, and so on) that are used by an installation.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_Binary : Win32_MSIResource
{
  string Caption;
  string Data;
  string Description;
  string Name;
  string ProductCode;
  string SettingID;
};
```

## Members

The **Win32\_Binary** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_Binary** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Short textual description (one line) of the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object.

</dd> <dt>

**Data**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Binary data associated with the object.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Textual description of the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Name used to identify the object.

</dd> <dt>

**ProductCode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Product code for the product of which this binary is a part.

</dd> <dt>

**SettingID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifier by which the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object is known.

</dd> </dl>

## Remarks

The **Win32\_Binary** class is derived from [**Win32\_MSIResource**](win32-msiresource.md).

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

 

 





