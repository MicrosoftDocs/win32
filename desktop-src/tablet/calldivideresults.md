---
description: Retrieves analysis results from the InkDivider object.
ms.assetid: 7fc2bb5a-172f-4f4e-84dd-e31925f86982
title: CallDivideResults function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CallDivideResults
api_type: 
- LibDef
api_location: 
- InkDiv.dll
- InkDiv.dll.dll
---

# CallDivideResults function

Retrieves analysis results from the [**InkDivider**](inkdivider-class.md) object.

This function is not intended to be used by application code.

## Syntax


```C++
HRESULT WINAPI CallDivideResults(
  _In_  INT_PTR   hDivider,
  _Out_ int       aWordStrokeIds[],
  _Out_ int       aLineStrokeIds[],
  _Out_ int       aParagraphStrokeIds[],
  _Out_ int       aDrawingStrokeIds[],
  _Out_ SAFEARRAY **pastrWords,
  _Out_ SAFEARRAY **pastrLines,
  _Out_ SAFEARRAY **pastrParagraphs,
  _Out_ int       *aWordRotationCenterX,
  _Out_ int       *aWordRotationCenterY,
  _Out_ float     *aWordAngle,
  _Out_ int       *aLineRotationCenterX,
  _Out_ int       *aLineRotationCenterY,
  _Out_ float     *aLineAngle
);
```



## Parameters

<dl> <dt>

*hDivider* \[in\]
</dt> <dd>

A handle to the [**InkDivider**](inkdivider-class.md) object.

</dd> <dt>

*aWordStrokeIds* \[out\]
</dt> <dd>

An array of identifiers associated with the word that is passed in to the [**InkDivider**](inkdivider-class.md) class.

</dd> <dt>

*aLineStrokeIds* \[out\]
</dt> <dd>

An array of [**ID**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkstrokedisp-get_id) properties for the [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) objects associated with the line that is passed in to the [**InkDivider**](inkdivider-class.md) class.

</dd> <dt>

*aParagraphStrokeIds* \[out\]
</dt> <dd>

An array of the [**ID**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkstrokedisp-get_id) properties for the [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) objects associated with the paragraph from the [**InkDivider**](inkdivider-class.md) class.

</dd> <dt>

*aDrawingStrokeIds* \[out\]
</dt> <dd>

An array of [**ID**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkstrokedisp-get_id) properties for the [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) objects associated with the drawing from the [**InkDivider**](inkdivider-class.md) class.

</dd> <dt>

*pastrWords* \[out\]
</dt> <dd>

An array of words returned from ink analysis.

</dd> <dt>

*pastrLines* \[out\]
</dt> <dd>

An array of lines returned from ink analysis.

</dd> <dt>

*pastrParagraphs* \[out\]
</dt> <dd>

An array of paragraphs returned from ink analysis.

</dd> <dt>

*aWordRotationCenterX* \[out\]
</dt> <dd>

An array of the center points of the words along the x-axis from ink analysis.

</dd> <dt>

*aWordRotationCenterY* \[out\]
</dt> <dd>

An array of the center points of the words along the y-axis from ink analysis.

</dd> <dt>

*aWordAngle* \[out\]
</dt> <dd>

An array containing the angles by which to rotate the words for best analysis results.

</dd> <dt>

*aLineRotationCenterX* \[out\]
</dt> <dd>

An array containing the center points of the lines along the x-axis.

</dd> <dt>

*aLineRotationCenterY* \[out\]
</dt> <dd>

An array containing the center points of the lines along the y-axis.

</dd> <dt>

*aLineAngle* \[out\]
</dt> <dd>

An array containing the angles by which to rotate the lines for best analysis results.

</dd> </dl>

## Return value

This function can return one of these values.



| Return code                                                                                   | Description                                                       |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | The function succeeded.<br/>                                |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *hDivider* parameter is invalid.<br/>                   |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Could not allocate enough memory to store the results.<br/> |



 

## Remarks

To avoid memory leaks you must release the resources for *pastrWords*, *pastrLines*, and *pastrParagraphs*.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | None supported<br/>                                                             |
| Library<br/>                  | <dl> <dt>InkDiv.dll</dt> </dl> |



 

 




