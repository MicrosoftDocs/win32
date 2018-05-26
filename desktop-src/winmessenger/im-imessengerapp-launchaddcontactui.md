---
title: IMessengerApp LaunchAddContactUI method
description: Launches the Contact wizard for adding a contact.
ms.assetid: dcf13250-cfaf-46c5-b7f2-6927b585c50d
keywords:
- LaunchAddContactUI method Windows Messenger
- LaunchAddContactUI method Windows Messenger , IMessengerApp interface
- IMessengerApp interface Windows Messenger , LaunchAddContactUI method
topic_type:
- apiref
api_name:
- IMessengerApp.LaunchAddContactUI
api_location:
- Msmsgs.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMessengerApp::LaunchAddContactUI method

\[**LaunchAddContactUI** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Launches the Contact wizard for adding a contact.

> [!Note]  
> The **LaunchAddContactUI** method is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**AddContact**](im-imessenger-addcontact.md) instead.

 

## Syntax


```C++
HRESULT LaunchAddContactUI(
  [in] BSTR bstrEMail
);
```



## Parameters

<dl> <dt>

*bstrEMail* \[in\]
</dt> <dd>

Type: **BSTR**

**BSTR** that specifies the contact to add.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Mdisp.h</dt> </dl>    |
| IDL<br/>                   | <dl> <dt>Mdisp.idl</dt> </dl>  |
| DLL<br/>                   | <dl> <dt>Msmsgs.exe</dt> </dl> |



 

 





