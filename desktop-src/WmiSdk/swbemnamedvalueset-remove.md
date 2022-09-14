---
description: The Remove method of the SWbemNamedValueSet object deletes a named value from the context.
ms.assetid: 8cb353fb-c6d7-41d9-a2d0-ff1ad37264e4
ms.tgt_platform: multiple
title: SWbemNamedValueSet.Remove method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemNamedValueSet.Remove
- ISWbemNamedValueSet.Remove
- ISWbemNamedValueSet.Remove
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemNamedValueSet.Remove method

The **Remove** method of the [**SWbemNamedValueSet**](swbemnamedvalueset.md) object deletes a named value from the context.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
SWbemNamedValueSet.Remove( _
  ByVal strName, _
  [ ByVal iFlags ] _
)
```



## Parameters

<dl> <dt>

*strName* \[in\]
</dt> <dd>

Required. Name of the value to remove.

</dd> <dt>

*iFlags* \[in, optional\]
</dt> <dd>

Reserved. This value must be zero if specified.

</dd> </dl>

## Return value

This method does not return a value.

## Error codes

Upon completion of the **Remove** method, the **Err** object may contain one of the error codes in the following list.

<dl> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error.

</dd> <dt>

**wbemErrInvalidParameter** - 2147749896 (0x80041008)
</dt> <dd>

An invalid parameter was specified, or the namespace could not be parsed.

</dd> <dt>

**wbemErrNotFound** - 2147749890 (0x80041002)
</dt> <dd>

The requested item was not found.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemNamedValueSet<br/>                                                    |
| IID<br/>                      | IID\_ISWbemNamedValueSet<br/>                                                     |



## See also

<dl> <dt>

[**SWbemNamedValueSet**](swbemnamedvalueset.md)
</dt> </dl>

 

 




