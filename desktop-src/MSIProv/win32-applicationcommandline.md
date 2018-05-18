---
title: Win32\_ApplicationCommandLine class
description: The Win32\_ApplicationCommandLine association WMI class identifies a connection between an application and its command-line access point.
ms.assetid: 'f8e10112-d292-4d7b-ac44-e5c08cf2524a'
keywords: ["Win32_ApplicationCommandLine class", "Win32_ApplicationCommandLine class, described"]
topic_type:
- apiref
api_name:
- Win32_ApplicationCommandLine
- Win32_ApplicationCommandLine.Antecedent
- Win32_ApplicationCommandLine.Dependent
api_location:
- Msiprov.dll
api_type:
- DllExport
---

# Win32\_ApplicationCommandLine class

The **Win32\_ApplicationCommandLine** association [WMI class](https://msdn.microsoft.com/library/aa393244) identifies a connection between an application and its command-line access point.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider)

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_ApplicationCommandLine : CIM_ServiceAccessBySAP
{
  Win32_ApplicationService Antecedent;
  Win32_CommandLineAccess  Dependent;
};
```

## Members

The **Win32\_ApplicationCommandLine** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ApplicationCommandLine** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ApplicationService**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to the instance that represents the application.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_CommandLineAccess**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to the instance that represents the command used to access the antecedent.

</dd> </dl>

## Remarks

The **Win32\_ApplicationCommandLine** class is derived from [**CIM\_ServiceAccessBySAP**](https://msdn.microsoft.com/library/aa388445).

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

 

 





