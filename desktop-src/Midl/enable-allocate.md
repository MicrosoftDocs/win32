---
title: enable\_allocate attribute
description: The \ enable\_allocate\ ACF attribute specifies that the server stub code should enable the stub memory management environment.
ms.assetid: 3a232a82-f114-4d8c-8b71-cf8860c77db3
keywords:
- enable_allocate attribute MIDL
topic_type:
- apiref
api_name:
- enable_allocate
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# enable\_allocate attribute

The **\[enable\_allocate\]** ACF attribute specifies that the server stub code should enable the stub memory management environment.

> [!Note]  
> The **\[enable\_allocate\]** attribute is obsolete and is no longer supported.

 

``` syntax
[
    enable_allocate
  [ , optional-attribute-list]
]
interface interface-name
{
    . . .
};
```

## Parameters

<dl> <dt>

*optional-attribute-list* 
</dt> <dd>

Specifies a list of zero or more additional MIDL attributes.

</dd> <dt>

*interface-name* 
</dt> <dd>

The name of the interface to which the **\[enable\_allcoate\]** attribute will be applied.

</dd> </dl>

## Remarks

In default mode, the server stub enables the memory environment only when the **\[enable\_allocate\]** attribute is used. The memory management environment must be enabled before memory can be allocated using [**RpcSmAllocate**](https://msdn.microsoft.com/library/windows/desktop/aa378458). In **osf** mode (when you compile using the [**/osf**](-osf.md) switch), the stub enables this environment automatically, or on request when the **\[enable\_allocate\]** attribute is used.

The client side stub may be sensitive to the **Rpcss** memory management environment. If a sensitive client stub is executed when the **Rpcss** package is disabled, the default user allocator/deallocators are called (for example, [midl\_user\_allocate](https://msdn.microsoft.com/library/windows/desktop/aa378715)/ [midl\_user\_free](https://msdn.microsoft.com/library/windows/desktop/aa378716)). When enabled, the **Rpcss** package uses the allocator/deallocator pair from the package. In the default mode, the client is sensitive only when the **\[enable\_allocate\]** attribute is used. Typically, the client side stub operates in the disabled environment. In **osf** mode (when you compile using the [**/osf**](-osf.md) switch), the client is always sensitive to the **Rpcss** memory management environment and, therefore, the **\[enable\_allocate\]** attribute will not affect the client stubs.

## See also

<dl> <dt>

[Application Configuration File (ACF)](application-configuration-file-acf-.md)
</dt> <dt>

[midl\_user\_allocate](https://msdn.microsoft.com/library/windows/desktop/aa378715)
</dt> <dt>

[midl\_user\_free](https://msdn.microsoft.com/library/windows/desktop/aa378716)
</dt> <dt>

[**/osf**](-osf.md)
</dt> <dt>

[RpcSmDisableAllocate](https://msdn.microsoft.com/library/windows/desktop/aa378461)
</dt> <dt>

[RpcSmEnableAllocate](https://msdn.microsoft.com/library/windows/desktop/aa378462)
</dt> <dt>

[RpcSmFree](https://msdn.microsoft.com/library/windows/desktop/aa378463)
</dt> </dl>

 

 




