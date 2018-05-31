---
Description: Submits one or more documents to the fax service for processing.Note  This method is supported only in Windows Vista and later. 
ms.assetid: 6adffb23-0a42-4846-b60d-dcdfc9ef63b6
title: FaxDocument.Submit2 method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDocument.Submit2 method

Submits one or more documents to the fax service for processing.

> [!Note]  
> This method is supported only in Windows Vista and later.

 

## Syntax


```VB
FaxDocument.Submit2( _
  ByVal bstrFaxServerName As String, _
  ByRef pvFaxOutgoingJobIDs As Variant _
) As Long
```



## Parameters

<dl> <dt>

*bstrFaxServerName* \[in\]
</dt> <dd>

Type: **String**

**String** that specifies a fax server. If this parameter is **NULL** or an empty string, the local fax server is specified.

</dd> <dt>

*pvFaxOutgoingJobIDs* \[out\]
</dt> <dd>

Type: **Variant\***

**Variant** that specifies a collection of outbound job IDs, one for each recipient of the fax.

</dd> </dl>

## Return value

Type: **Long\***

A **Long** representing the zero-based position of the submitted file that caused the fax send operation to fail. See Remarks.

## Remarks

You must set the [**Bodies**](-mfax-faxdocument2-bodies-vb.md) property with a semi-colon delimited list of the files to be faxed before calling **Submit2**.

> [!Note]  
> This [**Body**](-mfax-faxdocument-body-vb.md) property must be **NULL** to use **Submit2**.

 

You must provide the server name when submitting the document. To submit the document to the local server, set the *bstrFaxServerName* parameter to **Null** or an empty string. The method returns a collection of fax job IDs, one for each recipient of the fax.

To succeed, the **Submit2** method requires that the fax has at least one recipient, and either a cover page or a fax body. You can only use this method if the server (remote or local) is installed as a network printer on the local computer.

This method is not supported for a remote connection to a fax server running Windows XP Home Edition or Windows XP Professional, and will return the error [FAX\_E\_NOT\_SUPPORTED\_ON\_THIS\_SKU](-mfax-fax-error-codes.md).

To use this method, a user must have the [****far2SUBMIT\_LOW****](-mfax-fax-access-rights-enum-2.md), [****far2SUBMIT\_NORMAL****](-mfax-fax-access-rights-enum-2.md), or [****far2SUBMIT\_HIGH****](-mfax-fax-access-rights-enum-2.md) access set correctly, depending on the [**Priority**](-mfax-faxdocument-priority-vb.md) of the fax document.

As an example of *plErrorBodyFile*, consider the following example: The following list of files is submitted as the value of [**Bodies**](-mfax-faxdocument2-bodies-vb.md):

"MyTextFile.txt;AnotherTextFile.txt;MyPDFfile.pdf;MyWordFile.doc".

Because the "\*.pdf" extension is not supported, the send operation will fail and *plErrorBodyFile* will return as 2.

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

 

 




