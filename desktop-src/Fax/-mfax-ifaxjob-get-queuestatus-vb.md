---
Description: The QueueStatus property is a null-terminated string that describes the job queue status of the fax job.
ms.assetid: c94d2da0-f304-4892-8d88-e3ff3aca67c7
title: FaxJob.QueueStatus property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxJob.QueueStatus property

The **QueueStatus** property is a null-terminated string that describes the job queue status of the fax job.

This property is read-only.

## Syntax


```VB
Property QueueStatus As String
```



## Property value

A **String** that receives the queue status of the specified fax job. Following are the English string equivalents.

<dt>

<span id="Pending"></span><span id="pending"></span><span id="PENDING"></span>

<span id="Pending"></span><span id="pending"></span><span id="PENDING"></span>**Pending** (Pending)


</dt> <dd>

The fax job is in the queue and pending service.

</dd> <dt>

<span id="In_Progress"></span><span id="in_progress"></span><span id="IN_PROGRESS"></span>

<span id="In_Progress"></span><span id="in_progress"></span><span id="IN_PROGRESS"></span>**In Progress** (In Progress)


</dt> <dd>

The fax job is in progress.

</dd> <dt>

<span id="Deleting"></span><span id="deleting"></span><span id="DELETING"></span>

<span id="Deleting"></span><span id="deleting"></span><span id="DELETING"></span>**Deleting** (Deleting)


</dt> <dd>

The fax server is deleting the fax job.

</dd> <dt>

<span id="Failed"></span><span id="failed"></span><span id="FAILED"></span>

<span id="Failed"></span><span id="failed"></span><span id="FAILED"></span>**Failed** (Failed)


</dt> <dd>

The fax job failed.

</dd> <dt>

<span id="Paused"></span><span id="paused"></span><span id="PAUSED"></span>

<span id="Paused"></span><span id="paused"></span><span id="PAUSED"></span>**Paused** (Paused)


</dt> <dd>

The fax server paused the fax job.

</dd> <dt>

<span id="No_Line"></span><span id="no_line"></span><span id="NO_LINE"></span>

<span id="No_Line"></span><span id="no_line"></span><span id="NO_LINE"></span>**No Line** (No Line)


</dt> <dd>

There is no line available to send the fax. The fax server will send the transmission when a line is available.

</dd> <dt>

<span id="Retrying"></span><span id="retrying"></span><span id="RETRYING"></span>

<span id="Retrying"></span><span id="retrying"></span><span id="RETRYING"></span>**Retrying** (Retrying)


</dt> <dd>

The fax job failed. The fax server will attempt to retransmit the fax after a specified interval.

</dd> <dt>

<span id="Retries_Exceeded"></span><span id="retries_exceeded"></span><span id="RETRIES_EXCEEDED"></span>

<span id="Retries_Exceeded"></span><span id="retries_exceeded"></span><span id="RETRIES_EXCEEDED"></span>**Retries Exceeded** (Retries Exceeded)


</dt> <dd>

The fax server exceeded the maximum number of retransmission attempts allowed. The fax will not be sent.

</dd> </dl>

## Remarks

> [!Note]  
> The **Deleting**, **Failed**, **Paused**, **No Line**, **Retrying**, and **Retries Exceeded** values are supported only in Windows XP with Service Pack 1 installed, and in Windows Server 2003.

 

**QueueStatus** allocates the memory required for the buffer pointed to by the *pVal* parameter. The client application must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with this parameter. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

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

[**IFaxJob**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxjob?branch=master)
</dt> <dt>

[**IFaxJobs**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxjobs?branch=master)
</dt> </dl>

 

 




