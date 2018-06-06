---
Description: The IPrintOemUni::PublishDriverInterface method allows a rendering plug-in for Unidrv to obtain the Unidrv driver's IPrintOemDriverUni or IPrintCoreHelperUni interface.
ms.assetid: 72bfa383-a7f2-4aa6-a45c-564928705e42
title: IPrintOemUni::PublishDriverInterface method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemUni::PublishDriverInterface method

The `IPrintOemUni::PublishDriverInterface` method allows a rendering plug-in for Unidrv to obtain the Unidrv driver's **IPrintOemDriverUni** or **IPrintCoreHelperUni** interface.

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

Caller-supplied pointer to the **IUnknown** interface of the driver's [IPrintOemDriverUni COM Interface](https://www.bing.com/search?q=IPrintOemDriverUni+COM+Interface) or [IPrintCoreHelperUni interface](iprintcorehelperuni-interface.md).

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                            | Description                         |
|----------------------------------------------------------------------------------------|-------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | The operation succeeded.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl> | The operation failed.<br/>    |



 

## Remarks

A rendering plug-in for [*Unidrv*](wdkgloss.u#wdkgloss-unidrv) must implement the `IPrintOemUni::PublishDriverInterface` method, and the method must return S\_OK in response to at least one call. Otherwise, the driver will not call the plug-in's other **IPrintOemUni** interface methods.

The method should return information on its supported Unidrv interfaces as follows:

1.  The Unidrv driver first calls the `IPrintOemUI::PublishDriverInterface` method with the *pIUnknown* pointer set to the **IPrintOemDriverUni** instance's **IUnknown** interface. If the rendering plug-in will be calling **IPrintOemDriverUni** interface methods, it must use the received **IUnknown** interface pointer to call **IUnknown::QueryInterface** (described in the Microsoft Windows SDK documentation) in order to obtain a pointer to the driver's supported version of the **IPrintOemDriverUni** interface. For more information, see [Interface Identifiers for Printer Drivers](https://www.bing.com/search?q=Interface+Identifiers+for+Printer+Drivers).

2.  If the plug-in's [**IPrintOemUni::GetInfo**](iprintoemuni-getinfo.md) method has returned a value of OEMPUBLISH\_IPRINTCOREHELPER in *pBuffer* in response to a call with *dwMode* set to OEMGI\_GETREQUESTEDHELPERINTERFACES, the Unidrv driver calls the `IPrintOemUni::PublishDriverInterface` method again, but with the *pIUnknown* pointer set to an object that implements the **IPrintCoreHelperUni** and **IPrintCoreHelper** interfaces. If the plug-in retains a pointer to the object, the method should return S\_OK. Otherwise, the method should return E\_FAIL.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemUni**](iprintoemuni-interface.md)
</dt> <dt>

[**IPrintOemUni::GetInfo**](iprintoemuni-getinfo.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUni::PublishDriverInterface%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





