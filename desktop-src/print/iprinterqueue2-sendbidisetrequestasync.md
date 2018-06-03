---
Description: Uses an XML string value to send a Bidi Set request as an asynchronous operation.
ms.assetid: 05FF8A47-A586-4DA7-94AD-A7186265ADB4
title: IPrinterQueue2::SendBidiSetRequestAsync method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrinterQueue2::SendBidiSetRequestAsync method

Uses an XML string value to send a Bidi Set request as an asynchronous operation.

This method allows the user to perform device maintenance tasks from within a UWP device app for printers.

## Syntax


```C++
HRESULT SendBidiSetRequestAsync(
  [in]          BSTR                            bstrBidiRequest,
  [in]          IPrinterBidiSetRequestCallback  *pCallback,
  [out, retval] IPrinterExtensionAsyncOperation ** ppAsyncOperation
);
```



## Parameters

<dl> <dt>

*bstrBidiRequest* \[in\]
</dt> <dd>

XML string that is used to transfer the data for the Set request.

</dd> <dt>

*pCallback* \[in\]
</dt> <dd>

Callback object for the Bidi Set request.

</dd> <dt>

 *ppAsyncOperation* \[out, retval\]
</dt> <dd>

Context object associated with the asynchronous Bidi Set request (operation).

</dd> </dl>

## Return value

This method returns the appropriate **HRESULT** value.

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                             |
| Target platform<br/>          | <dl> <dt>Desktop</dt> </dl>            |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrinterBidiSetRequestCallback**](iprinterbidisetrequestcallback.md)
</dt> <dt>

[**IPrinterExtensionAsyncOperation**](iprinterextensionasyncoperation.md)
</dt> <dt>

[**IPrinterQueue2**](iprinterqueue2.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterQueue2::SendBidiSetRequestAsync%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





