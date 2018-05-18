---
title: DELETE\_BAND\_PARAMETERS structure
description: A configured band is deleted according to the parameters in a DELETE\_BAND\_PARAMETERS structure. This structure is input for an IOCTL\_EHSTOR\_BANDMGMT\_DELETE\_BAND request.
ms.assetid: '6C96CF49-A7B2-4A99-8C7A-FC1C8C389C18'
keywords: ["DELETE_BAND_PARAMETERS structure Storage Devices", "PDELETE_BAND_PARAMETERS structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- DELETE_BAND_PARAMETERS
api_location:
- EhStorBandMgmt.h
api_type:
- HeaderDef
---

# DELETE\_BAND\_PARAMETERS structure

A configured band is deleted according to the parameters in a **DELETE\_BAND\_PARAMETERS** structure. This structure is input for an [**IOCTL\_EHSTOR\_BANDMGMT\_DELETE\_BAND**](ioctl-ehstor-bandmgmt-delete-band.md) request.

## Syntax


```C++
typedef struct _DELETE_BAND_PARAMETERS {
  ULONG         StructSize;
  ULONG         Flags;
  ULONG         Reserved;
  ULONG         BandId;
  LARGE_INTEGER BandStart;
  ULONG         AuthKeyOffset;
} DELETE_BAND_PARAMETERS, *PDELETE_BAND_PARAMETERS;
```



## Members

<dl> <dt>

**StructSize**
</dt> <dd>

The size of this structure in bytes. Set to **sizeof**(DELETE\_BAND\_PARAMETERS).

</dd> <dt>

**Flags**
</dt> <dd>

Delete operation flags. This value is a bitwise OR combination of the following.



| Value                                                                                                                                                                                                     | Meaning                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| <span id="DELBAND_ERASE_BEFORE_DELETE"></span><span id="delband_erase_before_delete"></span><dl> <dt>**DELBAND\_ERASE\_BEFORE\_DELETE**</dt> </dl> | Perform a cryptographic erase of the band property data before delete.<br/> |



 

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> <dt>

**BandId**
</dt> <dd>

The identifier of a single band to return information for. **BandSize** must be 0 when a single band is selected with **BandId**. To use **BandStart** and **BandSize** instead of **BandId** to select a band, set **BandId** = (ULONG) –1.

</dd> <dt>

**BandStart**
</dt> <dd>

The starting byte location on the storage device to begin a band search. An attempt is made to match a band at or after **BandStart**.

</dd> <dt>

**AuthKeyOffset**
</dt> <dd>

The offset, in bytes, of an **AUTH\_KEY** structure containing the authorization key for the band. The offset is from the beginning of **DELETE\_BAND\_PARAMETERS**. **AUTH\_KEY** is declared in *ehstorbandmgmt.h* as the following.


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

To specify a default authentication key to the band, set **AuthKeyOffset** = **EHSTOR\_BANDMGR\_NO\_KEY**. If **Flags** contains **DELBAND\_ERASE\_BEFORE\_DELETE**, **AuthKeyOffset** must be set to **EHSTOR\_BANDMGR\_NO\_KEY**.

</dd> </dl>

## Remarks

Precedence is given to **BandID** for band selection. If **BandID** is greater than 0 and **BandID** is less than the **MaxBandCount** member of [**BAND\_MANAGEMENT\_CAPABILITIES**](band-management-capabilities.md), then **BandID** is used as the only selection criteria for a band match. If **BandID** == –1, then **BandStart** is used as the match criteria to select a band. If no band matches either selection criteria, then STATUS\_INVALID\_PARAMETER is returned in the *IoStatus* block for [**IOCTL\_EHSTOR\_BANDMGMT\_DELETE\_BAND**](ioctl-ehstor-bandmgmt-delete-band.md).

If **DELBAND\_ERASE\_BEFORE\_DELETE** is set in **Flags**, then an authentication key is not needed to delete the band. If this flag is not set, the current authentication key must be included at **AuthKeyOffset**.

.

## Requirements



|                    |                                                                                                                        |
|--------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8<br/>                                                                           |
| Header<br/>  | <dl> <dt>EhStorBandMgmt.h (include EhStorBandMgmt.h)</dt> </dl> |



## See also

<dl> <dt>

[**BAND\_MANAGEMENT\_CAPABILITIES**](band-management-capabilities.md)
</dt> <dt>

[**IOCTL\_EHSTOR\_BANDMGMT\_DELETE\_BAND**](ioctl-ehstor-bandmgmt-delete-band.md)
</dt> <dt>

[**IOCTL\_EHSTOR\_BANDMGMT\_ERASE\_BAND**](ioctl-ehstor-bandmgmt-erase-band.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DELETE_BAND_PARAMETERS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






