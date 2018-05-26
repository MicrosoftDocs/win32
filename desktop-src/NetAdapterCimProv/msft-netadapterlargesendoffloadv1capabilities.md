---
Description: This class is used to report LSOv1 capabilities on a network adapter.
ms.assetid: 2cbb492c-4c91-476d-9c98-486426a3cdc5
title: MSFT\_NetAdapterLargeSendOffloadV1Capabilities class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFT\_NetAdapterLargeSendOffloadV1Capabilities class

This class is used to report LSOv1 capabilities on a network adapter.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapterLargeSendOffloadV1Capabilities
{
  string  IPv4Encapsulation;
  uint32  IPv4MaxOffloadSizeSupported;
  uint32  IPv4MinSegmentCountSupported;
  boolean IPv4TcpOptionsSupported;
  boolean IPv4IpOptionsSupported;
};
```

## Members

The **MSFT\_NetAdapterLargeSendOffloadV1Capabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapterLargeSendOffloadV1Capabilities** class has these properties.

<dl> <dt>

**IPv4Encapsulation**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Defines the LSOv1 encapsulation settings for the Adapter.

</dd> <dt>

**IPv4IpOptionsSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if the Adapter supports segmentation of a packet containing IPv4 options.

</dd> <dt>

**IPv4MaxOffloadSizeSupported**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum bytes of user data in a single packet supported by the Adapter.

</dd> <dt>

**IPv4MinSegmentCountSupported**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Minimum number of segments that a large TCP packet must be divisible by before offloading to Adapter for segmentation.

</dd> <dt>

**IPv4TcpOptionsSupported**
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



 

 




