---
description: The CIM\_HostedJobDestination class represents an association between a job destination and the system on which it resides. A system may host many job queues. Job destinations defer to the hosting system.
ms.assetid: 5d853826-1f27-417b-a053-5e0ee9816376
ms.tgt_platform: multiple
title: CIM_HostedJobDestination class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_HostedJobDestination
- CIM_HostedJobDestination.Dependent
- CIM_HostedJobDestination.Antecedent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_HostedJobDestination class

The **CIM\_HostedJobDestination** class represents an association between a job destination and the system on which it resides. A system may host many job queues. Job destinations defer to the hosting system.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{7880DD16-DB36-11d2-85FC-0000F8102E5F}"), AMENDMENT]
class CIM_HostedJobDestination : CIM_Dependency
{
  CIM_JobDestination REF Dependent;
  CIM_System         REF Antecedent;
};
```

## Members

The **CIM\_HostedJobDestination** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_HostedJobDestination** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_System**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Max**](/windows/desktop/WmiSdk/standard-qualifiers) (1), [**Min**](/windows/desktop/WmiSdk/standard-qualifiers) (1), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

A [**CIM\_System**](cim-system.md) that describes the hosting system.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_JobDestination**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent"), [**Weak**](/windows/desktop/WmiSdk/standard-qualifiers)
</dt> </dl>

A [**CIM\_JobDestination**](cim-jobdestination.md) describing the job destination hosted on the system.

</dd> </dl>

## Remarks

**CIM\_HostedJobDestination** is derived from [**CIM\_Dependency**](cim-dependency.md).

WMI does not implement this class.

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

