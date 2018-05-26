---
title: GetProperty method of the BitsCompactServerUrlGroup class
description: The GetProperty method gets either the bandwidth or connection limit that is associated with the URL group.
ms.assetid: f4377366-aef0-4a52-a334-7b3211d30bc2
keywords:
- GetProperty method
- GetProperty method, BitsCompactServerUrlGroup class
- BitsCompactServerUrlGroup class, GetProperty method
topic_type:
- apiref
api_name:
- BitsCompactServerUrlGroup.GetProperty
api_location:
- Root\microsoft\bits
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GetProperty method of the BitsCompactServerUrlGroup class

The **GetProperty** method gets either the bandwidth or connection limit that is associated with the URL group.

## Syntax


```mof
uint32 GetProperty(
  [in]  string Property,
  [out] uint32 Value
);
```



## Parameters

<dl> <dt>

*Property* \[in\]
</dt> <dd>

Specifies the property name to get. This string can be set to one of the following values.

<dl> <dt>

<span id="ConnectionLimit"></span><span id="connectionlimit"></span><span id="CONNECTIONLIMIT"></span>**ConnectionLimit** (Specifies the connection limit property name. )
</dt> <dt>

<span id="BandwidthLimit"></span><span id="bandwidthlimit"></span><span id="BANDWIDTHLIMIT"></span>**BandwidthLimit** (Specifies the bandwidth limit property name. )
</dt> </dl> </dd> <dt>

*Value* \[out\]
</dt> <dd>

Specifies the value for the property. The VARIANT type should be V\_UI4.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                           |
| Redistributable<br/>          | Windows Management Framework on Windows Server 2008 with SP2<br/>                     |
| Namespace<br/>                | Root\\microsoft\\bits<br/>                                                            |
| MOF<br/>                      | <dl> <dt>BitsProvider.mof</dt> </dl> |



## See also

<dl> <dt>

[**BitsCompactServerUrlGroup**](bitslightweightserverurlgroup.md)
</dt> </dl>

 

 





