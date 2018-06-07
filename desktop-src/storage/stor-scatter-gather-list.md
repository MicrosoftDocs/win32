---
title: STOR\_SCATTER\_GATHER\_LIST structure
description: The STOR\_SCATTER\_GATHER\_LIST structure is used in conjunction with the StorPortGetScatterGatherList routine to retrieve the scatter/gather list for a SCSI request block (SRB).
ms.assetid: 9fbb8dea-67d3-4bb9-afc2-d623bea2ca8d
keywords:
- STOR_SCATTER_GATHER_LIST structure Storage Devices
- PSTOR_SCATTER_GATHER_LIST structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STOR_SCATTER_GATHER_LIST
api_location:
- storport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# STOR\_SCATTER\_GATHER\_LIST structure

The STOR\_SCATTER\_GATHER\_LIST structure is used in conjunction with the [**StorPortGetScatterGatherList**](storportgetscattergatherlist.md) routine to retrieve the scatter/gather list for a SCSI request block (SRB).

## Syntax


```C++
typedef struct _STOR_SCATTER_GATHER_LIST {
  ULONG                       NumberOfElements;
  ULONG_PTR                   Reserved;
  STOR_SCATTER_GATHER_ELEMENT List[];
} STOR_SCATTER_GATHER_LIST, *PSTOR_SCATTER_GATHER_LIST;
```



## Members

<dl> <dt>

**NumberOfElements**
</dt> <dd>

Contains the number of scatter/gather elements in the list.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> <dt>

**List**
</dt> <dd>

Contains the array of scatter/gather elements.

</dd> </dl>

## Remarks

Miniport drivers that work with the Storport driver call the Storport support routine, [**StorPortGetScatterGatherList**](storportgetscattergatherlist.md), to retrieve the scatter gather list for an SRB. **StorPortGetScatterGatherList** returns a structure of type STOR\_SCATTER\_GATHER\_LIST. Each scatter/gather element is of type [**STOR\_SCATTER\_GATHER\_ELEMENT**](stor-scatter-gather-element.md).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Storport.h (include Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**STOR\_SCATTER\_GATHER\_ELEMENT**](stor-scatter-gather-element.md)
</dt> <dt>

[**StorPortGetScatterGatherList**](storportgetscattergatherlist.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STOR_SCATTER_GATHER_LIST%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






