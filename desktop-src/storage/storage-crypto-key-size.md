---
title: STORAGE\_CRYPTO\_KEY\_SIZE enumeration
description: The STORAGE\_CRYPTO\_KEY\_SIZE enum returns the Size of the key in bits.
ms.assetid: C3E5CEC6-34A2-48DF-B963-677C69A97E0B
keywords:
- STORAGE_CRYPTO_KEY_SIZE enumeration Storage Devices
- STORAGE_CRYPTO_KEY_SIZE, PSTORAGE_CRYPTO_KEY_SIZE enumeration Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_CRYPTO_KEY_SIZE, PSTORAGE_CRYPTO_KEY_SIZE
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# STORAGE\_CRYPTO\_KEY\_SIZE enumeration

The **STORAGE\_CRYPTO\_KEY\_SIZE** enum returns the Size of the key in bits.

## Syntax


```C++
typedef enum _STORAGE_CRYPTO_KEY_SIZE { 
  StorageCryptoKeySizeUnknown  = 0,
  StorageCryptoKeySize128Bits  = 1,
  StorageCryptoKeySize192Bits,
  StorageCryptoKeySize256Bits,
  StorageCryptoKeySize512Bits
} STORAGE_CRYPTO_KEY_SIZE, *PSTORAGE_CRYPTO_KEY_SIZE;
```



## Constants

<dl> <dt>

<span id="StorageCryptoKeySizeUnknown"></span><span id="storagecryptokeysizeunknown"></span><span id="STORAGECRYPTOKEYSIZEUNKNOWN"></span>**StorageCryptoKeySizeUnknown**
</dt> <dd>

Reserved for system use.

</dd> <dt>

<span id="StorageCryptoKeySize128Bits"></span><span id="storagecryptokeysize128bits"></span><span id="STORAGECRYPTOKEYSIZE128BITS"></span>**StorageCryptoKeySize128Bits**
</dt> <dd>

Reserved for system use.

</dd> <dt>

<span id="StorageCryptoKeySize192Bits"></span><span id="storagecryptokeysize192bits"></span><span id="STORAGECRYPTOKEYSIZE192BITS"></span>**StorageCryptoKeySize192Bits**
</dt> <dd>

Reserved for system use.

</dd> <dt>

<span id="StorageCryptoKeySize256Bits"></span><span id="storagecryptokeysize256bits"></span><span id="STORAGECRYPTOKEYSIZE256BITS"></span>**StorageCryptoKeySize256Bits**
</dt> <dd>

Reserved for system use.

</dd> <dt>

<span id="StorageCryptoKeySize512Bits"></span><span id="storagecryptokeysize512bits"></span><span id="STORAGECRYPTOKEYSIZE512BITS"></span>**StorageCryptoKeySize512Bits**
</dt> <dd>

Reserved for system use.

</dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_CRYPTO_KEY_SIZE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





