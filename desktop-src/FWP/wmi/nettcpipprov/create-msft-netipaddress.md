---
description: Creates the IPAddress.
ms.assetid: 5c4657fd-9cf6-4538-90ee-5aaa881e945b
title: Create method of the MSFT\_NetIPAddress class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- kbSyntax
api_name: 
api_type: 
api_location: 
---

# Create method of the MSFT\_NetIPAddress class

Creates the IPAddress.

## Syntax


```mof
uint32 Create(
  [in]  uint32            InterfaceIndex,
  [in]  string            InterfaceAlias,
  [in]  string            IPAddress,
  [in]  uint16            AddressFamily,
  [in]  uint8             PrefixLength,
  [in]  uint8             Type,
  [in]  uint16            PrefixOrigin,
  [in]  uint16            SuffixOrigin,
  [in]  uint16            AddressState,
  [in]  datetime          ValidLifetime,
  [in]  datetime          PreferredLifetime,
  [in]  boolean           SkipAsSource,
  [in]  string            DefaultGateway,
  [in]  string            PolicyStore,
  [in]  boolean           PassThru,
  [out] MSFT_NetIPAddress CmdletOutput[]
);
```



## Parameters

<dl> <dt>

*InterfaceIndex* \[in\]
</dt> <dd>

The user-friendly interface index.

</dd> <dt>

*InterfaceAlias* \[in\]
</dt> <dd>

The user-friendly interface name.

</dd> <dt>

*IPAddress* \[in\]
</dt> <dd>

The IP address.

</dd> <dt>

*AddressFamily* \[in\]
</dt> <dd>

Indicates whether the address family for this IP address is v4 or v6.



| Value                                                                                                                                                            | Meaning                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| <span id="2"></span><dl> <dt>**2**</dt> <dt>IPv4</dt> </dl>   | The address family is IPv4<br/> |
| <span id="23"></span><dl> <dt>**23**</dt> <dt>IPv6</dt> </dl> | The address family is IPv6<br/> |



 

</dd> <dt>

*PrefixLength* \[in\]
</dt> <dd>

The type of address.



| Value                                                                                                                                                             | Meaning                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <span id="1"></span><dl> <dt>**1**</dt> <dt>Unicast</dt> </dl> | Marks the address as a unicast address. This is the default<br/> |
| <span id="2"></span><dl> <dt>**2**</dt> <dt>Anycast</dt> </dl> | Marks the address as an anycast address<br/>                     |



 

</dd> <dt>

*Type* \[in\]
</dt> <dd>

The type of address.



| Value                                                                                                                                                             | Meaning                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <span id="1"></span><dl> <dt>**1**</dt> <dt>Unicast</dt> </dl> | Marks the address as a unicast address. This is the default<br/> |
| <span id="2"></span><dl> <dt>**2**</dt> <dt>Anycast</dt> </dl> | Marks the address as an anycast address<br/>                     |



 

</dd> <dt>

*PrefixOrigin* \[in\]
</dt> <dd>

Prefix origin of this address.

<dl> <dt>

<span id="0"></span>**0** (Other)
</dt> <dt>

<span id="1"></span>**1** (Manual)
</dt> <dt>

<span id="2"></span>**2** (WellKnown)
</dt> <dt>

<span id="3"></span>**3** (Dhcp)
</dt> <dt>

<span id="4"></span>**4** (RouterAdvertisement)
</dt> </dl> </dd> <dt>

*SuffixOrigin* \[in\]
</dt> <dd>

Suffix origin of this address.

<dl> <dt>

<span id="0"></span>**0** (Other)
</dt> <dt>

<span id="1"></span>**1** (Manual)
</dt> <dt>

<span id="2"></span>**2** (WellKnown)
</dt> <dt>

<span id="3"></span>**3** (Dhcp)
</dt> <dt>

<span id="4"></span>**4** (Link)
</dt> <dt>

<span id="5"></span>**5** (Random)
</dt> </dl> </dd> <dt>

*AddressState* \[in\]
</dt> <dd>

Address lifetime state.

<dl> <dt>

<span id="0"></span>**0** (Invalid)
</dt> <dt>

<span id="1"></span>**1** (Tentative)
</dt> <dt>

<span id="2"></span>**2** (Duplicate)
</dt> <dt>

<span id="3"></span>**3** (Deprecated)
</dt> <dt>

<span id="4"></span>**4** (Preferred)
</dt> </dl> </dd> <dt>

*ValidLifetime* \[in\]
</dt> <dd>

Lifetime over which the address is valid. The default value is infinite.

</dd> <dt>

*PreferredLifetime* \[in\]
</dt> <dd>

Lifetime over which the address is preferred. The default value is infinite.

</dd> <dt>

*SkipAsSource* \[in\]
</dt> <dd>

true to not use the address as source address for any outgoing packet unless explicitly asked to.

</dd> <dt>

*DefaultGateway* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*PolicyStore* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifies whether the method should output an object that represents the newly created IP address in the *CmdletOutput* parameter.

</dd> <dt>

*CmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**MSFT\_NetIPAddress**](msft-netipaddress.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                           |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                                           |
| Header<br/>                   | <dl> <dt>Spcollec.h (include Dxtmpl.h)</dt> </dl> |
| MOF<br/>                      | <dl> <dt>NetTCPIP.mof</dt> </dl>                  |
| DLL<br/>                      | <dl> <dt>NetTCPIP.dll</dt> </dl>                  |



## See also

<dl> <dt>

[**MSFT\_NetIPAddress**](msft-netipaddress.md)
</dt> </dl>

 

 




