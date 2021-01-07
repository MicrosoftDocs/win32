---
description: Controls when an event provider is unloaded.
ms.assetid: 7f11e521-d0f6-4c3c-8bfe-ceed2d106ed3
ms.tgt_platform: multiple
title: '__EventProviderCacheControl class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __EventProviderCacheControl
- Root.__EventProviderCacheControl.ClearAfter
api_type: 
- Schema
api_location: 
- Root
---

# \_\_EventProviderCacheControl class

The **\_\_EventProviderCacheControl** system class controls when an event provider is unloaded. It is located only in the \\root namespace.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[singleton]
class __EventProviderCacheControl : __CacheControl
{
  datetime ClearAfter;
};
```

## Members

The **\_\_EventProviderCacheControl** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_EventProviderCacheControl** class has these properties.

<dl> <dt>

**ClearAfter**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Time interval after Windows Management Instrumentation (WMI) releases an event provider. The time is in [interval format](interval-format.md). It may take up to twice the interval specified to unload the provider.

</dd> </dl>

## Remarks

The **\_\_EventProviderCacheControl** class is derived from [**\_\_CacheControl**](--cachecontrol.md).

For more information about using this class, see [Unloading a Provider](unloading-a-provider.md).

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
</dt> </dl>

 

