---
description: Invokes helper functionality for the IDispatch interface.
ms.assetid: ccef47af-d9dd-48c3-93d3-ee997dacf7a8
title: InvokeIDispatch function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- InvokeIDispatch
api_type: 
- LibDef
api_location: 
- InkObj.dll
- InkObj.dll.dll
---

# InvokeIDispatch function

Invokes helper functionality for the IDispatch interface.

This function is not intended to be used by application code.

## Syntax


```C++
HRESULT WINAPI InvokeIDispatch(
        IDispatch  *pDispatch,
        DISPID     dispid,
        DISPPARAMS *pDisp,
  _Out_ VARIANT    *pVarResult
);
```



## Parameters

<dl> <dt>

*pDispatch* 
</dt> <dd>

The instance of the IDispatch interface.

</dd> <dt>

*dispid* 
</dt> <dd>

The method, property, or argument to pass in.

</dd> <dt>

*pDisp* 
</dt> <dd>

The parameters to pass in.

</dd> <dt>

*pVarResult* \[out\]
</dt> <dd>

A structure that receives the retrieved values.

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If it fails, possible return codes include, but are not limited to, the values shown in the following table.



| Return code                                                                                  | Description                                      |
|----------------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The value for *pDispatch* is invalid.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | None supported<br/>                                                             |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl> |



 

 




