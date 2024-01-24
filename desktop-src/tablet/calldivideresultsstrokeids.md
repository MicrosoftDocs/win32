---
description: Retrieves the Id properties for the IInkStrokeDisp objects of the corresponding word, line, paragraph, or drawing determined by ink analysis.
ms.assetid: f05ffa3b-2a47-46fe-bb8f-e682aa094b69
title: CallDivideResultsStrokeIds function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CallDivideResultsStrokeIds
api_type: 
- LibDef
api_location: 
- InkDiv.dll
- InkDiv.dll.dll
---

# CallDivideResultsStrokeIds function

Retrieves the [**Id**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkstrokedisp-get_id) properties for the [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) objects of the corresponding word, line, paragraph, or drawing determined by ink analysis.

This function is not intended to be used by application code.

## Syntax


```C++
HRESULT WINAPI CallDivideResultsStrokeIds(
  _In_  INT_PTR hDivider,
  _Out_ int     aWordStrokeIds[],
  _Out_ int     aLineStrokeIds[],
  _Out_ int     aParagraphStrokeIds[],
  _Out_ int     aDrawingStrokeIds[]
);
```



## Parameters

<dl> <dt>

*hDivider* \[in\]
</dt> <dd>

A handle to the [Divider](the-divider-object.md) object.

</dd> <dt>

*aWordStrokeIds\[\]* \[out\]
</dt> <dd>

An array of the stroke IDs of the ink in the word.

</dd> <dt>

*aLineStrokeIds\[\]* \[out\]
</dt> <dd>

An array of the stroke IDs of the ink in the line.

</dd> <dt>

*aParagraphStrokeIds\[\]* \[out\]
</dt> <dd>

An array of the stroke IDs of the ink in the paragraph.

</dd> <dt>

*aDrawingStrokeIds\[\]* \[out\]
</dt> <dd>

An array of the stroke IDs of the ink in the drawing.

</dd> </dl>

## Return value

This function can return one of these values.



| Return code                                                                                  | Description                                     |
|----------------------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The function succeeded.<br/>              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The *hDivider* parameter is invalid.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | None supported<br/>                                                             |
| Library<br/>                  | <dl> <dt>InkDiv.dll</dt> </dl> |



 

 




