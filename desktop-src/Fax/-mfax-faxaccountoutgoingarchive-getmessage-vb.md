---
Description: 'Returns a fax message from the archive of outbound faxes for a particular fax account, by using the fax message ID.'
ms.assetid: '87bb32e8-0068-473a-af73-5a963527b9ca'
title: 'FaxAccountOutgoingArchive.GetMessage method'
---

# FaxAccountOutgoingArchive.GetMessage method

Returns a fax message from the archive of outbound faxes for a particular fax account, by using the fax message ID.

## Syntax


```VB
FaxAccountOutgoingArchive.GetMessage( _
  ByVal bstrMessageId As String _
) As IFaxOutgoingMessage2
```



## Parameters

<dl> <dt>

*bstrMessageId* \[in\]
</dt> <dd>

Type: **String**

Specifies a null-terminated string that contains the message ID of the fax to retrieve from the archive of outbound faxes.

</dd> </dl>

## Return value

Type: **[**IFaxOutgoingMessage2**](-mfax-faxoutgoingmessage2-cpp.md)\*\***

A [**IFaxOutgoingMessage2**](-mfax-faxoutgoingmessage2-cpp.md) object.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxAccountOutgoingArchive**](-mfax-faxaccountoutgoingarchive.md)
</dt> <dt>

[**IFaxAccountOutgoingArchive**](-mfax-faxaccountoutgoingarchive-cpp.md)
</dt> </dl>

 

 




