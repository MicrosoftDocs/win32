---
title: CREATE\_BAND\_PARAMETERS structure
description: The parameters to create a band on a storage device for an IOCTL\_EHSTOR\_BANDMGMT\_CREATE\_BAND request are specified in a CREATE\_BAND\_PARAMETERS structure.
ms.assetid: DFDD92F8-95B7-40F7-950C-A105F035B2E9
keywords:
- CREATE_BAND_PARAMETERS structure Storage Devices
- PCREATE_BAND_PARAMETERS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- CREATE_BAND_PARAMETERS
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

# CREATE\_BAND\_PARAMETERS structure

The parameters to create a band on a storage device for an [**IOCTL\_EHSTOR\_BANDMGMT\_CREATE\_BAND**](ioctl-ehstor-bandmgmt-create-band.md) request are specified in a **CREATE\_BAND\_PARAMETERS** structure.

## Syntax


```C++
typedef struct _CREATE_BAND_PARAMETERS {
  ULONG StructSize;
  ULONG Flags;
  ULONG BandLocationInfoOffset;
  ULONG BandSecurityInfoOffset;
  ULONG AuthKeyOffset;
} CREATE_BAND_PARAMETERS, *PCREATE_BAND_PARAMETERS;
```



## Members

<dl> <dt>

**StructSize**
</dt> <dd>

The size of this structure in bytes. Set to **sizeof**(CREATE\_BAND\_PARAMETERS).

</dd> <dt>

**Flags**
</dt> <dd>

Band creation flags. This value is a bitwise OR combination of the following.



| Value                                                                                                                                                                                                                          | Meaning                                                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="CREATEBAND_AUTHKEY_CACHING_ENABLED"></span><span id="createband_authkey_caching_enabled"></span><dl> <dt>**CREATEBAND\_AUTHKEY\_CACHING\_ENABLED**</dt> </dl> | The authentication key for this band is cached, which allows automation of later operations. The authentication key is cached when this flag is set and the band is not locked for both reading and writing.<br/> |



 

</dd> <dt>

**BandLocationInfoOffset**
</dt> <dd>

The offset, in bytes, of a [**BAND\_LOCATION\_INFO**](band-location-info.md) structure. The offset is from the beginning of **CREATE\_BAND\_PARAMETERS**.

</dd> <dt>

**BandSecurityInfoOffset**
</dt> <dd>

The offset, in bytes, of a [**BAND\_SECURITY\_INFO**](band-security-info.md) structure. The offset is from the beginning of **CREATE\_BAND\_PARAMETERS**. If this value is 0, meaning band security info is not present, key manager metadata for the band is set to all zeros. Also, when this member is 0, the read and write lock states default to PERSISTANT\_UNLOCK.

</dd> <dt>

**AuthKeyOffset**
</dt> <dd>

The offset, in bytes, of an **AUTH\_KEY** structure that contains the authorization key for the new band. The offset is from the beginning of **CREATE\_BAND\_PARAMETERS**. **AUTH\_KEY** is declared in *ehstorbandmgmt.h* as the following.


```
typedef struct _AUTH_KEY
{
    ULONG   KeySize;
    UCHAR   Key[ANYSIZE_ARRAY];
} AUTH_KEY;
```



<dl> <dt>

<span id="KeySize"></span><span id="keysize"></span><span id="KEYSIZE"></span>KeySize
</dt> <dd>

The size of the key, in bytes, of the key data at **Key**. If **KeySize** is set to 0, a default key is used.

</dd> <dt>

<span id="Key"></span><span id="key"></span><span id="KEY"></span>Key
</dt> <dd>

A variable length byte array that contains the key data.

</dd> </dl>

To assign a default authorization key to the band, set **AuthKeyOffset** = **EHSTOR\_BANDMGR\_NO\_KEY**.

</dd> </dl>

## Remarks

The **CryptoAlgoIdType** and **CryptoAlgoOidString** members of the [**BAND\_SECURITY\_INFO**](band-security-info.md) structure at **BandSecurityInfoOffset** are not used in a band creation request and must be set to 0.

## Requirements



|                    |                                                                                                                        |
|--------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8<br/>                                                                           |
| Header<br/>  | <dl> <dt>EhStorBandMgmt.h (include EhStorBandMgmt.h)</dt> </dl> |



## See also

<dl> <dt>

[**BAND\_LOCATION\_INFO**](band-location-info.md)
</dt> <dt>

[**BAND\_SECURITY\_INFO**](band-security-info.md)
</dt> <dt>

[**IOCTL\_EHSTOR\_BANDMGMT\_CREATE\_BAND**](ioctl-ehstor-bandmgmt-create-band.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CREATE_BAND_PARAMETERS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






