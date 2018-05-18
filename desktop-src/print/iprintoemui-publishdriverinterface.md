---
Description: 'The IPrintOemUI::PublishDriverInterface method allows a user interface plug-in to obtain the Unidrv or Pscript5 driver''s IPrintOemDriverUI, IPrintCoreUI2, IPrintCoreHelperPS, or IPrintCoreHelperUni interface.'
ms.assetid: '4c2053ec-c6b3-4584-b689-dc887610c57e'
title: 'IPrintOemUI::PublishDriverInterface method'
---

# IPrintOemUI::PublishDriverInterface method

The `IPrintOemUI::PublishDriverInterface` method allows a user interface plug-in to obtain the Unidrv or Pscript5 driver's **IPrintOemDriverUI**, **IPrintCoreUI2**, **IPrintCoreHelperPS**, or **IPrintCoreHelperUni** interface.

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

Caller-supplied pointer to the **IUnknown** interface of the driver's [IPrintCoreUI2 COM Interface](print.iprintcoreui2_com_interface), [IPrintOemDriverUI COM Interface](print.iprintoemdriverui_com_interface), [IPrintCoreHelperPS Interface](iprintcorehelperps-interface.md), or [IPrintCoreHelperUni Interface](iprintcorehelperuni-interface.md). See Remarks.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                            | Description                         |
|----------------------------------------------------------------------------------------|-------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | The operation succeeded.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl> | The operation failed.<br/>    |



 

## Remarks

The Pscript5 driver supports the **IPrintCoreUI2**, **IPrintOemDriverUI**, and **IPrintCoreHelperPS** interfaces. Unidrv supports the **IPrintOemDriverUI** and **IPrintCoreHelperUni** interfaces. User interface plug-ins for both types of driver must implement the `IPrintOemUI::PublishDriverInterface` method.

The method should return information on its supported Pscript5 interfaces as follows:

1.  The Pscript5 driver first calls the `IPrintOemUI::PublishDriverInterface` method with the *pIUnknown* pointer set to the **IPrintCoreUI2** instance's **IUnknown** interface. If the user interface plug-in is able to use the **IPrintCoreUI2** interface, the method must return S\_OK. Otherwise, the plug-in should return E\_FAIL.

2.  If the plug-in has returned E\_FAIL, the Pscript5 driver calls the `IPrintOemUI::PublishDriverInterface` method again, but with the *pIUnknown* pointer set to the **IPrintOemDriverUI** instance's **IUnknown** interface. If the plug-in can use the **IPrintOemDriverUI** interface, the method must return S\_OK. Otherwise, the plug-in should return E\_FAIL.

3.  If the plug-in's **IPrintOemUI::GetInfo** method has returned a value of OEMPUBLISH\_IPRINTCOREHELPER in *pBuffer* in response to a call with *dwMode* set to OEMGI\_GETREQUESTEDHELPERINTERFACES, the Pscript5 driver calls the `IPrintOemUI::PublishDriverInterface` method again, but with the *pIUnknown* pointer set to an object that implements the **IPrintCoreHelperPS** and **IPrintCoreHelper** interfaces. If the plug-in can use the **IPrintCoreHelperPS** or **IPrintCoreHelper** interface, the method should return S\_OK. Otherwise, the method should return E\_FAIL.

The method should return information on its supported Unidrv interfaces as follows:

1.  The Unidrv driver first calls the `IPrintOemUI::PublishDriverInterface` method with the *pIUnknown* pointer set to the **IPrintOemDriverUI** instance's **IUnknown** interface. If the plug-in is able to use the **IPrintOemDriverUI** interface, the method must return S\_OK. Otherwise, the plug-in should return E\_FAIL.

2.  If the plug-in's [**IPrintOemUI::GetInfo**](iprintoemui-getinfo.md) method has returned a value of OEMPUBLISH\_IPRINTCOREHELPER in *pBuffer* in response to a call with *dwMode* set to OEMGI\_GETREQUESTEDHELPERINTERFACES, the Unidrv driver calls the `IPrintOemUI::PublishDriverInterface` method again, but with the *pIUnknown* pointer set to an object that implements the **IPrintCoreHelperUni** and **IPrintCoreHelper** interfaces. If the plug-in uses the **IPrintCoreHelperUni** or **IPrintCoreHelper** interface, the method should return S\_OK. Otherwise, the method should return E\_FAIL.

If the plug-in fails all calls to `IPrintOemUI::PublishDriverInterface`, the plug-in will not receive further calls. If the user interface plug-in will be calling **IPrintCoreUI2**, **IPrintOemDriverUI**, **IPrintCoreHelperPS**, or **IPrintCoreHelperUni** interface methods, it must use the received **IUnknown** interface pointer to call **IUnknown::QueryInterface** (described in the Microsoft Windows SDK documentation) in order to obtain a pointer to the driver's supported version of the **IPrintCoreUI2**, **IPrintOemDriverUI**, **IPrintCoreHelperPS**, or **IPrintCoreHelperUni** interface. For more information, see [Interface Identifiers for Printer Drivers](print.interface_identifiers_for_printer_drivers).

During processing of each DDI function, UI plug-ins should not mix the use of methods of the pre-Windows Vista interfaces (for example, the [IPrintOemDriverUI](iprintoemdriverui-interface.md) or [IPrintCoreUI2](iprintcoreui2-interface.md) interface) and the new methods of the Windows Vista interfaces (for example, [IPrintCoreHelperUni](iprintcorehelperuni-interface.md) or [IPrintCoreHelperPS](iprintcorehelperps-interface.md)) to read or write driver settings. For example, during the [**IPrintOemUI::DocumentPropertySheets**](iprintoemui-documentpropertysheets.md) method, the UI plug-in should not use the [**IPrintOemDriverUI::DrvUpdateUISetting**](iprintoemdriverui-drvupdateuisetting.md) method to write settings and use the [**IPrintCoreHelper::GetOption**](iprintcorehelper-getoption.md) method to read settings. For another example, during the [**IPrintOemUI::PrinterEvent**](iprintoemui-printerevent.md) method, the UI plug-in should not use the [**IPrintCoreUI2::GetOptions**](iprintcoreui2-getoptions.md) method to read settings and use the [**IPrintCoreHelper::SetOptions**](iprintcorehelper-setoptions.md) method to write settings. Synchronization of the reading and writing of settings is not supported between these different versions of interfaces.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemUI**](iprintoemui-interface.md)
</dt> <dt>

[**IPrintOemUI::GetInfo**](iprintoemui-getinfo.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUI::PublishDriverInterface%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





