---
description: Represents global Teredo configuration shared across all Teredo interfaces.
ms.assetid: ab40dee3-8154-4dfc-bba4-ea5ac96246bb
title: MSFT\_NetTeredoConfiguration class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetTeredoConfiguration
- MSFT_NetTeredoConfiguration.PolicyStore
- MSFT_NetTeredoConfiguration.Type
- MSFT_NetTeredoConfiguration.ServerName
- MSFT_NetTeredoConfiguration.msft_netteredoconfiguration
- MSFT_NetTeredoConfiguration.ClientPort
- MSFT_NetTeredoConfiguration.ServerShunt
- MSFT_NetTeredoConfiguration.ServerVirtualIP
- MSFT_NetTeredoConfiguration.DefaultQualified
api_type: 
- DllExport
api_location: 
- NetTtCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetTeredoConfiguration class

Represents global Teredo configuration shared across all Teredo interfaces.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetTtCim")]
class MSFT_NetTeredoConfiguration : MSFT_NetSettingData
{
  string     PolicyStore;
  uint32     Type;
  string     ServerName;
  uint32 REF msft_netteredoconfiguration;
  uint32     ClientPort;
  boolean    ServerShunt;
  string     ServerVirtualIP;
  boolean    DefaultQualified;
};
```

## Members

The **MSFT\_NetTeredoConfiguration** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_NetTeredoConfiguration** class has these methods.



| Method                                             | Description                                 |
|:---------------------------------------------------|:--------------------------------------------|
| [**Reset**](reset-msft-netteredoconfiguration.md) | Resets the Teredo configuration.<br/> |



 

### Properties

The **MSFT\_NetTeredoConfiguration** class has these properties.

<dl> <dt>

**ClientPort**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the client's UDP port.

</dd> <dt>

**DefaultQualified**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Write-only
</dt> </dl>

Sets Teredo as ready to communicate, a process referred to as qualification. By default, Teredo enters a dormant state when not in use; the qualification process brings it out of a dormant state.

</dd> <dt>

**msft\_netteredoconfiguration**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the client refresh interval in seconds.

</dd> <dt>

**PolicyStore**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the store from which to retrieve the Teredo configuration policy.

</dd> <dt>

**ServerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the name or the IPv4 address of the Teredo server.

</dd> <dt>

**ServerShunt**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether to bypass the tunnel miniport and IPv4 routing layer for high throughput on the Teredo Relay functionality of the Teredo Server.

</dd> <dt>

**ServerVirtualIP**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Represents the IPv4 address of the server virtual IP. Not applicable if running as a Teredo client.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Describes the Teredo service using one of the following values:

<dl> <dt>

<span id="default_"></span><span id="DEFAULT_"></span>**default** (0)
</dt> <dt>

<span id="relay_"></span><span id="RELAY_"></span>**relay** (1)
</dt> <dt>

<span id="client_"></span><span id="CLIENT_"></span>**client** (2)
</dt> <dt>

<span id="server_"></span><span id="SERVER_"></span>**server** (3)
</dt> <dt>

<span id="disabled_"></span><span id="DISABLED_"></span>**disabled** (4)
</dt> <dt>

<span id="automatic_"></span><span id="AUTOMATIC_"></span>**automatic** (5)
</dt> <dt>

<span id="enterpriseclient_"></span><span id="ENTERPRISECLIENT_"></span>**enterpriseclient** (6 )
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCIMV2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTtCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTtCim.dll</dt> </dl> |



 

 




