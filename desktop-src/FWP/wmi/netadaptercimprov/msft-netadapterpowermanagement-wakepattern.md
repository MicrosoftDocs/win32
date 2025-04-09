---
description: MSFT\_NetAdapterPowerManagement\_WakePattern defines a Wake-on-Lan (WOL) pattern.
ms.assetid: 4d4d0795-cdfe-453f-bd18-32f23af4bfea
title: MSFT\_NetAdapterPowerManagement\_WakePattern class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterPowerManagement_WakePattern
- MSFT_NetAdapterPowerManagement_WakePattern.WakePacketType
- MSFT_NetAdapterPowerManagement_WakePattern.ID
- MSFT_NetAdapterPowerManagement_WakePattern.Priority
- MSFT_NetAdapterPowerManagement_WakePattern.FriendlyName
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapterPowerManagement\_WakePattern class

MSFT\_NetAdapterPowerManagement\_WakePattern defines a Wake-on-Lan (WOL) pattern.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapterPowerManagement_WakePattern
{
  uint32 WakePacketType;
  uint32 ID;
  uint32 Priority;
  string FriendlyName;
};
```

## Members

The **MSFT\_NetAdapterPowerManagement\_WakePattern** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapterPowerManagement\_WakePattern** class has these properties.

<dl> <dt>

**FriendlyName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the friendly name of the wake pattern.

</dd> <dt>

**ID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the system defined ID of the wake pattern

</dd> <dt>

**Priority**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the priority of the wake pattern.

</dd> <dt>

**WakePacketType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the type of wake pattern.

<dl> <dt>

<span id="Unspecified"></span><span id="unspecified"></span><span id="UNSPECIFIED"></span>**Unspecified** (0)
</dt> <dt>

<span id="BitmapPattern"></span><span id="bitmappattern"></span><span id="BITMAPPATTERN"></span>**BitmapPattern** (1)
</dt> <dt>

<span id="MagicPacket"></span><span id="magicpacket"></span><span id="MAGICPACKET"></span>**MagicPacket** (2)
</dt> <dt>

<span id="IPv4TcpSyn"></span><span id="ipv4tcpsyn"></span><span id="IPV4TCPSYN"></span>**IPv4TcpSyn** (3)
</dt> <dt>

<span id="IPv6TcpSyn"></span><span id="ipv6tcpsyn"></span><span id="IPV6TCPSYN"></span>**IPv6TcpSyn** (4)
</dt> <dt>

<span id="EapolRequestIdMessage"></span><span id="eapolrequestidmessage"></span><span id="EAPOLREQUESTIDMESSAGE"></span>**EapolRequestIdMessage** (5)
</dt> <dt>

<span id="WildCard_"></span><span id="wildcard_"></span><span id="WILDCARD_"></span>**WildCard** (6 )
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

 




