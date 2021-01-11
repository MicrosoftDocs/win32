---
description: Tests whether the InkDivider object can use the InkRecognizerContext class to analyze words.
ms.assetid: fd848fcc-5258-401f-8b51-b9d57da173da
title: RecognizerContextSet function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RecognizerContextSet
api_type: 
- LibDef
api_location: 
- InkDiv.dll
- InkDiv.dll.dll
---

# RecognizerContextSet function

Tests whether the [**InkDivider**](inkdivider-class.md) object can use the [**InkRecognizerContext**](inkrecognizercontext-class.md) class to analyze words.

This function is not intended to be used by application code.

## Syntax


```C++
HRESULT WINAPI RecognizerContextSet(
  _In_ INT_PTR hDivider
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
| <dl> <dt>**S\_OK**</dt> </dl>         | The function succeeded.<br/>              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The *pDivider* parameter is invalid.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | None supported<br/>                                                             |
| Library<br/>                  | <dl> <dt>InkDiv.dll</dt> </dl> |



 

 




