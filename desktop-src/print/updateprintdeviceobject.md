---
Description: The UpdatePrintDeviceObject function updates the properties of a device object that is in the print provider queue.
ms.assetid: 52E8F8BF-0362-4BA9-BABD-7B009B3FFA7F
title: UpdatePrintDeviceObject function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# UpdatePrintDeviceObject function

> \[!Warning\]
>
> Starting with Windows 10, the APIs which support third-party print providers are deprecated. Microsoft does not recommend any investment into third-party print providers. Additionally, on Windows 8 and newer products where the v4 print driver model is available, third-party print providers may not create or manage queues which use v4 print drivers.

 

The **UpdatePrintDeviceObject** function updates the properties of a device object that is in the print provider queue.

## Syntax


```C++
HRESULT WINAPI UpdatePrintDeviceObject(
  _In_ HANDLE hPrinter,
  _In_ HANDLE hDeviceObject
);
```



## Parameters

<dl> <dt>

*hPrinter* \[in\]
</dt> <dd>

The HANDLE to an open printer. This should be a handle that was returned by the **AddPrinter** or **OpenPrinter** spooler functions.

</dd> <dt>

*hDeviceObject* \[in\]
</dt> <dd>

The HANDLE to the device object to be updated. This should be a device object that was created with [**AddPrintDeviceObject**](addprintdeviceobject.md).

</dd> </dl>

## Return value

The **UpdatePrintDeviceObject** function returns S\_OK, if the properties of the device object were updated successfully. Otherwise it returns an error.

For example, this function can return HRESULT\_FROM\_WIN32(ERROR\_INVALID\_HANDLE), if the function call was made with an invalid HANDLE, or the device object was removed before the function call was made.

## Remarks

The [PRINTER\_INFO\_2](http://msdn.microsoft.com/en-us/library/windows/desktop/dd162845.aspx) structure is a good example of the kind of properties that **UpdatePrintDeviceObject** can update.

## Requirements



|                            |                                                                                                           |
|----------------------------|-----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                        |
| Header<br/>          | <dl> <dt>Winsplp.h (include Winspool.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>WinSpool.lib</dt> </dl>                   |
| DLL<br/>             | <dl> <dt>WinSpool.drv</dt> </dl>                   |



## See also

<dl> <dt>

[**AddPrintDeviceObject**](addprintdeviceobject.md)
</dt> <dt>

[PRINTER\_INFO\_2](http://msdn.microsoft.com/en-us/library/windows/desktop/dd162845.aspx)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20UpdatePrintDeviceObject%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





