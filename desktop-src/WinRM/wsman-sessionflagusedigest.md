---
title: WSMan.SessionFlagUseDigest method (WSManDisp.h)
description: Returns the value of the WSManFlagUseDigest authentication flag for use in the flags parameter of the WSMan.CreateSession method.
ms.assetid: dba2448a-4f72-4000-8687-4c1be812fc3b
ms.tgt_platform: multiple
keywords:
- SessionFlagUseDigest method Windows Remote Management
- SessionFlagUseDigest method Windows Remote Management , WSMan object
- WSMan object Windows Remote Management , SessionFlagUseDigest method
topic_type:
- apiref
api_name:
- WSMan.SessionFlagUseDigest
api_location:
- WSMAuto.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# WSMan.SessionFlagUseDigest method

The **WSMan.SessionFlagUseDigest** method returns the value of the **WSManFlagUseDigest** authentication flag for use in the *flags* parameter of the [**WSMan.CreateSession**](wsman-createsession.md) method. This method provides a more efficient syntax for using the constant so that scripts are not required to set a constant value. For more information about how to call this method, see [Session Constants](session-constants.md).

**WSManFlagUseDigest** is a value in the **\_\_WSManSessionFlags** enumeration. For more information, see [Authentication Constants](authentication-constants.md).

## Syntax


```VB
WSMan.SessionFlagUseDigest( _
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

 

 





