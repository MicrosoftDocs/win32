---
Description: Called when a bidi response is received.
ms.assetid: D0CD9950-DF73-4D46-B901-FA45BA88D3CF
title: IPrinterQueueEvent::OnBidiResponseReceived method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrinterQueueEvent::OnBidiResponseReceived method

Called when a bidi response is received.

## Syntax


```C++
HRESULT OnBidiResponseReceived(
  [in] BSTR    bstrResponse,
  [in] HRESULT hrStatus
);
```



## Parameters

<dl> <dt>

*bstrResponse* \[in\]
</dt> <dd>

The received response.

</dd> <dt>

*hrStatus* \[in\]
</dt> <dd>

An HRESULT value.

</dd> </dl>

## Return value

This method returns an **HRESULT** value.

## Remarks

The *bstrResponse* parameter is formatted according to the schema that is described in [Bidi Request and Response Schemas](http://msdn.microsoft.com/en-us/library/windows/desktop/dd183368.aspx).

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Target platform<br/>          | <dl> <dt>Desktop</dt> </dl>            |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[Bidi Request and Response Schemas](http://msdn.microsoft.com/en-us/library/windows/desktop/dd183368.aspx)
</dt> <dt>

[**IPrinterQueue::SendBidiQuery**](iprinterqueue-sendbidiquery.md)
</dt> <dt>

[**IPrinterQueue**](iprinterqueue-interface.md)
</dt> <dt>

[**IPrinterQueueEvent**](iprinterqueueevent-interface.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterQueueEvent::OnBidiResponseReceived%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





