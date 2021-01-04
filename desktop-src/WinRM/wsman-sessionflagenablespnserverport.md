---
title: WSMan.SessionFlagEnableSPNServerPort method (WSManDisp.h)
description: Returns the value of the authentication flag WSManFlagEnableSPNServerPort for use in the flags parameter of the WSMan.CreateSession method.
ms.assetid: a18a87e6-dcee-4e9f-8e8c-262fef36ab1a
ms.tgt_platform: multiple
keywords:
- SessionFlagEnableSPNServerPort method Windows Remote Management
- SessionFlagEnableSPNServerPort method Windows Remote Management , WSMan object
- WSMan object Windows Remote Management , SessionFlagEnableSPNServerPort method
topic_type:
- apiref
api_name:
- WSMan.SessionFlagEnableSPNServerPort
api_location:
- WSMAuto.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# WSMan.SessionFlagEnableSPNServerPort method

The **WSMan.SessionFlagEnableSPNServerPort** method returns the value of the authentication flag **WSManFlagEnableSPNServerPort** for use in the *flags* parameter of the [**WSMan.CreateSession**](wsman-createsession.md) method. This method provides a more efficient syntax for using the constant so that scripts are not required to set a constant value. For more information about how to call this method, see [Session Constants](session-constants.md).

**WSManFlagEnableSPNServerPort** is a constant in the **\_\_WSManSessionFlags** enumeration. For more information, see [**Other Session Constants**](other-session-constants.md).

## Syntax


```VB
WSMan.SessionFlagEnableSPNServerPort( _
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



| Requirement | Value |
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

 

 





