---
description: Controls when a class or instance provider is unloaded.
ms.assetid: 4cbeb820-8a65-4fab-97f1-2a973b2a4310
ms.tgt_platform: multiple
title: '__ObjectProviderCacheControl class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __ObjectProviderCacheControl
- Root.__ObjectProviderCacheControl.ClearAfter
api_type: 
- Schema
api_location: 
- Root
---

# \_\_ObjectProviderCacheControl class

The **\_\_ObjectProviderCacheControl** system class controls when a class or instance provider is unloaded. It is located only in the \\root namespace.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[singleton]
class __ObjectProviderCacheControl : __CacheControl
{
  datetime ClearAfter;
};
```

## Members

The **\_\_ObjectProviderCacheControl** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_ObjectProviderCacheControl** class has these properties.

<dl> <dt>

**ClearAfter**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Time interval after which WMI releases an instance, class, or method provider. The time is in [interval format](interval-format.md).

</dd> </dl>

## Remarks

The **\_\_ObjectProviderCacheControl** class is derived from [**\_\_CacheControl**](--cachecontrol.md). For more information about using this class, see [Unloading a Provider](unloading-a-provider.md).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | Root<br/>                |



## See also

<dl> <dt>

[**\_\_CacheControl**](/windows/desktop/WmiSdk/--cachecontrol)
</dt> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> <dt>

[Receiving Events at All Times](receiving-events-at-all-times.md)
</dt> </dl>

 

