---
Description: The Resume method resumes the paused outbound fax job.
ms.assetid: be4a7cb5-7e25-4356-92e2-829bcb84660f
title: FaxOutgoingJob.Resume method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxOutgoingJob.Resume method

The **Resume** method resumes the paused outbound fax job.

## Syntax


```VB
FaxOutgoingJob.Resume() As Long
```



## Parameters

This method has no parameters.

## Remarks

To use this method, a user must have the [**farSUBMIT\_LOW**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) or **farMANAGE\_JOBS** access right. With the **farSUBMIT\_LOW** access right, users will be able to use this method only for their own faxes. With the **farMANAGE\_JOBS** access right, users will be able to use this method for all faxes on the server.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-outgoing-jobs.md)
</dt> <dt>

[**FaxOutgoingJob**](-mfax-faxoutgoingjob.md)
</dt> <dt>

[**IFaxOutgoingJob**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxoutgoingjob?branch=master)
</dt> </dl>

 

 




