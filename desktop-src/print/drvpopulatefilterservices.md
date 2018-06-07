---
Description: The DrvPopulateFilterServices function is called by the XPSDrv filter pipeline manager to allow the service provider to instantiate filter service objects in the filter pipeline property bag specified by the pPropertyBag parameter.
ms.assetid: A24DAC54-57FE-419D-8B5D-54B8AFC338DE
title: DrvPopulateFilterServices function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DrvPopulateFilterServices function

The **DrvPopulateFilterServices** function is called by the XPSDrv filter pipeline manager to allow the service provider to instantiate filter service objects in the filter pipeline property bag specified by the *pPropertyBag* parameter.

## Syntax


```C++
HRESULT WINAPI DrvPopulateFilterServices(
  _In_ IPrintPipelinePropertyBag *pPropertyBag
);
```



## Parameters

<dl> <dt>

*pPropertyBag* \[in\]
</dt> <dd>

Pointer to a print pipeline property bag.

</dd> </dl>

## Return value

This function returns an HRESULT value.

## Remarks

The [XPSDrv printer driver](https://www.bing.com/search?q=XPSDrv+printer+driver) can specify filter service provider module using the &lt;*FilterServiceProvider*&gt; or &lt;*OptionalFilterServiceProvider*&gt; element in the [filter pipeline configuration file](https://www.bing.com/search?q=filter+pipeline+configuration+file). The service provider module must export the **DrvPopulateFilterServices** function.

## Requirements



|                            |                                                                                             |
|----------------------------|---------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>          |
| Header<br/>          | <dl> <dt>Filterpipeline.h</dt> </dl> |



## See also

<dl> <dt>

[Filter pipeline configuration file](https://www.bing.com/search?q=Filter+pipeline+configuration+file)
</dt> <dt>

[**IPrintPipelinePropertyBag**](https://msdn.microsoft.com/3997291f-0af3-4fa8-8d36-20ff36551f42)
</dt> <dt>

[XPSDrv printer driver](https://www.bing.com/search?q=XPSDrv+printer+driver)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DrvPopulateFilterServices%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





