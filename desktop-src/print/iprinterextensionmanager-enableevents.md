---
Description: 'The EnableEvents method allows events to be generated for the specified printer driver until DisableEvents is called.'
ms.assetid: '8DF89C18-10CA-4E8B-8E2A-B373C80F7B39'
title: 'IPrinterExtensionManager::EnableEvents method'
---

# IPrinterExtensionManager::EnableEvents method

The EnableEvents method allows events to be generated for the specified printer driver until [**DisableEvents**](iprinterextensionmanager-disableevents.md) is called.

## Syntax


```C++
HRESULT EnableEvents(
  [in] GUID printerDriverId
);
```



## Parameters

<dl> <dt>

*printerDriverId* \[in\]
</dt> <dd>

The GUID representing the specified driver for which to enable events. This GUID is specified in the INF file, and is also specified by the manifest file directive 'PrinterDriverID'.

</dd> </dl>

## Return value

This method returns an **HRESULT** value.

The printer extension should call this method when it is launched so that driver events are generated for it to consume.

## Remarks

In the case of a driver event like, for example, Print Preferences or Printer Notifications, the app is expected to call **EnableEvents**. But if the app doesn't call **EnableEvents** within 30s, the print system assumes that a UI was called but it's not being responsive so a standard UI is displayed instead.

## Requirements



|                            |                                                                                               |
|----------------------------|-----------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>            |
| Version<br/>         | Windows 8<br/>                                                                          |
| Header<br/>          | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrinterExtensionManager**](iprinterextensionmanager-interface.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterExtensionManager::EnableEvents%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





