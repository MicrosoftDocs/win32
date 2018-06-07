---
title: STORAGE\_CRYPTO\_ALGORITHM\_ID enumeration
description: The STORAGE\_CRYPTO\_ALGORITHM\_ID enum provides an output buffer for StorageAdapterCryptoProperty and PropertyStandardQuery.
ms.assetid: 5D1CCF3D-D677-47B0-9C7B-7E35C649A7D5
keywords:
- STORAGE_CRYPTO_ALGORITHM_ID enumeration Storage Devices
- STORAGE_CRYPTO_ALGORITHM_ID, PSTORAGE_CRYPTO_ALGORITHM_ID enumeration Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_CRYPTO_ALGORITHM_ID, PSTORAGE_CRYPTO_ALGORITHM_ID
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

# STORAGE\_CRYPTO\_ALGORITHM\_ID enumeration

The **STORAGE\_CRYPTO\_ALGORITHM\_ID** enum provides an output buffer for **StorageAdapterCryptoProperty** and **PropertyStandardQuery**.

## Syntax


```C++
typedef enum _STORAGE_CRYPTO_ALGORITHM_ID { 
  StorageCryptoAlgorithmUnknown          = 0,
  StorageCryptoAlgorithmXTSAES           = 1,
  StorageCryptoAlgorithmBitlockerAESCBC,
  StorageCryptoAlgorithmAESECB,
  StorageCryptoAlgorithmESSIVAESCBC,
  StorageCryptoAlgorithmMax
} STORAGE_CRYPTO_ALGORITHM_ID, *PSTORAGE_CRYPTO_ALGORITHM_ID;
```



## Constants

<dl> <dt>

<span id="StorageCryptoAlgorithmUnknown"></span><span id="storagecryptoalgorithmunknown"></span><span id="STORAGECRYPTOALGORITHMUNKNOWN"></span>**StorageCryptoAlgorithmUnknown**
</dt> <dd>

Reserved for system use.

</dd> <dt>

<span id="StorageCryptoAlgorithmXTSAES"></span><span id="storagecryptoalgorithmxtsaes"></span><span id="STORAGECRYPTOALGORITHMXTSAES"></span>**StorageCryptoAlgorithmXTSAES**
</dt> <dd>

Reserved for system use.

</dd> <dt>

<span id="StorageCryptoAlgorithmBitlockerAESCBC"></span><span id="storagecryptoalgorithmbitlockeraescbc"></span><span id="STORAGECRYPTOALGORITHMBITLOCKERAESCBC"></span>**StorageCryptoAlgorithmBitlockerAESCBC**
</dt> <dd>

Reserved for system use.

</dd> <dt>

<span id="StorageCryptoAlgorithmAESECB"></span><span id="storagecryptoalgorithmaesecb"></span><span id="STORAGECRYPTOALGORITHMAESECB"></span>**StorageCryptoAlgorithmAESECB**
</dt> <dd>

Reserved for system use.

</dd> <dt>

<span id="StorageCryptoAlgorithmESSIVAESCBC"></span><span id="storagecryptoalgorithmessivaescbc"></span><span id="STORAGECRYPTOALGORITHMESSIVAESCBC"></span>**StorageCryptoAlgorithmESSIVAESCBC**
</dt> <dd>

Reserved for system use.

</dd> <dt>

<span id="StorageCryptoAlgorithmMax"></span><span id="storagecryptoalgorithmmax"></span><span id="STORAGECRYPTOALGORITHMMAX"></span>**StorageCryptoAlgorithmMax**
</dt> <dd>

Reserved for system use.

</dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_CRYPTO_ALGORITHM_ID%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





