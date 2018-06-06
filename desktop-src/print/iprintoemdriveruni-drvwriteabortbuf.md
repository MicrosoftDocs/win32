---
Description: The IPrintOemDriverUni::DrvWriteAbortBuf method is provided by the Unidrv driver to allow an OEM rendering plug-in to send printer clean-up code after a user terminates a print job.
ms.assetid: 4f7aff9b-32cf-42a0-ba3b-ddc87ecdb8c3
title: IPrintOemDriverUni::DrvWriteAbortBuf method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPrintOemDriverUni::DrvWriteAbortBuf method

The `IPrintOemDriverUni::DrvWriteAbortBuf` method is provided by the Unidrv driver to allow an OEM [rendering plug-in](https://www.bing.com/search?q=rendering+plug-in) to send printer clean-up code after a user terminates a print job.

## Syntax


```C++
HRESULT DrvWriteAbortBuf(
   PDEVOBJ pdevobj,
   PVOID   pBuffer,
   DWORD   cbSize,
   DWORD   dwWait
);
```



## Parameters

<dl> <dt>

*pdevobj* 
</dt> <dd>

Caller-supplied pointer to a [**DEVOBJ**](devobj.md) structure.

</dd> <dt>

*pBuffer* 
</dt> <dd>

Caller-supplied pointer to a buffer containing a code fragment to be sent to the printer.

</dd> <dt>

*cbSize* 
</dt> <dd>

Caller-supplied number of bytes in the buffer pointed to by *pBuffer*.

</dd> <dt>

*dwWait* 
</dt> <dd>

Caller-supplied length of time the printer must wait, in milliseconds, before it can start a new print job after the current job is aborted.

</dd> </dl>

## Return value

The method must return one of the following values.



| Return code                                                                               | Description                               |
|-------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The operation succeeded.<br/>       |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | The operation failed.<br/>          |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | The method is not implemented.<br/> |



 

## Remarks

OEMs use [**IPrintOemDriverUni::DrvWriteSpoolBuf**](iprintoemdriveruni-drvwritespoolbuf.md) to send output to the printer. If a print job is terminated by the user, `IPrintOemDriverUni::DrvWriteSpoolBuf` returns E\_FAIL and can no longer be used to send any data to the printer. When this occurs, certain printers must have a clean-up code fragment sent to them, resetting their states before they can start new print jobs. For these printers, `IPrintOemDriverUni::DrvWritetAbortBuf` is used to send this code fragment to the printer.

`IPrintOemDriverUni::DrvWriteAbortBuf` can only be called after `IPrintOemDriverUni::DrvWriteSpoolBuf` has returned E\_FAIL. `IPrintOemDriverUni::DrvWriteAbortBuf` should not be called more than once per job.

Rendering plug-ins are described in [Customizing Microsoft's Printer Drivers](https://www.bing.com/search?q=Customizing+Microsoft's+Printer+Drivers).

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemDriverUni::DrvWriteAbortBuf%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




