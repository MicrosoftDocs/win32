---
Description: Sets the flags of a FAX\_ACCOUNT\_EVENTS\_TYPE\_ENUM variable that represents the events for which the account is listening.
ms.assetid: 25c9bfac-34fd-4839-af89-ba2576b62c7b
title: FaxAccount.ListenToAccountEvents method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxAccount.ListenToAccountEvents method

Sets the flags of a [**FAX\_ACCOUNT\_EVENTS\_TYPE\_ENUM**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_account_events_type_enum?branch=master) variable that represents the events for which the account is listening.

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

Type: **[**FAX\_ACCOUNT\_EVENTS\_TYPE\_ENUM**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_account_events_type_enum?branch=master)**

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

[**IFaxAccount**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxaccount?branch=master)
</dt> </dl>

 

 




