---
Description: 'The IPrintOemUni::MemoryUsage method can be used with Unidrv-supported printers to specify the amount of memory required for use by a rendering plug-in''s IPrintOemUni::ImageProcessing method.'
ms.assetid: 'bdf9c43d-d747-40e8-86ba-976f3f6a19d6'
title: 'IPrintOemUni::MemoryUsage method'
---

# IPrintOemUni::MemoryUsage method

The `IPrintOemUni::MemoryUsage` method can be used with Unidrv-supported printers to specify the amount of memory required for use by a rendering plug-in's [**IPrintOemUni::ImageProcessing**](iprintoemuni-imageprocessing.md) method.

## Syntax


```C++
HRESULT MemoryUsage(
   PDEVOBJ         pdevobj,
   POEMMEMORYUSAGE pMemoryUsage
);
```



## Parameters

<dl> <dt>

*pdevobj* 
</dt> <dd>

Caller-supplied pointer to a [**DEVOBJ**](devobj.md) structure.

</dd> <dt>

*pMemoryUsage* 
</dt> <dd>

Caller-supplied pointer to an [**OEMMEMORYUSAGE**](oemmemoryusage.md) structure.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed.<br/>          |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

The `IPrintOemUni::MemoryUsage` method's purpose is to help the Unidrv driver determine the optimum size for the GDI drawing surface, based on the memory requirements of the [**IPrintOemUni::ImageProcessing**](iprintoemuni-imageprocessing.md) method. Implementation of the `IPrintOemUni::MemoryUsage` method is optional.

The `IPrintOemUni::MemoryUsage` method should return two values, as follows:

-   The amount of permanently-allocated, fixed-sized memory that the **IPrintOemUni::ImageProcessing** method needs to allocate.

    This value is returned in the **dwFixedMemoryUsage** member of the [**OEMMEMORYUSAGE**](oemmemoryusage.md) structure.

-   The amount of memory required to hold a bitmap after the **IPrintOemUni::ImageProcessing** method has finished processing it.

    The rendering plug-in either returns this processed bitmap to Unidrv, or spools it. The amount of memory required to store the processed bitmap is returned in the **dwPercentMemoryUsage** member of the OEMMEMORYUSAGE structure, and is expressed as a percentage of the source bitmap's size.

The value returned in the **dwPercentMemoryUsage** member should include, in addition to the processed bitmap's size, the amount of any additional memory allocations that are dependent on the size of the source bitmap.

The **dwMaxBandSize** member of the OEMMEMORYUSAGE structure is supplied by Unidrv and specifies the default maximum band size.

Before the Unidrv driver creates a drawing surface, it requests GDI to determine the optimum size for image banding bitmaps, based on available system memory. This optimum memory space must be shared, for each banding bitmap, between a source bitmap that is passed to the **IPrintOemUni::ImageProcessing** method and a (typically smaller) processed bitmap that the method either returns or outputs. Unidrv calls the rendering plug-in's `IPrintOemUni::MemoryUsage` method, if it exists, and uses the result to calculate how best to divide the optimum memory space.

For example, suppose GDI reports that the optimum amount of memory to use for drawing is 6 megabytes (contained in the OEMMEMORYUSAGE structure's **dwMaxBandSize** member), while the rendering plug-in's `IPrintOemUni::MemoryUsage` method returns values of zero for **dwFixedMemoryUsage** and 50 for **dwPercentMemoryUsage**. The value of 50 means that the **IPrintOemUni::ImageProcessing** method's output bitmaps will be 50 percent smaller than the source bitmaps. Therefore, Unidrv will allocate a source bitmap size of 4 megabytes, thus causing output bitmaps to be 2 megabytes.

If an `IPrintOemUni::MemoryUsage` method is not provided, Unidrv allocates all the optimum available space to the source bitmap. This is acceptable if the **IPrintOemUni::ImageProcessing** method returns the processed bitmap in the memory space allocated for the source bitmap. However, if a rendering plug-in's **IPrintOemUni::ImageProcessing** method does allocate space for a destination bitmap but does not provide an `IPrintOemUni::MemoryUsage` method, the result is that more memory will be allocated for bitmaps than the optimum available size, potentially causing performance degradation.

The `IPrintOemUni::MemoryUsage` method is optional. If a rendering plug-in implements this method, the plug-in's [**IPrintOemUni::GetImplementedMethod**](iprintoemuni-getimplementedmethod.md) method must return S\_OK when it receives "MemoryUsage" as input.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemUni**](iprintoemuni-interface.md)
</dt> <dt>

[**IPrintOemUni::ImageProcessing**](iprintoemuni-imageprocessing.md)
</dt> <dt>

[**OEMMEMORYUSAGE**](oemmemoryusage.md)
</dt> <dt>

[**DEVOBJ**](devobj.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUni::MemoryUsage%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





