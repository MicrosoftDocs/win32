---
description: Checks whether a builder should be associated with a particular property.
ms.assetid: 8fab2dc2-3549-4559-b704-6783d929274e
title: IProvidePropertyBuilder::MapPropertyToBuilder method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IProvidePropertyBuilder.MapPropertyToBuilder
api_type: 
- COM
api_location: 
- Vsp.dll
---

# IProvidePropertyBuilder::MapPropertyToBuilder method

Checks whether a builder should be associated with a particular property.

## Syntax


```C++
void MapPropertyToBuilder(
  [in]          LONG   dispid,
  [out]         DWORD  *pdwCtlBldType,
  [out]         LPBSTR pbstrGuidBldr,
  [out, retval] LPBOOL builderAvailable
);
```



## Parameters

<dl> <dt>

*dispid* \[in\]
</dt> <dd>

The DISPID of the property in question.

</dd> <dt>

*pdwCtlBldType* \[out\]
</dt> <dd>

The builder to be mapped. This parameter can be a combination of the following values.



| Value                                                                                                                                                                                                                                                          | Meaning                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| <span id="CTLBLDTYPE_FSTDPROPBUILDER"></span><span id="ctlbldtype_fstdpropbuilder"></span><dl> <dt>**CTLBLDTYPE\_FSTDPROPBUILDER**</dt> <dt>1</dt> </dl>    | Invoke a standard system builder (not supported in Visual Studio).<br/> |
| <span id="CTLBLDTYPE_FINTERNALBUILDER"></span><span id="ctlbldtype_finternalbuilder"></span><dl> <dt>**CTLBLDTYPE\_FINTERNALBUILDER**</dt> <dt>2</dt> </dl> | Invoke a custom builder.<br/>                                           |
| <span id="CTLBLDTYPE_EDITSOBJDIRECTLY"></span><span id="ctlbldtype_editsobjdirectly"></span><dl> <dt>**CTLBLDTYPE\_EDITSOBJDIRECTLY**</dt> <dt>4</dt> </dl> | Builder modifies the object. This is common behavior.<br/>              |



 

</dd> <dt>

*pbstrGuidBldr* \[out\]
</dt> <dd>

The GUID that identifies the builder for this property.

</dd> <dt>

*builderAvailable* \[out, retval\]
</dt> <dd>

This parameter is **TRUE** if this property currently supports a builder.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Requirements



| Requirement | Value |
|----------------|------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Vsp.dll</dt> </dl> |



## See also

<dl> <dt>

[**IProvidePropertyBuilder**](iprovidepropertybuilder.md)
</dt> </dl>

 

 




