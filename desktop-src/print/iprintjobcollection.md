---
Description: This interfaces provides an enumeration of the jobs in the print queue.
ms.assetid: 757328A6-DD2C-4057-820B-39EB83277194
title: IPrintJobCollection interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IPrintJobCollection interface

This interfaces provides an enumeration of the jobs in the print queue.

The enumerated list of jobs represents a snapshot of the current job status.

## Members

The **IPrintJobCollection** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/windows/desktop/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IPrintJobCollection** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IPrintJobCollection** interface has these methods.



| Method                                     | Description                                                            |
|:-------------------------------------------|:-----------------------------------------------------------------------|
| [**GetAt**](iprintjobcollection-getat.md) | Gets a pointer to an [**IPrintJob**](iprintjob.md) object.<br/> |



 

### Properties

The **IPrintJobCollection** interface has these properties.



| Property                                                  | Access type          | Description                                                                     |
|:----------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------|
| [**Count**](iprintjobcollection-count.md)<br/>     | Read-only<br/> | Gets the number of jobs in the print queue.<br/>                          |
| [**NewEnum**](iprintjobcollection-newenum.md)<br/> | Read-only<br/> | Gets a pointer to the enumerants of **IPrintJobCollection** objects.<br/> |



 

## Remarks

The order of print jobs in the enumerated list is the same as the order provided by [EnumJobs](http://msdn.microsoft.com/en-us/library/windows/desktop/dd162625.aspx), which is the actual print queue order.

**IPrintJobCollection** also helps to make it possible to perform job management from a UWP device app or from a printer extension. For more information, see [Job Management](https://www.bing.com/search?q=Job Management).

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                             |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[EnumJobs](http://msdn.microsoft.com/en-us/library/windows/desktop/dd162625.aspx)
</dt> <dt>

[Job Management](https://www.bing.com/search?q=Job Management)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintJobCollection%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





