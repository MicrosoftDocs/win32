---
title: ProgressUpdateEventArgs structure
description: Represents information provided to a solution during the OnProgressUpdate callback.
ms.assetid: 3C3AEB9B-48F9-4973-ACD3-AACC38D67142
keywords:
- ProgressUpdateEventArgs structure Access Execution Engine
topic_type:
- apiref
api_name:
- ProgressUpdateEventArgs
api_location:
- AxeHosting.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# ProgressUpdateEventArgs structure

Represents information provided to a solution during the *OnProgressUpdate* callback.

## Syntax


```C++
struct ProgressUpdateEventArgs {
  DWORD            Size;
  INT              AssessmentIndex;
  const Assessment *Assessment;
  AxeProgressType  ProgressType;
  UINT             ProgressValue;
  LPCWSTR          ProgressMessage;
};
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

The number of bytes in the structure. Used to detect different versions of structure.

</dd> <dt>

**AssessmentIndex**
</dt> <dd>

The index of the assessment in the job s assessment list.

</dd> <dt>

**Assessment**
</dt> <dd>

A pointer to the assessment object.

</dd> <dt>

**ProgressType**
</dt> <dd>

The type of progress data that is contained within the other parameters. Client applications need to interpret the other parameters based on the value in this parameter.

</dd> <dt>

**ProgressValue**
</dt> <dd>

An integer value that is interpreted according to the **ProgressType** parameter.

</dd> <dt>

**ProgressMessage**
</dt> <dd>

A string that is interpreted according to the **ProgressType** parameter.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |



 

 





