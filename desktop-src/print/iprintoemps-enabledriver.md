---
Description: The IPrintOemPS::EnableDriver method allows a rendering plug-in for Pscript to hook out some graphics DDI functions.
ms.assetid: 12e65e91-f540-49fd-a723-c6b93708b166
title: IPrintOemPS::EnableDriver method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemPS::EnableDriver method

The `IPrintOemPS::EnableDriver` method allows a rendering plug-in for [*Pscript*](https://msdn.microsoft.com/139a10e9-203b-499b-9291-8537eae9189c) to hook out some graphics DDI functions.

## Syntax


```C++
STDMETHOD EnableDriver(
   DWORD          DriverVersion,
   DWORD          cbSize,
   PDRVENABLEDATA pded
);
```



## Parameters

<dl> <dt>

*DriverVersion* 
</dt> <dd>

Caller-supplied interface version number. This value is defined by PRINTER\_OEMINTF\_VERSION, in printoem.h.

</dd> <dt>

*cbSize* 
</dt> <dd>

Caller-supplied size, in bytes, of the structure pointed to by *pded*.

</dd> <dt>

*pded* 
</dt> <dd>

Caller-supplied pointer to a [**DRVENABLEDATA**](https://msdn.microsoft.com/dbeaecf8-dea1-4412-babb-6e40bf5dc7b0) structure.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed<br/>           |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

The `IPrintOemPS::EnableDriver` method allows a rendering plug-in to perform the same types of operations as the [**DrvEnableDriver**](https://msdn.microsoft.com/b7aa5442-bbf5-4f9e-ad39-bf8a2d01c50e) function that is exported by printer graphics DLLs.

Like the **DrvEnableDriver** function, the `IPrintOemPS::EnableDriver` method is responsible for providing addresses of internally supported graphics DDI functions, known as hooking functions. It can also perform other one-time initialization operations. Unlike the **DrvEnableDriver** function, implementation of the `IPrintOemPS::EnableDriver` method is optional.

> [!Note]  
> If you implement `IPrintOemPS::EnableDriver`, you must also implement [**IPrintOemPS::DisableDriver**](iprintoemps-disabledriver.md). Actions begun in the former method might need to be completed in the latter method. For example, if a large buffer is allocated in `IPrintOemPS::EnableDriver`, but not deallocated in **IPrintOemPS::DisableDriver**, a memory leak can occur.

 

The method should fill the supplied [**DRVENABLEDATA**](https://msdn.microsoft.com/dbeaecf8-dea1-4412-babb-6e40bf5dc7b0) structure and allocate an array of [**DRVFN**](https://msdn.microsoft.com/2ff20004-ec2e-4192-a5f1-e3e9d2bfad3c) structures. It should fill the array with pointers to hooking functions, along with winddi.h-defined index values that identify the hooked out graphics DDI functions.

A rendering plug-in for Pscript5 can hook out a graphics DDI function only if the Pscript5 driver defines the function. The following graphics DDI functions are defined in Pscript5 and or Unidrv and can therefore be hooked out:

<dl>

[**DrvAlphaBlend**](https://msdn.microsoft.com/fff3df30-cb29-4da3-97bc-dba5fbba1db5)  
[**DrvBitBlt**](https://msdn.microsoft.com/d7b4e25c-b9a1-4200-b449-b7c7ed059db4)  
[**DrvCopyBits**](https://msdn.microsoft.com/c2d42c7a-3d6e-416c-a194-2228cc1b0fd9)  
[**DrvDitherColor**](https://msdn.microsoft.com/635a4af8-ec19-4f99-80b2-bad2a6e87edc) (Unidrv only)  
[**DrvEndDoc**](https://msdn.microsoft.com/905813fd-281d-4cc8-b006-a2d284041bb7)  
[**DrvEscape**](https://msdn.microsoft.com/7b59dc85-27f4-4529-847e-6027dae8a45a)  
[**DrvFillPath**](https://msdn.microsoft.com/6f499d08-d2a1-46d0-b931-e6c16c4e1d3a)  
[**DrvFontManagement**](https://msdn.microsoft.com/cd52e32a-6d95-4aaf-96d3-45da2e5359e4)  
[**DrvGetGlyphMode**](https://msdn.microsoft.com/8e11c4e7-0203-4445-8f33-3b928161c62a)  
[**DrvGradientFill**](https://msdn.microsoft.com/c8a51b5f-5509-4801-8432-c4d895cefbda)  
[**DrvIcmCreateColorTransform**](https://msdn.microsoft.com/a4fda665-ba26-4799-820d-c4d82a58d6fd) (Pscript only)  
[**DrvIcmDeleteColorTransform**](https://msdn.microsoft.com/aa1226d3-7b2a-4911-b785-eea9f72016f5) (Pscript only)  
[**DrvLineTo**](https://msdn.microsoft.com/e1e5dd93-444d-4176-9f7f-8aa220cddf78) (Unidrv only)  
[**DrvNextBand**](https://msdn.microsoft.com/7c02d32b-6c95-4dd5-b9cf-2f64ba78f25a) (Unidrv only)  
[**DrvPlgBlt**](https://msdn.microsoft.com/5bd478f1-0c01-4d7f-9ed1-af84e5bbe773)  
[**DrvQueryDeviceSupport**](https://msdn.microsoft.com/684c5dd5-edf0-4b7d-888c-c01eb9670846) (Pscript only)  
[**DrvQueryAdvanceWidths**](https://msdn.microsoft.com/b97114b5-6cc7-4af6-badb-d6aa5fc581ef)  
[**DrvQueryFont**](https://msdn.microsoft.com/2ba6c8e3-9707-48dd-98d9-072f3eee8cd0)  
[**DrvQueryFontData**](https://msdn.microsoft.com/3f6efd3c-3ddf-4ce6-9527-730e01c45e74)  
[**DrvQueryFontTree**](https://msdn.microsoft.com/29601ea6-9b68-4cdc-a7a1-b6a922524760)  
[**DrvRealizeBrush**](https://msdn.microsoft.com/2948f274-cef2-4fcf-9607-79540b6e5a5f)  
[*DrvSendPage*](https://msdn.microsoft.com/d9c452e3-3850-4ca2-8114-b3866fbdeba6)  
[**DrvStartBanding**](https://msdn.microsoft.com/c9006dd1-055b-4fb0-92e8-c7b6bc294941) (Unidrv only)  
[**DrvStartDoc**](https://msdn.microsoft.com/f73adc24-2e61-4b62-9d38-12a23b62ed01)  
[**DrvStartPage**](https://msdn.microsoft.com/31e42524-de9a-459a-95a7-94b2597c3cd8)  
[**DrvStretchBlt**](https://msdn.microsoft.com/3520533d-4e42-4abc-bc10-557c674caa33)  
[**DrvStretchBltROP**](https://msdn.microsoft.com/eeaec7f4-2dfe-42a9-8789-a9ce11aec7b2)  
[**DrvStrokeAndFillPath**](https://msdn.microsoft.com/92a04fe5-146d-4839-a854-1ac50705b447)  
[**DrvStrokePath**](https://msdn.microsoft.com/c931a39d-c0ae-4f40-b70f-f51d5621c228)  
[**DrvTextOut**](https://msdn.microsoft.com/f2f61687-d833-4d09-8cd5-99e81436c1c1)  
[**DrvTransparentBlt**](https://msdn.microsoft.com/67e61a43-b962-4905-8876-9a0380848ed0)  
</dl>

If you provide a customized hooking function, it preempts the driver's equivalent graphics DDI function. Hooking functions can also call back into the driver's graphics DDI functions. For more information, see [Customized Graphics DDI Functions](https://www.bing.com/search?q=Customized+Graphics+DDI+Functions).

Customized hooking functions have the same input and output parameters as the equivalent graphics DDI function, with one exception - where graphics DDI functions receive PDEV pointers, customized hooking functions receive [**DEVOBJ**](devobj.md) pointers. There are two ways for these functions to receive PDEV pointers:

1.  As the contents of the **dhpdev** member of a [**SURFOBJ**](https://msdn.microsoft.com/cee7cb50-1e8a-422b-aebe-7030ae96fb34) structure for the destination surface.

    For the equivalent customized hooking function, the destination SURFOBJ structure's **dhpdev** member points to a DEVOBJ structure, and must be cast to type PDEVOBJ when referenced. An example graphics DDI function is **DrvBitBlt**.

2.  As an input argument for a *dhpdev* parameter.

    The equivalent customized hooking function must cast this input parameter to type PDEVOBJ when referencing it. An example graphics DDI function is **DrvDitherColor**.

Note that while a [printer graphics DLL](https://www.bing.com/search?q=printer+graphics+DLL) includes the addresses of its [**DrvEnablePDEV**](https://msdn.microsoft.com/9a7ed18a-f21c-486b-9261-59a3fe5aef9e), [**DrvDisablePDEV**](https://msdn.microsoft.com/dff04000-e307-4a1c-80fe-d6666929df76), and [**DrvResetPDEV**](https://msdn.microsoft.com/8e530874-7774-4f8f-852c-001b2ce4a707) functions in the DRVENABLEDATA structure, a rendering plug-in for Pscript5 implements **EnablePDEV**, **DisablePDEV**, and **ResetPDEV** as methods of the **IPrintOemPS** interface and does not place their addresses in the DRVENABLEDATA structure.

If `IPrintOemPS::EnableDriver` methods are exported by multiple rendering plug-ins, the methods are called in the order that the plug-ins are specified for installation.

> [!Note]  
> Each graphics DDI function can be hooked out by one rendering plug-in. If multiple plug-ins attempt to hook out the same graphics DDI function, all hook-outs after the first one are ignored.

 

For more information about creating and installing rendering plug-ins, see [Customizing Microsoft's Printer Drivers](https://www.bing.com/search?q=Customizing+Microsoft's+Printer+Drivers).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemPS::EnableDriver%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




