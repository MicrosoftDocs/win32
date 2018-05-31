---
Description: The Subject property is a null-terminated string that contains the contents of the subject field on the cover page of the fax.
ms.assetid: 5909d09d-1874-4941-84a4-7bd7d7e1c2a6
title: FaxOutgoingJob.Subject property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutgoingJob.Subject property

The **Subject** property is a null-terminated string that contains the contents of the subject field on the cover page of the fax.

This property is read-only.

## Syntax


```VB
Property Subject As String
```



## Property value

A **String** that receives text that describes the subject of the fax transmission. The text appears on the cover page.

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

 

 




