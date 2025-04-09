---
description: This class describes a QoS classification element.
ms.assetid: 524799ca-41df-4edf-ad19-cc00a77457ce
title: MSFT\_NetAdapter\_QosClassificationElement class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapter_QosClassificationElement
- MSFT_NetAdapter_QosClassificationElement.ProtocolSelector
- MSFT_NetAdapter_QosClassificationElement.ProtocolSpecificValue
- MSFT_NetAdapter_QosClassificationElement.Priority
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapter\_QosClassificationElement class

This class describes a QoS classification element.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapter_QosClassificationElement
{
  uint16 ProtocolSelector;
  uint16 ProtocolSpecificValue;
  uint8  Priority;
};
```

## Members

The **MSFT\_NetAdapter\_QosClassificationElement** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapter\_QosClassificationElement** class has these properties.

<dl> <dt>

**Priority**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxValue** (7)
</dt> </dl>

Specifies the IEEE 802.1p priority value to use when a match is made.

</dd> <dt>

**ProtocolSelector**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the protocol used in the ProtocolSpecificValue field.

<dl> <dt>

<span id="Reserved"></span><span id="reserved"></span><span id="RESERVED"></span>**Reserved** (0)
</dt> <dt>

<span id="Default"></span><span id="default"></span><span id="DEFAULT"></span>**Default** (1)
</dt> <dt>

<span id="TCP_Port"></span><span id="tcp_port"></span><span id="TCP_PORT"></span>**TCP Port** (2)
</dt> <dt>

<span id="UDP_Port"></span><span id="udp_port"></span><span id="UDP_PORT"></span>**UDP Port** (3)
</dt> <dt>

<span id="TCP_or_UDP_Port"></span><span id="tcp_or_udp_port"></span><span id="TCP_OR_UDP_PORT"></span>**TCP or UDP Port** (4)
</dt> <dt>

<span id="Ethertype"></span><span id="ethertype"></span><span id="ETHERTYPE"></span>**Ethertype** (5)
</dt> <dt>

<span id="NetDirect_Port"></span><span id="netdirect_port"></span><span id="NETDIRECT_PORT"></span>**NetDirect Port** (6)
</dt> </dl>

</dd> <dt>

**ProtocolSpecificValue**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies a protocol-specific value for classification. For example, this property is set to a TCP port number if ProtocolSelector is set to "TCP Port", or Ethertype value is ProtocolSelector is set to "Ethertype".

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

 




