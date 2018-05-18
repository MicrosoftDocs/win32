---
Description: 'Submits one or more fax documents to the connected FaxServer.'
ms.assetid: '6a62e987-8853-41f0-b440-1571e761ac75'
title: 'FaxDocument.ConnectedSubmit2 method'
---

# FaxDocument.ConnectedSubmit2 method

Submits one or more fax documents to the connected [**FaxServer**](-mfax-faxserver.md). This method returns an array of fax job ID strings, one for each recipient of the fax.

> [!Note]  
> This method is supported only in Windows Vista and later.

 

## Syntax


```VB
FaxDocument.ConnectedSubmit2( _
  ByVal pFaxServer As IFaxServer, _
  ByRef pvFaxOutgoingJobIDs As Variant _
) As Long
```



## Parameters

<dl> <dt>

*pFaxServer* \[in\]
</dt> <dd>

Type: **IFaxServer\***

A [**FaxServer**](-mfax-faxserver.md) object that specifies a connected fax server.

</dd> <dt>

*pvFaxOutgoingJobIDs* \[out\]
</dt> <dd>

Type: **Variant\***

A **Variant** that holds an array of outbound job ID strings, one for each recipient of the fax.

</dd> </dl>

## Return value

Type: **Long\***

A **Long** representing the zero-based position of the submitted file that caused the fax send operation to fail. See Remarks.

## Remarks

> [!Note]  
> To succeed, the **ConnectedSubmit2** method requires that the fax have at least one recipient, and either a cover page or a fax body. You can only use this method if the server (remote or local) is installed as a network printer on the local computer.

 

You must set the [**Bodies**](-mfax-faxdocument2-bodies-vb.md) property with a semi-colon delimited list of the files to be faxed before calling **ConnectedSubmit2**.

> [!Note]  
> The [**Body**](-mfax-faxdocument-body-vb.md) property must be **NULL** to use **ConnectedSubmit2**.

 

This method is not supported for a remote connection to a fax server running Windows XP Home Edition or Windows XP Professional, and will return the error: [FAX\_E\_NOT\_SUPPORTED\_ON\_THIS\_SKU](-mfax-fax-error-codes.md).

To use this method, a user must have the [****far2SUBMIT\_LOW****](-mfax-fax-access-rights-enum-2.md), [****far2SUBMIT\_NORMAL****](-mfax-fax-access-rights-enum-2.md), or [****far2SUBMIT\_HIGH****](-mfax-fax-access-rights-enum-2.md) access set correctly, depending on the [**Priority**](-mfax-faxdocument-priority-vb.md) of the fax document.

To illustrate *plErrorBodyFile*, here is an example: The following list of files is submitted as the value of [**Bodies**](-mfax-faxdocument2-bodies-vb.md):

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

 

 




