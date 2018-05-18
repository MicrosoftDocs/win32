---
title: Win32\_SoftwareElementResource class
description: The Win32\_SoftwareElementResource association WMI class relates an Installer feature with an action used to register and publish the feature.
ms.assetid: 'f101475f-f815-467d-bbdf-cbb6ab48bece'
keywords: ["Win32_SoftwareElementResource class", "Win32_SoftwareElementResource class, described"]
topic_type:
- apiref
api_name:
- Win32_SoftwareElementResource
- Win32_SoftwareElementResource.Element
- Win32_SoftwareElementResource.Setting
api_location:
- Msiprov.dll
api_type:
- DllExport
---

# Win32\_SoftwareElementResource class

The **Win32\_SoftwareElementResource** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates an Installer feature with an action used to register and publish the feature.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_SoftwareElementResource : Win32_ManagedSystemElementResource
{
  Win32_SoftwareElement REF Element;
  Win32_MSIResource     REF Setting;
};
```

## Members

The **Win32\_SoftwareElementResource** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SoftwareElementResource** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **Win32\_SoftwareElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to a [**Win32\_SoftwareElement**](win32-softwareelement.md) instance.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_MSIResource**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to a [**Win32\_MSIResource**](win32-msiresource.md) instance.

</dd> </dl>

## Remarks

The **Win32\_SoftwareElementResource** class is derived from [**Win32\_ManagedSystemElementResource**](win32-managedsystemelementresource.md).

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

 

 





