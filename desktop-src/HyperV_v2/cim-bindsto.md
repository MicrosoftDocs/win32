---
description: Represents an association where a CIM\_ServiceAccessPoint object requests protocol services from a CIM\_ProtocolEndpoint object.
ms.assetid: d1ef774d-f0e0-43e7-8a9d-63c2fad5ca4a
title: CIM_BindsTo class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_BindsTo
- CIM_BindsTo.Antecedent
- CIM_BindsTo.Dependent
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_BindsTo class

Represents an association where a [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md) object requests protocol services from a [**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md) object.

## Syntax

``` syntax
[Association, Abstract, Version("2.10.0"), UMLPackagePath("CIM::Core::Service"), AMENDMENT]
class CIM_BindsTo : CIM_SAPSAPDependency
{
  CIM_ProtocolEndpoint   REF Antecedent;
  CIM_ServiceAccessPoint REF Dependent;
};
```

## Members

The **CIM\_BindsTo** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_BindsTo** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ProtocolEndpoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

The lower level endpoint that is accessed by the service access point.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ServiceAccessPoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent")
</dt> </dl>

The access point or protocol endpoint that is dependent on the lower level endpoint.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_SAPSAPDependency**](cim-sapsapdependency.md)
</dt> </dl>

 

