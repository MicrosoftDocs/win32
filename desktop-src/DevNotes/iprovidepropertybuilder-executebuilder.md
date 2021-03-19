---
description: Notifies an object that it should display its builder for the specified property.
ms.assetid: 4d855aed-aaa1-4cc8-be9d-1175c254a813
title: IProvidePropertyBuilder::ExecuteBuilder method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IProvidePropertyBuilder.ExecuteBuilder
api_type: 
- COM
api_location: 
- Vsp.dll
---

# IProvidePropertyBuilder::ExecuteBuilder method

Notifies an object that it should display its builder for the specified property.

## Syntax


```C++
void ExecuteBuilder(
  [in]          LONG      dispid,
  [in]          BSTR      bstrGuidBldr,
  [in]          IDispatch *pdispApp,
  [in]          LONG_PTR  hwndBldrOwner,
  [in, out]     LPVARIANT pvarValue,
  [out, retval] LPBOOL    pbActionCommitted
);
```



## Parameters

<dl> <dt>

*dispid* \[in\]
</dt> <dd>

The DISPID of the property for which the builder displays.

</dd> <dt>

*bstrGuidBldr* \[in\]
</dt> <dd>

The **BSTR** of the builder GUID to invoke. This is returned from [**MapToPropertyBuilder**](iprovidepropertybuilder-mappropertytobuilder.md).

</dd> <dt>

*pdispApp* \[in\]
</dt> <dd>

Set to **NULL**.

</dd> <dt>

*hwndBldrOwner* \[in\]
</dt> <dd>

A handle to the parent pop-up builder window.

</dd> <dt>

*pvarValue* \[in, out\]
</dt> <dd>

The current value of the property. This value can be modified by the object and changes to the new value if *pbActionCommitted* is **TRUE**.

</dd> <dt>

*pbActionCommitted* \[out, retval\]
</dt> <dd>

A value that indicates whether the builder performed an action on the object. Can be used when a user modifies something, then presses OK on the pop-up builder dialog box.

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

 

 




