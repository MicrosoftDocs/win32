---
Description: Print Provider Functions
ms.assetid: '10fe18f0-15f7-4dd9-91e4-65d5649798f2'
title: Print Provider Functions
---

# Print Provider Functions

## 

> \[!Warning\]
>
> Starting with Windows 10, the APIs which support third-party print providers are deprecated. Microsoft does not recommend any investment into third-party print providers. Additionally, on Windows 8 and newer products where the v4 print driver model is available, third-party print providers may not create or manage queues which use v4 print drivers.

 

This section describes functions supplied by [print providers](print.print_providers). Most provider functions are described in the Microsoft Windows SDK documentation, so this section describes only functions not included in SDK documentation. Print providers must supply pointers to all defined functions by using a [**PRINTPROVIDOR**](printprovidor.md) structure.

This section includes:

<dl>

[**AddPrintDeviceObject**](addprintdeviceobject.md)  
[**FindFirstPrinterChangeNotification**](print.findfirstprinterchangenotification)  
[**GetJobAttributes**](getjobattributes.md)  
[**GetJobAttributesEx**](getjobattributesex.md)  
[**InitializePrintProvidor**](initializeprintprovidor.md)  
[**RefreshPrinterChangeNotification**](print.refreshprinterchangenotification)  
[**RemovePrintDeviceObject**](removeprintdeviceobject.md)  
[**UpdatePrintDeviceObject**](updateprintdeviceobject.md)  
[**XcvData**](print.xcvdata)  
</dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Print%20Provider%20Functions%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



