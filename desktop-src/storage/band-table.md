---
title: BAND\_TABLE structure
description: The BAND\_TABLE structure contains the table of bands returned from an IOCTL\_EHSTOR\_BANDMGMT\_ENUMERATE\_BANDS request.
ms.assetid: '2714E346-6BDD-49EF-9820-6B82F8F29380'
keywords: ["BAND_TABLE structure Storage Devices", "PBAND_TABLE structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- BAND_TABLE
api_location:
- EhStorBandMgmt.h
api_type:
- HeaderDef
---

# BAND\_TABLE structure

The **BAND\_TABLE** structure contains the table of bands returned from an [**IOCTL\_EHSTOR\_BANDMGMT\_ENUMERATE\_BANDS**](ioctl-ehstor-bandmgmt-enumerate-bands.md) request. The bands in the band table are selected by a match condition sent as input for **IOCTL\_EHSTOR\_BANDMGMT\_ENUMERATE\_BANDS** in the [**ENUMERATE\_BANDS\_PARAMETERS**](enumerate-bands-parameters.md) structure.

## Syntax


```C++
typedef struct _BAND_TABLE {
  ULONG StructSize;
  ULONG BandTableOffset;
  ULONG BandTableEntryCount;
  ULONG BandTableEntrySize;
} BAND_TABLE, *PBAND_TABLE;
```



## Members

<dl> <dt>

**StructSize**
</dt> <dd>

The size of this structure in bytes. Set to **sizeof**(BAND\_TABLE).

</dd> <dt>

**BandTableOffset**
</dt> <dd>

The offset, in bytes, to the start of an array of [**BAND\_TABLE\_ENTRY**](band-table-entry.md) structures.

</dd> <dt>

**BandTableEntryCount**
</dt> <dd>

The number of [**BAND\_TABLE\_ENTRY**](band-table-entry.md) returned in the array at **BandTableOffset**.

</dd> <dt>

**BandTableEntrySize**
</dt> <dd>

The size of each entry, in bytes, in the array at **BandTableOffset**. Instead of using the value of **sizeof**(BAND\_TABLE\_ENTRY), callers must use **BandTableEntrySize** when advancing to the next element in the band table array.

</dd> </dl>

## Requirements



|                    |                                                                                                                        |
|--------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8<br/>                                                                           |
| Header<br/>  | <dl> <dt>EhStorBandMgmt.h (include EhStorBandMgmt.h)</dt> </dl> |



## See also

<dl> <dt>

[**BAND\_TABLE\_ENTRY**](band-table-entry.md)
</dt> <dt>

[**ENUMERATE\_BANDS\_PARAMETERS**](enumerate-bands-parameters.md)
</dt> <dt>

[**IOCTL\_EHSTOR\_BANDMGMT\_ENUMERATE\_BANDS**](ioctl-ehstor-bandmgmt-enumerate-bands.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20BAND_TABLE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






