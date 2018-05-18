---
Description: 'This structure contains the type of event to log (eEventType), the job ID, and the data required by the event.'
ms.assetid: 'B49FEED5-C90A-4E4F-9B73-E06E56FB4311'
title: BranchOfficeJobData structure
---

# BranchOfficeJobData structure

This structure contains the type of event to log (eEventType), the job ID, and the data required by the event.

## Syntax


```C++
typedef struct {
  EBranchOfficeJobEventType eEventType;
  DWORD                     JobId;
  union {
    BranchOfficeJobDataPrinted        LogJobPrinted;
    BranchOfficeJobDataRendered       LogJobRendered;
    BranchOfficeJobDataError          LogJobError;
    BranchOfficeJobDataPipelineFailed LogPipelineFailed;
    BranchOfficeLogOfflineFileFull    LogOfflineFileFull;
  } JobInfo;
} BranchOfficeJobData, *PBranchOfficeJobData;
```



## Members

<dl> <dt>

**eEventType**
</dt> <dd>

Specifies the type of event to be logged.

</dd> <dt>

**JobId**
</dt> <dd>

Specifies the ID of the job on the client.

</dd> <dt>

**JobInfo**
</dt> <dd> <dl> <dt>

**LogJobPrinted**
</dt> <dd>

Describes the **BranchOfficeJobDataPrinted** type member **LogJobPrinted**.

</dd> <dt>

**LogJobRendered**
</dt> <dd>

Describes the **BranchOfficeJobDataRendered** type member **LogJobRendered**.

</dd> <dt>

**LogJobError**
</dt> <dd>

Describes the **BranchOfficeJobDataError** type member **LogJobError**.

</dd> <dt>

**LogPipelineFailed**
</dt> <dd>

Describes the **BranchOfficeJobDataPipelineFailed** type member **LogPipelineFailed**.

</dd> <dt>

**LogOfflineFileFull**
</dt> <dd>

Describes the **BranchOfficeLogOfflineFileFull** type member **LogOfflineFileFull**.

</dd> </dl> </dd> </dl>

## Requirements



|                   |                                                                                      |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winsplp.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20BranchOfficeJobData%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




