---
title: BG_JOB_TIMES structure (Deliveryoptimization.h)
description: The BG_JOB_TIMES structure provides job-related time stamps.
ms.assetid: 0147478F-C850-4B66-AB15-042C1A81D6B5
keywords:
- BG_JOB_TIMES structure
topic_type:
- apiref
api_name:
- BG_JOB_TIMES
api_location:
- deliveryoptimization.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# BG_JOB_TIMES structure

The **BG_JOB_TIMES** structure provides job-related time stamps.

## Syntax


```C++
typedef struct _BG_JOB_TIMES {
  FILETIME CreationTime;
  FILETIME ModificationTime;
  FILETIME TransferCompletionTime;
} BG_JOB_TIMES;
```



## Members

<dl> <dt>

**CreationTime**
</dt> <dd>

Time the job was created. The time is specified as [FILETIME](/windows/win32/api/minwinbase/ns-minwinbase-filetime).

</dd> <dt>

**ModificationTime**
</dt> <dd>

Time the job was last modified or bytes were transferred. Adding files or calling any of the set methods in the [**IBackgroundCopyJob\***](/previous-versions//mt811348(v=vs.85)) interfaces changes this value. In addition, changes to the state of the job and calling the [**Suspend**](ibackgroundcopyjob-suspend.md), [**Resume**](ibackgroundcopyjob-resume.md), [**Cancel**](ibackgroundcopyjob-cancel.md), and [**Complete**](ibackgroundcopyjob-complete.md) methods change this value. The time is specified as [FILETIME](/windows/win32/api/minwinbase/ns-minwinbase-filetime).

</dd> <dt>

**TransferCompletionTime**
</dt> <dd>

Time the job entered the BG_JOB_STATE_TRANSFERRED state. The time is specified as [FILETIME](/windows/win32/api/minwinbase/ns-minwinbase-filetime).

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl> |



## See also

<dl> <dt>

[**IBackgroundCopyJob::GetTimes**](ibackgroundcopyjob-gettimes.md)
</dt> </dl>

 

