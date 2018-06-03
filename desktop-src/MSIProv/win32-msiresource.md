---
title: Win32\_MSIResource class
description: The Win32\_MSIResource abstract WMI class represents any resources that are used by the Installer during the course of an installation, an update, or an upgrade.
ms.assetid: df938beb-f629-4c97-83a9-48603cb36bb0
keywords:
- Win32_MSIResource class
- Win32_MSIResource class, described
topic_type:
- apiref
api_name:
- Win32_MSIResource
- Win32_MSIResource.Caption
- Win32_MSIResource.Description
- Win32_MSIResource.SettingID
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

# Win32\_MSIResource class

The **Win32\_MSIResource** abstract [WMI class](https://msdn.microsoft.com/library/aa393244) represents any resources that are used by the Installer during the course of an installation, an update, or an upgrade.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class Win32_MSIResource : CIM_Setting
{
  string Caption;
  string Description;
  string SettingID;
};
```

## Members

The **Win32\_MSIResource** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_MSIResource** class has these properties.

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

**SettingID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifier by which the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object is known.

</dd> </dl>

## Remarks

The **Win32\_MSIResource** class is derived from [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461).

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

 

 





