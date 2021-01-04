---
title: WSMan.EnumerationFlagReturnEPR method (WSManDisp.h)
description: Returns the value of the enumeration flag EnumerationFlagReturnEPR for use in the flags parameter of Session.Enumerate.
ms.assetid: 5e168aa9-5be1-46b3-bb9b-59895e68a75d
ms.tgt_platform: multiple
keywords:
- EnumerationFlagReturnEPR method Windows Remote Management
- EnumerationFlagReturnEPR method Windows Remote Management , WSMan object
- WSMan object Windows Remote Management , EnumerationFlagReturnEPR method
topic_type:
- apiref
api_name:
- WSMan.EnumerationFlagReturnEPR
api_location:
- WSMAuto.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# WSMan.EnumerationFlagReturnEPR method

The **EnumerationFlagReturnEPR** method returns the value of the enumeration flag **EnumerationFlagReturnEPR** for use in the *flags* parameter of [**Session.Enumerate**](session-enumerate.md). This method provides a more efficient syntax for using the constant so that scripts are not required to set a constant value. For more information about how to call this method, see [Session Constants](session-constants.md).

**EnumerationFlagReturnEPR** is a constant in the **\_WSManEnumFlags** enumeration and is described in [**Enumeration Constants**](enumeration-constants.md).

## Syntax


```VB
WSMan.EnumerationFlagReturnEPR( _
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

 

 





