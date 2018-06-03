---
title: IBasicIMOld AutoLogon method
description: Initiates a Logon without using a UI if the user is connected to the network and has saved a password.
ms.assetid: 789faba1-5cbd-4d85-9e1c-48513b8c0e85
keywords:
- AutoLogon method Windows Messenger
- AutoLogon method Windows Messenger , IBasicIMOld interface
- IBasicIMOld interface Windows Messenger , AutoLogon method
topic_type:
- apiref
api_name:
- IBasicIMOld.AutoLogon
api_location:
- Msgsc.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IBasicIMOld::AutoLogon method

\[**AutoLogon** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Initiates a Logon without using a UI if the user is connected to the network and has saved a password.

> [!Note]  
> The **AutoLogon** method is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**AutoSignin**](im-imessenger-autosignin.md) instead.

 

## Syntax


```C++
HRESULT AutoLogon();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                  |
| End of server support<br/> | Windows Server 2003<br/>                                                         |
| Header<br/>                | <dl> <dt>Basicim.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Basicim.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>   |



 

 





