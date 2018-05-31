---
Description: The CurrentPage property is a number that identifies the page that the fax service is actively receiving on an inbound fax job.
ms.assetid: a259d9ea-f007-4909-b109-5861fa46b71d
title: FaxIncomingJob.CurrentPage property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxIncomingJob.CurrentPage property

The **CurrentPage** property is a number that identifies the page that the fax service is actively receiving on an inbound fax job.

This property is read-only.

## Syntax


```VB
Property CurrentPage As Long
```



## Property value

A **Long** that receives the number of the page in the inbound fax transmission that the fax service is currently receiving.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-the-incoming-queue.md)
</dt> <dt>

[**FaxIncomingJob**](-mfax-faxincomingjob.md)
</dt> <dt>

[**IFaxIncomingJob**](-mfax-faxincomingjob-cpp.md)
</dt> </dl>

 

 




