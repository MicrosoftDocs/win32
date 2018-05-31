---
Description: Specifies if the fax has a cover page.
ms.assetid: beaa5a29-e184-43e3-b532-d8a4a9b28a09
title: FaxOutgoingJob.HasCoverPage property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutgoingJob.HasCoverPage property

Specifies if the fax has a cover page.

This property is read-only.

## Syntax


```VB
Property HasCoverPage As Boolean
```



## Property value

A **Boolean** that receives a value that indicates whether the fax has a cover page.

## Remarks

The value is VARIANT\_TRUE if there is a cover page; otherwise VARIANT\_FALSE.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxOutgoingJob**](-mfax-faxoutgoingjob.md)
</dt> <dt>

[**IFaxOutgoingJob2**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxoutgoingjob2)
</dt> </dl>

 

 




