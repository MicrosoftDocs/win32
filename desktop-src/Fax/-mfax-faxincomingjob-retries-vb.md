---
Description: The Retries property is a value that indicates the number of times the fax service attempted to route an incoming fax when the initial routing attempt failed.
ms.assetid: 5a864bb4-4205-47bd-b370-0dbe048c4bb9
title: FaxIncomingJob.Retries property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxIncomingJob.Retries property

The **Retries** property is a value that indicates the number of times the fax service attempted to route an incoming fax when the initial routing attempt failed.

This property is read-only.

## Syntax


```VB
Property Retries As Long
```



## Property value

A **Long** that receives the number of times the fax service attempted to route an incoming fax when the initial routing attempt failed.

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

[**IFaxIncomingJob**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxincomingjob)
</dt> </dl>

 

 




