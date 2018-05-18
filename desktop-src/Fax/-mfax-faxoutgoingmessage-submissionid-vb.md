---
Description: 'The SubmissionId property is a null-terminated string that contains the unique identifier assigned to the fax message during the submission process. All fax jobs created by the same submission process share the same unique submission ID.'
ms.assetid: '877af482-f2fc-4ff2-a4f3-36cee2c07bd8'
title: 'FaxOutgoingMessage.SubmissionId property'
---

# FaxOutgoingMessage.SubmissionId property

The **SubmissionId** property is a null-terminated string that contains the unique identifier assigned to the fax message during the submission process. All fax jobs created by the same submission process share the same unique submission ID.

This property is read-only.

## Syntax


```VB
Property SubmissionId As String
```



## Property value

A **String** that receives the unique submission ID assigned to the outbound fax message.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-opening-a-fax-from-the-outgoing-archive.md)
</dt> <dt>

[**FaxOutgoingMessage**](-mfax-faxoutgoingmessage.md)
</dt> <dt>

[**IFaxOutgoingMessage**](-mfax-faxoutgoingmessage-cpp.md)
</dt> </dl>

 

 




