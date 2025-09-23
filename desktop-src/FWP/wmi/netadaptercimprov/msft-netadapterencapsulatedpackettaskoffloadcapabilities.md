---
description: Used to report the offload capabilities of a network adapter when it transmits or receives encapsulated packets.
ms.assetid: 3fdb59a6-347f-437e-9e4d-22393593ef34
title: MSFT\_NetAdapterEncapsulatedPacketTaskOffloadCapabilities class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterEncapsulatedPacketTaskOffloadCapabilities
- MSFT_NetAdapterEncapsulatedPacketTaskOffloadCapabilities.TransmitChecksumOffloadSupported
- MSFT_NetAdapterEncapsulatedPacketTaskOffloadCapabilities.ReceiveChecksumOffloadSupported
- MSFT_NetAdapterEncapsulatedPacketTaskOffloadCapabilities.LsoV2Supported
- MSFT_NetAdapterEncapsulatedPacketTaskOffloadCapabilities.RssSupported
- MSFT_NetAdapterEncapsulatedPacketTaskOffloadCapabilities.VmqSupported
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapterEncapsulatedPacketTaskOffloadCapabilities class

Used to report the offload capabilities of a network adapter when it transmits or receives encapsulated packets.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapterEncapsulatedPacketTaskOffloadCapabilities
{
  uint32 TransmitChecksumOffloadSupported;
  uint32 ReceiveChecksumOffloadSupported;
  uint32 LsoV2Supported;
  uint32 RssSupported;
  uint32 VmqSupported;
};
```

## Members

The **MSFT\_NetAdapterEncapsulatedPacketTaskOffloadCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapterEncapsulatedPacketTaskOffloadCapabilities** class has these properties.

<dl> <dt>

**LsoV2Supported**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates network adapter support for Large Send Offload (LSO) V2 for encapsulated packets

</dd> <dt>

**ReceiveChecksumOffloadSupported**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates network adapter support for Receive Checksum Offload for this encapsulated packet type

</dd> <dt>

**RssSupported**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates network adapter support for Receive Side Scaling (RSS) for encapsulated packets

</dd> <dt>

**TransmitChecksumOffloadSupported**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates network adapter support for Transmit Checksum Offload for this encapsulated packet type

</dd> <dt>

**VmqSupported**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates network adapter support for Virtual Machine Queue (VMQ) for encapsulated packets

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



## See also

<dl> <dt>

[NetAdapterCim Provider](network-adapter-classes.md)
</dt> </dl>

 

 




