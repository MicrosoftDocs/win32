---
title: CreateUrlGroup method of the BitsCompactServerUrlGroup class
description: The CreateUrlGroup method creates a URL group on the host if the URL group was not available earlier.
ms.assetid: 12e71079-8f86-4238-bbe1-a80265039d57
keywords:
- CreateUrlGroup method
- CreateUrlGroup method, BitsCompactServerUrlGroup class
- BitsCompactServerUrlGroup class, CreateUrlGroup method
topic_type:
- apiref
api_name:
- BitsCompactServerUrlGroup.CreateUrlGroup
api_location:
- Root\microsoft\bits
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateUrlGroup method of the BitsCompactServerUrlGroup class

The **CreateUrlGroup** method creates a URL group on the host if the URL group was not available earlier.

## Syntax


```mof
uint32 CreateUrlGroup(
  [in] string UrlGroup
);
```



## Parameters

<dl> <dt>

*UrlGroup* \[in\]
</dt> <dd>

Specifies the URL prefix string for the URL group.

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

 

 





