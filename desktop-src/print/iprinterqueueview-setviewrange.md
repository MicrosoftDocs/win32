---
Description: 'Sets the range of print jobs being monitored.'
ms.assetid: 'DB3C0439-EB82-4E49-8FEA-003C1B4A9EE0'
title: 'IPrinterQueueView::SetViewRange method'
---

# IPrinterQueueView::SetViewRange method

Sets the range of print jobs being monitored.

## Syntax


```C++
HRESULT SetViewRange(
  [in] ULONG ulViewOffset,
  [in] ULONG ulViewSize
);
```



## Parameters

<dl> <dt>

*ulViewOffset* \[in\]
</dt> <dd>

The start of the range of jobs being monitored. Note that the offset value uses a zero-based index.

</dd> <dt>

*ulViewSize* \[in\]
</dt> <dd>

The size of the range of jobs being monitored.

</dd> </dl>

## Return value

This method returns the appropriate **HRESULT** value.

## Remarks

Invoking this method causes the events for status change to the jobs to be fired. The [**IPrinterQueueViewEvent::OnChanged**](iprinterqueueviewevent-onchanged.md) event method returns the live queue in response, using the specified maximum range size.

> [!Note]  
> *ulViewSize* must be specified as a value less than or equal to 25. If the caller specifies a size which exceeds 25, this method will return E\_INVALIDARG.

 

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                             |
| Target platform<br/>          | <dl> <dt>Desktop</dt> </dl>            |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrinterQueue2::GetPrinterQueueView**](iprinterqueue2-getprinterqueueview.md)
</dt> <dt>

[**IPrinterQueueView**](iprinterqueueview.md)
</dt> <dt>

[**IPrinterQueueViewEvent::OnChanged**](iprinterqueueviewevent-onchanged.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterQueueView::SetViewRange%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





