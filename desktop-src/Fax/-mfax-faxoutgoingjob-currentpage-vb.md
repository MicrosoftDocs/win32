---
Description: The CurrentPage property is a number that identifies the page that the fax service is actively transmitting on an outbound fax job.
ms.assetid: 5fa69801-e386-4fce-9601-b75d9a73e579
title: FaxOutgoingJob.CurrentPage property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutgoingJob.CurrentPage property

The **CurrentPage** property is a number that identifies the page that the fax service is actively transmitting on an outbound fax job.

This property is read-only.

## Syntax


```VB
Property CurrentPage As Long
```



## Property value

A **Long** that receives the number of the page in the outbound fax transmission that the fax service is currently transmitting.

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

[**IFaxOutgoingJob**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxoutgoingjob)
</dt> </dl>

 

 




