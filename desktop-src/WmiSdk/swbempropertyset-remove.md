---
description: The Remove method of the SWbemPropertySet object deletes a property from the SWbemPropertySet collection.
ms.assetid: 2a1005db-033c-48f9-8ea0-0bd43b8c989f
ms.tgt_platform: multiple
title: SWbemPropertySet.Remove method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemPropertySet.Remove
- ISWbemPropertySet.Remove
- ISWbemPropertySet.Remove
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemPropertySet.Remove method

The **Remove** method of the [**SWbemPropertySet**](swbempropertyset.md) object deletes a property from the **SWbemPropertySet** collection.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
SWbemPropertySet.Remove( _
  ByVal strName, _
  [ ByVal iFlags ] _
)
```



## Parameters

<dl> <dt>

*strName* \[in\]
</dt> <dd>

Required. Name of the item to remove.

</dd> <dt>

*iFlags* \[in, optional\]
</dt> <dd>

Reserved. This value must be 0 (zero) if specified.

</dd> </dl>

## Return value

This method does not return a value.

## Error codes

After completion of the **Remove** method, the **Err** object may contain one of the error codes in the following list.

<dl> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified failure.

</dd> <dt>

**wbemErrInvalidOperation** - 2147749910 (0x80041016)
</dt> <dd>

User attempted to delete a property that cannot be deleted.

</dd> <dt>

**wbemErrInvalidParameter** - 2147749896 (0x80041008)
</dt> <dd>

Invalid parameter was specified.

</dd> <dt>

**wbemErrNotFound** - 2147749890 (0x80041002)
</dt> <dd>

Specified property does not exist.

</dd> <dt>

**wbemErrOutOfMemory** - 2147749894 (0x80041006)
</dt> <dd>

Not enough memory for this method to execute.

</dd> <dt>

**wbemErrPropagatedProperty** - 142927303552 (0x2147219380)
</dt> <dd>

User attempted to delete a property that was not owned. The property was inherited from a parent class.

</dd> <dt>

**wbemErrResetToDefault** - 2147758082 (0x80043002)
</dt> <dd>

User deleted an override default value for the current class. The default value for this property in the parent class has been reactivated.

</dd> </dl>

## Remarks

Properties cannot be removed from class instances or derived classes with inherited properties. Such deletion attempts raise an error and the property is not removed; the property is reset to its default value.

You cannot iterate a collection while removing items because when you remove an element from a collection, the collection pointer is moved to the next element. For more information, see [Accessing a Collection](accessing-a-collection.md).

## Examples

For a code example that uses this method, see the [**SWbemPropertySet**](swbempropertyset.md) topic.

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



## See also

<dl> <dt>

[**SWbemPropertySet**](swbempropertyset.md)
</dt> <dt>

[**SWbemPropertySet.Add**](swbempropertyset-add.md)
</dt> </dl>

 

 




