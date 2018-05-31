---
Description: Returns a fax message from the archive of inbound faxes, for a particular fax account, by using the fax message ID.
ms.assetid: b37bbc8f-04f3-4030-bb1b-811a63810090
title: FaxAccountIncomingArchive.GetMessage method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxAccountIncomingArchive.GetMessage method

Returns a fax message from the archive of inbound faxes, for a particular fax account, by using the fax message ID.

## Syntax


```VB
FaxAccountIncomingArchive.GetMessage( _
  ByVal bstrMessageId As String _
) As IFaxIncomingMessage2
```



## Parameters

<dl> <dt>

*bstrMessageId* \[in\]
</dt> <dd>

Type: **String**

Specifies a null-terminated string that contains the message ID of the fax to retrieve from the archive of inbound faxes.

</dd> </dl>

## Return value

Type: **[**IFaxIncomingMessage2**](-mfax-faxincomingmessage2-cpp.md)\*\***

An [**IFaxIncomingMessage2**](-mfax-faxincomingmessage2-cpp.md) object.

## Remarks

To use this method, a user must have the [****far2QUERY\_ARCHIVES****](-mfax-fax-access-rights-enum-2.md) access right.

If the setting 'All incoming faxes are viewable by everyone' is true (see [**IncomingFaxesArePublic**](-mfax-ifaxconfiguration-incomingfaxesarepublic.md)) or if [****far2MANAGE\_RECEIVE\_FOLDER****](-mfax-fax-access-rights-enum-2.md) access rights, then the fax service searches all faxes in the Incoming archive of the Fax Server Receive Folder.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxAccountIncomingArchive**](-mfax-faxaccountincomingarchive.md)
</dt> <dt>

[**IFaxAccountIncomingArchive**](-mfax-faxaccountincomingarchive-cpp.md)
</dt> </dl>

 

 




