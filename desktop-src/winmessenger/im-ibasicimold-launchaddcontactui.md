---
title: IBasicIMOld LaunchAddContactUI method
description: Initiates an Add Contact dialog.
ms.assetid: '002fd314-c04d-4e13-96d8-fe4e7a152301'
keywords: ["LaunchAddContactUI method Windows Messenger", "LaunchAddContactUI method Windows Messenger , IBasicIMOld interface", "IBasicIMOld interface Windows Messenger , LaunchAddContactUI method"]
topic_type:
- apiref
api_name:
- IBasicIMOld.LaunchAddContactUI
api_location:
- Msgsc.dll
api_type:
- COM
---

# IBasicIMOld::LaunchAddContactUI method

\[**LaunchAddContactUI** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Initiates an Add Contact dialog.

> [!Note]  
> The **LaunchAddContactUI** method type is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**AddContact**](im-imessenger-addcontact.md) instead.

 

## Syntax


```C++
HRESULT LaunchAddContactUI(
  [in] BSTR bstrEMail
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



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                  |
| End of server support<br/> | Windows Server 2003<br/>                                                         |
| Header<br/>                | <dl> <dt>Basicim.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Basicim.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>   |



 

 





