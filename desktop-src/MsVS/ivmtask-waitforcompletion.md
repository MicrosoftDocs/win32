---
title: IVMTask WaitForCompletion method
description: The WaitForCompletion method waits for the task to complete or until the specified timeout expires.
ms.assetid: 56a943f9-881d-4233-8ee1-b6d6812f6582
keywords:
- WaitForCompletion method Virtual Server
- WaitForCompletion method Virtual Server , IVMTask interface
- IVMTask interface Virtual Server , WaitForCompletion method
topic_type:
- apiref
api_name:
- IVMTask.WaitForCompletion
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVMTask::WaitForCompletion method

The **WaitForCompletion** method waits for the task to complete or until the specified timeout expires.

## Syntax


```C++
HRESULT WaitForCompletion(
  [in] long timeout
);
```



## Parameters

<dl> <dt>

*timeout* \[in\]
</dt> <dd>

Specifies the time in milliseconds that this method will wait for the task completion before returning control to the caller. A value of -1 specifies that method will wait until the task completes without timing out. Other valid timeout values range from 0 to 4,000,000 milliseconds.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                       | Description                                                               |
|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>              | The operation was successful.<br/>                                  |
| <dl> <dt>**E\_POINTER**</dt> </dl>         | The *timeout* parameter was outside its valid range of values.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl> | An unexpected error occurred.<br/>                                  |



 

## Remarks

The **WaitForCompletion** method puts the current execution thread to sleep until it returns. Specifying an infinite wait (*timeout* = **-1**) is not recommended unless it is absolutely critical that the task completes under any circumstance.

## Examples

This example compacts a dynamic hard disk image using the specified timeout. It throws exceptions on any error back to the calling routine.


```C++
void CompactWithTimeout(IVMHardDIskPtr pIHD, long seconds){}
void CompactWithTimeout(IVMHardDiskPtr pIHD, long seconds) throw(/*...*/)
{
  try
  {
    // Check calling arguments, do not allow an infinite wait
    if (pIHD == NULL || seconds < 1)
    { 
        throw _com_error(E_POINTER); 
    }
    else 
    {
      try
      {
        IVMTaskPtr pITask = pIHD->Compact();     // start HD compaction
        pITask->WaitForCompletion(seconds*1000); // IVMTask timeout is in mSec
      }
      catch (/*...*/) {throw;}
    }
  }
  // toss error back to caller
  catch (/*...*/) {throw;}
}
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMTask**](ivmtask.md)
</dt> </dl>

 

 





