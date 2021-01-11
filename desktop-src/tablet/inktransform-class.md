---
description: Represents a 3x3 matrix that, in turn, represents an affine transformation.
ms.assetid: 79abff2e-d1d3-4a32-9ac2-f46c1b21f742
title: InkTransform class (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- InkTransform
api_type: 
- COM
api_location: 
- InkObj.dll
- InkObj.dll.dll
---

# InkTransform class

Represents a 3x3 matrix that, in turn, represents an affine transformation.

**InkTransform** has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **InkTransform** class has these methods.



| Method                                                  | Description                                                                                                                 |
|:--------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------|
| [**GetTransform**](/windows/desktop/api/msinkaut/nf-msinkaut-iinktransform-gettransform)       | Retrieves the **InkTransform** as 6 floats.<br/>                                                                      |
| [**Reflect**](/windows/desktop/api/msinkaut/nf-msinkaut-iinktransform-reflect)                 | Reflects the transform in either the horizontal or vertical directions.<br/>                                          |
| [**Reset**](/windows/desktop/api/msinkaut/nf-msinkaut-iinktransform-reset)                     | Resets the transform to its original state.<br/>                                                                      |
| [**Rotate**](/windows/desktop/api/msinkaut/nf-msinkaut-iinktransform-rotate)                   | Rotates the transform by an angle measured in degrees, and optionally specifies a center point for the rotation.<br/> |
| [**ScaleTransform**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkstrokedisp-scaletransform) | Scales the transform by X and Y factors.<br/>                                                                         |
| [**SetTransform**](/windows/desktop/api/msinkaut/nf-msinkaut-iinktransform-settransform)       | Modifies the **InkTransform** using 6 floats.<br/>                                                                    |
| [**Shear**](/windows/desktop/api/msinkaut/nf-msinkaut-iinktransform-shear)                     | Applies a shear with the specified horizontal and vertical factors.<br/>                                              |
| [**Translate**](/windows/desktop/api/msinkaut/nf-msinkaut-iinktransform-translate)             | Moves the transform by the specified horizontal and vertical components.<br/>                                         |



 

### Properties

The **InkTransform** class has these properties.



| Property                                     | Access type           | Description                                                                                          |
|:---------------------------------------------|:----------------------|:-----------------------------------------------------------------------------------------------------|
| [**Data**](/windows/desktop/api/msinkaut/nf-msinkaut-iinktransform-get_data)<br/> | Read/write<br/> | Gets or sets the Automation version of the WIN32 XFORM struct.<br/>                            |
| [**eDx**](/windows/desktop/api/msinkaut/nf-msinkaut-iinktransform-get_edx)<br/>   | Read/write<br/> | Gets or sets the real number that specifies the element in the third row, first column.<br/>   |
| [**eDy**](/windows/desktop/api/msinkaut/nf-msinkaut-iinktransform-get_edy)<br/>   | Read/write<br/> | Gets or sets the real number that specifies the element in the third row, second column.<br/>  |
| [**eM11**](/windows/desktop/api/msinkaut/nf-msinkaut-iinktransform-get_em11)<br/> | Read/write<br/> | Gets or sets the real number that specifies the element in the first row, first column.<br/>   |
| [**eM12**](/windows/desktop/api/msinkaut/nf-msinkaut-iinktransform-get_em12)<br/> | Read/write<br/> | Gets or sets the real number that specifies the element in the first row, second column.<br/>  |
| [**eM21**](/windows/desktop/api/msinkaut/nf-msinkaut-iinktransform-get_em21)<br/> | Read/write<br/> | Gets or sets the real number that specifies the element in the second row, first column.<br/>  |
| [**eM22**](/windows/desktop/api/msinkaut/nf-msinkaut-iinktransform-get_em22)<br/> | Read/write<br/> | Gets or sets the real number that specifies the element in the second row, second column.<br/> |



 

## Remarks

This object can be instantiated by calling the [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) method in C++.

The object stores only six of the nine numbers in a 3x3 matrix because all 3x3 matrices that represent affine transformations have the same third column (0, 0, 1). This object in turn is used to describe transformation operations such as moving, shearing, scaling, or rotating in an [**InkRenderer**](inkrenderer-class.md) object, [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) object, or [InkStrokes](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) collection.

> [!Note]  
> The **InkTransform** object correlates to the [**XFORM**](/windows/win32/api/wingdi/ns-wingdi-xform) structure.

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



 

