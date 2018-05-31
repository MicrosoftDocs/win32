---
Description: A set of flags indicating the type of events for which the account is listening.
ms.assetid: 44206ee3-1a79-41b2-87a8-4d659657bb1b
title: FaxAccount.RegisteredEvents property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxAccount.RegisteredEvents property

A set of flags indicating the type of events for which the account is listening.

This property is read-only.

## Syntax


```VB
Property RegisteredEvents As FAX_ACCOUNT_EVENTS_TYPE_ENUM
```



## Property value

Pointer to a variable of type [**FAX\_ACCOUNT\_EVENTS\_TYPE\_ENUM**](-mfax-fax-account-events-type-enum.md) which indicates the events for which the account is listening.

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

 

 




