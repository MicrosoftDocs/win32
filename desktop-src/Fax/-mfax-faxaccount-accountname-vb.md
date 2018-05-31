---
Description: Retrieves the name of a particular fax account on the server.
ms.assetid: 3f376d12-e678-401c-a32f-ee8f330363b8
title: FaxAccount.AccountName property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxAccount.AccountName property

Retrieves the name of a particular fax account on the server.

This property is read-only.

## Syntax


```VB
Property AccountName As String
```



## Property value

A **String** that receives the name for the account.

## Remarks

If the account is not in the local domain, the format of name returned is &lt;domain\_name&gt;\\&lt;user\_name&gt;.

If the account is in the domain but not on the server, the format name returned is &lt;computer\_name&gt;\\&lt;user\_name&gt; where &lt;computer\_name&gt; is the name of the server that holds the account.

If the account is on the same server as the fax server, just the &lt;user\_name&gt; of the account is returned.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxAccount**](-mfax-faxaccount.md)
</dt> <dt>

[**IFaxAccount**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxaccount)
</dt> </dl>

 

 




