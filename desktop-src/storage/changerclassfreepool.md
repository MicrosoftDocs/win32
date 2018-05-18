---
title: ChangerClassFreePool routine
description: The ChangerClassFreePool routine frees pool memory previously allocated using ChangerClassAllocatePool.
ms.assetid: 'c20c39f9-ceee-47f0-849a-f8686fb05e6a'
keywords: ["ChangerClassFreePool routine Storage Devices"]
topic_type:
- apiref
api_name:
- ChangerClassFreePool
api_location:
- Mcd.lib
- Mcd.dll
api_type:
- LibDef
---

# ChangerClassFreePool routine

The **ChangerClassFreePool** routine frees pool memory previously allocated using [**ChangerClassAllocatePool**](changerclassallocatepool.md).

## Syntax


```C++
VOID ChangerClassFreePool(
  _In_ PVOID PoolToFree
);
```



## Parameters

<dl> <dt>

*PoolToFree* \[in\]
</dt> <dd>

Pointer to the block of memory to be freed.

</dd> </dl>

## Return value

None

## Requirements



|                            |                                                                                                                |
|----------------------------|----------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                             |
| Header<br/>          | <dl> <dt>Mcd.h (include Mcd.h or Ntddchgr.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Mcd.lib</dt> </dl>                             |



## See also

<dl> <dt>

[**ChangerClassAllocatePool**](changerclassallocatepool.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ChangerClassFreePool%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






