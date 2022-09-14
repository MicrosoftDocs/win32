---
description: Deletes an InkDivider object and releases associated resources.
ms.assetid: adf772e0-2829-4410-83c4-45a24bf3a848
title: DeleteInkDivider function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DeleteInkDivider
api_type: 
- LibDef
api_location: 
- InkDiv.dll
- InkDiv.dll.dll
---

# DeleteInkDivider function

Deletes an [**InkDivider**](inkdivider-class.md) object and releases associated resources.

This function is not intended to be used by application code.

## Syntax


```C++
HRESULT WINAPI DeleteInkDivider(
  _In_ INT_PTR hDivider
);
```



## Parameters

<dl> <dt>

*hDivider* \[in\]
</dt> <dd>

A handle to the [**InkDivider**](inkdivider-class.md) object.

</dd> </dl>

## Return value

This function can return one of these values.



| Return code                                                                                  | Description                                     |
|----------------------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The method succeeded.<br/>                |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The *hDivider* parameter is invalid.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | None supported<br/>                                                             |
| Library<br/>                  | <dl> <dt>InkDiv.dll</dt> </dl> |



 

 




