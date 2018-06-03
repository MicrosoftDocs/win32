---
title: SetCHAPSharedSecret\_IN structure
description: The SetCHAPSharedSecret\_IN structure holds the input data for the SetCHAPSharedSecret method.
ms.assetid: d352785b-982f-4469-bee8-6274c0ce1cd6
keywords:
- SetCHAPSharedSecret_IN structure Storage Devices
- PSetCHAPSharedSecret_IN structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SetCHAPSharedSecret_IN
api_location:
- iscsiop.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# SetCHAPSharedSecret\_IN structure

The SetCHAPSharedSecret\_IN structure holds the input data for the [SetCHAPSharedSecret](https://msdn.microsoft.com/library/windows/hardware/ff565585) method.

## Syntax


```C++
typedef struct _SetCHAPSharedSecret_IN {
  ULONG SharedSecretSize;
  UCHAR SharedSecret[1];
} SetCHAPSharedSecret_IN, *PSetCHAPSharedSecret_IN;
```



## Members

<dl> <dt>

**SharedSecretSize**
</dt> <dd>

The size, in bytes, of the shared secret.

</dd> <dt>

**SharedSecret**
</dt> <dd>

A variable-length array that contains the shared secret.

</dd> </dl>

## Remarks

You must implement this method.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiop.h (include Iscsiop.h)</dt> </dl> |



## See also

<dl> <dt>

[SetCHAPSharedSecret](https://msdn.microsoft.com/library/windows/hardware/ff565585)
</dt> <dt>

[**SetCHAPSharedSecret\_OUT**](setchapsharedsecret-out.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SetCHAPSharedSecret_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






