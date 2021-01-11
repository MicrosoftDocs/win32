---
description: Represents an association in which protocol endpoints depend on a forwarding service to forward data.
ms.assetid: b63dbd2c-2842-498a-a352-b7ab7f7c841a
title: CIM_ForwardsAmong class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_ForwardsAmong
- CIM_ForwardsAmong.Antecedent
- CIM_ForwardsAmong.Dependent
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_ForwardsAmong class

Represents an association in which protocol endpoints depend on a forwarding service to forward data.

## Syntax

``` syntax
[Association, Abstract, Version("2.6.0"), UMLPackagePath("CIM::Network::RoutingForwarding")]
class CIM_ForwardsAmong : CIM_ServiceSAPDependency
{
  CIM_ProtocolEndpoint  REF Antecedent;
  CIM_ForwardingService REF Dependent;
};
```

## Members

The **CIM\_ForwardsAmong** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ForwardsAmong** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ProtocolEndpoint**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

The protocol endpoints send and receive the forwarded data.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ForwardingService**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent")
</dt> </dl>

The forwarding service that forwards the data.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                       |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_ServiceSAPDependency**](cim-servicesapdependency.md)
</dt> </dl>

 

