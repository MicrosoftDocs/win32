---
description: This class is used to report LSOv2 capabilities on a network adapter.
ms.assetid: 54fb5b10-31a3-43a7-8907-219558b461dc
title: MSFT\_NetAdapterLargeSendOffloadV2Capabilities class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterLargeSendOffloadV2Capabilities
- MSFT_NetAdapterLargeSendOffloadV2Capabilities.IPv4Encapsulation
- MSFT_NetAdapterLargeSendOffloadV2Capabilities.IPv4MaxOffloadSizeSupported
- MSFT_NetAdapterLargeSendOffloadV2Capabilities.IPv4MinSegmentCountSupported
- MSFT_NetAdapterLargeSendOffloadV2Capabilities.IPv6Encapsulation
- MSFT_NetAdapterLargeSendOffloadV2Capabilities.IPv6MaxOffLoadSizeSupported
- MSFT_NetAdapterLargeSendOffloadV2Capabilities.IPv6MinSegmentCountSupported
- MSFT_NetAdapterLargeSendOffloadV2Capabilities.IPv6IpExtensionHeadersSupported
- MSFT_NetAdapterLargeSendOffloadV2Capabilities.IPv6TcpOptionsSupported
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapterLargeSendOffloadV2Capabilities class

This class is used to report LSOv2 capabilities on a network adapter.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapterLargeSendOffloadV2Capabilities
{
  string  IPv4Encapsulation;
  uint32  IPv4MaxOffloadSizeSupported;
  uint32  IPv4MinSegmentCountSupported;
  string  IPv6Encapsulation;
  uint32  IPv6MaxOffLoadSizeSupported;
  uint32  IPv6MinSegmentCountSupported;
  boolean IPv6IpExtensionHeadersSupported;
  boolean IPv6TcpOptionsSupported;
};
```

## Members

The **MSFT\_NetAdapterLargeSendOffloadV2Capabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapterLargeSendOffloadV2Capabilities** class has these properties.

<dl> <dt>

**IPv4Encapsulation**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Defines the IPv4 LSOv2 encapsulation settings for the Adapter.

</dd> <dt>

**IPv4MaxOffloadSizeSupported**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum bytes of user data in a single packet supported by the Adapter for IPv4 packets.

</dd> <dt>

**IPv4MinSegmentCountSupported**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Minimum number of segments that a large TCP packet must be divisible by before offloading to Adapter for segmentation for IPv4 packets.

</dd> <dt>

**IPv6Encapsulation**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Defines the IPv6 LSOv2 encapsulation settings for the Adapter.

</dd> <dt>

**IPv6IpExtensionHeadersSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if the Adapter supports segmentation of a packet containing IPv6 Extension headers.

</dd> <dt>

**IPv6MaxOffLoadSizeSupported**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum bytes of user data in a single packet supported by the Adapter for IPv6 packets.

</dd> <dt>

**IPv6MinSegmentCountSupported**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Minimum number of segments that a large TCP packet must be divisible by before offloading to Adapter for segmentation for IPv6 packets.

</dd> <dt>

**IPv6TcpOptionsSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if the Adapter supports segmentation of a packet containing TCP options.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

 




