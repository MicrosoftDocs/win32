---
Description: The AddPrintDeviceObject print provider function creates a device object for a print provider queue.
ms.assetid: C01071FD-7D1D-4D6F-AFDD-355FFDA699EA
title: AddPrintDeviceObject function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddPrintDeviceObject function

> \[!Warning\]
>
> Starting with Windows 10, the APIs which support third-party print providers are deprecated. Microsoft does not recommend any investment into third-party print providers. Additionally, on Windows 8 and newer products where the v4 print driver model is available, third-party print providers may not create or manage queues which use v4 print drivers.

 

The **AddPrintDeviceObject** print provider function creates a device object for a print provider queue.

## Syntax


```C++
HRESULT WINAPI AddPrintDeviceObject(
  _In_  HANDLE hPrinter,
  _Out_ HANDLE *phDeviceObject
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

A HANDLE to an open printer. This should be a HANDLE returned by the **AddPrinter** or **OpenPrinter** spooler functions.

</dd> <dt>

*phDeviceObject* \[out\]
</dt> <dd>

A HANDLE to the device object, if it was created successfully.

</dd> </dl>

## Return value

The **AddPrintDeviceObject** function returns S\_OK, if the device object was created successfully. Otherwise it returns an error.

## Remarks

The **AddPrintDeviceObject** function should be called in the following situations:

**User installs a Printer**

-   The print provider should call this function after installing the printer.

-   The function must be called by impersonating the user who is installing the printer.

**Print Provider is intialized after spooler service starts**

-   The print provider should call this function for each previously-installed Printer owned by the provider. During this time, **AddPrintDeviceObject** doesn't have to impersonate the user context when it is called.

    > [!Note]  
    > Any device object that is added using **AddPrintDeviceObject** will persist until you remove it using [**RemovePrintDeviceObject**](removeprintdeviceobject.md), or until the spooler service restarts. And when the spooler services stops, all the device objects are automatically deleted.

     

## Requirements



|                            |                                                                                                           |
|----------------------------|-----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                        |
| Header<br/>          | <dl> <dt>Winsplp.h (include Winspool.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>WinSpool.lib</dt> </dl>                   |
| DLL<br/>             | <dl> <dt>WinSpool.drv</dt> </dl>                   |



## See also

<dl> <dt>

[**RemovePrintDeviceObject**](removeprintdeviceobject.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20AddPrintDeviceObject%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





