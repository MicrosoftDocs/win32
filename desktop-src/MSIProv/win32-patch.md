---
title: Win32\_Patch class
description: The Win32\_Patch WMI class represents an individual update to be applied to a particular file and whose source resides at a specified location.
ms.assetid: 36aaf936-f1d3-4dbc-85e9-4738941c18e7
keywords:
- Win32_Patch class
- Win32_Patch class, described
topic_type:
- apiref
api_name:
- Win32_Patch
- Win32_Patch.Attributes
- Win32_Patch.Caption
- Win32_Patch.Description
- Win32_Patch.File
- Win32_Patch.PatchSize
- Win32_Patch.ProductCode
- Win32_Patch.Sequence
- Win32_Patch.SettingID
api_location:
- Msiprov.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_Patch class

The **Win32\_Patch** [WMI class](https://msdn.microsoft.com/library/aa393244) represents an individual update to be applied to a particular file and whose source resides at a specified location.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_Patch : Win32_MSIResource
{
  uint16 Attributes;
  string Caption;
  string Description;
  string File;
  uint32 PatchSize;
  string ProductCode;
  sint16 Sequence;
  string SettingID;
};
```

## Members

The **Win32\_Patch** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_Patch** class has these properties.

<dl> <dt>

**Attributes**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Bit flag that represents update attributes. A value of 1 (one) indicates that the failure to apply this update is not a fatal error.

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

**File**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

File identifier of the [**Win32\_FileSpecification**](win32-filespecification.md) instance to which this update applies.

</dd> <dt>

**PatchSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Size, in bytes, of the update.

</dd> <dt>

**ProductCode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Product code for the product to which this update is applied.

</dd> <dt>

**Sequence**
</dt> <dd> <dl> <dt>

Data type: **sint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Position of this update in the sequence of patches on the source media.

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

The **Win32\_Patch** class is derived from [**Win32\_MSIResource**](win32-msiresource.md).

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

 

 





