---
Description: The IPrintOemUni::GetImplementedMethod method is used by Unidrv to determine which IPrintOemUni interface methods a rendering plug-in has implemented.
ms.assetid: bc2a00ea-214a-435a-86fa-d694188d0245
title: IPrintOemUni::GetImplementedMethod method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemUni::GetImplementedMethod method

The `IPrintOemUni::GetImplementedMethod` method is used by Unidrv to determine which **IPrintOemUni** interface methods a rendering plug-in has implemented.

## Syntax


```C++
HRESULT GetImplementedMethod(
   PSTR pMethodName
);
```



## Parameters

<dl> <dt>

*pMethodName* 
</dt> <dd>

Caller-supplied pointer to a string that represents the name of an **IPrintOemUni** interface method, such as "ImageProcessing" for **IPrintOemUni::ImageProcessing** or "FilterGraphics" for **IPrintOemUni::FilterGraphics**.

</dd> </dl>

## Return value

`GetImplementedMethod` must return one of the following values.



| Return code                                                                             | Description                                                                         |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | The operation succeeded (that is, the specified method is implemented).<br/>  |
| <dl> <dt>**S\_FALSE**</dt> </dl> | The operation failed (that is, the specified method is not implemented).<br/> |



 

## Remarks

A rendering plug-in for Unidrv must implement the `IPrintOemUni::GetImplementedMethod` method, together with several other methods in this interface. For those methods that are optional, `IPrintOemUni::GetImplementedMethod` examines the input method name string and returns a value that indicates whether the associated method is implemented within the plug-in. For example, if `IPrintOemUni::GetImplementedMethod` is called with the string "ImageProcessing", it should return S\_OK if the **IPrintOemUni::ImageProcessing** method is implemented and S\_FALSE otherwise.

The `IPrintOemUni::GetImplementedMethod` method must recognize the following name strings:

<dl> "CommandCallback"  
"Compression"  
"DownloadCharGlyph"  
"DownloadFontHeader"  
"FilterGraphics"  
"HalftonePattern"  
"ImageProcessing"  
"MemoryUsage"  
"OutputCharStr"  
"SendFontCmd"  
"TextOutAsBitmap"  
"TTDownloadMethod"  
"TTYGetInfo"  
</dl>

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUni::GetImplementedMethod%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




