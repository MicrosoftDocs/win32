---
Description: Provides a collection of one or more documents to the fax document.
ms.assetid: c5e0fd2b-9d64-4854-954e-a6e7557f6d3d
title: FaxDocument.Bodies property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDocument.Bodies property

Provides a collection of one or more documents to the fax document.

> [!Note]  
> This property is supported only in Windows Vista and later.

 

This property is read/write.

## Syntax


```VB
Property Bodies As Variant
```



## Property value

A **Variant** that specifies or receives the documents in the fax.

## Remarks

Examples of documents that you can send as fax bodies include text files (.txt), Microsoft Word documents (.doc), or Microsoft Excel spreadsheets (.xls). Filenames are separated with semi-colons ";". For example, "myfile.txt;anotherfile.doc".

Either the **Bodies** property or the [**Body**](-mfax-faxdocument-body-vb.md) property must be **NULL**. You must use **Bodies** if you will be submitting using either [**ConnectedSubmit2**](-mfax-faxdocument2-connectedsubmit2-vb.md) or [**Submit2**](-mfax-faxdocument2-submit2-vb.md) (both available only in Windows Vista or later). You must use **Body** if you will be submitting using either [**ConnectedSubmit**](-mfax-faxdocument-connectedsubmit.md) or [**Submit**](-mfax-faxdocument-submit-vb.md).

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

[**IFaxDocument2**](-mfax-faxdocument2-cpp.md)
</dt> </dl>

 

 




