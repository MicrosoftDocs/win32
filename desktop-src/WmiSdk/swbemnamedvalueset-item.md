---
description: The Item method of the SWbemNamedValueSet object gets an SWbemNamedValue object from the collection.
ms.assetid: ccebe65e-6032-43d5-9004-2247c3b96d6d
ms.tgt_platform: multiple
title: SWbemNamedValueSet.Item method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemNamedValueSet.Item
- ISWbemNamedValueSet.Item
- ISWbemNamedValueSet.Item
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemNamedValueSet.Item method

The **Item** method of the [**SWbemNamedValueSet**](swbemnamedvalueset.md) object gets an [**SWbemNamedValue**](swbemnamedvalue.md) object from the collection.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objNamedValue = .Item( _
  ByVal strName, _
  [ ByVal iFlags ] _
)
```



## Parameters

<dl> <dt>

*strName* \[in\]
</dt> <dd>

Required. Name of the value to retrieve.

</dd> <dt>

*iFlags* \[in, optional\]
</dt> <dd>

Reserved. This value must be zero if specified.

</dd> </dl>

## Return value

If successful, the requested [**SWbemNamedValue**](swbemnamedvalue.md) object is returned.

## Error codes

Upon completion of the **Item** method, the **Err** object may contain one of the error codes in the following list.

<dl> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error.

</dd> <dt>

**wbemErrInvalidParameter** - 2147749896 (0x80041008)
</dt> <dd>

An invalid parameter was specified, or the namespace could not be parsed.

</dd> <dt>

**wbemErrOutOfMemory** - 2147749894 (0x80041006)
</dt> <dd>

Not enough memory to complete the operation.

</dd> <dt>

**wbemErrNotFound** - 2147749890 (0x80041002)
</dt> <dd>

The requested item was not found.

</dd> </dl>

## Remarks

For examples of adding and retrieving named values, see [**SWbemNamedValue.Value**](swbemnamedvalue-value.md).

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

 

 




