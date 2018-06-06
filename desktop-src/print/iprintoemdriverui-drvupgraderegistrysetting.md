---
Description: The IPrintOemDriverUI::DrvUpdateRegistrySetting method is provided by the Unidrv and Pscript5 minidrivers so that user interface plug-ins can update device settings stored in the registry.
ms.assetid: 9249dd75-7d90-414a-b6b5-4be0fc4f3170
title: IPrintOemDriverUI::DrvUpgradeRegistrySetting method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemDriverUI::DrvUpgradeRegistrySetting method

The `IPrintOemDriverUI::DrvUpdateRegistrySetting` method is provided by the Unidrv and Pscript5 minidrivers so that user interface plug-ins can update device settings stored in the registry.

## Syntax


```C++
HRESULT DrvUpgradeRegistrySetting(
   HANDLE hPrinter,
   PCSTR  pFeature,
   PCSTR  pOption
);
```



## Parameters

<dl> <dt>

*hPrinter* 
</dt> <dd>

Caller-supplied printer handle.

</dd> <dt>

*pFeature* 
</dt> <dd>

Caller-supplied pointer to a string identifying a printer feature name contained in the printer's [*GPD*](wdkgloss.g#wdkgloss-generic-printer-description--gpd-) or [*PPD*](wdkgloss.p#wdkgloss-postscript-printer-description--ppd-) file.

</dd> <dt>

*pOption* 
</dt> <dd>

Caller-supplied pointer to a string identifying an option name, associated with the specified feature, contained in the printer's GPD or PPD file.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed.<br/>          |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

The `IPrintOemDriverUI::DrvUpdateRegistrySetting` method is meant to be called from a user interface plug-in's [**IPrintOemUI::UpgradePrinter**](iprintoemui-upgradeprinter.md) method, when it is necessary to update registry settings that were stored in private registry keys for an earlier version of the driver, but are now contained in a GPD or PPD file.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemDriverUI::DrvUpgradeRegistrySetting%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




