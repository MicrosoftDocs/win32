---
title: STORAGE\_CRYPTO\_DESCRIPTOR structure
description: Reserved for system use.
ms.assetid: 1D948882-2286-4080-A41B-D20714FC0A66
keywords:
- STORAGE_CRYPTO_DESCRIPTOR structure Storage Devices
- PSTORAGE_CRYPTO_DESCRIPTOR structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_CRYPTO_DESCRIPTOR
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

# STORAGE\_CRYPTO\_DESCRIPTOR structure

Reserved for system use.

## Syntax


```C++
typedef struct _STORAGE_CRYPTO_DESCRIPTOR {
  DWORD                                                          Version;
  DWORD                                                          Size;
  DWORD                                                          NumKeysSupported;
  DWORD                                                          NumCryptoCapabilities;
   _Field_size_(NumCryptoCapabilities) STORAGE_CRYPTO_CAPABILITY CryptoCapabilities[ANYSIZE_ARRAY];
} STORAGE_CRYPTO_DESCRIPTOR, *PSTORAGE_CRYPTO_DESCRIPTOR;
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

**NumKeysSupported**
</dt> <dd>

Reserved for system use.

</dd> <dt>

**NumCryptoCapabilities**
</dt> <dd>

Reserved for system use.

</dd> <dt>

**CryptoCapabilities**
</dt> <dd>

Reserved for system use.

</dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_CRYPTO_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





