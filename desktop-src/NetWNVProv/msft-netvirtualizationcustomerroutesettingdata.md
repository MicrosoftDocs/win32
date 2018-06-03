---
Description: The MSFT\_NetVirtualizationCustomerRouteSettingData class represents a customer route or forwarding rule in the WNV module policy table to define virtual network topology seen by the virtual machines.
ms.assetid: b9a4b523-2d7e-42cd-8fff-db5563a1b4f6
title: MSFT\_NetVirtualizationCustomerRouteSettingData class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_NetVirtualizationCustomerRouteSettingData class

The MSFT\_NetVirtualizationCustomerRouteSettingData class represents a customer route or forwarding rule in the WNV module policy table to define virtual network topology seen by the virtual machines.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetVirtualizationCustomerRouteSettingData : MSFT_NetSettingData
{
  uint32 VirtualSubnetID;
  string DestinationPrefix;
  string NextHop;
  string CustomerID;
  uint32 Metric;
  string RoutingDomainID;
};
```

## Members

The **MSFT\_NetVirtualizationCustomerRouteSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetVirtualizationCustomerRouteSettingData** class has these properties.

<dl> <dt>

**CustomerID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The GUID set by the administrators to identify a customer entity for this route record.

</dd> <dt>

**DestinationPrefix**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The destination IP prefix for this route record.

</dd> <dt>

**Metric**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The metric used to arbitrate between multiple matching routes of the same destination prefix.

</dd> <dt>

**NextHop**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The next hop gateway IP address for this route record.

</dd> <dt>

**RoutingDomainID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The GUID set by the administrators for the WNV module to uniquely identify a virtual network that composes of multiple virtual subnets routable to each other.

</dd> <dt>

**VirtualSubnetID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxValue** ( 16777215 )
</dt> </dl>

A unique identifier number of the virtual subnet of this customer route record.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                        |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                        |
| MOF<br/>                      | <dl> <dt>NetWNV.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetWNV.dll</dt> </dl> |



 

 




