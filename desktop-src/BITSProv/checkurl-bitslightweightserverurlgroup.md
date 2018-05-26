---
title: CheckUrl method of the BitsCompactServerUrlGroup class
description: The CheckUrl method determines whether a URL exists on a server.
ms.assetid: b40c2ee0-4ded-4343-bc8e-2af217698402
keywords:
- CheckUrl method
- CheckUrl method, BitsCompactServerUrlGroup class
- BitsCompactServerUrlGroup class, CheckUrl method
topic_type:
- apiref
api_name:
- BitsCompactServerUrlGroup.CheckUrl
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

# CheckUrl method of the BitsCompactServerUrlGroup class

The **CheckUrl** method determines whether a URL exists on a server.

## Syntax


```mof
uint32 CheckUrl(
  [in]  string  UrlSuffix,
  [out] boolean UrlExists
);
```



## Parameters

<dl> <dt>

*UrlSuffix* \[in\]
</dt> <dd>

Specifies the URL suffix to locate.

</dd> <dt>

*UrlExists* \[out\]
</dt> <dd>

If this parameter is set to **TRUE**, the URL suffix is present in the URL group. Otherwise, the parameter is set to **FALSE**.

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

 

 





