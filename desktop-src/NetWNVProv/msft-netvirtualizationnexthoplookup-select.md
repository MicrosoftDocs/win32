---
Description: Determines the next hop for the destination address.
ms.assetid: 46856EAF-47E7-458E-B805-FBB0A0036340
title: Select method of the MSFT\_NetVirtualizationNextHopLookup class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Select method of the MSFT\_NetVirtualizationNextHopLookup class

Determines the next hop for the destination address.

## Syntax


```mof
static uint32 Select(
  [in]  string                              SourceCustomerAddress,
  [in]  string                              DestinationCustomerAddress,
  [in]  uint32                              SourceVirtualSubnetID,
  [out] MSFT_NetVirtualizationNextHopLookup CmdletOutput[]
);
```



## Parameters

<dl> <dt>

*SourceCustomerAddress* \[in\]
</dt> <dd>

The IP address of the source.

</dd> <dt>

*DestinationCustomerAddress* \[in\]
</dt> <dd>

The IP address of the destination.

</dd> <dt>

*SourceVirtualSubnetID* \[in\]
</dt> <dd>

A unique identifier that corresponds to a virtual subnet.

</dd> <dt>

*CmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**MSFT\_NetVirtualizationNextHopLookup**](msft-netvirtualizationnexthoplookup.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                        |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                        |
| MOF<br/>                      | <dl> <dt>NetWNV.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetWNV.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_NetVirtualizationNextHopLookup**](msft-netvirtualizationnexthoplookup.md)
</dt> </dl>

 

 




