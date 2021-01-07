---
description: Controls the cache when a property provider is unloaded.
ms.assetid: 8fc7de7a-889c-4d53-97ea-a676879de1d3
ms.tgt_platform: multiple
title: '__PropertyProviderCacheControl class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __PropertyProviderCacheControl
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_PropertyProviderCacheControl class

The **\_\_PropertyProviderCacheControl** class controls the cache when a property provider is unloaded. This class exists only in the \\root namespace.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __PropertyProviderCacheControl
{
  datetime ClearAfter;
};
```

## Members

The **\_\_PropertyProviderCacheControl** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_PropertyProviderCacheControl** class has these properties.

<dl> <dt>

**ClearAfter**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Time interval after WMI releases a property provider. The time is in the interval format.

</dd> </dl>

## Remarks

The **\_\_PropertyProviderCacheControl** class is derived from [**\_\_CacheControl**](--cachecontrol.md). For more information, see [Unloading a Provider](unloading-a-provider.md).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> </dl>

 

 




