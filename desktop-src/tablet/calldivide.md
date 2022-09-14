---
description: Retrieves analysis information from the InkDivider object.
ms.assetid: 1b073da4-80f4-48f4-8ff6-b21793c173a8
title: CallDivide function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CallDivide
api_type: 
- LibDef
api_location: 
- InkDiv.dll
- InkDiv.dll.dll
---

# CallDivide function

Retrieves analysis information from the [**InkDivider**](inkdivider-class.md) object.

This function is not intended to be used by application code.

## Syntax


```C++
HRESULT WINAPI CallDivide(
  _In_  INT_PTR hDivider,
  _In_  int     *pWordSize,
  _In_  int     *pLineSize,
  _In_  int     *pParagraphSize,
  _In_  int     *pDrawingSize,
  _Out_ int     *pWordCount,
  _Out_ int     *pLineCount,
  _Out_ int     *pParagraphCount
);
```



## Parameters

<dl> <dt>

*hDivider* \[in\]
</dt> <dd>

A handle to the [**InkDivider**](inkdivider-class.md) object.

</dd> <dt>

*pWordSize* \[in\]
</dt> <dd>

The size of the word returned by the [**InkDivider**](inkdivider-class.md) object.

</dd> <dt>

*pLineSize* \[in\]
</dt> <dd>

The size of the line returned by the [**InkDivider**](inkdivider-class.md) object.

</dd> <dt>

*pParagraphSize* \[in\]
</dt> <dd>

The size of the paragraph returned by the [**InkDivider**](inkdivider-class.md) object.

</dd> <dt>

*pDrawingSize* \[in\]
</dt> <dd>

The size of the drawing returned by the [**InkDivider**](inkdivider-class.md) object.

</dd> <dt>

*pWordCount* \[out\]
</dt> <dd>

The number of words returned by ink analysis.

</dd> <dt>

*pLineCount* \[out\]
</dt> <dd>

The number of lines returned by ink analysis.

</dd> <dt>

*pParagraphCount* \[out\]
</dt> <dd>

The number of paragraphs returned by ink analysis.

</dd> </dl>

## Return value

This function can return one of these values.



| Return code                                                                                  | Description                                    |
|----------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The function suceeded.<br/>              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | One or more parameters are invalid.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | None supported<br/>                                                             |
| Library<br/>                  | <dl> <dt>InkDiv.dll</dt> </dl> |



 

 




