---
description: Provides configuration settings for DNS64.
ms.assetid: d5478d7f-0fb4-451e-948f-54f403fb7ff2
title: MSFT\_NetDnsTransitionConfiguration class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetDnsTransitionConfiguration
- MSFT_NetDnsTransitionConfiguration.State
- MSFT_NetDnsTransitionConfiguration.OnlySendAQuery
- MSFT_NetDnsTransitionConfiguration.Latency
- MSFT_NetDnsTransitionConfiguration.AlwaysSynthesize
- MSFT_NetDnsTransitionConfiguration.PrefixMapping
- MSFT_NetDnsTransitionConfiguration.ExclusionList
- MSFT_NetDnsTransitionConfiguration.SendInterface
- MSFT_NetDnsTransitionConfiguration.AcceptInterface
api_type: 
- DllExport
api_location: 
- NetTtCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetDnsTransitionConfiguration class

Provides configuration settings for DNS64.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetTtCim")]
class MSFT_NetDnsTransitionConfiguration : MSFT_NetSettingData
{
  uint32  State;
  boolean OnlySendAQuery;
  uint32  Latency;
  boolean AlwaysSynthesize;
  string  PrefixMapping[];
  string  ExclusionList[];
  string  SendInterface[];
  string  AcceptInterface[];
};
```

## Members

The **MSFT\_NetDnsTransitionConfiguration** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_NetDnsTransitionConfiguration** class has these methods.



| Method                                                        | Description                                    |
|:--------------------------------------------------------------|:-----------------------------------------------|
| [**Disable**](disable-msft-netdnstransitionconfiguration.md) | Turns DNS 64 off.<br/>                   |
| [**Enable**](enable-msft-netdnstransitionconfiguration.md)   | Turns DNS64 on.<br/>                     |
| [**Reset**](reset-msft-netdnstransitionconfiguration.md)     | Resets the configuration for DNS64.<br/> |



 

### Properties

The **MSFT\_NetDnsTransitionConfiguration** class has these properties.

<dl> <dt>

**AcceptInterface**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the names of interfaces on which to accept incoming queries.

</dd> <dt>

**AlwaysSynthesize**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether to return synthesized AAAA response even if an A record was found.

</dd> <dt>

**ExclusionList**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies a list of addresses that DNS64 should not translate.

</dd> <dt>

**Latency**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates the delay in milliseconds (ms) between the queries for AAAA records and A records.

</dd> <dt>

**OnlySendAQuery**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether to send a query only for A records (32-bit IPv4 addresses), or to send a query for AAAA records (128-bit IPv6 addresses) before sending a query for A records.

</dd> <dt>

**PrefixMapping**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates the mapping of IPv4 address ranges to IPv4 prefixes.

</dd> <dt>

**SendInterface**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the names of the interfaces on which to send outgoing queries.

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether DNS64 is turned on.



| Value                                                                                                                                                                                                                           | Meaning                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| <span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span><dl> <dt>**Enabled**</dt> <dt>0</dt> </dl>     | DNS 64 is turned on.<br/>  |
| <span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span><dl> <dt>**Disabled**</dt> <dt>1</dt> </dl> | DNS 64 is turned off.<br/> |



 

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTtCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTtCim.dll</dt> </dl> |



 

 




