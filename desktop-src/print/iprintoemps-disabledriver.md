---
Description: The IPrintOemPSDisableDriver method allows a rendering plug-in for Pscript to free resources that were allocated by the plug-ins IPrintOemPSEnableDriver method.
ms.assetid: 4fa25706-dc79-45fd-a805-7b9d110213ed
title: IPrintOemPSDisableDriver method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintOemPS::DisableDriver method

The `IPrintOemPS::DisableDriver` method allows a rendering plug-in for [*Pscript*](wdkgloss.p#wdkgloss-pscript) to free resources that were allocated by the plug-in's [**IPrintOemPS::EnableDriver**](iprintoemps-enabledriver.md) method.

## Syntax


```C++
STDMETHOD DisableDriver();
```



## Parameters

This method has no parameters.

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed<br/>           |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

The `IPrintOemPS::DisableDriver` method, provided by rendering plug-ins for Pscript5, performs the same types of operations as the [**DrvDisableDriver**](display.drvdisabledriver) function that is exported by Pscript5's printer graphics DLL.

`IPrintOemPS::DisableDriver` and **IPrintOemPS::EnableDriver** must be implemented as a pair. If you implement one, you must implement the other. For more information, see the Remarks section in [**IPrintOemPS::EnableDriver**](iprintoemps-enabledriver.md).

This is the last **IPrintOemPS** interface method that is called before the rendering plug-in is unloaded.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemPS::DisableDriver%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




