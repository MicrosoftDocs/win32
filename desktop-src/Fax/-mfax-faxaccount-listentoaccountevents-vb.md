---
Description: 'Sets the flags of a FAX\_ACCOUNT\_EVENTS\_TYPE\_ENUM variable that represents the events for which the account is listening.'
ms.assetid: '25c9bfac-34fd-4839-af89-ba2576b62c7b'
title: 'FaxAccount.ListenToAccountEvents method'
---

# FaxAccount.ListenToAccountEvents method

Sets the flags of a [**FAX\_ACCOUNT\_EVENTS\_TYPE\_ENUM**](-mfax-fax-account-events-type-enum.md) variable that represents the events for which the account is listening.

## Syntax


```VB
FaxAccount.ListenToAccountEvents( _
  ByVal EventTypes As FAX_ACCOUNT_EVENTS_TYPE_ENUM _
) As Long
```



## Parameters

<dl> <dt>

*EventTypes* \[in\]
</dt> <dd>

Type: **[**FAX\_ACCOUNT\_EVENTS\_TYPE\_ENUM**](-mfax-fax-account-events-type-enum.md)**

A variable that specifies the types of events for which the account is listening.

</dd> </dl>

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

[**IFaxAccount**](-mfax-faxaccount-cpp.md)
</dt> </dl>

 

 




