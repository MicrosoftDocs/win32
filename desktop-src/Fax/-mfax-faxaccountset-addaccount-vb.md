---
Description: 'Adds a fax account to the fax server and returns the new IFaxAccount object.'
ms.assetid: '5df2598a-ecd1-4a1b-8422-59b1591a68fb'
title: 'FaxAccountSet.AddAccount method'
---

# FaxAccountSet.AddAccount method

Adds a fax account to the fax server and returns the new [**IFaxAccount**](-mfax-faxaccount-cpp.md) object.

## Syntax


```VB
FaxAccountSet.AddAccount( _
  ByVal bstrAccountName As String _
) As IFaxAccount
```



## Parameters

<dl> <dt>

*bstrAccountName* \[in\]
</dt> <dd>

Type: **String**

Specifies a null-terminated string that contains a name for the new account.

</dd> </dl>

## Return value

Type: **[**IFaxAccount**](-mfax-faxaccount-cpp.md)\*\***

The address of a pointer to an [**IFaxAccount**](-mfax-faxaccount-cpp.md) object.

## Remarks

*bstrAccountName* must be of the form &lt;domainName&gt;\\&lt;username&gt; or just &lt;username&gt; for local users.

When the new account is returned, all its values except the name are set to defaults.

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

[**IFaxAccountSet**](-mfax-faxaccountset-cpp.md)
</dt> </dl>

 

 




