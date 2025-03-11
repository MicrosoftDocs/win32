---
description: MSFT\_NetAdapterPowerManagement\_WakePattern\_TcpSyn defines settings for a TCP SYN wake pattern.
ms.assetid: e8973c66-fba2-4475-b438-3294e29e7766
title: MSFT\_NetAdapterPowerManagement\_WakePattern\_TcpSyn class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterPowerManagement_WakePattern_TcpSyn
- MSFT_NetAdapterPowerManagement_WakePattern_TcpSyn.SourceAddress
- MSFT_NetAdapterPowerManagement_WakePattern_TcpSyn.DestinationAddress
- MSFT_NetAdapterPowerManagement_WakePattern_TcpSyn.SourcePort
- MSFT_NetAdapterPowerManagement_WakePattern_TcpSyn.DestinationPort
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapterPowerManagement\_WakePattern\_TcpSyn class

MSFT\_NetAdapterPowerManagement\_WakePattern\_TcpSyn defines settings for a TCP SYN wake pattern.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapterPowerManagement_WakePattern_TcpSyn : MSFT_NetAdapterPowerManagement_Wake
{
  string SourceAddress;
  string DestinationAddress;
  uint16 SourcePort;
  uint16 DestinationPort;
};
```

## Members

The **MSFT\_NetAdapterPowerManagement\_WakePattern\_TcpSyn** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapterPowerManagement\_WakePattern\_TcpSyn** class has these properties.

<dl> <dt>

**DestinationAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the destination address of the SYN packet.

</dd> <dt>

**DestinationPort**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the TCP destination port number of the SYN packet.

</dd> <dt>

**SourceAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the source address of the SYN packet.

</dd> <dt>

**SourcePort**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Supplies the TCP source port number of the SYN packet.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

 




