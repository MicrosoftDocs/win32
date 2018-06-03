---
title: Win32\_SoftwareFeatureSoftwareElements class
description: The Win32\_SoftwareFeatureSoftwareElements association WMI class identifies the software elements that make up a particular software feature.
ms.assetid: 9a6067f4-8a83-4888-8dca-53e9466eaf5d
keywords:
- Win32_SoftwareFeatureSoftwareElements class
- Win32_SoftwareFeatureSoftwareElements class, described
topic_type:
- apiref
api_name:
- Win32_SoftwareFeatureSoftwareElements
- Win32_SoftwareFeatureSoftwareElements.GroupComponent
- Win32_SoftwareFeatureSoftwareElements.PartComponent
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

# Win32\_SoftwareFeatureSoftwareElements class

The **Win32\_SoftwareFeatureSoftwareElements** association [WMI class](https://msdn.microsoft.com/library/aa393244) identifies the software elements that make up a particular software feature.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_SoftwareFeatureSoftwareElements : CIM_SoftwareFeatureSoftwareElements
{
  Win32_SoftwareFeature REF GroupComponent;
  Win32_SoftwareElement REF PartComponent;
};
```

## Members

The **Win32\_SoftwareFeatureSoftwareElements** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SoftwareFeatureSoftwareElements** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_SoftwareFeature**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to a [**Win32\_SoftwareFeature**](win32-softwarefeature.md) instance.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_SoftwareElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to a [**Win32\_SoftwareElement**](win32-softwareelement.md) instance.

</dd> </dl>

## Remarks

The **Win32\_SoftwareFeatureSoftwareElements** class is derived from [**CIM\_SoftwareFeatureSoftwareElements**](https://msdn.microsoft.com/library/aa388478).

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

 

 





