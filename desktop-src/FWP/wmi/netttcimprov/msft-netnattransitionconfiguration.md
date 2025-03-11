---
description: Provides configuration settings for Network Address Translation (NAT).
ms.assetid: 3582d8c5-2944-4fe7-af19-9c0219c050f9
title: MSFT\_NetNatTransitionConfiguration class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetNatTransitionConfiguration
- MSFT_NetNatTransitionConfiguration.InstanceName
- MSFT_NetNatTransitionConfiguration.PolicyStore
- MSFT_NetNatTransitionConfiguration.State
- MSFT_NetNatTransitionConfiguration.InboundInterface
- MSFT_NetNatTransitionConfiguration.OutboundInterface
- MSFT_NetNatTransitionConfiguration.PrefixMapping
- MSFT_NetNatTransitionConfiguration.IPv4AddressPortPool
- MSFT_NetNatTransitionConfiguration.TcpMappingTimeout
api_type: 
- DllExport
api_location: 
- NetTtCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetNatTransitionConfiguration class

Provides configuration settings for Network Address Translation (NAT).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetTtCim")]
class MSFT_NetNatTransitionConfiguration : MSFT_NetSettingData
{
  string InstanceName;
  uint32 PolicyStore;
  uint32 State;
  string InboundInterface[];
  string OutboundInterface[];
  string PrefixMapping[];
  string IPv4AddressPortPool[];
         TcpMappingTimeout;
};
```

## Members

The **MSFT\_NetNatTransitionConfiguration** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_NetNatTransitionConfiguration** class has these methods.



| Method                                                        | Description                 |
|:--------------------------------------------------------------|:----------------------------|
| [**Disable**](disable-msft-netnattransitionconfiguration.md) | Turns NAT64 off.<br/> |
| [**Enable**](enable-msft-netnattransitionconfiguration.md)   | Turns NAT64 on.<br/>  |



 

### Properties

The **MSFT\_NetNatTransitionConfiguration** class has these properties.

<dl> <dt>

**InboundInterface**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates the names of the inbound interfaces.

</dd> <dt>

**InstanceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the name of this instance of Windows NAT.

</dd> <dt>

**IPv4AddressPortPool**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates the addresses and ports that are in the dedicated IPv4 address pool and port range.

</dd> <dt>

**OutboundInterface**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates the names of the outbound interfaces.

</dd> <dt>

**PolicyStore**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the store in which to store this configuration object.

<dl> <dt>

<span id="PersistentStore"></span><span id="persistentstore"></span><span id="PERSISTENTSTORE"></span>**PersistentStore** (0)
</dt> <dt>

<span id="ActiveStore"></span><span id="activestore"></span><span id="ACTIVESTORE"></span>**ActiveStore** (1)
</dt> </dl>

</dd> <dt>

**PrefixMapping**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates how IPv4 address ranges map to IPv6 prefixes.

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether NAT is turned on.



| Value                                                                                                                                                                                                                           | Meaning                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>0</dt> </dl> | NAT is turned off.<br/> |
| <span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span><dl> <dt>**Enabled**</dt> <dt>1</dt> </dl>     | NAT is turned on.<br/>  |



 

</dd> <dt>

**TcpMappingTimeout**
</dt> <dd> <dl> <dt>

Access type: Read/write
</dt> </dl>

Indicates the amount of time an established TCP session can remain idle before timing out.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTtCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTtCim.dll</dt> </dl> |



 

 




