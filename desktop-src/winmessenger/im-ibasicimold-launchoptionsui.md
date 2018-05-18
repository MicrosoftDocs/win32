---
title: IBasicIMOld LaunchOptionsUI method
description: Initiates an Options dialog.
ms.assetid: '1637907c-b003-4eb9-a52c-abc150b303c4'
keywords: ["LaunchOptionsUI method Windows Messenger", "LaunchOptionsUI method Windows Messenger , IBasicIMOld interface", "IBasicIMOld interface Windows Messenger , LaunchOptionsUI method"]
topic_type:
- apiref
api_name:
- IBasicIMOld.LaunchOptionsUI
api_location:
- Msgsc.dll
api_type:
- COM
---

# IBasicIMOld::LaunchOptionsUI method

\[**LaunchOptionsUI** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Initiates an Options dialog.

> [!Note]  
> The **LaunchOptionsUI** method is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger.

 

## Syntax


```C++
HRESULT LaunchOptionsUI();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                  |
| End of server support<br/> | Windows Server 2003<br/>                                                         |
| Header<br/>                | <dl> <dt>Basicim.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Basicim.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>   |



 

 





