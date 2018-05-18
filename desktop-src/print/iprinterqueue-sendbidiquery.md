---
Description: 'Performs an asynchronous refresh operation with the specified query, and invokes the IPrinterQueueEvent::OnBidiResponseReceived method.'
ms.assetid: 'E98A121A-514A-4437-A542-E8629697B7EA'
title: 'IPrinterQueue::SendBidiQuery method'
---

# IPrinterQueue::SendBidiQuery method

Performs an asynchronous refresh operation with the specified query, and invokes the [**IPrinterQueueEvent::OnBidiResponseReceived**](iprinterqueueevent-onbidiresponsereceived.md) method.

## Syntax


```C++
HRESULT SendBidiQuery(
  [in] BSTR bstrBidiQuery
);
```



## Parameters

<dl> <dt>

*bstrBidiQuery* \[in\]
</dt> <dd>

The specified query.

</dd> </dl>

## Return value

This method returns an **HRESULT** value.

## Remarks

When the **SendBidiQuery** method is called, it immediately raises the [**IPrinterQueueEvent::OnBidiResponseReceived**](iprinterqueueevent-onbidiresponsereceived.md) event, if there is a cached response available. The print system then starts an asynchronous operation to use the [Bidi Communication Interfaces](http://msdn.microsoft.com/en-us/library/dd183365). At this point **SendBidiQuery** returns, thus unblocking the caller. When the asynchronous operation completes, the print system raises the **IPrinterQueueEvent::OnBidiResponseReceived** event again. **SendBidiQuery** is decoupled from its associated response on purpose. The decoupling is done because, in the case where there is no cached data, the resulting latency can be due to many factors and an immediate response cannot be expected. Additionally the caller may receive multiple responses based on whether there is cached data, and whether there is a response from the device.

Using the [Bidi Communication Interfaces](http://msdn.microsoft.com/en-us/library/dd183365) causes the port monitor to refresh the underlying requested values. In the case of USB, if a JavaScript component is available, then the JavaScript code is invoked to refresh the requested values.

The cache is also updated in the following situations:

**At predetermined intervals**

<dl> For WSD devices the data is updated when the device reports changes via events.  
For TCP & USB devices the refresh interval is based on where the Bidi value is defined. All standard Bidi values (as defined by the port monitor’s embedded Bidi files) are refreshed at an interval that is preset by the port monitors. If the specific Bidi Query is part of the IHV Bidi Extension, then the refresh interval is specified in the XML extension file for each individual value.  
</dl>

**When printer configuration changes**

<dl> For example, when a WSD-based device raises an event to let the spooler (WSDMon) know that something about the device has changed. In other words, the printer configuration has changed.  
</dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Target platform<br/>          | <dl> <dt>Desktop</dt> </dl>            |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[Bidi Communication Interfaces](http://msdn.microsoft.com/en-us/library/dd183365)
</dt> <dt>

[**IPrinterQueue**](iprinterqueue-interface.md)
</dt> <dt>

[**IPrinterQueueEvent::OnBidiResponseReceived**](iprinterqueueevent-onbidiresponsereceived.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterQueue::SendBidiQuery%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





