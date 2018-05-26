---
title: WSMan.SessionFlagUseNegotiate method
description: Returns the value of the WSManFlagUseNegotiate authentication flag for use in the flags parameter of the WSMan.CreateSession method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 86d8ed13-5eae-4a06-8ceb-b0ec067f4a4c
ms.prod: windows-server-dev
ms.technology: windows-remote-management
ms.tgt_platform: multiple
keywords:
- SessionFlagUseNegotiate method Windows Remote Management
- SessionFlagUseNegotiate method Windows Remote Management , WSMan object
- WSMan object Windows Remote Management , SessionFlagUseNegotiate method
topic_type:
- apiref
api_name:
- WSMan.SessionFlagUseNegotiate
api_location:
- WSMAuto.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# WSMan.SessionFlagUseNegotiate method

The **WSMan.SessionFlagUseNegotiate** method returns the value of the **WSManFlagUseNegotiate** authentication flag for use in the *flags* parameter of the [**WSMan.CreateSession**](wsman-createsession.md) method. This method provides a more efficient syntax for using the constant so that scripts are not required to set a constant value. For more information about how to call this method, see [Session Constants](session-constants.md).

**WSManFlagUseNegotiate** is a constant in the **\_\_WSManSessionFlags** enumeration. For more information, see [Authentication Constants](authentication-constants.md).

## Syntax


```VB
WSMan.SessionFlagUseNegotiate( _
  ByRef flags _
)
```



## Parameters

<dl> <dt>

*flags* \[out\]
</dt> <dd>

The value of the constant.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Header<br/>                   | <dl> <dt>WSManDisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>WSManDisp.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>WSManDisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WSMAuto.dll</dt> </dl>   |



## See also

<dl> <dt>

[**WSMan**](wsman.md)
</dt> <dt>

[**Session**](session.md)
</dt> </dl>

 

 





