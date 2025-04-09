---
description: Creates a MSFT\_NetNeighbor object for a new TCP/IP neighbor.
ms.assetid: 31e7a7bd-83b0-4da0-809d-a5ba8940a9fc
title: Create method of the MSFT\_NetNeighbor class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- kbSyntax
api_name: 
api_type: 
api_location: 
---

# Create method of the MSFT\_NetNeighbor class

Creates a [**MSFT\_NetNeighbor**](msft-netneighbor.md) object for a new TCP/IP neighbor.

## Syntax


```mof
uint32 Create(
  [in]  uint32           InterfaceIndex,
  [in]  string           InterfaceAlias,
  [in]  string           IPAddress,
  [in]  string           PolicyStore,
  [in]  string           LinkLayerAddress,
  [in]  uint8            State,
  [in]  uint16           AddressFamily,
  [in]  boolean          PassThru,
  [out] MSFT_NetNeighbor CmdletOutput[]
);
```



## Parameters

<dl> <dt>

*InterfaceIndex* \[in\]
</dt> <dd>

Specifies the interface index of the neighbor.

</dd> <dt>

*InterfaceAlias* \[in\]
</dt> <dd>

Specifies the interface alias of the neighbor.

</dd> <dt>

*IPAddress* \[in\]
</dt> <dd>

Specifies the network address of the neighbor.

</dd> <dt>

*PolicyStore* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*LinkLayerAddress* \[in\]
</dt> <dd>

Specifies the link layer address of the neighbor.

</dd> <dt>

*State* \[in\]
</dt> <dd>

Specifies the discovery state of the neighbor. You can specify one of the following values.



| Value                                                                        | Meaning                |
|------------------------------------------------------------------------------|------------------------|
| <dl> <dt>0</dt> </dl> | Unreachable<br/> |
| <dl> <dt>1</dt> </dl> | Incomplete<br/>  |
| <dl> <dt>2</dt> </dl> | Probe<br/>       |
| <dl> <dt>3</dt> </dl> | Delay<br/>       |
| <dl> <dt>4</dt> </dl> | Stale<br/>       |
| <dl> <dt>5</dt> </dl> | Reachable<br/>   |
| <dl> <dt>6</dt> </dl> | Permanent<br/>   |



 

</dd> <dt>

*AddressFamily* \[in\]
</dt> <dd>

Specifies the address family of the neighbor. You can specify one of the following values.



| Value                                                                                                                                                                                                            | Meaning                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| <span id="IPv4"></span><span id="ipv4"></span><span id="IPV4"></span><dl> <dt>**IPv4**</dt> <dt>2</dt> </dl>  | The address family is IPv4.<br/> |
| <span id="IPv6"></span><span id="ipv6"></span><span id="IPV6"></span><dl> <dt>**IPv6**</dt> <dt>23</dt> </dl> | The address family is IPv6.<br/> |



 

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifies whether the method should output an object that represents the newly created TCP/IP neighbor in the *CmdletOutput* parameter.

</dd> <dt>

*CmdletOutput* \[out\]
</dt> <dd>

Receives the new [**MSFT\_NetNeighbor**](msft-netneighbor.md) object.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTCPIP.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTCPIP.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_NetNeighbor**](msft-netneighbor.md)
</dt> </dl>

 

 




