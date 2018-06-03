---
Description: The IPrintOemUI::UpgradePrinter method allows a user interface plug-in to upgrade device option values that are stored in the registry.
ms.assetid: 405f0000-c239-4f2c-83ad-5d35441a5df2
title: IPrintOemUI::UpgradePrinter method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemUI::UpgradePrinter method

The `IPrintOemUI::UpgradePrinter` method allows a user interface plug-in to upgrade device option values that are stored in the registry.

## Syntax


```C++
HRESULT UpgradePrinter(
   DWORD dwLevel,
   PBYTE pDriverUpgradeInfo
);
```



## Parameters

<dl> <dt>

*dwLevel* 
</dt> <dd>

Caller-supplied version number of the structure pointed to by *pDriverUpgradeInfo*. Current valid value is 1.

</dd> <dt>

*pDriverUpgradeInfo* 
</dt> <dd>

Caller-supplied pointer to a [**DRIVER\_UPGRADE\_INFO\_1**](driver-upgrade-info-1.md) structure.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed.<br/>          |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

If you provide a user interface plug-in for one of Microsoft's printer drivers, and if the user interface plug-in stores device option values in the registry, it should implement the `IPrintOemUI::UpgradePrinter` method to update those values.

A user interface plug-in's `IPrintOemUI::UpgradePrinter` method performs the same types of operations as the **DrvUpgradePrinter** function that is exported by user-mode printer interface DLLs. When the driver's [**DrvUpgradePrinter**](drvupgradeprinter.md) function is called, it updates its own registry values and then calls the `IPrintOemUI::UpgradePrinter` method.

If `IPrintOemUI::UpgradePrinter` methods are exported by multiple user interface plug-ins, the methods are called in the order that the plug-ins are specified for installation.

For more information about creating and installing user interface plug-ins, see [Customizing Microsoft's Printer Drivers](https://www.bing.com/search?q=Customizing Microsoft's Printer Drivers).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUI::UpgradePrinter%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




