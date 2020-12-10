---
title: Rect Type Function (D2d1helper.h)
description: Creates a rectangle structure that stores its coordinates using the specified data type.
ms.assetid: b152efaf-0779-4024-b998-82a347abba71
keywords:
- Rect Type Function Direct2D
topic_type:
- apiref
api_name:
- Rect Type Function
api_location:
- D2d1.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Rect<Type> Function

Creates a rectangle structure that stores its coordinates using the specified data type.

``` syntax
template<typename Type>
typename TypeTraits<Type>::Rect Rect(
  Type left,
  Type top,
  Type right,
  Type bottom
);
```

## Template Parameters



| Parameter | Description                                                                                                |
|-----------|------------------------------------------------------------------------------------------------------------|
| Type      | The data type used to store the dimensions of the rectangle. Possible values are **FLOAT** and **UINT32**. |



 

## Parameters



| Parameter | Description                                             |
|-----------|---------------------------------------------------------|
| left      | The x-coordinate of the rectangle's upper-left corner.  |
| top       | The y-coordinate of the rectangle's upper-left corner.  |
| right     | The x-coordinate of the rectangle's lower-right corner. |
| bottom    | The y-coordinate of the rectangle's lower-right corner. |



 

## Return Value

A rectangle structure that contains the specified coordinates.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7, Windows Vista with SP2 and Platform Update for Windows Vista \[desktop apps \| UWP apps\]<br/>                          |
| Minimum supported server<br/> | Windows Server 2008 R2, Windows Server 2008 with SP2 and Platform Update for Windows Server 2008 \[desktop apps \| UWP apps\]<br/> |
| Minimum supported phone<br/>  | Windows Phone 8.1 \[Windows Phone Silverlight 8.1 and Windows Runtime apps\]<br/>                                                  |
| Header<br/>                   | <dl> <dt>D2d1helper.h</dt> </dl>                                                  |
| Library<br/>                  | <dl> <dt>D2d1.lib</dt> </dl>                                                      |
| DLL<br/>                      | <dl> <dt>D2d1.dll</dt> </dl>                                                      |



 

 





