---
Description: 'Call the SetStatus method to pause, resume, cancel, or restart a specified fax job.'
ms.assetid: '32398e50-9771-46fe-b762-72662fda5a4e'
title: 'FaxJob.SetStatus method'
---

# FaxJob.SetStatus method

Call the **SetStatus** method to pause, resume, cancel, or restart a specified fax job.

## Syntax


```VB
FaxJob.SetStatus( _
  ByVal Command As Long _
) As Long
```



## Parameters

<dl> <dt>

*Command* \[in\]
</dt> <dd>

Type: **Long**

Specifies a **Long** variable that indicates the job command to perform. This parameter can be one of the following values.

<dt>

<span id="JC_DELETE"></span><span id="jc_delete"></span>

<span id="JC_DELETE"></span><span id="jc_delete"></span>**JC\_DELETE** (JC\_DELETE)


</dt> <dd>

Cancel the specified fax job. The job can be active or queued.

</dd> <dt>

<span id="JC_PAUSE"></span><span id="jc_pause"></span>

<span id="JC_PAUSE"></span><span id="jc_pause"></span>**JC\_PAUSE** (JC\_PAUSE)


</dt> <dd>

Pause the specified queued fax job. If the fax job is active, the fax service pauses the job when it returns to the queued state.

</dd> <dt>

<span id="JC_RESUME"></span><span id="jc_resume"></span>

<span id="JC_RESUME"></span><span id="jc_resume"></span>**JC\_RESUME** (JC\_RESUME)


</dt> <dd>

Resume the paused fax job.

</dd> <dt>

<span id="JC_RESTART"></span><span id="jc_restart"></span>

<span id="JC_RESTART"></span><span id="jc_restart"></span>**JC\_RESTART** (JC\_RESTART)


</dt> <dd>

Restart the specified fax job.

</dd> </dl> </dd> </dl>

## Remarks

You can use the [**QueueStatus**](-mfax-ifaxjob-get-queuestatus-vb.md) property to retrieve the job queue status of a fax job.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Faxcom.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Faxcom.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxJob**](-mfax-faxjob-object-visual-basic-.md)
</dt> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[Fax Service Client API Interfaces](-mfax-fax-service-client-api-interfaces.md)
</dt> <dt>

[**IFaxJob**](-mfax-ifaxjob.md)
</dt> <dt>

[**IFaxJobs**](-mfax-ifaxjobs.md)
</dt> <dt>

[**QueueStatus**](-mfax-ifaxjob-get-queuestatus-vb.md)
</dt> <dt>

[Managing Fax Jobs](-mfax-managing-fax-jobs.md)
</dt> </dl>

 

 




