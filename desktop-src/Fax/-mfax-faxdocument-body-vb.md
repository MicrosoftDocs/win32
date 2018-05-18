---
Description: 'The Body property provides the path to the file that comprises the body of a fax. The body of a fax consists of the fax pages other than the cover page.'
ms.assetid: '1679d433-5a62-4e98-a083-f15ac9d4fb2d'
title: 'FaxDocument.Body property'
---

# FaxDocument.Body property

The **Body** property provides the path to the file that comprises the body of a fax. The body of a fax consists of the fax pages other than the cover page.

This property is read/write.

## Syntax


```VB
Property Body As String
```



## Property value

A **String** that specifies or receives the path to the body file.

## Remarks

Examples of documents that you can send as a fax body are a text file (.txt), a Microsoft Word document (.doc), or a Microsoft Excel spreadsheet (.xls). When you send a fax from a client computer, the body has to be associated with an application that is installed on that computer, and the application has to support the **PrintTo** verb; otherwise, the fax will fail.

Either the [**Bodies**](-mfax-faxdocument2-bodies-vb.md) property or the **Body** property must be **NULL**. You must use **Bodies** if you will be submitting with either [**ConnectedSubmit2**](-mfax-faxdocument2-connectedsubmit2-vb.md) or [**Submit2**](-mfax-faxdocument2-submit2-vb.md) (both available only in Windows Vista or later). You must use **Body** if you will be submitting with either [**ConnectedSubmit**](-mfax-faxdocument-connectedsubmit.md) or [**Submit**](-mfax-faxdocument-submit-vb.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-sending-a-fax.md)
</dt> <dt>

[**FaxDocument**](-mfax-faxdocument.md)
</dt> <dt>

[**IFaxDocument**](-mfax-faxdocument-cpp.md)
</dt> </dl>

 

 




