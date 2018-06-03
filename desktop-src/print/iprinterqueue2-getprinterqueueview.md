---
Description: Retrieves an IPrinterQueueView object, and initializes the object with the range of jobs to be monitored.
ms.assetid: C565288C-B014-4A92-9F50-1641EAA30D22
title: IPrinterQueue2::GetPrinterQueueView method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrinterQueue2::GetPrinterQueueView method

Retrieves an [**IPrinterQueueView**](iprinterqueueview.md) object, and initializes the object with the range of jobs to be monitored.

This method allows the user to perform job management tasks from within a UWP device app for printers.

## Syntax


```C++
HRESULT GetPrinterQueueView(
  [in]          ULONG              ulViewOffset,
  [in]          ULONG              ulViewSize,
  [out, retval] IPrinterQueueView ** ppJobView 
);
```



## Parameters

<dl> <dt>

 *ulViewOffset* \[in\]
</dt> <dd>

Indicates the start of the range of jobs to be monitored.

</dd> <dt>

 *ulViewSize* \[in\]
</dt> <dd>

Indicates the size or the range of jobs to be monitored.

</dd> <dt>

 *ppJobView* \[out, retval\]
</dt> <dd>

IPrinterQueueView object that shows the range of jobs to be monitored.

</dd> </dl>

## Return value

If the method call is successful, **GetPrinterQueueView** returns S\_OK.

Otherwise, if a call to **GetPrinterQueueView** results in an error condition, then one of the following **HRESULT** values can be returned. 

| HRESULT value            | Description                                                               |
|--------------------------|---------------------------------------------------------------------------|
| E\_ILLEGAL\_METHOD\_CALL | Indicates an attempt to retrieve more than one printer queue view object. |
| E\_INVALIDARG            | Indicates an attempt to create a view size larger than the maximum size.  |



 

## Remarks

Only one [**IPrinterQueueView**](iprinterqueueview.md) object can be retrieved per [**IPrinterQueue2**](iprinterqueue2.md) object. However it is possible to move around the single view that you retrieve. In other words, it is possible to change the positions of the monitored jobs by invoking [**IPrinterQueueView::SetViewRange**](iprinterqueueview-setviewrange.md).

> [!Note]  
> There is work underway to implement a cap on the maximum size of the printer queue view.

 

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                             |
| Target platform<br/>          | <dl> <dt>Desktop</dt> </dl>            |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrinterQueue2**](iprinterqueue2.md)
</dt> <dt>

[**IPrinterQueueView**](iprinterqueueview.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrinterQueue2::GetPrinterQueueView%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





