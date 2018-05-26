---
title: Win32\_SoftwareFeatureAction class
description: This Win32\_SoftwareFeatureAction association WMI class relates an Installer feature with an action used to register and publish the feature.
ms.assetid: b8d394b0-6311-41f0-8556-f3aaa541b02b
keywords:
- Win32_SoftwareFeatureAction class
- Win32_SoftwareFeatureAction class, described
topic_type:
- apiref
api_name:
- Win32_SoftwareFeatureAction
- Win32_SoftwareFeatureAction.Action
- Win32_SoftwareFeatureAction.Element
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

# Win32\_SoftwareFeatureAction class

This **Win32\_SoftwareFeatureAction** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates an Installer feature with an action used to register and publish the feature.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_SoftwareFeatureAction
{
  CIM_Action            REF Action;
  Win32_SoftwareFeature REF Element;
};
```

## Members

The **Win32\_SoftwareFeatureAction** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SoftwareFeatureAction** class has these properties.

<dl> <dt>

**Action**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Action**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to a [**CIM\_Action**](https://msdn.microsoft.com/library/aa387206) instance.

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



 

 





