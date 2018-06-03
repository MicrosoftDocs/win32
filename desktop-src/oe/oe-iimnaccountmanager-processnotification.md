---
title: IImnAccountManager ProcessNotification method
description: Processes Internet Mail and News (IMN) account notifications.
ms.assetid: 06bb4844-06d9-489d-ac0a-007e59e87d8e
keywords:
- ProcessNotification method Windows Mail (formerly Outlook Express)
- ProcessNotification method Windows Mail (formerly Outlook Express) , IImnAccountManager interface
- IImnAccountManager interface Windows Mail (formerly Outlook Express) , ProcessNotification method
topic_type:
- apiref
api_name:
- IImnAccountManager.ProcessNotification
api_location:
- Msoeacct.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IImnAccountManager::ProcessNotification method

\[**IImnAccountManager::ProcessNotification** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Processes Internet Mail and News (IMN) account notifications.

> [!Note]  
> The parameters of this method are the same as those received by the client application's [WindowProc](http://msdn.microsoft.com/library/winui/WinUI/WindowsUserInterface/Windowing/WindowProcedures/WindowProcedureReference/WindowProcedureFunctions/WindowProc.asp) function. These values should be passed to this method without modification.

 

## Syntax


```C++
HRESULT ProcessNotification(
  [in] UINT   uMsg,
  [in] WPARAM wParam,
  [in] LPARAM lParam
);
```



## Parameters

<dl> <dt>

*uMsg* \[in\]
</dt> <dd>

Type: **UINT**

Specifies the message.

</dd> <dt>

*wParam* \[in\]
</dt> <dd>

Type: **WPARAM**

Specifies the type of account notification.

<dl><span id="AN_DEFAULT_CHANGED"></span><span id="an_default_changed"></span><dt>

**AN\_DEFAULT\_CHANGED**
</dt><span id="AN_ACCOUNT_DELETED"></span><span id="an_account_deleted"></span><dt>

**AN\_ACCOUNT\_DELETED**
</dt><span id="AN_ACCOUNT_ADDED"></span><span id="an_account_added"></span><dt>

**AN\_ACCOUNT\_ADDED**
</dt><span id="AN_ACCOUNT_CHANGED"></span><span id="an_account_changed"></span><dt>

**AN\_ACCOUNT\_CHANGED**
</dt> </dl> </dd> <dt>

*lParam* \[in\]
</dt> <dd>

Type: **LPARAM**

Specifies the ID of the process that generated the notification.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                             | Description                                                                                                                          |
|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | Indicates that the Account Manager processed the Windows message. The client should not continue processing the message. <br/> |
| <dl> <dt>**S\_FALSE**</dt> </dl> | Indicates that the message is not an account notification message. The client should continue to handle the message. <br/>     |



 

## Remarks

The Account Manager broadcasts a Windows message to all top-level windows when it generates a Windows message.

A client must call this method to detect IMN account changes that are made in other applications. If the client generated the notification, the Account Manager ignores the notification.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Msoeacct.dll (version 6.0 or later)</dt> </dl> |



 

 





