---
Description: Returns a fax message from the archive of outbound faxes for a particular fax account, by using the fax message ID.
ms.assetid: 87bb32e8-0068-473a-af73-5a963527b9ca
title: FaxAccountOutgoingArchive.GetMessage method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

Type: **[**IFaxOutgoingMessage2**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxoutgoingmessage2)\*\***

A [**IFaxOutgoingMessage2**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxoutgoingmessage2) object.

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

[**IFaxAccountOutgoingArchive**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxaccountoutgoingarchive)
</dt> </dl>

 

 




