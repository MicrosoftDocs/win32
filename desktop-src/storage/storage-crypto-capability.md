---
title: STORAGE\_CRYPTO\_CAPABILITY structure
description: Reserved for system use.
ms.assetid: 9DFAB3C6-F833-487D-87FC-292B3AFAD767
keywords:
- STORAGE_CRYPTO_CAPABILITY structure Storage Devices
- PSTORAGE_CRYPTO_CAPABILITY structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_CRYPTO_CAPABILITY
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# STORAGE\_CRYPTO\_CAPABILITY structure

Reserved for system use.

## Syntax


```C++
typedef struct _STORAGE_CRYPTO_CAPABILITY {
  ULONG                       Version;
  ULONG                       Size;
  ULONG                       CryptoCapabilityIndex;
  STORAGE_CRYPTO_ALGORITHM_ID AlgorithmId;
  STORAGE_CRYPTO_KEY_SIZE     KeySize;
  ULONG                       DataUnitSizeBitmask;
} STORAGE_CRYPTO_CAPABILITY, *PSTORAGE_CRYPTO_CAPABILITY;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

Reserved for system use.

</dd> <dt>

**Size**
</dt> <dd>

Reserved for system use.

</dd> <dt>

**CryptoCapabilityIndex**
</dt> <dd>

Reserved for system use.

</dd> <dt>

**AlgorithmId**
</dt> <dd>

Reserved for system use.

</dd> <dt>

**KeySize**
</dt> <dd>

Reserved for system use.

</dd> <dt>

**DataUnitSizeBitmask**
</dt> <dd>

Reserved for system use.

</dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_CRYPTO_CAPABILITY%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





