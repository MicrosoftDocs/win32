---
title: Win32\_SoftwareFeatureParent class
description: The Win32\_SoftwareFeatureParent generic association WMI class establishes dependency relationships between objects.
ms.assetid: 2411380d-98b3-43b8-bb0f-e060494de2a0
keywords:
- Win32_SoftwareFeatureParent class
- Win32_SoftwareFeatureParent class, described
topic_type:
- apiref
api_name:
- Win32_SoftwareFeatureParent
- Win32_SoftwareFeatureParent.Antecedent
- Win32_SoftwareFeatureParent.Dependent
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

# Win32\_SoftwareFeatureParent class

The **Win32\_SoftwareFeatureParent** generic association [WMI class](https://msdn.microsoft.com/library/aa393244) establishes dependency relationships between objects.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_SoftwareFeatureParent
{
  Win32_SoftwareFeature REF Antecedent;
  Win32_SoftwareFeature REF Dependent;
};
```

## Members

The **Win32\_SoftwareFeatureParent** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SoftwareFeatureParent** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_SoftwareFeature**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to the instance representing an independent object in the association.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_SoftwareFeature**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to the instance representing an object dependent on **Antecedent**.

</dd> </dl>

## Remarks

The **Win32\_SoftwareFeatureParent** class is derived from [**CIM\_Dependency**](https://msdn.microsoft.com/library/aa387238).

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

 

 





