---
title: STOR\_SCATTER\_GATHER\_ELEMENT structure
description: The STOR\_SCATTER\_GATHER\_ELEMENT structure is used with STOR\_SCATTER\_GATHER\_LIST to build a list of scatter/gather elements.
ms.assetid: '2e387418-a37c-492b-8ee4-b6ff8f0e53b0'
keywords: ["STOR_SCATTER_GATHER_ELEMENT structure Storage Devices", "PSTOR_SCATTER_GATHER_ELEMENT structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STOR_SCATTER_GATHER_ELEMENT
api_location:
- storport.h
api_type:
- HeaderDef
---

# STOR\_SCATTER\_GATHER\_ELEMENT structure

The STOR\_SCATTER\_GATHER\_ELEMENT structure is used with [**STOR\_SCATTER\_GATHER\_LIST**](stor-scatter-gather-list.md) to build a list of scatter/gather elements.

## Syntax


```C++
typedef struct _STOR_SCATTER_GATHER_ELEMENT {
  STOR_PHYSICAL_ADDRESS PhysicalAddress;
  ULONG                 Length;
  ULONG_PTR             Reserved;
} STOR_SCATTER_GATHER_ELEMENT, *PSTOR_SCATTER_GATHER_ELEMENT;
```



## Members

<dl> <dt>

**PhysicalAddress**
</dt> <dd>

Contains the physical address of the scatter/gather element.

</dd> <dt>

**Length**
</dt> <dd>

Contains the length in bytes of this scatter/gather element.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> </dl>

## Remarks

Miniport drivers used with the Storport driver retrieve an array of these structures using [**StorPortGetScatterGatherList**](storportgetscattergatherlist.md).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Storport.h (include Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**STOR\_SCATTER\_GATHER\_LIST**](stor-scatter-gather-list.md)
</dt> <dt>

[**StorPortGetScatterGatherList**](storportgetscattergatherlist.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STOR_SCATTER_GATHER_ELEMENT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






