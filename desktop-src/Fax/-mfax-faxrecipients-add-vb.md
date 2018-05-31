---
Description: The Add method adds a new FaxRecipient object to the FaxRecipients collection.
ms.assetid: 828ac490-ef76-423e-9b18-c03e2e3b1fa4
title: FaxRecipients.Add method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxRecipients.Add method

The **Add** method adds a new [**FaxRecipient**](-mfax-faxrecipient.md) object to the [**FaxRecipients**](-mfax-faxrecipients.md) collection.

## Syntax


```VB
FaxRecipients.Add( _
  ByVal bstrFaxNumber As String, _
  [ ByVal bstrRecipientName As String ] _
) As IFaxRecipient
```



## Parameters

<dl> <dt>

*bstrFaxNumber* 
</dt> <dd>

Type: **String**

Specifies the fax number of the fax recipient.

</dd> <dt>

*bstrRecipientName* \[optional\]
</dt> <dd>

Type: **String**

Specifies the name of the fax recipient.

</dd> </dl>

## Return value

Type: **[**IFaxRecipient**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxrecipient)\*\***

A [**FaxRecipient**](-mfax-faxrecipient.md) object.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxRecipients**](-mfax-faxrecipients.md)
</dt> <dt>

[**IFaxRecipients**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxrecipients)
</dt> <dt>

[Broadcasting a Fax](-mfax-broadcasting-a-fax.md)
</dt> </dl>

 

 




