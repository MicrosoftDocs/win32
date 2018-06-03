---
title: Win32\_SoftwareFeatureCheck class
description: The Win32\_SoftwareFeatureCheck association WMI class relates an Installer feature, with any condition or locational information that a feature may require.
ms.assetid: d96e6fa8-9d08-4155-b993-cc7ae69a15bc
keywords:
- Win32_SoftwareFeatureCheck class
- Win32_SoftwareFeatureCheck class, described
topic_type:
- apiref
api_name:
- Win32_SoftwareFeatureCheck
- Win32_SoftwareFeatureCheck.Check
- Win32_SoftwareFeatureCheck.Element
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

# Win32\_SoftwareFeatureCheck class

The **Win32\_SoftwareFeatureCheck** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates an Installer feature, with any condition or locational information that a feature may require.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_SoftwareFeatureCheck
{
  CIM_Check             REF Check;
  Win32_SoftwareFeature REF Element;
};
```

## Members

The **Win32\_SoftwareFeatureCheck** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SoftwareFeatureCheck** class has these properties.

<dl> <dt>

**Check**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Check**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to a [**CIM\_Check**](https://msdn.microsoft.com/library/aa387206) instance.

</dd> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **Win32\_SoftwareFeature**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to a [**Win32\_SoftwareFeature**](win32-softwarefeature.md) instance.

</dd> </dl>

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

 

 





