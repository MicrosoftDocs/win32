---
title: Win32\_PatchPackage class
description: The Win32\_PatchPackage WMI class describes all patch packages that have been applied to the product. For each patch package, the unique identifier for the update is provided along with information about the media image on which the update is located.
ms.assetid: 'e78fa3e4-ab90-4b2d-a733-481057eba6f5'
keywords: ["Win32_PatchPackage class", "Win32_PatchPackage class, described"]
topic_type:
- apiref
api_name:
- Win32_PatchPackage
- Win32_PatchPackage.Caption
- Win32_PatchPackage.Description
- Win32_PatchPackage.PatchID
- Win32_PatchPackage.ProductCode
- Win32_PatchPackage.SettingID
api_location:
- Msiprov.dll
api_type:
- DllExport
---

# Win32\_PatchPackage class

The **Win32\_PatchPackage** [WMI class](https://msdn.microsoft.com/library/aa393244) describes all patch packages that have been applied to the product. For each patch package, the unique identifier for the update is provided along with information about the media image on which the update is located.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_PatchPackage : Win32_MSIResource
{
  string Caption;
  string Description;
  string PatchID;
  string ProductCode;
  string SettingID;
};
```

## Members

The **Win32\_PatchPackage** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PatchPackage** class has these properties.

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

**PatchID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Unique identifier for an update package.

</dd> <dt>

**ProductCode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Product code for the product to which this update package is applied.

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

The **Win32\_PatchPackage** class is derived from [**Win32\_MSIResource**](win32-msiresource.md).

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

 

 





