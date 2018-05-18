---
title: IBasicIMOld LaunchIMUI method
description: Initiates an Instant Messaging Service (IM) Window.
ms.assetid: 'f2a2ad44-18d9-4f79-92c6-867910d952b4'
keywords: ["LaunchIMUI method Windows Messenger", "LaunchIMUI method Windows Messenger , IBasicIMOld interface", "IBasicIMOld interface Windows Messenger , LaunchIMUI method"]
topic_type:
- apiref
api_name:
- IBasicIMOld.LaunchIMUI
api_location:
- Msgsc.dll
api_type:
- COM
---

# IBasicIMOld::LaunchIMUI method

\[**LaunchIMUI** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Initiates an Instant Messaging Service (IM) Window.

> [!Note]  
> The **LaunchIMUI** method is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger.

 

## Syntax


```C++
HRESULT LaunchIMUI(
  [in] VARIANT vUser
);
```



## Parameters

<dl> <dt>

*vUser* \[in\]
</dt> <dd>

Type: **VARIANT**

**VARIANT** that specifies the user.

</dd> </dl>

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



 

 





