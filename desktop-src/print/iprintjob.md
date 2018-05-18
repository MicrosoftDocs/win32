---
Description: 'Contains properties that represent a print job.'
ms.assetid: '068E53EC-26B8-48E7-A605-081709C94043'
title: IPrintJob interface
---

# IPrintJob interface

Contains properties that represent a print job.

This interface also provides a method that allows a print job to be cancelled.

## Members

The **IPrintJob** interface inherits from the [**IUnknown**](com.iunknown) interface. **IPrintJob** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IPrintJob** interface has these methods.



| Method                                           | Description                                          |
|:-------------------------------------------------|:-----------------------------------------------------|
| [**RequestCancel**](iprintjob-requestcancel.md) | Requests the cancellation of a print job.<br/> |
| [**Status**](iprintjob-status.md)               | Gets the current status of the print job.<br/> |



 

### Properties

The **IPrintJob** interface has these properties.



| Property                                                      | Access type          | Description                                                                                                                                           |
|:--------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Id**](iprintjob-id.md)<br/>                         | Read-only<br/> | Gets the print job identifier (ID).<br/>                                                                                                        |
| [**Name**](iprintjob-name.md)<br/>                     | Read-only<br/> | Gets the name of the print job.<br/>                                                                                                            |
| [**PrintedPages**](iprintjob-printedpages.md)<br/>     | Read-only<br/> | Gets the number of pages that have been printed.<br/>                                                                                           |
| [**SubmissionTime**](iprintjob-submissiontime.md)<br/> | Read-only<br/> | Gets the submission time, in the “DATE” format, provided in the user’s local time (not in the UTC format that is provided by the spooler).<br/> |
| [**TotalPages**](iprintjob-totalpages.md)<br/>         | Read-only<br/> | Gets the total number of pages that the document contains.<br/>                                                                                 |



 

## Remarks

The **IPrintJob** interface provides a wrapper around select properties of the spooler’s [JOB\_INFO\_1](http://msdn.microsoft.com/en-us/library/windows/desktop/dd145019.aspx) structure.

**IPrintJob** also helps to make it possible to perform job management from a UWP device app or from a printer extension. For more information, see [Job Management](print.job_management).

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                             |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[Job Management](print.job_management)
</dt> <dt>

[JOB\_INFO\_1](http://msdn.microsoft.com/en-us/library/windows/desktop/dd145019.aspx)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintJob%20interface%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





