---
Description: The IPrintOemPS::PublishDriverInterface method allows a rendering plug-in for Pscript5 to obtain the Pscript5 driver's IPrintCorePS2, IPrintOemDriverPS, or IPrintCoreHelperPS interface.
ms.assetid: f878a674-7c08-4a7a-ab00-6c79f02566be
title: IPrintOemPS::PublishDriverInterface method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemPS::PublishDriverInterface method

The `IPrintOemPS::PublishDriverInterface` method allows a rendering plug-in for Pscript5 to obtain the Pscript5 driver's **IPrintCorePS2**, **IPrintOemDriverPS**, or **IPrintCoreHelperPS** interface.

## Syntax


```C++
HRESULT PublishDriverInterface(
   IUnknown *pIUnknown
);
```



## Parameters

<dl> <dt>

*pIUnknown* 
</dt> <dd>

Caller-supplied pointer to the **IUnknown** interface of the driver's [IPrintCorePS2 COM Interface](https://www.bing.com/search?q=IPrintCorePS2 COM Interface), [IPrintOemDriverPS COM Interface](https://www.bing.com/search?q=IPrintOemDriverPS COM Interface), or [IPrintCoreHelperPS Interface](iprintcorehelperps-interface.md).

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                            | Description                         |
|----------------------------------------------------------------------------------------|-------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | The operation succeeded.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl> | The operation failed<br/>     |



 

## Remarks

The Pscript5 driver supports the **IPrintCorePS2**, **IPrintOemDriverPS**, and **IPrintCoreHelperPS** interfaces. A rendering plug-in for Pscript5 must implement the `IPrintOemPS::PublishDriverInterface` method. The method should return information on its supported Pscript5 interfaces as follows:

1.  The Pscript5 driver first calls the `IPrintOemPS::PublishDriverInterface` method with the *pIUnknown* pointer set to the **IPrintCorePS2** instance's **IUnknown** interface. If the rendering plug-in is able to use the **IPrintCorePS2** interface, the method must return S\_OK. Otherwise, the plug-in should return E\_FAIL.

2.  If the plug-in has returned E\_FAIL, the Pscript5 driver calls the `IPrintOemPS::PublishDriverInterface` method again, but with the *pIUnknown* pointer set to the **IPrintOemDriverPS** instance's **IUnknown** interface. If the plug-in is able to use the **IPrintOemDriverPS** interface, the method must return S\_OK. Otherwise, the plug-in should return E\_FAIL.

3.  If the plug-in's [**IPrintOemPS::GetInfo**](iprintoemps-getinfo.md) method has returned a value of OEMPUBLISH\_IPRINTCOREHELPER in *pBuffer* in response to a call with *dwMode* set to OEMGI\_GETREQUESTEDHELPERINTERFACES in *pBuffer*, the Pscript5 driver calls the `IPrintOemPS::PublishDriverInterface` method again, but with the *pIUnknown* pointer set to an object that implements the **IPrintCoreHelperPS** and **IPrintCoreHelper** interfaces. If the plug-in retains a pointer to the object interface, the method should return S\_OK. Otherwise, the method should return E\_FAIL.

If the plug-in fails all calls to `IPrintOemPS::PublishDriverInterface`, the plug-in will not receive further calls. If the plug-in will be calling **IPrintCorePS2**, **IPrintOemDriverPS**, or **IPrintCoreHelperPS** interface methods, it must use the received **IUnknown** interface pointer to call **IUnknown::QueryInterface** (described in the Microsoft Windows SDK documentation) in order to obtain a pointer to the driver's supported version of the **IPrintCorePS2**, **IPrintOemDriverPS**, or **IPrintCoreHelperPS** interface. For more information, see [Accessing Printer Driver Interfaces from Plug-Ins](https://www.bing.com/search?q=Accessing Printer Driver Interfaces from Plug-Ins).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemPS**](iprintoemps-interface.md)
</dt> <dt>

[**IPrintOemPS::GetInfo**](iprintoemps-getinfo.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemPS::PublishDriverInterface%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





