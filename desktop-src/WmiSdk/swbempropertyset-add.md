---
description: The Add method of the SWbemPropertySet object adds an SWbemProperty object to the SWbemPropertySet collection. If a property with the same name already exists in the collection, its contents are replaced with the new definition.
ms.assetid: 52a5f964-3d53-441b-9a58-650afdc5b1b9
ms.tgt_platform: multiple
title: SWbemPropertySet.Add method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemPropertySet.Add
- ISWbemPropertySet.Add
- ISWbemPropertySet.Add
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemPropertySet.Add method

The **Add** method of the [**SWbemPropertySet**](swbempropertyset.md) object adds an [**SWbemProperty**](swbemproperty.md) object to the **SWbemPropertySet** collection. If a property with the same name already exists in the collection, its contents are replaced with the new definition.

> [!Note]  
> The value of the added property is **NULL** (unassigned) after this operation. To set or change the value of a WMI property, you must set the [**Value**](swbemdatetime-value.md) property of the returned [**SWbemProperty**](swbemproperty.md) object.

 

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objProperty = .Add( _
  ByVal strName, _
  ByVal iCIMType, _
  [ ByVal bIsArray ], _
  [ ByVal iFlags ] _
)
```



## Parameters

<dl> <dt>

*strName* \[in\]
</dt> <dd>

Required. Name of the new property.

</dd> <dt>

*iCIMType* \[in\]
</dt> <dd>

Required. An integer that represents the **CIMType** qualifier of the new property. See [**WbemCimTypeEnum**](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemcimtypeenum) for the list with the **CIMType** qualifiers and their values.

</dd> <dt>

*bIsArray* \[in, optional\]
</dt> <dd>

Specifies whether the property is an array type. The default value for this parameter is **FALSE**.

</dd> <dt>

*iFlags* \[in, optional\]
</dt> <dd>

Reserved and must be zero if specified.

</dd> </dl>

## Return value

If successful, this method returns an [**SWbemProperty**](swbemproperty.md) object that represents the new property. Otherwise, a **null** object is returned.

## Error codes

After completion of the **Add** method, the **Err** object may contain one of the error codes below.

<dl> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified failure.

</dd> <dt>

**wbemErrInvalidParameter** - 2147749896 (0x80041008)
</dt> <dd>

Invalid parameter was specified.

</dd> <dt>

**wbemErrOutOfMemory** - 2147749894 (0x80041006)
</dt> <dd>

Not enough memory for this method to execute.

</dd> <dt>

**wbemErrInvalidPropertyType** - 2147749930
</dt> <dd>

The **CIMType** qualifier is not recognized.

</dd> </dl>

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

[**SWbemPropertySet.Remove**](swbempropertyset-remove.md)
</dt> <dt>

[**SWbemProperty.Value**](swbemproperty-value.md)
</dt> </dl>

 

 




