---
Description: The MSFT\_NetVirtualizationProviderRouteSettingData represents a physical route configured on the network interface the WNV module is configured on.
ms.assetid: a096336e-65d3-44f5-956d-a5b9ad4eb6f8
title: MSFT\_NetVirtualizationProviderRouteSettingData class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_NetVirtualizationProviderRouteSettingData class

The MSFT\_NetVirtualizationProviderRouteSettingData represents a physical route configured on the network interface the WNV module is configured on.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetVirtualizationProviderRouteSettingData : MSFT_NetSettingData
{
  uint32 InterfaceIndex;
  string DestinationPrefix;
  string NextHop;
  string CustomerID;
  uint32 Metric;
};
```

## Members

The **MSFT\_NetVirtualizationProviderRouteSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetVirtualizationProviderRouteSettingData** class has these properties.

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

**InterfaceIndex**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Index of the interface WNV module is configured on.

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

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                        |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                        |
| MOF<br/>                      | <dl> <dt>NetWNV.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetWNV.dll</dt> </dl> |



 

 




