---
description: The CIM\_SoftwareFeatureServiceImplementation class represents an association between a service and how it is implemented in software.
ms.assetid: fa80cc91-8dd7-4726-a24a-5c4dfa3e786b
ms.tgt_platform: multiple
title: CIM_SoftwareFeatureServiceImplementation class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_SoftwareFeatureServiceImplementation
- CIM_SoftwareFeatureServiceImplementation.Dependent
- CIM_SoftwareFeatureServiceImplementation.Antecedent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_SoftwareFeatureServiceImplementation class

The **CIM\_SoftwareFeatureServiceImplementation** class represents an association between a service and how it is implemented in software. A service can be provided by more than one software feature, operating in conjunction with one another. Additionally, a software feature can provide more than one service. When multiple software features are associated with a single service, it is assumed that the elements operate in conjunction to provide the service. If different implementations of a service exist, each implementation would result in individual instantiations of the service object. Individual instantiations would then have associations to the unique implementations.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[UUID("{8AC984F4-DB37-11d2-85FC-0000F8102E5F}"), Abstract, AMENDMENT]
class CIM_SoftwareFeatureServiceImplementation : CIM_Dependency
{
  CIM_Service         REF Dependent;
  CIM_SoftwareFeature REF Antecedent;
};
```

## Members

The **CIM\_SoftwareFeatureServiceImplementation** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SoftwareFeatureServiceImplementation** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_SoftwareFeature**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Min**](/windows/desktop/WmiSdk/standard-qualifiers) (0), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

A [**CIM\_SoftwareFeature**](cim-softwarefeature.md) that describes the antecedent software feature.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Service**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Min**](/windows/desktop/WmiSdk/standard-qualifiers) (0), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent")
</dt> </dl>

A [**CIM\_Service**](cim-service.md) that describes the dependent service.

</dd> </dl>

## Remarks

The **CIM\_SoftwareFeatureServiceImplementation** class is derived from [**CIM\_Dependency**](cim-dependency.md).

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

 

