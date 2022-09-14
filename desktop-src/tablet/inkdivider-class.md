---
description: Represents the ability to analyze the layout of a collection of strokes and divide them into text and graphics.
ms.assetid: 2c8e67fb-1032-4fcc-b419-82bae978daf8
title: InkDivider class (Msinkaut15.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- InkDivider
- InkDivider.IInkDivider
api_type: 
- COM
api_location: 
- Inkdiv.dll
- Inkdiv.dll.dll
---

# InkDivider class

Represents the ability to analyze the layout of a collection of strokes and divide them into text and graphics.

**InkDivider** has these types of members:

-   [Interfaces](#interfaces)
-   [Methods](#methods)
-   [Properties](#properties)

### Interfaces

The **InkDivider** class defines these interfaces.



| Interface       | Description                                                          |
|:----------------|:---------------------------------------------------------------------|
| **IInkDivider** | This object implements the **IInkDivider** COM interface.<br/> |



 

### Methods

The **InkDivider** class has these methods.



| Method                              | Description                                                                                                                                                        |
|:------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Divide**](/windows/win32/api/msinkaut15/nf-msinkaut15-iinkdivider-divide) | Returns an [**IInkDivisionResult**](/windows/desktop/api/msinkaut15/nn-msinkaut15-iinkdivisionresult) object that contains structural information about the strokes in the **InkDivider** object.<br/> |



 

### Properties

The **InkDivider** class has these properties.



| Property                                                             | Access type           | Description                                                                                                                     |
|:---------------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------------------------------------------|
| [**LineHeight**](/windows/win32/api/msinkaut15/nf-msinkaut15-iinkdivider-get_lineheight)<br/>               | Read/write<br/> | Gets or sets the expected handwriting height in HIMETRIC units.<br/>                                                      |
| [**RecognizerContext**](/windows/win32/api/msinkaut15/nf-msinkaut15-iinkdivider-get_recognizercontext)<br/> | Read/write<br/> | Gets or sets the [**InkRecognizerContext**](inkrecognizercontext-class.md) object used for handwriting recognition.<br/> |
| [**Strokes**](/windows/win32/api/msinkaut15/nf-msinkaut15-iinkdivider-get_strokes)<br/>                     | Read/write<br/> | Gets or sets the [**InkStrokes**](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) collection contained by the **InkDivider** object. <br/>     |



 

## Remarks

This object can be instantiated by calling the [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) method in C++.

The **InkDivider** object uses the layout of the strokes, the order in which the strokes are added, the direction in which the strokes are drawn, and other factors to perform the analysis of the ink. The [InkStrokes](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) collection that the **InkDivider** object analyzes is contained in the [**Strokes**](/windows/win32/api/msinkaut15/nf-msinkaut15-iinkdivider-get_strokes) property of the **InkDivider** object. The **InkDivider** object dynamically analyzes the InkStrokes collection as you add to or delete from the collection, but it performs no modification of the strokes.

The analysis results are returned in an [**IInkDivisionResult**](/windows/desktop/api/msinkaut15/nn-msinkaut15-iinkdivisionresult) object.

The **InkDivider** object uses an [**InkRecognizerContext**](inkrecognizercontext-class.md) object to more accurately divide the strokes and to assign a recognition string to the results.

> [!Note]  
> The **InkDivider** object uses the default property settings of the [**InkRecognizerContext**](inkrecognizercontext-class.md) object.

 

If you do not assign a recognizer context to the **InkDivider** object, the **InkDivider** object still analyzes the ink, but it divides the strokes less accurately and does not associate text with the division results.

> [!Note]  
> The [**RecognizerContext**](/windows/win32/api/msinkaut15/nf-msinkaut15-iinkdivider-get_recognizercontext) property should be set before adding strokes to the [**Strokes**](/windows/win32/api/msinkaut15/nf-msinkaut15-iinkdivider-get_strokes) property. After strokes have been added to the **InkDivider** object, the **RecognizerContext** property cannot be changed.

 

The **InkDivider** does not currently support vertical languages. For the **InkDivider** object to recognize these languages properly the [**IInkRecognizer**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkrecognizer) object for the language must support the free input capability and the characters must be written from left to right.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | None supported<br/>                                                                                               |
| Header<br/>                   | <dl> <dt>Msinkaut15.h (also requires Msinkaut15\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Inkdiv.dll</dt> </dl>                                   |



## See also

<dl> <dt>

[**IInkDivisionResult Interface**](/windows/desktop/api/msinkaut15/nn-msinkaut15-iinkdivisionresult)
</dt> <dt>

[**InkRecognizerContext Class**](inkrecognizercontext-class.md)
</dt> <dt>

[InkStrokes Collection](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85))
</dt> </dl>

 

