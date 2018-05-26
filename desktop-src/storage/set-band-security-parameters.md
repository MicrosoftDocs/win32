---
title: SET\_BAND\_SECURITY\_PARAMETERS structure
description: The parameters to set security properties for a band on a storage device for a IOCTL\_EHSTOR\_BANDMGMT\_SET\_BAND\_SECURITY request are specified in a SET\_BAND\_SECURITY\_PARAMETERS structure.
ms.assetid: D1703D6F-A453-4E3E-8705-344469D61412
keywords:
- SET_BAND_SECURITY_PARAMETERS structure Storage Devices
- PSET_BAND_SECURITY_PARAMETERS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SET_BAND_SECURITY_PARAMETERS
api_location:
- EhStorBandMgmt.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SET\_BAND\_SECURITY\_PARAMETERS structure

The parameters to set security properties for a band on a storage device for a [**IOCTL\_EHSTOR\_BANDMGMT\_SET\_BAND\_SECURITY**](ioctl-ehstor-bandmgmt-set-band-security.md) request are specified in a **SET\_BAND\_SECURITY\_PARAMETERS** structure.

## Syntax


```C++
typedef struct _SET_BAND_SECURITY_PARAMETERS {
  ULONG         StructSize;
  ULONG         Flags;
  ULONG         BandId;
  LARGE_INTEGER BandStart;
  ULONG         CurrentAuthKeyOffset;
  ULONG         NewAuthKeyOffset;
                BandSecurityInfoOffset;
} SET_BAND_SECURITY_PARAMETERS, *PSET_BAND_SECURITY_PARAMETERS;
```



## Members

<dl> <dt>

**StructSize**
</dt> <dd>

The size of this structure in bytes. Set to **sizeof**(SET\_BAND\_SECURITY\_PARAMETERS).

</dd> <dt>

**Flags**
</dt> <dd>

Security parameter flags. This value is a bitwise OR combination of the following.



| Value                                                                                                                                                                                                                          | Meaning                                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| <span id="SETBANDSEC_AUTHKEY_CACHING_ENABLED"></span><span id="setbandsec_authkey_caching_enabled"></span><dl> <dt>**SETBANDSEC\_AUTHKEY\_CACHING\_ENABLED**</dt> </dl> | The new authentication key can be cached to automate some band operations.<br/> |



 

</dd> <dt>

**BandId**
</dt> <dd>

The identifier of a single band to return information for. **BandSize** must be 0 when a single band is selected with **BandId.** To use **BandStart** and **BandSize** instead of **BandId** to select a band, set **BandId** = (ULONG)  1.

</dd> <dt>

**BandStart**
</dt> <dd>

The starting byte location on the storage device to begin a band search. An attempt is made to match a band at or after **BandStart**.

</dd> <dt>

**CurrentAuthKeyOffset**
</dt> <dd>

The offset, in bytes, of an **AUTH\_KEY** structure containing the current authentication key for the band. This authentication key is required and must be present following this structure. The offset is from the beginning of **SET\_BAND\_SECURITY\_PARAMETERS**. **AUTH\_KEY** is declared in *ehstorbandmgmt.h* as the following.


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

A variable-length byte array containing the key data.

</dd> </dl>

To specify a default authentication key to the band, set **AuthKeyOffset** = **EHSTOR\_BANDMGR\_NO\_KEY**.

</dd> <dt>

**NewAuthKeyOffset**
</dt> <dd>

The offset, in bytes, of an **AUTH\_KEY** structure containing the new authentication key for the band. The offset is from the beginning of **SET\_BAND\_SECURITY\_PARAMETERS**. **AUTH\_KEY** is declared in *ehstorbandmgmt.h* as the following.


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

A variable-length byte array that contains the key data.

</dd> </dl>

To assign a default authentication key to the band, set **AuthKeyOffset** = **EHSTOR\_BANDMGR\_NO\_KEY**. If **NewAuthKeyOffset** == **CurrentAuthKeyOffset**, the authentication key for the band is left unchanged.

</dd> <dt>

**BandSecurityInfoOffset**
</dt> <dd>

The offset, in bytes, of a [**BAND\_SECURITY\_INFO**](band-security-info.md) structure. The offset is from the beginning of **SET\_BAND\_SECURITY\_PARAMETERS**.

</dd> </dl>

## Remarks

Precedence is given to **BandID** for band selection. If **BandID** is greater than 0 and **BandID** is less than the **MaxBandCount** member of [**BAND\_MANAGEMENT\_CAPABILITIES**](band-management-capabilities.md), then **BandID** is used as the only selection criteria for a band match. If **BandID** ==  1, then **BandStart** is used as the match criteria to select a band. If no band matches either selection criteria, then STATUS\_INVALID\_PARAMETER is returned in the *IoStatus* block for [**IOCTL\_EHSTOR\_BANDMGMT\_SET\_BAND\_SECURITY**](ioctl-ehstor-bandmgmt-set-band-security.md).

If **BandID** and **BandStart** are both set to  1, then the [**IOCTL\_EHSTOR\_BANDMGMT\_SET\_BAND\_SECURITY**](ioctl-ehstor-bandmgmt-set-band-security.md) request will change the properties of the global band.

**NewAuthKeyOffset** and **BandSecurityInfoOffset** are optional depending on the requirements of the operation. If only the authentication key is changed, then **NewAuthKeyOffset** is set to the location of the **AUTH\_KEY** structure for the new key and **BandSecurityInfoOffset** is set to zero. Similarly, if only security properties are changed, **BandSecurityInfoOffset** is set to the location of [**BAND\_SECURITY\_INFO**](band-security-info.md) and **NewAuthKeyOffset** is set to 0.

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

[**BAND\_MANAGEMENT\_CAPABILITIES**](band-management-capabilities.md)
</dt> <dt>

[**IOCTL\_EHSTOR\_BANDMGMT\_SET\_BAND\_LOCATION**](ioctl-ehstor-bandmgmt-set-band-location.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SET_BAND_SECURITY_PARAMETERS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






