---
Description: The CSID property is a null-terminated string that contains the called station identifier (CSID) for the job.
ms.assetid: 33fe8ba9-9836-4951-a934-e451b83a61ab
title: FaxJobStatus.CSID property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxJobStatus.CSID property

The **CSID** property is a null-terminated string that contains the called station identifier (CSID) for the job.

This property is read-only.

## Syntax


```VB
Property CSID As String
```



## Property value

A **String** that receives the CSID for the fax job.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-registering-for-fax-events.md)
</dt> <dt>

[**FaxJobStatus**](-mfax-faxjobstatus.md)
</dt> <dt>

[**IFaxJobStatus**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxjobstatus)
</dt> </dl>

 

 




