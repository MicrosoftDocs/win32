---
Description: 'The CIM\_HostedBootService class associates a hosting system and a boot service. Since this relationship is subclassed from CIM\_HostedService, it inherits the scoping/naming scheme defined for service, where a service defers to its hosting system.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '91621288-a231-4423-94df-7601bdf2ebe1'
ms.prod: 'windows-server-dev'
ms.technology:
- cimwin32
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'CIM\_HostedBootService class'
---

# CIM\_HostedBootService class

The **CIM\_HostedBootService** class associates a hosting system and a boot service. Since this relationship is subclassed from [**CIM\_HostedService**](cim-hostedservice.md), it inherits the scoping/naming scheme defined for service, where a service defers to its hosting system.

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{6DAE7092-DB36-11d2-85FC-0000F8102E5F}"), AMENDMENT]
class CIM_HostedBootService : CIM_HostedService
{
  CIM_System      REF Antecedent;
  CIM_BootService REF Dependent;
};
```

## Members

The **CIM\_HostedBootService** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_HostedBootService** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_System**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Antecedent)
</dt> </dl>

A [**CIM\_System**](cim-system.md) that describes the hosting system.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_BootService**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

A [**CIM\_BootService**](cim-bootservice.md) that describes the boot service hosted on the system.

</dd> </dl>

## Remarks

The **CIM\_HostedBootService** class is derived from [**CIM\_HostedService**](cim-hostedservice.md).

WMI does not implement this class.

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_HostedService**](cim-hostedservice.md)
</dt> </dl>

 

 




