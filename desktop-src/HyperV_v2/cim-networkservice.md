---
description: This class is deprecated. Instead, we recommend deriving from the CIM\_Service class.
ms.assetid: 67b3a96e-4549-41e0-8097-f8d145df0c49
title: CIM_NetworkService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_NetworkService
- CIM_NetworkService.Keywords
- CIM_NetworkService.ServiceURL
- CIM_NetworkService.StartupConditions
- CIM_NetworkService.StartupParameters
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_NetworkService class

This class is deprecated. Instead, we recommend deriving from the [**CIM\_Service**](cim-service.md) class.

## Syntax

``` syntax
[Deprecated("CIM_Service"), Abstract, Version("2.7.0"), UMLPackagePath("CIM::Network::RoutingForwarding"), AMENDMENT]
class CIM_NetworkService : CIM_Service
{
  string Keywords[];
  string ServiceURL;
  string StartupConditions[];
  string StartupParameters[];
};
```

## Members

The **CIM\_NetworkService** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_NetworkService** class has these properties.

<dl> <dt>

**Keywords**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](/windows/desktop/WmiSdk/standard-wmi-qualifiers) ("No value")
</dt> </dl>

This property is deprecated and should not be used.

> [!Note]  
> Deprecated description: An array of keywords that can be used in queries.

 

</dd> <dt>

**ServiceURL**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](/windows/desktop/WmiSdk/standard-wmi-qualifiers) ("CIM\_ServiceAccessURI")
</dt> </dl>

This property is deprecated. Instead, we recommend the **CIM\_ServiceAccessURI** class.

> [!Note]  
> Deprecated description: A URL that provides the protocol, network location, and other service-specific information required in order to access the service.

 

</dd> <dt>

**StartupConditions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](/windows/desktop/WmiSdk/standard-wmi-qualifiers) ("No value")
</dt> </dl>

This property is deprecated and should not be used.

> [!Note]  
> Deprecated description: The pre-conditions that must be met in order for this service to start correctly.

 

</dd> <dt>

**StartupParameters**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](/windows/desktop/WmiSdk/standard-wmi-qualifiers) ("No value")
</dt> </dl>

This property is deprecated and should not be used.

> [!Note]  
> Deprecated description: The parameters that must be supplied to the **StartService** method in order for this service to start correctly.

 

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

[**CIM\_Service**](cim-service.md)
</dt> </dl>

 

