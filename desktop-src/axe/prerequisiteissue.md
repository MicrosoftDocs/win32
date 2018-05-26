---
title: PrerequisiteIssue structure
description: This structure defines the data for a single failed prerequisite check.
ms.assetid: E7BC5590-8CFD-4247-8DAE-3CA41E897B8D
keywords:
- PrerequisiteIssue structure Access Execution Engine
topic_type:
- apiref
api_name:
- PrerequisiteIssue
api_location:
- AxeCore.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PrerequisiteIssue structure

This structure defines the data for a single failed prerequisite check.

## Syntax


```C++
struct PrerequisiteIssue {
  DWORD                                             Size;
  const Microsoft::Assessments::Hosting::Assessment *Assessment;
  IssueType                                         IssueType;
  LPCWSTR                                           ProgrammaticName;
  LPCWSTR                                           Name;
  LPCWSTR                                           ToolTip;
};
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

The number of bytes in the structure. Used to detect different versions of structure. This is set to "sizeof( PrerequisiteIssue )" by the AXE engine.

</dd> <dt>

**Assessment**
</dt> <dd>

The assessment object that failed the prerequisite check.

</dd> <dt>

**IssueType**
</dt> <dd>

The severity of the issue.

</dd> <dt>

**ProgrammaticName**
</dt> <dd>

The XML node of the prerequisite check in the assessment manifest that failed.

</dd> <dt>

**Name**
</dt> <dd>

The name of the issue for displaying in a user interface. The name can be localized.

</dd> <dt>

**ToolTip**
</dt> <dd>

Additional explanation of the issue that can be displayed in a user interface tooltip.

</dd> </dl>

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                              |
| Header<br/>                   | <dl> <dt>AxeCore.h</dt> </dl> |



 

 





