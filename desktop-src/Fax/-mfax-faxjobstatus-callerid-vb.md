---
Description: The CallerId property is a null-terminated string that identifies the calling device associated with the fax job.
ms.assetid: 4350ba4e-5b3f-419e-b2d2-8d75f3aaa29e
title: FaxJobStatus.CallerId property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxJobStatus.CallerId property

The **CallerId** property is a null-terminated string that identifies the calling device associated with the fax job.

This property is read-only.

## Syntax


```VB
Property CallerId As String
```



## Property value

A **String** that receives the caller ID for the fax job. The string identifies the calling device associated with the fax transmission.

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

 

 




