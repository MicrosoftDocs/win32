---
Description: A print processor's ControlPrintProcessor function allows the spooler to control a print job.
ms.assetid: a0a19747-ab39-4606-a49b-78e5e056da32
title: ControlPrintProcessor function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ControlPrintProcessor function

A print processor's **ControlPrintProcessor** function allows the spooler to control a print job.

## Syntax


```C++
BOOL ControlPrintProcessor(
  _In_ HANDLE hPrintProcessor,
  _In_ DWORD  Command
);
```



## Parameters

<dl> <dt>

*hPrintProcessor* \[in\]
</dt> <dd>

Caller-supplied print processor handle. This is the handle returned by a previous call to [**OpenPrintProcessor**](openprintprocessor.md).

</dd> <dt>

*Command* \[in\]
</dt> <dd>

Caller-supplied command indicating the type of operation to perform. The following commands are valid:



| Command                         | Definition                                                   |
|---------------------------------|--------------------------------------------------------------|
| JOB\_CONTROL\_CANCEL<br/> | The function should cancel the current print job.<br/> |
| JOB\_CONTROL\_PAUSE<br/>  | The function should pause the current print job.<br/>  |
| JOB\_CONTROL\_RESUME<br/> | The function should resume the current print job.<br/> |



 

</dd> </dl>

## Return value

If the operation succeeds, the function should return **TRUE**. If the operation fails, the function should call SetLastError to set an error code, and then return **FALSE**.

## Remarks

Print processors are required to export a **ControlPrintProcessor** function. The spooler calls the function when an application calls the SetJob function, described in the Microsoft Windows SDK documentation.

Based on the value received for *Command*, the function should either pause, resume, or cancel the current job. The **ControlPrintProcessor** function can be called asynchronously while the print processor's [**PrintDocumentOnPrintProcessor**](printdocumentonprintprocessor.md) function is executing. Thus some sort of synchronization technique must be employed, such as setting an internally-defined event object to pause a job and resetting the event object when the job is resumed. The **ControlPrintProcessor** function can quickly return after setting or resetting the event object, and PrintDocumentOnPrintProcessor can wait for the event to be in the proper state.

## Requirements



|                            |                                                                                                          |
|----------------------------|----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                       |
| Header<br/>          | <dl> <dt>Winsplp.h (include Winsplp.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Nwprint.lib</dt> </dl>                   |



## See also

<dl> <dt>

[**OpenPrintProcessor**](openprintprocessor.md)
</dt> <dt>

[**PrintDocumentOnPrintProcessor**](printdocumentonprintprocessor.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20ControlPrintProcessor%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





