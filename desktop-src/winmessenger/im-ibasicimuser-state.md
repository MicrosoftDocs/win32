---
title: IBasicIMUser State property
description: Retrieves the state of the user.
ms.assetid: '2d5273b1-994a-40b3-a817-89fe02775804'
keywords: ["State property Windows Messenger", "State property Windows Messenger , IBasicIMUser interface", "IBasicIMUser interface Windows Messenger , State property"]
topic_type:
- apiref
api_name:
- IBasicIMUser.State
- IBasicIMUser.get_State
api_location:
- Msgsc.dll
api_type:
- COM
---

# IBasicIMUser::State property

\[**State** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves the state of the user.

> [!Note]  
> The **State** property is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**Status**](im-imessengercontact-status.md) instead.

 

This property is read-only.

## Syntax


```C++
HRESULT get_State(
  [out, retval] BIMSTATE *pbimState
);
```



## Property value

Pointer to a [**BIMSTATE**](im-bimstate.md) enumerated type that receives user state information.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                  |
| End of server support<br/> | Windows Server 2003<br/>                                                         |
| Header<br/>                | <dl> <dt>Basicim.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Basicim.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>   |



 

 





