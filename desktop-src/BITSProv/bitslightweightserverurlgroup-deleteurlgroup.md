---
title: DeleteUrlGroup method of the BitsCompactServerUrlGroup class
description: The DeleteUrlGroup method deletes the URL group on the host if the URL group was available earlier.
ms.assetid: '7d3c3c8b-8db4-4675-8c00-339a46df10a4'
keywords: ["DeleteUrlGroup method", "DeleteUrlGroup method, BitsCompactServerUrlGroup class", "BitsCompactServerUrlGroup class, DeleteUrlGroup method"]
topic_type:
- apiref
api_name:
- BitsCompactServerUrlGroup.DeleteUrlGroup
api_location:
- Root\microsoft\bits
api_type:
- COM
---

# DeleteUrlGroup method of the BitsCompactServerUrlGroup class

The **DeleteUrlGroup** method deletes the URL group on the host if the URL group was available earlier.

## Syntax


```mof
uint32 DeleteUrlGroup(
  [in] string UrlGroup
);
```



## Parameters

<dl> <dt>

*UrlGroup* \[in\]
</dt> <dd>

Specifies the URL prefix string for the URL group to delete.

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

 

 





