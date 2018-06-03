---
title: CHANGER\_ELEMENT\_LIST structure
description: The CHANGER\_ELEMENT\_LIST structure indicates a range of elements of a single type.
ms.assetid: 6e85eaa7-d622-4b05-9efd-c1b6b7789c03
keywords:
- CHANGER_ELEMENT_LIST structure Storage Devices
- PCHANGER_ELEMENT_LIST structure pointer Storage Devices
topic_type:
- apiref
api_name:
- CHANGER_ELEMENT_LIST
api_location:
- ntddchgr.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# CHANGER\_ELEMENT\_LIST structure

The CHANGER\_ELEMENT\_LIST structure indicates a range of elements of a single type.

## Syntax


```C++
typedef struct _CHANGER_ELEMENT_LIST {
  CHANGER_ELEMENT Element;
  ULONG           NumberOfElements;
} CHANGER_ELEMENT_LIST, *PCHANGER_ELEMENT_LIST;
```



## Members

<dl> <dt>

**Element**
</dt> <dd>

Describes the first element of type [**CHANGER\_ELEMENT**](changer-element.md) in a range **NumberOfElements** long.

</dd> <dt>

**NumberOfElements**
</dt> <dd>

Specifies the number of elements in the range.

</dd> </dl>

## Remarks

A changer class driver uses CHANGER\_ELEMENT\_LIST to indicate a range of elements of a single type, typically for an operation such as getting or initializing the status of multiple elements.

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddchgr.h</dt> </dl> |



## See also

<dl> <dt>

[**CHANGER\_ELEMENT**](changer-element.md)
</dt> <dt>

[**ChangerGetElementStatus**](changergetelementstatus.md)
</dt> <dt>

[**ChangerInitializeElementStatus**](changerinitializeelementstatus.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CHANGER_ELEMENT_LIST%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






