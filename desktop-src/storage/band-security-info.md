---
title: BAND\_SECURITY\_INFO structure
description: The BAND\_SECURITY\_INFO structure specifies the security information for a band table entry query.
ms.assetid: 310F996F-F350-4F25-BC8A-386513908557
keywords:
- BAND_SECURITY_INFO structure Storage Devices
- BAND_LOCATION_INFO structure Storage Devices
- PBAND_LOCATION_INFO structure pointer Storage Devices
topic_type:
- apiref
api_name:
- BAND_LOCATION_INFO
api_location:
- EhStorBandMgmt.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# BAND\_SECURITY\_INFO structure

The **BAND\_SECURITY\_INFO** structure specifies the security information for a band table entry query.

## Syntax


```C++
typedef struct _BAND_LOCATION_INFO {
  ULONG      StructSize;
  LOCKSTATE  ReadLock;
  LOCKSTATE  WriteLock;
  ALGOIDTYPE CryptoAlgoIdType;
  union {
    struct {
      ULONG Offset;
      ULONG Length;
    } CryptoAlgoOidString;
    ULONG  CryptoAlgoNumericId;
  };
  BYTE       Metadata[32];
} BAND_LOCATION_INFO, *PBAND_LOCATION_INFO;
```



## Members

<dl> <dt>

**StructSize**
</dt> <dd>

The size of the structure in bytes. Set to **sizeof**(BAND\_SECURITY\_INFO).

</dd> <dt>

**ReadLock**
</dt> <dd>

Whether the band is accessible for reading and how a read lock is affected by a power reset.

</dd> <dt>

**WriteLock**
</dt> <dd>

Whether the band is accessible for writing and how a write lock is affected by a power reset.

</dd> <dt>

**CryptoAlgoIdType**
</dt> <dd>

The type of encryption algorithm identifier used. This must be set to **AlgoIdTypeOidString**.

</dd> <dt>

**CryptoAlgoOidString**
</dt> <dd>

The encryption algorithm used to protect the data in the band.

<dl> <dt>

**Offset**
</dt> <dd>

The offset from the beginning of this structure where the encryption algorithm OID string begins.

</dd> <dt>

**Length**
</dt> <dd>

The length of the OID string identifying the encryption algorithm. This is a byte-length value including a NULL terminator for the OID string.

</dd> </dl> </dd> <dt>

**CryptoAlgoNumericId**
</dt> <dd>

Reserved.

</dd> <dt>

**Metadata**
</dt> <dd>

A metadata field available for use by a key manager.

</dd> </dl>

## Remarks

Both **Readlock** and **Writelock** are **LOCKSTATE** values and indicate locking state and lock persistence. Their values are one of the following.



| Lock State            | Description                                                     |
|-----------------------|-----------------------------------------------------------------|
| INVALID\_LOCK\_STATE  | The lock state is not valid.                                    |
| PERSISTENT\_UNLOCK    | The device is unlocked and remains unlocked during power reset. |
| NONPERSISTENT\_UNLOCK | The device is unlocked but becomes locked during power reset.   |
| PERSISTENT\_LOCK      | The device is locked and remains locked during power reset.     |



 

**CryptoAlgoOidString** specifies the data encryption algorithm only if **ENUMBANDS\_REPORT\_CRYPTO\_ALGO** is set in the **Flags** member of [**ENUMERATE\_BANDS\_PARAMETERS**](enumerate-bands-parameters.md) in an [**IOCTL\_EHSTOR\_BANDMGMT\_ENUMERATE\_BANDS**](ioctl-ehstor-bandmgmt-enumerate-bands.md) request. Otherwise, both **CryptoAlgoOidString.Offset** and **CryptoAlgoOidString.Length** are set to 0. The following are possible encryption algorithm OID strings returned for **CryptoAlgoOidString**.



| Algorithm   | OID                     |
|-------------|-------------------------|
| IAES128-ECB | 2.16.840.1.101.3.4.1.1  |
| AES128-CBC  | 2.16.840.1.101.3.4.1.2. |
| AES128-OFB  | 2.16.840.1.101.3.4.1.3  |
| AES128-CFB  | 2.16.840.1.101.3.4.1.4  |
| AES128-XTS  | 1.3.111.2.1619.0.1.1    |
| AES256-ECB  | 2.16.840.1.101.3.4.1.41 |
| AES256-CBC  | 2.16.840.1.101.3.4.1.42 |
| AES256-OFB  | 2.16.840.1.101.3.4.1.43 |
| AES256-CFB  | 2.16.840.1.101.3.4.1.44 |
| AES256-XTS  | 1.3.111.2.1619.0.1.2    |



 

When **BAND\_SECURITY\_INFO** is used in an input parameter set, **CryptoAlgoIdType** and **CryptoAlgoOidString** are not used and must be set to 0.

## Requirements



|                    |                                                                                                                        |
|--------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8<br/>                                                                           |
| Header<br/>  | <dl> <dt>EhStorBandMgmt.h (include EhStorBandMgmt.h)</dt> </dl> |



## See also

<dl> <dt>

[**BAND\_TABLE\_ENTRY**](band-table-entry.md)
</dt> <dt>

[**ENUMERATE\_BANDS\_PARAMETERS**](enumerate-bands-parameters.md)
</dt> <dt>

[**IOCTL\_EHSTOR\_BANDMGMT\_CREATE\_BAND**](ioctl-ehstor-bandmgmt-create-band.md)
</dt> <dt>

[**IOCTL\_EHSTOR\_BANDMGMT\_ENUMERATE\_BANDS**](ioctl-ehstor-bandmgmt-enumerate-bands.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20BAND_SECURITY_INFO%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






