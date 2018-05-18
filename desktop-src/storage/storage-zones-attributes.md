---
title: STORAGE\_ZONES\_ATTRIBUTES enumeration
description: Note This structure is for internal use only and should not be called from your code. .
ms.assetid: '6C86A931-C87C-4273-9409-A45A3FDB8B4C'
keywords: ["STORAGE_ZONES_ATTRIBUTES enumeration Storage Devices", "PSTORAGE_ZONES_ATTRIBUTES enumeration pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STORAGE_ZONES_ATTRIBUTES
api_location:
- Ntddstor.h
api_type:
- HeaderDef
---

# STORAGE\_ZONES\_ATTRIBUTES enumeration

> [!Note]  
> This structure is for internal use only and should not be called from your code.

 

## Syntax


```C++
typedef enum _STORAGE_ZONES_ATTRIBUTES { 
  ZonesAttributeTypeAndLengthMayDifferent        = 0,
  ZonesAttributeTypeSameLengthSame               = 1,
  ZonesAttributeTypeSameLastZoneLengthDifferent  = 2,
  ZonesAttributeTypeMayDifferentLengthSame       = 3
} STORAGE_ZONES_ATTRIBUTES, *PSTORAGE_ZONES_ATTRIBUTES;
```



## Constants

<dl> <dt>

<span id="ZonesAttributeTypeAndLengthMayDifferent"></span><span id="zonesattributetypeandlengthmaydifferent"></span><span id="ZONESATTRIBUTETYPEANDLENGTHMAYDIFFERENT"></span>**ZonesAttributeTypeAndLengthMayDifferent**
</dt> <dd>

N/A

</dd> <dt>

<span id="ZonesAttributeTypeSameLengthSame"></span><span id="zonesattributetypesamelengthsame"></span><span id="ZONESATTRIBUTETYPESAMELENGTHSAME"></span>**ZonesAttributeTypeSameLengthSame**
</dt> <dd>

N/A

</dd> <dt>

<span id="ZonesAttributeTypeSameLastZoneLengthDifferent"></span><span id="zonesattributetypesamelastzonelengthdifferent"></span><span id="ZONESATTRIBUTETYPESAMELASTZONELENGTHDIFFERENT"></span>**ZonesAttributeTypeSameLastZoneLengthDifferent**
</dt> <dd>

N/A

</dd> <dt>

<span id="ZonesAttributeTypeMayDifferentLengthSame"></span><span id="zonesattributetypemaydifferentlengthsame"></span><span id="ZONESATTRIBUTETYPEMAYDIFFERENTLENGTHSAME"></span>**ZonesAttributeTypeMayDifferentLengthSame**
</dt> <dd>

N/A

</dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_ZONES_ATTRIBUTES%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





