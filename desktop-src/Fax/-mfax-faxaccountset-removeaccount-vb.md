---
Description: Removes a fax account from the fax server.
ms.assetid: 613fe57f-59cc-4c63-9131-536588ab827b
title: FaxAccountSet.RemoveAccount method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxAccountSet.RemoveAccount method

Removes a fax account from the fax server.

## Syntax


```VB
FaxAccountSet.RemoveAccount( _
  ByVal bstrAccountName As String _
) As Long
```



## Parameters

<dl> <dt>

*bstrAccountName* \[in\]
</dt> <dd>

Type: **String**

Specifies a null-terminated string that contains the name of the account to be removed.

</dd> </dl>

## Remarks

*bstrAccountName* must be of the form &lt;domainName&gt;\\&lt;username&gt; or just &lt;username&gt; for local users.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxAccountSet**](-mfax-faxaccountset.md)
</dt> <dt>

[**IFaxAccountSet**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxaccountset?branch=master)
</dt> </dl>

 

 




