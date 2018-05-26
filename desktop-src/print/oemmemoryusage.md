---
Description: The OEMMEMORYUSAGE structure is used as an input parameter to a rendering plug-ins IPrintOemUniMemoryUsage method.
ms.assetid: a7a522b8-7aa2-45b6-9200-407471dca82f
title: OEMMEMORYUSAGE structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# OEMMEMORYUSAGE structure

The OEMMEMORYUSAGE structure is used as an input parameter to a rendering plug-in's [**IPrintOemUni::MemoryUsage**](iprintoemuni-memoryusage.md) method.

## Syntax


```C++
typedef struct {
  DWORD dwFixedMemoryUsage;
  DWORD dwPercentMemoryUsage;
  DWORD dwMaxBandSize;
} OEMMEMORYUSAGE, *POEMMEMORYUSAGE;
```



## Members

<dl> <dt>

**dwFixedMemoryUsage**
</dt> <dd>

Specifies the amount, in bytes, of fixed-sized memory required by the **IPrintOemUni::MemoryUsage** method. Supplied by the rendering plug-in.

</dd> <dt>

**dwPercentMemoryUsage**
</dt> <dd>

Specifies the amount of variably-sized memory required by the **IPrintOemUni::MemoryUsage** method, expressed as a percentage of the size of the source bitmap received by [**IPrintOemUni::ImageProcessing**](iprintoemuni-imageprocessing.md). Supplied by the rendering plug-in.

</dd> <dt>

**dwMaxBandSize**
</dt> <dd>

Specifies the maximum size, in bytes, that can be used for source bitmaps. This is the value that Unidrv uses to subtract from when applying the plug-in supplied values contained in **dwFixedMemoryUsage** and **dwPercentMemoryUsage**. Supplied by Unidrv.

</dd> </dl>

## Remarks

The Unidrv driver uses the values in the **dwFixedMemoryUsage** and **dwPercentMemoryUsage** members of this structure to determine the optimum size for a GDI drawing surface, taking into account any memory requirements of a rendering plug-in's **IPrintOemUni::ImageProcessing** method. For more information about how these members are used, see the Remarks section in [**IPrintOemUni::MemoryUsage**](iprintoemuni-memoryusage.md).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemUni::ImageProcessing**](iprintoemuni-imageprocessing.md)
</dt> <dt>

[**IPrintOemUni::MemoryUsage**](iprintoemuni-memoryusage.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20OEMMEMORYUSAGE%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





