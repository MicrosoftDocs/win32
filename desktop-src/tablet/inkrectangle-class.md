---
description: Represents access to a rectangle.
ms.assetid: 78e6c29c-0f43-46a5-9d30-948de5f369c8
title: InkRectangle class (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- InkRectangle
- InkRectangle.IInkRectangle
api_type: 
- COM
api_location: 
- InkObj.dll
- InkObj.dll.dll
---

# InkRectangle class

Represents access to a rectangle.

**InkRectangle** has these types of members:

-   [Interfaces](#interfaces)
-   [Methods](#methods)
-   [Properties](#properties)

### Interfaces

The **InkRectangle** class defines these interfaces.



| Interface         | Description                                                            |
|:------------------|:-----------------------------------------------------------------------|
| **IInkRectangle** | This object implements the **IInkRectangle** COM interface.<br/> |



 

### Methods

The **InkRectangle** class has these methods.



| Method                                            | Description                                                                        |
|:--------------------------------------------------|:-----------------------------------------------------------------------------------|
| [**GetRectangle**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrectangle-getrectangle) | Retrieves the elements of the **InkRectangle** object in a single call.<br/> |
| [**SetRectangle**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrectangle-setrectangle) | Modifies the elements of the **InkRectangle** object in a single call.<br/>  |



 

### Properties

The **InkRectangle** class has these properties.



| Property                                         | Access type           | Description                                                        |
|:-------------------------------------------------|:----------------------|:-------------------------------------------------------------------|
| [**Bottom**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrectangle-get_bottom)<br/> | Read/write<br/> | Gets or sets the bottom position of the rectangle.<br/>      |
| [**Data**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrectangle-get_data)<br/>     | Read/write<br/> | Gets or sets access to the rectangle struct (C++ only).<br/> |
| [**Left**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrectangle-get_left)<br/>     | Read/write<br/> | Gets or sets the left position of the rectangle.<br/>        |
| [**Right**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrectangle-get_right)<br/>   | Read/write<br/> | Gets or sets the right position of the rectangle.<br/>       |
| [**Top**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrectangle-get_top)<br/>       | Read/write<br/> | Gets or sets the top position of the rectangle.<br/>         |



 

## Remarks

> [!Note]  
> A point is within an **InkRectangle** if it lies on the [**Left**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrectangle-get_left) or [**Top**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrectangle-get_top) side or is within all four sides. A point on the [**Right**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrectangle-get_right) or [**Bottom**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrectangle-get_bottom) side is considered outside the rectangle.

 

This object can be instantiated by calling the [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) method.

> [!Note]  
> An **InkRectangle** cannot be used if it is larger than LONG\_MAX (2^31 - 1) in either dimension.

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



 

