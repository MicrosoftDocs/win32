---
Description: Sets the LineHeight property on the InkDivider object.
ms.assetid: ce5e40c5-faa1-4d66-94f4-d5bd1a11ee4c
title: SetLineHeight function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetLineHeight function

Sets the [**LineHeight**](https://msdn.microsoft.com/en-us/library/ms699524(v=VS.85).aspx) property on the [**InkDivider**](https://msdn.microsoft.com/en-us/library/ms696382(v=VS.85).aspx) object.

This helper function is not intended to be used by application code.

## Syntax


```C++
HRESULT WINAPI SetLineHeight(
  _In_ INT_PTR hDivider,
  _In_ LONG    lLineHeight
);
```



## Parameters

<dl> <dt>

*hDivider* \[in\]
</dt> <dd>

A handle to the [**InkDivider**](https://msdn.microsoft.com/en-us/library/ms696382(v=VS.85).aspx) object.

</dd> <dt>

*lLineHeight* \[in\]
</dt> <dd>

The [**LineHeight**](https://msdn.microsoft.com/en-us/library/ms699524(v=VS.85).aspx) property of the [**InkDivider**](https://msdn.microsoft.com/en-us/library/ms696382(v=VS.85).aspx) object, in HIMETRIC units.

</dd> </dl>

## Return value

This function can return one of these values.



| Return code                                                                                  | Description                                     |
|----------------------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The function succeeded.<br/>              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The *pDivider* parameter is invalid.<br/> |



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | None supported<br/>                                                             |
| Library<br/>                  | <dl> <dt>InkDiv.dll</dt> </dl> |



 

 




