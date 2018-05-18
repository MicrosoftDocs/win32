---
title: Win32\_ServiceSpecificationService class
description: The Win32\_ServiceSpecificationService association WMI class represents instances of Win32\_ServiceSpecification and Win32\_Service.
ms.assetid: '95f19ddd-de3c-4933-809b-ea1900c61539'
keywords: ["Win32_ServiceSpecificationService class", "Win32_ServiceSpecificationService class, described"]
topic_type:
- apiref
api_name:
- Win32_ServiceSpecificationService
- Win32_ServiceSpecificationService.Check
- Win32_ServiceSpecificationService.Element
api_location:
- Msiprov.dll
api_type:
- DllExport
---

# Win32\_ServiceSpecificationService class

The **Win32\_ServiceSpecificationService** association [WMI class](https://msdn.microsoft.com/library/aa393244) represents instances of [**Win32\_ServiceSpecification**](win32-servicespecification.md) and [**Win32\_Service**](https://msdn.microsoft.com/library/aa394418).

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_ServiceSpecificationService
{
  Win32_ServiceSpecification REF Check;
  Win32_Service              REF Element;
};
```

## Members

The **Win32\_ServiceSpecificationService** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ServiceSpecificationService** class has these properties.

<dl> <dt>

**Check**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ServiceSpecification**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to a [**Win32\_ServiceSpecification**](win32-servicespecification.md) instance.

</dd> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Service**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to a [**Win32\_Service**](https://msdn.microsoft.com/library/aa394418) instance.

</dd> </dl>

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

 

 





