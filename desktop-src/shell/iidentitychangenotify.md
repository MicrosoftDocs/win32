---
Description: Deprecated. Provides notification of modifications to user identities on the system, as well as user requests to switch the current user identity.
ms.assetid: 09903aa6-62bf-4820-9a09-79956d775441
title: IIdentityChangeNotify interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IIdentityChangeNotify interface

\[The **IIdentityChangeNotify** interface is available for use in Windows 2000. In Windows XP, this functionality has been superseded by [User Accounts with Fast User Switching and Remote Desktop](fastuserswitching.md), and might be altered or unavailable in subsequent versions.\]

Deprecated. Provides notification of modifications to user identities on the system, as well as user requests to switch the current user identity.

## Members

The **IIdentityChangeNotify** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/33f1d79a-33fc-4ce5-a372-e08bda378332) interface. **IIdentityChangeNotify** also has these types of members:

-   [Methods](#methods)

### Methods

The **IIdentityChangeNotify** interface has these methods.



| Method                                                                                 | Description                                                                                                                           |
|:---------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------|
| [**IdentityInformationChanged**](iidentitychangenotify-identityinformationchanged.md) | Deprecated. Called when information about a user identity has changed, or when a user identity has been added or deleted.<br/>  |
| [**QuerySwitchIdentities**](iidentitychangenotify-queryswitchidentities.md)           | Deprecated. Called when the current user has requested that their user identity be switched, but before the switch occurs.<br/> |
| [**SwitchIdentities**](iidentitychangenotify-switchidentities.md)                     | Deprecated. Called when user identities are switched.<br/>                                                                      |



 

## Remarks

To implement notifications, a derived interface must connect to the [**IUserIdentityManager**](iuseridentitymanager.md) by calling [**IConnectionPoint::Advise**](https://msdn.microsoft.com/11257f24-096c-4240-8fac-4e42a6161d66) and by passing a pointer to the interface.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Msident.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msident.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msoe.dll</dt> </dl>    |



## See also

<dl> <dt>

[**IUserIdentityManager**](iuseridentitymanager.md)
</dt> <dt>

[**IConnectionPoint**](https://msdn.microsoft.com/ef5a917c-b57f-4000-8daa-86fdbfb47579)
</dt> </dl>

 

 




