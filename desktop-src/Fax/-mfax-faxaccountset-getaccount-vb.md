---
Description: Returns an IFaxAccount object by using the account name.
ms.assetid: 8b59bcff-c5f5-40a3-a900-ad9eab8fcbf2
title: FaxAccountSet.GetAccount method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxAccountSet.GetAccount method

Returns an [**IFaxAccount**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxaccount?branch=master) object by using the account name.

## Syntax


```VB
FaxAccountSet.GetAccount( _
  ByVal bstrAccountName As String _
) As IFaxAccount
```



## Parameters

<dl> <dt>

*bstrAccountName* \[in\]
</dt> <dd>

Type: **String**

Specifies a null-terminated string that contains the name of the account to return.

</dd> </dl>

## Return value

Type: **[**IFaxAccount**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxaccount?branch=master)\*\***

The address of a pointer to an [**IFaxAccount**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxaccount?branch=master) object.

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

 

 




