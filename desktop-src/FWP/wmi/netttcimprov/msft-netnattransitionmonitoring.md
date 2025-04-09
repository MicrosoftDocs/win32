---
description: Describes current active sessions for NAT.
ms.assetid: 4b30006b-73ef-4a28-a80e-bd10bd4a6445
title: MSFT\_NetNatTransitionMonitoring class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetNatTransitionMonitoring
- MSFT_NetNatTransitionMonitoring.TransportProtocol
- MSFT_NetNatTransitionMonitoring.InboundAddress
- MSFT_NetNatTransitionMonitoring.OutboundAddress
- MSFT_NetNatTransitionMonitoring.NatOutboundAddress
api_type: 
- DllExport
api_location: 
- NetTtCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetNatTransitionMonitoring class

Describes current active sessions for NAT.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetTtCim")]
class MSFT_NetNatTransitionMonitoring : MSFT_NetSettingData
{
  uint32 TransportProtocol;
  string InboundAddress;
  string OutboundAddress;
  string NatOutboundAddress;
};
```

## Members

The **MSFT\_NetNatTransitionMonitoring** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetNatTransitionMonitoring** class has these properties.

<dl> <dt>

**InboundAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the inbound address and port.

</dd> <dt>

**NatOutboundAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the NAT outbound address and port.

</dd> <dt>

**OutboundAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the outbound address and port.

</dd> <dt>

**TransportProtocol**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the transport protocol being translated.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCIMV2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTtCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTtCim.dll</dt> </dl> |



 

 




