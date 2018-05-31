---
Description: The GetMessage method returns a fax message from the archive of outbound faxes by using the fax message ID.
ms.assetid: ca7dbedc-a5b5-4da1-b5e1-545e679369db
title: FaxOutgoingArchive.GetMessage method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxOutgoingArchive.GetMessage method

The **GetMessage** method returns a fax message from the archive of outbound faxes by using the fax message ID.

## Syntax


```VB
FaxOutgoingArchive.GetMessage( _
  ByVal bstrMessageId As String _
) As FaxOutgoingMessage
```



## Parameters

<dl> <dt>

*bstrMessageId* 
</dt> <dd>

Type: **String**

Specifies a null-terminated string that contains the message ID of the fax to retrieve from the archive of outbound faxes.

</dd> </dl>

## Return value

Type: **[**FaxOutgoingMessage**](-mfax-faxoutgoingmessage.md)**

A [**FaxOutgoingMessage**](-mfax-faxoutgoingmessage.md) object.

## Remarks

To use this method, a user must have the [**farSUBMIT\_LOW**](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum) or **farQUERY\_OUT\_ARCHIVE** access right. With the **farSUBMIT\_LOW** access right, the user will be able to use this method only for his own faxes. With the **farQUERY\_OUT\_ARCHIVE** access right, he will be able to use this method for all of the faxes on the server.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-the-outgoing-archive.md)
</dt> <dt>

[**FaxOutgoingArchive**](-mfax-faxoutgoingarchive.md)
</dt> <dt>

[**IFaxOutgoingArchive**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxoutgoingarchive)
</dt> </dl>

 

 




