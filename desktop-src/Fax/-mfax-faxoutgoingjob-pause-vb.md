---
Description: The Pause method pauses the outbound fax job.
ms.assetid: 247d5778-cb04-4e72-bd05-46913904661e
title: FaxOutgoingJob.Pause method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutgoingJob.Pause method

The **Pause** method pauses the outbound fax job.

## Syntax


```VB
FaxOutgoingJob.Pause() As Long
```



## Parameters

This method has no parameters.

## Remarks

Use the [**Resume**](-mfax-faxoutgoingjob-resume-vb.md) method to resume a fax job after it has been paused.

To use this method, a user must have the [**farSUBMIT\_LOW**](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum) or **farMANAGE\_JOBS** access right. With the **farSUBMIT\_LOW** access right, users will be able to use this method only for their own faxes. With the **farMANAGE\_JOBS** access right, users will be able to use this method for all faxes on the server.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxOutgoingJob**](-mfax-faxoutgoingjob.md)
</dt> </dl>

 

 




