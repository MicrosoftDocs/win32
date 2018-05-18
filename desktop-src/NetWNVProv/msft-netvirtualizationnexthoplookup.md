---
Description: 'Represents a result of looking up a route for the customer address (CA) space address for a given destination.'
ms.assetid: '1C91ECC8-ACA0-45E1-8530-9DC779C06FA8'
title: 'MSFT\_NetVirtualizationNextHopLookup class'
---

# MSFT\_NetVirtualizationNextHopLookup class

Represents a result of looking up a route for the customer address (CA) space address for a given destination.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_NetVirtualizationNextHopLookup : MSFT_NetSettingData
{
  string SourceCustomerAddress;
  string DestinationCustomerAddress;
  uint32 SourceVirtualSubnetID;
  string NextHopAddress;
  string SourceMACAddress;
  string NextHopMACAddress;
};
```

## Members

The **MSFT\_NetVirtualizationNextHopLookup** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_NetVirtualizationNextHopLookup** class has these methods.



| Method                                                       | Description                                                     |
|:-------------------------------------------------------------|:----------------------------------------------------------------|
| [**Select**](msft-netvirtualizationnexthoplookup-select.md) | Determines the next hop for the destination address.<br/> |



 

### Properties

The **MSFT\_NetVirtualizationNextHopLookup** class has these properties.

<dl> <dt>

**DestinationCustomerAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IP address of the destination.

</dd> <dt>

**NextHopAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IP address of the next hop.

</dd> <dt>

**NextHopMACAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The MAC address of the destination.

</dd> <dt>

**SourceCustomerAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IP address of the source.

</dd> <dt>

**SourceMACAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The MAC address of the source.

</dd> <dt>

**SourceVirtualSubnetID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A unique identifier that corresponds to a virtual subnet.

Range: *value* = 16777215

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                        |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                        |
| MOF<br/>                      | <dl> <dt>NetWNV.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetWNV.dll</dt> </dl> |



## See also

<dl> <dt>

[NetWNV Provider Classes](net-virtualization-classes.md)
</dt> </dl>

 

 




