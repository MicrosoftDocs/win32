---
Description: The IPrintOemUI2::HideStandardUI method allows a user interface plug-in to specify whether the standard property sheets should be displayed or hidden.
ms.assetid: 144618d0-0d77-487c-a074-8bd9f6030de2
title: IPrintOemUI2::HideStandardUI method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemUI2::HideStandardUI method

The `IPrintOemUI2::HideStandardUI` method allows a user interface plug-in to specify whether the standard property sheets should be displayed or hidden. Beginning with Microsoft Windows XP, this method can be implemented by a Pscript5 user interface plug-in. Beginning with Windows Vista, this method can be implemented by a Unidrv user interface plug-in.

## Syntax


```C++
HRESULT HideStandardUI(
   DWORD dwMode
);
```



## Parameters

<dl> <dt>

*dwMode* 
</dt> <dd>

Specifies which type of property sheet UI -- document property sheet or device property sheet -- to hide. This parameter should be set to one of the following constants, which are defined in printoem.h:



| Value                       | Meaning                                              |
|-----------------------------|------------------------------------------------------|
| OEMCUIP\_DOCPROP<br/> | Hide standard document property sheet UI.<br/> |
| OEMCUIP\_PRNPROP<br/> | Hide standard device property sheet UI.<br/>   |



 

</dd> </dl>

## Return value

On success, this method should return S\_OK. Otherwise, it should return E\_NOTIMPL. See Remarks for additional information.

## Remarks

This method is supported in Windows Vista for Pscript 5 and Unidrv plug-ins, and in Windows XP only for Pscript5 plug-ins.

Within the [**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md) or [**DrvDevicePropertySheets**](drvdevicepropertysheets.md) DDIs when pPSUIInfo--&gt;Reason is set to PROPSHEETUI\_REASON\_INIT, the driver calls the `IPrintOemUI2::HideStandardUI` method to ask the UI plug-in about user interface requests. This method can respond in any of four ways:

1.  Hide standard document property sheet UI.

2.  Hide standard device property sheet UI.

3.  Hide all standard property sheet UI.

4.  Do not hide any standard property sheet UI.

The following table summarizes how the `IPrintOemUI2::HideStandardUI` method would respond in each of these situations.



| To indicate this response...                                                                                                         | IPrintOemUI2::HideStandardUI returns...                                                |
|--------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Hide standard document property sheet UI. The plug-in implements its own document property sheet UI.<br/>                      | If *dwMode* == OEMCUIP\_DOCPROP, return S\_OK; otherwise return E\_NOTIMPL.<br/> |
| Hide standard device property sheet UI. The plug-in implements its own device property sheet UI.<br/>                          | If *dwMode* == OEMCUIP\_PRNPROP, return S\_OK; otherwise return E\_NOTIMPL.<br/> |
| Hide all standard property sheet UI. The plug-in implements its own document property sheet and device property sheet UI.<br/> | Return S\_OK, regardless of the value of *dwMode*.<br/>                          |
| Display all standard property sheet UI.<br/>                                                                                   | Return E\_NOTIMPL, regardless of the value of *dwMode*.<br/>                     |



 

If the `IPrintOemUI2::HideStandardUI` method indicates to the driver that all standard property sheets should be hidden, the driver omits calls to compstui.dll (see [Pscript Components](https://www.bing.com/search?q=Pscript Components)) to add the standard property sheets. A UI plug-in must implement at least one custom property sheet UI if `IPrintOemUI2::HideStandardUI` returns S\_OK.

When the printer has multiple UI plug-ins installed, the driver calls UI plug-ins in the order they were installed, until one of them returns S\_OK, or until all of the UI plug-ins have been called and none of them returned S\_OK. The former case indicates to the driver that the standard property sheet UI should be hidden. The latter case indicates to the driver that the standard property sheet UI should be displayed.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintOemUI2**](iprintoemui2-interface.md)
</dt> <dt>

[**DrvDocumentPropertySheets**](drvdocumentpropertysheets.md)
</dt> <dt>

[**DrvDevicePropertySheets**](drvdevicepropertysheets.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUI2::HideStandardUI%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





