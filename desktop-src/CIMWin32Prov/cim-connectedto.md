---
description: The CIM\_ConnectedTo class represents an association that indicates that two or more physical connectors are connected.
ms.assetid: fedd9227-8a3b-461a-995b-08cbceb81181
ms.tgt_platform: multiple
title: CIM_ConnectedTo class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ConnectedTo
- CIM_ConnectedTo.Dependent
- CIM_ConnectedTo.Antecedent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_ConnectedTo class

The **CIM\_ConnectedTo** class represents an association that indicates that two or more physical connectors are connected.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Abstract, UUID("{FAF76B85-798C-11D2-AAD1-006008C78BC7}"), AMENDMENT]
class CIM_ConnectedTo : CIM_Dependency
{
  CIM_PhysicalConnector REF Dependent;
  CIM_PhysicalConnector REF Antecedent;
};
```

## Members

The **CIM\_ConnectedTo** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ConnectedTo** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_PhysicalConnector**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

A [**CIM\_PhysicalConnector**](cim-physicalconnector.md) that represents a physical connector that serves as one end of the connection.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_PhysicalConnector**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent")
</dt> </dl>

A [**CIM\_PhysicalConnector**](cim-physicalconnector.md) that represents another physical connector that serves as the other end of the connection.

</dd> </dl>

## Remarks

The **CIM\_ConnectedTo** class is inherited from [**CIM\_Dependency**](cim-dependency.md).

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

 

