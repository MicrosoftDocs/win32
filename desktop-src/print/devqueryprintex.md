---
Description: A printer interface DLLs DevQueryPrintEx function determines if a specified print job is compatible with the printers current configuration and can therefore be printed.
ms.assetid: f4cd0fe6-acdc-43e6-8dd7-7b547b1ec7cc
title: DevQueryPrintEx function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DevQueryPrintEx function

A printer interface DLL's **DevQueryPrintEx** function determines if a specified print job is compatible with the printer's current configuration and can therefore be printed.

## Syntax


```C++
BOOL DevQueryPrintEx(
  _Inout_ PDEVQUERYPRINT_INFO pDQPInfo
);
```



## Parameters

<dl> <dt>

*pDQPInfo* \[in, out\]
</dt> <dd>

Caller-supplied pointer to a [**DEVQUERYPRINT\_INFO**](devqueryprint-info.md) structure.

</dd> </dl>

## Return value

If the print job can be printed, the function should return **TRUE**; otherwise, it should return **FALSE**.

## Remarks

Printer interface DLLs must define a **DevQueryPrintEx** function. The function is called by the print spooler if the **Hold Mismatched Documents** option is checked on the **Advanced** page of the printer's property sheet. If the function returns **TRUE**, the spooler queues the print job for printing. Otherwise, the job is held, under the assumption that the printer will eventually be reconfigured so the job can print.

The received [**DEVQUERYPRINT\_INFO**](devqueryprint-info.md) structure points to a [**DEVMODEW**](display.devmodew) structure describing the printer characteristics required by the print job. The **DevQueryPrintEx** function should first verify that the size and version members of the received DEVMODEW structure are compatible with the driver. Then it should determine if the supplied DEVMODEW contents are compatible with the current printer configuration.

If the job can be printed, the function should just return **TRUE**. If the job should be held until later, the function should return **FALSE** after supplying a displayable text string (in the buffer pointed to by the DEVQUERYPRINT\_INFO structure's **pszErrorStr** member) describing the reason the job cannot be printed.

Displayable text strings should be defined as string resources in a resource file.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Winddiui.h (include Winddiui.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Winspool.lib</dt> </dl>                    |
| DLL<br/>             | <dl> <dt>WinSpool.drv</dt> </dl>                    |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DevQueryPrintEx%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




