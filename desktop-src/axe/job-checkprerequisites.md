---
title: Job CheckPrerequisites method
description: Retrieves a collection of unmet assessment prerequisites.
ms.assetid: 7de9bb18-5d1d-4384-91d7-40c8e7c84533
keywords:
- CheckPrerequisites method Access Execution Engine
- CheckPrerequisites method Access Execution Engine , Job interface
- Job interface Access Execution Engine , CheckPrerequisites method
topic_type:
- apiref
api_name:
- Job.CheckPrerequisites
api_location:
- AxeCore.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Job::CheckPrerequisites method

Retrieves a collection of unmet assessment prerequisites.

## Syntax


```C++
virtual HRESULT CheckPrerequisites(
  [out] PrerequisiteCollection **issues
) = 0;
```



## Parameters

<dl> <dt>

*issues* \[out\]
</dt> <dd>

A collection of prerequisites that did not pass. Prerequisites can be warnings or blocking issues. Both types are returned in the *issues* parameter.

</dd> </dl>

## Return value

If successful, this method returns **S\_OK**.

If there is insufficient memory to create an object, this method returns **E\_OUTOFMEMORY**.

If *issues* is null, this method returns **E\_POINTER**.

## Remarks

Assessment prerequisites are defined in the [**Properties**](properties.md) section of the assessment manifest.

Prerequisites can be warnings or blocking issues. Both types of prerequisite failures are returned in the issues parameter.

Managed code uses the [**Job.CheckPrerequisites \| checkPrerequisites**](axe-job_checkprerequisites_om) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Job**](job-if.md)
</dt> <dt>

[**PrerequisiteCollection**](prerequisitecollection.md)
</dt> <dt>

[**PrerequisiteIssue**](prerequisiteissue.md)
</dt> </dl>

 

 





