---
Description: Sets the LineHeight property on the InkDivider object.
ms.assetid: ce5e40c5-faa1-4d66-94f4-d5bd1a11ee4c
title: SetLineHeight function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SetLineHeight function

Sets the [**LineHeight**](/windows/win32/msinkaut15/?branch=master) property on the [**InkDivider**](/windows/win32/msinkaut15/?branch=master) object.

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

A handle to the [**InkDivider**](/windows/win32/msinkaut15/?branch=master) object.

</dd> <dt>

*lLineHeight* \[in\]
</dt> <dd>

The [**LineHeight**](/windows/win32/msinkaut15/?branch=master) property of the [**InkDivider**](/windows/win32/msinkaut15/?branch=master) object, in HIMETRIC units.

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



 

 




