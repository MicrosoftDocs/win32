---
Description: The IPrintOemuNI::DisableDriver method allows a rendering plug-in for Unidrv to free resources that were allocated by the plug-in's IPrintOemUni::EnableDriver method.
ms.assetid: a92d8c2e-52b5-4941-b49e-42e067e56e91
title: IPrintOemUni::DisableDriver method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemUni::DisableDriver method

The `IPrintOemuNI::DisableDriver` method allows a rendering plug-in for [*Unidrv*](wdkgloss.u#wdkgloss-unidrv) to free resources that were allocated by the plug-in's [**IPrintOemUni::EnableDriver**](iprintoemuni-enabledriver.md) method.

## Syntax


```C++
STDMETHOD DisableDriver(
    None
);
```



## Parameters

<dl> <dt>

*None* 
</dt> <dd></dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                            | Description                         |
|----------------------------------------------------------------------------------------|-------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | The operation succeeded.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl> | The operation failed<br/>     |



 

## Remarks

A rendering plug-in for Unidrv must implement the `IPrintOemUni::DisableDriver` method.

The `IPrintOemUni::DisableDriver` method, provided by rendering plug-ins for Unidrv, performs the same types of operations as the [**DrvDisableDriver**](https://msdn.microsoft.com/8f12cc40-6cff-4e40-a264-58d16d3e55bd) function that is exported by Unidrv's printer graphics DLL.

`IPrintOemUni::DisableDriver` and **IPrintOemUni::EnableDriver** must be implemented as a pair. If you implement one, you must implement the other. For more information, see the Remarks section in [**IPrintOemUni::EnableDriver**](iprintoemuni-enabledriver.md).

This is the last **IPrintOemUni** interface method that is called before the rendering plug-in is unloaded.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUni::DisableDriver%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




