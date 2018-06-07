---
title: ITsSbSession InitialProgram property
description: Retrieves or specifies the initial program for this session.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c299c4f7-3c5f-468f-9fc7-81eac322dfa2
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- InitialProgram property Remote Desktop Services
- InitialProgram property Remote Desktop Services , ITsSbSession interface
- ITsSbSession interface Remote Desktop Services , InitialProgram property
topic_type:
- apiref
api_name:
- ITsSbSession.InitialProgram
- ITsSbSession.get_InitialProgram
- ITsSbSession.put_InitialProgram
api_location:
- Sbtsv.idl
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ITsSbSession::InitialProgram property

Retrieves or specifies the initial program for this session. The initial program is the program that is launched when the user session starts.

This property is read/write.

## Syntax


```C++
HRESULT put_InitialProgram(
  [in]          BSTR Application
);

HRESULT get_InitialProgram(
  [out, retval] BSTR *app
);
```



## Property value

A **BSTR** variable that contains the initial program.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                       |
| IDL<br/>                      | <dl> <dt>Sbtsv.idl</dt> </dl> |



## See also

<dl> <dt>

[**ITsSbSession**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbsession)
</dt> </dl>

 

 





