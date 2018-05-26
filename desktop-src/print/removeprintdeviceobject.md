---
Description: The RemovePrintDeviceObject function removes a device object from a print provider queue.
ms.assetid: D94A669E-4293-4235-8BC4-C7883BB0C83C
title: RemovePrintDeviceObject function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RemovePrintDeviceObject function

> \[!Warning\]
>
> Starting with Windows 10, the APIs which support third-party print providers are deprecated. Microsoft does not recommend any investment into third-party print providers. Additionally, on Windows 8 and newer products where the v4 print driver model is available, third-party print providers may not create or manage queues which use v4 print drivers.

 

The **RemovePrintDeviceObject** function removes a device object from a print provider queue.

## Syntax


```C++
HRESULT WINAPI RemovePrintDeviceObject(
  _In_ HANDLE hDeviceObject
);
```



## Parameters

<dl> <dt>

*hDeviceObject* \[in\]
</dt> <dd>

The HANDLE to the device object to be removed. This should be a device object that was created with [**AddPrintDeviceObject**](addprintdeviceobject.md).

</dd> </dl>

## Return value

The **RemovePrintDeviceObject** function returns S\_OK, if the device object was removed successfully. Otherwise it returns an error.

For example, this function can return HRESULT\_FROM\_WIN32(ERROR\_INVALID\_HANDLE), if an invalid device object handle was used to call the function. And note that, regardless of the return value, the device object HANDLE becomes invalid after a call to **RemovePrintDeviceObject** has completed.

## Remarks

Call **RemovePrintDeviceObject** to remove the device object for a printer that has been deleted. When the spooler services stops, all the device objects are automatically deleted, so it is not required to call **RemovePrintDeviceObject** for each printer device object.

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
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20RemovePrintDeviceObject%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





