---
description: The Add method of the SWbemQualifierSet object adds an SWbemQualifier object to the SWbemQualifierSet collection. If a qualifier with the same name already exists in the collection, it is replaced.
ms.assetid: 8f4c4da2-4890-4515-a3dc-76d154dae43c
ms.tgt_platform: multiple
title: SWbemQualifierSet.Add method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemQualifierSet.Add
- ISWbemQualifierSet.Add
- ISWbemQualifierSet.Add
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemQualifierSet.Add method

The **Add** method of the [**SWbemQualifierSet**](swbemqualifierset.md) object adds an [**SWbemQualifier**](swbemqualifier.md) object to the **SWbemQualifierSet** collection. If a qualifier with the same name already exists in the collection, it is replaced.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objQualifier = .Add( _
  ByVal strName, _
  ByVal varVal, _
  [ ByVal bPropagatesToSubclasses ], _
  [ ByVal bPropagatesToInstances ], _
  [ ByVal bOverridable ], _
  [ ByVal iFlags ] _
)
```



## Parameters

<dl> <dt>

*strName* \[in\]
</dt> <dd>

Required. Name of the new qualifier.

</dd> <dt>

*varVal* \[in\]
</dt> <dd>

Required. Variant value of the new qualifier.

</dd> <dt>

*bPropagatesToSubclasses* \[in, optional\]
</dt> <dd>

Boolean value that indicates if this new qualifier is propagated to subclasses. The default value is **TRUE**.

</dd> <dt>

*bPropagatesToInstances* \[in, optional\]
</dt> <dd>

Boolean value that indicates if this new qualifier is propagated to instances. The default value is **TRUE**.

</dd> <dt>

*bOverridable* \[in, optional\]
</dt> <dd>

Boolean value that indicates if this qualifier can be overridden when propagated. The default value is **TRUE**.

</dd> <dt>

*iFlags* \[in, optional\]
</dt> <dd>

Reserved. The default value is 0.

</dd> </dl>

## Return value

If successful, this method returns an [**SWbemQualifier**](swbemqualifier.md) object that represents the new qualifier. Otherwise, a **null** object is returned.

## Error codes

After completion of the **Add** method, the **Err** object may contain one of the error codes in the following list.

<dl> <dt>

**wbemErrInvalidParameter** - 2147749896 (0x80041008)
</dt> <dd>

The *iFlags* parameter was not valid.

</dd> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error.

</dd> <dt>

**wbemErrCannotBeKey** - 2147749919 (0x8004101F)
</dt> <dd>

There was an illegal attempt to specify a **Key** qualifier on a property that cannot be a key. The keys are specified in the class definition for an object and cannot be altered on a per-instance basis.

</dd> <dt>

**wbemErrInvalidQualifierType** - 2147749929 (0x80041029)
</dt> <dd>

The *varVal* parameter is not of a legal qualifier type.

</dd> <dt>

**wbemErrOverrideNotAllowed** - 2147749914 (0x8004101A)
</dt> <dd>

It is not possible to perform the **SWbemQualifierSet.Add** operation on this qualifier because the owning object does not permit overrides.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemQualifierSet<br/>                                                     |
| IID<br/>                      | IID\_ISWbemQualifierSet<br/>                                                      |



## See also

<dl> <dt>

[**SWbemQualifierSet**](swbemqualifierset.md)
</dt> <dt>

[**SWbemQualifierSet.Remove**](swbemqualifierset-remove.md)
</dt> </dl>

 

 




