---
description: The Item method of the SWbemPropertySet object gets a named SWbemProperty from the collection. This is the default method for this object.
ms.assetid: 72025676-01dd-4fd7-b000-de6b09ecc6dc
ms.tgt_platform: multiple
title: SWbemPropertySet.Item method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemPropertySet.Item
- ISWbemPropertySet.Item
- ISWbemPropertySet.Item
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemPropertySet.Item method

The **Item** method of the [**SWbemPropertySet**](swbempropertyset.md) object gets a named [**SWbemProperty**](swbemproperty.md) from the collection. This is the default method for this object.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objProperty = .Item( _
  ByVal strName, _
  [ ByVal iFlags ] _
)
```



## Parameters

<dl> <dt>

*strName* \[in\]
</dt> <dd>

Required. Name of the property to retrieve.

</dd> <dt>

*iFlags* \[in, optional\]
</dt> <dd>

Reserved. This value must be zero if specified.

</dd> </dl>

## Return value

If successful, the requested [**SWbemProperty**](swbemproperty.md) object is returned.

## Error codes

After the completion of the **Item** method, the **Err** object may contain one of the error codes in the following list.

<dl> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified failure.

</dd> <dt>

**wbemErrInvalidParameter** - 2147749896 (0x80041008)
</dt> <dd>

Invalid parameter was specified.

</dd> <dt>

**wbemErrOutOfMemory** - 2147749896
</dt> <dd>

Not enough memory for this method to execute.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemPropertySet<br/>                                                      |
| IID<br/>                      | IID\_ISWbemPropertySet<br/>                                                       |



 

 




