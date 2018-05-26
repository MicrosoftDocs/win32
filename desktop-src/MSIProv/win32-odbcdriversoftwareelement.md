---
title: Win32\_ODBCDriverSoftwareElement class
description: The Win32\_ODBCDriverSoftwareElement association WMI class relates a Win32\_ODBCDriverSpecification instance and a Win32\_SoftwareElement instance.
ms.assetid: c45f7278-bebe-406c-a8a5-74b70e19b5e2
keywords:
- Win32_ODBCDriverSoftwareElement class
- Win32_ODBCDriverSoftwareElement class, described
topic_type:
- apiref
api_name:
- Win32_ODBCDriverSoftwareElement
- Win32_ODBCDriverSoftwareElement.Check
- Win32_ODBCDriverSoftwareElement.Element
- Win32_ODBCDriverSoftwareElement.Phase
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

# Win32\_ODBCDriverSoftwareElement class

The **Win32\_ODBCDriverSoftwareElement** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates a [**Win32\_ODBCDriverSpecification**](win32-odbcdriverspecification.md) instance and a [**Win32\_SoftwareElement**](win32-softwareelement.md) instance. Because software elements in a ready-to-run state cannot transition into another state, the value of the **Phase** property is restricted to in-state for [**CIM\_SoftwareElement**](https://msdn.microsoft.com/library/aa388467) objects in a ready-to-run state.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_ODBCDriverSoftwareElement : CIM_SoftwareElementChecks
{
  Win32_ODBCDriverSpecification REF Check;
  Win32_SoftwareElement         REF Element;
  uint16                            Phase;
};
```

## Members

The **Win32\_ODBCDriverSoftwareElement** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ODBCDriverSoftwareElement** class has these properties.

<dl> <dt>

**Check**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ODBCDriverSpecification**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to the instance representing a check.

</dd> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **Win32\_SoftwareElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to the instance representing an element.

</dd> <dt>

**Phase**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the referenced check is an in-state check or a next-state check.



| Value                                                                                                | Meaning               |
|------------------------------------------------------------------------------------------------------|-----------------------|
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | In-State<br/>   |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | Next-State<br/> |



 

</dd> </dl>

## Remarks

The **Win32\_ODBCDriverSoftwareElement** class is derived from [**CIM\_SoftwareElementChecks**](https://msdn.microsoft.com/library/aa388470).

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

 

 





