---
Description: Provides an IPrintJobCollection object that provides a snapshot of a range of print jobs in the queue.
ms.assetid: D964A0C4-041A-47BD-87AB-4AF523939DF0
title: IPrinterQueueViewEventOnChanged method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrinterQueueViewEvent::OnChanged method

Provides an [**IPrintJobCollection**](iprintjobcollection.md) object that provides a snapshot of a range of print jobs in the queue.

## Syntax


```C++
HRESULT OnChanged(
  [in] IPrintJobCollection *pCollection,
  [in] ULONG               ulViewOffset,
  [in] ULONG               ulViewSize,
  [in] ULONG               ulCountJobsInPrintQueue
);
```



## Parameters

<dl> <dt>

*pCollection* \[in\]
</dt> <dd>

An [**IPrintJobCollection**](iprintjobcollection.md) object.

</dd> <dt>

*ulViewOffset* \[in\]
</dt> <dd>

The start of the range of jobs being monitored.

</dd> <dt>

*ulViewSize* \[in\]
</dt> <dd>

The range of jobs being monitored.

</dd> <dt>

*ulCountJobsInPrintQueue* \[in\]
</dt> <dd>

The current number of jobs in the print queue.

</dd> </dl>

## Return value

This method returns the appropriate **HRESULT** value.

## Remarks

The job range is controlled by the [**IPrinterQueueView**](iprinterqueueview.md) interface. Additionally, this method provides the current number of jobs in the print queue, and the indices of the job range being monitored. Information about the number of jobs, and the indices of the jobs is provided in response to the [**IPrinterQueueView::SetViewRange**](iprinterqueueview-setviewrange.md) method being invoked.

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                             |
| Target platform<br/>          | <dl> <dt>Desktop</dt> </dl>            |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrinterQueueView**](iprinterqueueview.md)
</dt> <dt>

[**IPrinterQueueViewEvent**](iprinterqueueviewevent.md)
</dt> <dt>

[**IPrinterQueueView::SetViewRange**](iprinterqueueview-setviewrange.md)
</dt> <dt>

[**IPrintJobCollection**](iprintjobcollection.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterQueueViewEvent::OnChanged%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





