---
Description: Gets the number of pages that have been printed.
ms.assetid: 37F09500-1EDB-459D-8845-789734081B0C
title: IPrintJobPrintedPages property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPrintJob::PrintedPages property

Gets the number of pages that have been printed.

This property is read-only.

## Syntax


```C++
HRESULT get_PrintedPages(
  [out, retval] ULONG *pulPages
);
```



## Property value

The number of pages that have been printed.

## Remarks

If the **PrintedPages** and [**IPrintJob::TotalPages**](iprintjob-totalpages.md) properties are both zero, then page delimiting is not supported for the print job.

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                             |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrintJob::IPrintJob**](iprintjob.md)
</dt> <dt>

[**TotalPages**](iprintjob-totalpages.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintJob::PrintedPages%20property%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





