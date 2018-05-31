---
Description: Retrieves the submission identifier for the fax document.
ms.assetid: 13224162-3df7-4c69-ba9b-d7c839546f3e
title: FaxDocument.SubmissionId property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDocument.SubmissionId property

Retrieves the submission identifier for the fax document. Every job in a given broadcast receives the same submission identifier.

> [!Note]  
> This property is supported only in Windows Vista and later.

 

This property is read-only.

## Syntax


```VB
Property SubmissionId As String
```



## Property value

A **String** that receives a submission identifier of the fax document.

## Remarks

This property is set whenever a method that submits a fax completes.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxDocument**](-mfax-faxdocument.md)
</dt> <dt>

[**IFaxDocument2**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxdocument2)
</dt> </dl>

 

 




