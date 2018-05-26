---
title: ITsSbSession State property
description: Retrieves or specifies the session state.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4e769ff7-2bd5-4fcb-b2d7-4dedc853482b
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- State property Remote Desktop Services
- State property Remote Desktop Services , ITsSbSession interface
- ITsSbSession interface Remote Desktop Services , State property
topic_type:
- apiref
api_name:
- ITsSbSession.State
- ITsSbSession.get_State
- ITsSbSession.put_State
api_location:
- Sbtsv.idl
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ITsSbSession::State property

Retrieves or specifies the session state.

This property is read/write.

## Syntax


```C++
HRESULT put_State(
  [in]          TSSESSION_STATE State
);

HRESULT get_State(
  [out, retval] TSSESSION_STATE *pState
);
```



## Property value

A value of the [**TSSESSION\_STATE**](/windows/win32/SessDirPublicTypes/ne-sessdirpublictypes-_tssession_state?branch=master) enumeration that indicates the state of a session.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                       |
| IDL<br/>                      | <dl> <dt>Sbtsv.idl</dt> </dl> |



## See also

<dl> <dt>

[**ITsSbSession**](/windows/win32/sbtsv/nn-sbtsv-itssbsession?branch=master)
</dt> <dt>

[**TSSESSION\_STATE**](/windows/win32/SessDirPublicTypes/ne-sessdirpublictypes-_tssession_state?branch=master)
</dt> </dl>

 

 





