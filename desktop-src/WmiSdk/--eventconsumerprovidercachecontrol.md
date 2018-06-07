---
Description: Determines when WMI should release an event consumer provider.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 93246826-8070-4e05-96f0-f773041ed1d4
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: '\_\_EventConsumerProviderCacheControl class'
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# \_\_EventConsumerProviderCacheControl class

The **\_\_EventConsumerProviderCacheControl** system class determines when WMI should release an event consumer provider. The **\_\_EventConsumerProviderCacheControl** class is a singleton class. It is located only in the \\root namespace.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[singleton]
class __EventConsumerProviderCacheControl : CacheControl
{
  datetime ClearAfter;
};
```

## Members

The **\_\_EventConsumerProviderCacheControl** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_EventConsumerProviderCacheControl** class has these properties.

<dl> <dt>

**ClearAfter**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Time interval after which WMI releases an event consumer provider. It may take up to twice the interval specified to unload the provider. The time is in [interval format](interval-format.md).

</dd> </dl>

## Remarks

The **\_\_EventConsumerProviderCacheControl** class is derived from [**\_\_CacheControl**](--cachecontrol.md). For more information about using this class, see [Unloading a Provider](unloading-a-provider.md).

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | Root<br/>                |



## See also

<dl> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> </dl>

 

 




