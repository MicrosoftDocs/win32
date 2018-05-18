---
Description: 'The GetMessage method gets a fax message from the archive of inbound faxes by using the fax message ID.'
ms.assetid: 'e78f59d8-c78d-483e-98d6-2b155918b032'
title: 'FaxIncomingArchive.GetMessage method'
---

# FaxIncomingArchive.GetMessage method

The **GetMessage** method gets a fax message from the archive of inbound faxes by using the fax message ID.

## Syntax


```VB
FaxIncomingArchive.GetMessage( _
  ByVal bstrMessageId As String _
) As IFaxIncomingMessage
```



## Parameters

<dl> <dt>

*bstrMessageId* \[in\]
</dt> <dd>

Type: **String**

Specifies a null-terminated string that contains the message ID of the fax to retrieve from the archive of inbound faxes.

</dd> </dl>

## Return value

Type: **[**IFaxIncomingMessage**](-mfax-faxincomingmessage-cpp.md)\*\***

A [**FaxIncomingMessage**](-mfax-faxincomingmessage.md) object.

## Remarks

To use this method, a user must have the [****farQUERY\_IN\_ARCHIVE****](-mfax-fax-access-rights-enum.md) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-opening-a-fax-from-the-incoming-archive.md)
</dt> <dt>

[**FaxIncomingArchive**](-mfax-faxincomingarchive.md)
</dt> <dt>

[**IFaxIncomingArchive**](-mfax-faxincomingarchive-cpp.md)
</dt> </dl>

 

 




