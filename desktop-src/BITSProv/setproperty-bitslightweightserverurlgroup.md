---
title: SetProperty method of the BitsCompactServerUrlGroup class
description: The SetProperty method sets either the bandwidth or connection limit in BYTEs per second.
ms.assetid: 'f025ed37-0993-4cd3-adfe-5c4096e1d0b6'
keywords: ["SetProperty method", "SetProperty method, BitsCompactServerUrlGroup class", "BitsCompactServerUrlGroup class, SetProperty method"]
topic_type:
- apiref
api_name:
- BitsCompactServerUrlGroup.SetProperty
api_location:
- Root\microsoft\bits
api_type:
- COM
---

# SetProperty method of the BitsCompactServerUrlGroup class

The **SetProperty** method sets either the bandwidth or connection limit in BYTEs per second.

## Syntax


```mof
uint32 SetProperty(
  [in] string Property,
  [in] uint32 Value
);
```



## Parameters

<dl> <dt>

*Property* \[in\]
</dt> <dd>

Specifies the property name to set for the URL group. This string can be set to one of the following values.

<dl> <dt>

<span id="ConnectionLimit"></span><span id="connectionlimit"></span><span id="CONNECTIONLIMIT"></span>**ConnectionLimit** (Specifies the connection limit property name. )
</dt> <dt>

<span id="BandwidthLimit"></span><span id="bandwidthlimit"></span><span id="BANDWIDTHLIMIT"></span>**BandwidthLimit** (Specifies the bandwidth limit property name. )
</dt> </dl> </dd> <dt>

*Value* \[in\]
</dt> <dd>

Specifies the value to set for the property. The minimum value for the **BandwidthLimit** property is 1024 bytes.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                           |
| Redistributable<br/>          | Windows Management Framework on Windows Server 2008 with SP2<br/>                     |
| Namespace<br/>                | Root\\microsoft\\bits<br/>                                                            |
| MOF<br/>                      | <dl> <dt>BitsProvider.mof</dt> </dl> |



## See also

<dl> <dt>

[**BitsCompactServerUrlGroup**](bitslightweightserverurlgroup.md)
</dt> </dl>

 

 





