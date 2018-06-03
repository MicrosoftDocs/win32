---
title: IProgressUpdateEventHandler OnProgressUpdate method
description: The AXE Core raises this event to notify the solution of the current progress reported by the assessment.
ms.assetid: 08F35E50-1A69-420A-AE53-95B468D278A6
keywords:
- OnProgressUpdate method Access Execution Engine
- OnProgressUpdate method Access Execution Engine , IProgressUpdateEventHandler interface
- IProgressUpdateEventHandler interface Access Execution Engine , OnProgressUpdate method
topic_type:
- apiref
api_name:
- IProgressUpdateEventHandler .OnProgressUpdate
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IProgressUpdateEventHandler ::OnProgressUpdate method

The AXE Core raises this event to notify the solution of the current progress reported by the assessment.

## Syntax


```C++
virtual void OnProgressUpdate(
             Engine                  *sender,
  [in] const ProgressUpdateEventArgs *e
) = 0;
```



## Parameters

<dl> <dt>

*sender* 
</dt> <dd>

The [**Engine**](engine-if.md) object that raised the event.

</dd> <dt>

*e* \[in\]
</dt> <dd>

The [ProgressUpdateEventArgs](progressupdateeventargs.md) structure that contains information about the current progress.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The parameter of this method allows the assessment to report many different types of progress to a solution application. Percentage indicators, graphical spinners, textual and numerical phases can be used to represent some of the progress information reported by the assessment.

This method is only called by the AXE Engine.

Managed code uses the [**ProgressUpdateEventHandler**](https://www.bing.com/search?q=**ProgressUpdateEventHandler**) delegate.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IProgressUpdateEventHandler**](iprogressupdateeventhandler.md)
</dt> </dl>

 

 





