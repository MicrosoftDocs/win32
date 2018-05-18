---
Description: 'This enumeration is a one-to-one mapping to the spooler flags suppled in the JOB\_INFO\_X structures.'
ms.assetid: '856FDAE1-C1D9-458D-B386-0A2D8612EA33'
title: PrintJobStatus enumeration
---

# PrintJobStatus enumeration

This enumeration is a one-to-one mapping to the spooler flags suppled in the JOB\_INFO\_X structures.

For example, [JOB\_INFO\_1](http://msdn.microsoft.com/en-us/library/windows/desktop/dd145019.aspx) has the same set of status flags as shown in the following list.

## Syntax


```C++
typedef enum _PrintJobStatus { 
  PrintJobStatus_Paused              = 0x1,
  PrintJobStatus_Error               = 0x2,
  PrintJobStatus_Deleting            = 0x4,
  PrintJobStatus_Spooling            = 0x8,
  PrintJobStatus_Printing            = 0x10,
  PrintJobStatus_Offline             = 0x20,
  PrintJobStatus_PaperOut            = 0x40,
  PrintJobStatus_Printed             = 0x80,
  PrintJobStatus_Deleted             = 0x100,
  PrintJobStatus_BlockedDeviceQueue  = 0x200,
  PrintJobStatus_UserIntervention    = 0x400,
  PrintJobStatus_Restarted           = 0x800,
  PrintJobStatus_Complete            = 0x1000,
  PrintJobStatus_Retained            = 0x2000
} PrintJobStatus;
```



## Constants

<dl> <dt>

<span id="PrintJobStatus_Paused"></span><span id="printjobstatus_paused"></span><span id="PRINTJOBSTATUS_PAUSED"></span>**PrintJobStatus\_Paused**
</dt> <dd>

The job is paused.

</dd> <dt>

<span id="PrintJobStatus_Error"></span><span id="printjobstatus_error"></span><span id="PRINTJOBSTATUS_ERROR"></span>**PrintJobStatus\_Error**
</dt> <dd>

There is an error associated with the job.

</dd> <dt>

<span id="PrintJobStatus_Deleting"></span><span id="printjobstatus_deleting"></span><span id="PRINTJOBSTATUS_DELETING"></span>**PrintJobStatus\_Deleting**
</dt> <dd>

The job is being deleted.

</dd> <dt>

<span id="PrintJobStatus_Spooling"></span><span id="printjobstatus_spooling"></span><span id="PRINTJOBSTATUS_SPOOLING"></span>**PrintJobStatus\_Spooling**
</dt> <dd>

The job is spooling.

</dd> <dt>

<span id="PrintJobStatus_Printing"></span><span id="printjobstatus_printing"></span><span id="PRINTJOBSTATUS_PRINTING"></span>**PrintJobStatus\_Printing**
</dt> <dd>

The job is printing.

</dd> <dt>

<span id="PrintJobStatus_Offline"></span><span id="printjobstatus_offline"></span><span id="PRINTJOBSTATUS_OFFLINE"></span>**PrintJobStatus\_Offline**
</dt> <dd>

The printer is offline.

</dd> <dt>

<span id="PrintJobStatus_PaperOut"></span><span id="printjobstatus_paperout"></span><span id="PRINTJOBSTATUS_PAPEROUT"></span>**PrintJobStatus\_PaperOut**
</dt> <dd>

The printer is out of paper.

</dd> <dt>

<span id="PrintJobStatus_Printed"></span><span id="printjobstatus_printed"></span><span id="PRINTJOBSTATUS_PRINTED"></span>**PrintJobStatus\_Printed**
</dt> <dd>

The job printing is completed.

</dd> <dt>

<span id="PrintJobStatus_Deleted"></span><span id="printjobstatus_deleted"></span><span id="PRINTJOBSTATUS_DELETED"></span>**PrintJobStatus\_Deleted**
</dt> <dd>

The job has been deleted.

</dd> <dt>

<span id="PrintJobStatus_BlockedDeviceQueue"></span><span id="printjobstatus_blockeddevicequeue"></span><span id="PRINTJOBSTATUS_BLOCKEDDEVICEQUEUE"></span>**PrintJobStatus\_BlockedDeviceQueue**
</dt> <dd>

The driver cannot print the job.

</dd> <dt>

<span id="PrintJobStatus_UserIntervention"></span><span id="printjobstatus_userintervention"></span><span id="PRINTJOBSTATUS_USERINTERVENTION"></span>**PrintJobStatus\_UserIntervention**
</dt> <dd>

The printer has an error that requires intervention from the user.

</dd> <dt>

<span id="PrintJobStatus_Restarted"></span><span id="printjobstatus_restarted"></span><span id="PRINTJOBSTATUS_RESTARTED"></span>**PrintJobStatus\_Restarted**
</dt> <dd>

The job has been restarted.

</dd> <dt>

<span id="PrintJobStatus_Complete"></span><span id="printjobstatus_complete"></span><span id="PRINTJOBSTATUS_COMPLETE"></span>**PrintJobStatus\_Complete**
</dt> <dd>

The job data transfer to the printer is complete. Note that the printing of the job may not yet be complete.

</dd> <dt>

<span id="PrintJobStatus_Retained"></span><span id="printjobstatus_retained"></span><span id="PRINTJOBSTATUS_RETAINED"></span>**PrintJobStatus\_Retained**
</dt> <dd>

The job has been retained in the print queue and cannot be deleted.

</dd> </dl>

## Remarks

A **PrintJobStatus\_Retained** flag can be raised for several reasons. For example, jobs could be kept in the queue if the administrator of the queue used the desktop print queue UI to set the “Keep Printed Jobs” feature to be on.

It is possible for a job to have multiple flag values specified simultaneously.

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                             |
| Header<br/>                   | <dl> <dt>Printerextension.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrintJob::Status**](iprintjob-status.md)
</dt> <dt>

[JOB\_INFO\_1](http://msdn.microsoft.com/en-us/library/windows/desktop/dd145019.aspx)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PrintJobStatus%20enumeration%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





