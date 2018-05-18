---
title: DeleteUrl method of the BitsCompactServerUrlGroup class
description: The DeleteUrl method deletes a URL on the server.
ms.assetid: 'bc768d44-46dd-483f-8851-0c5286e981ff'
keywords: ["DeleteUrl method", "DeleteUrl method, BitsCompactServerUrlGroup class", "BitsCompactServerUrlGroup class, DeleteUrl method"]
topic_type:
- apiref
api_name:
- BitsCompactServerUrlGroup.DeleteUrl
api_location:
- Root\microsoft\bits
api_type:
- COM
---

# DeleteUrl method of the BitsCompactServerUrlGroup class

The [**DeleteUrl**](https://msdn.microsoft.com/library/windows/desktop/aa964276) method deletes a URL on the server.

## Syntax


```mof
uint32 DeleteUrl(
  [in] string UrlSuffix
);
```



## Parameters

<dl> <dt>

*UrlSuffix* \[in\]
</dt> <dd>

Specifies the URL suffix to delete.

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

 

 





