---
description: Disables the Large Send Offload (LSO) properties on the network adapter.
ms.assetid: b9e356a5-38de-4289-b4cf-1aa548fc7591
title: Disable method of the MSFT\_NetAdapterLsoSettingData class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterLsoSettingData.Disable
api_type: 
- COM
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# Disable method of the MSFT\_NetAdapterLsoSettingData class

Disables the Large Send Offload (LSO) properties on the network adapter.

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

Disables LSOv2 for IPv4 on the network adapter.

</dd> <dt>

*IPv6* \[in\]
</dt> <dd>

Disables LSOv2 for IPv6 on the network adapter.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Returns an embedded instance of the [**MSFT\_NetAdapterLsoSettingData**](msft-netadapterlsosettingdata.md) class.

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

[**MSFT\_NetAdapterLsoSettingData**](msft-netadapterlsosettingdata.md)
</dt> </dl>

 

 




