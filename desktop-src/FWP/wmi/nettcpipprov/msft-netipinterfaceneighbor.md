---
description: Represents an association between a TCP/IP network interface and a TCP/IP neighbor.
ms.assetid: 5a52e983-70c5-4e00-9220-6f5cf26484e0
title: MSFT\_NetIPInterfaceNeighbor class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetIPInterfaceNeighbor
- MSFT_NetIPInterfaceNeighbor.FrameType
- MSFT_NetIPInterfaceNeighbor.Antecedent
- MSFT_NetIPInterfaceNeighbor.Dependent
api_type: 
- DllExport
api_location: 
- NetTCPIP.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetIPInterfaceNeighbor class

Represents an association between a TCP/IP network interface and a TCP/IP neighbor.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, UMLPackagePath("CIM::Network::ProtocolEndpoints"), ClassVersion("1.0.0"), dynamic, provider("nettcpip"), AMENDMENT]
class MSFT_NetIPInterfaceNeighbor : CIM_BindsToLANEndpoint
{
  uint16                  FrameType;
  MSFT_NetIPInterface REF Antecedent;
  MSFT_NetNeighbor    REF Dependent;
};
```

## Members

The **MSFT\_NetIPInterfaceNeighbor** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetIPInterfaceNeighbor** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetIPInterface**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**Override**](/windows/win32/wmisdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

The [**MSFT\_NetIPInterface**](msft-netipinterface.md) object used to reach the neighbor.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetNeighbor**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/win32/wmisdk/key-qualifier), [**Override**](/windows/win32/wmisdk/standard-qualifiers) ("Dependent")
</dt> </dl>

The [**MSFT\_NetNeighbor**](msft-netneighbor.md) object for neighbor associated with the IP interface.

</dd> <dt>

**FrameType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This describes the framing method for the upper layer SAP or Endpoint that is bound to the LAN endpoint. Note that "Raw802.3" is only known to be used with the IPX protocol.

This property is inherited from [**CIM\_BindsToLANEndpoint**](cim-bindstolanendpoint.md).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Ethernet"></span><span id="ethernet"></span><span id="ETHERNET"></span>**Ethernet** (1)
</dt> <dt>

<span id="802.2"></span>**802.2** (2)
</dt> <dt>

<span id="SNAP"></span><span id="snap"></span>**SNAP** (3)
</dt> <dt>

<span id="Raw802.3"></span><span id="raw802.3"></span><span id="RAW802.3"></span>**Raw802.3** (4)
</dt> </dl>

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

[**CIM\_BindsToLANEndpoint**](cim-bindstolanendpoint.md)
</dt> <dt>

[NetTCPIP Provider Classes](net-tcpip-classes.md)
</dt> <dt>

[**MSFT\_NetIPInterface**](msft-netipinterface.md)
</dt> <dt>

[**MSFT\_NetNeighbor**](msft-netneighbor.md)
</dt> </dl>

 

