---
description: Disables the Receive Segment Coalescing (RSC) properties on the network adapter.
ms.assetid: c720e56f-6bf0-4744-ba71-57c50126db4f
title: Disable method of the MSFT\_NetAdapterRscSettingData class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterRscSettingData.Disable
api_type: 
- COM
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# Disable method of the MSFT\_NetAdapterRscSettingData class

Disables the Receive Segment Coalescing (RSC) properties on the network adapter.

## Syntax


```mof
uint32 Disable(
  [in]  boolean IPv4,
  [in]  boolean IPv6,
  [out] string  cmdletOutput
);
```



## Parameters

<dl> <dt>

*IPv4* \[in\]
</dt> <dd>

**true** to disable the RSC settings for IPv4 TCP packets.

</dd> <dt>

*IPv6* \[in\]
</dt> <dd>

**true** to disable the RSC settings for IPv4 TCP packets.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Returns an embedded instance of the [**MSFT\_NetAdapterRscSettingData**](msft-netadapterrscsettingdata.md) class.

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

[**MSFT\_NetAdapterRscSettingData**](msft-netadapterrscsettingdata.md)
</dt> </dl>

 

 




