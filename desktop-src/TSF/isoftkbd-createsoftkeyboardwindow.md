---
title: ISoftKbd CreateSoftKeyboardWindow method (Softkbdc.h)
description: The ISoftKbd CreateSoftKeyboardWindow method creates a soft keyboard window.
ms.assetid: e9aa9d88-d0bb-407f-9b53-98c8747be5d3
keywords:
- CreateSoftKeyboardWindow method Text Services Framework
- CreateSoftKeyboardWindow method Text Services Framework , ISoftKbd interface
- ISoftKbd interface Text Services Framework , CreateSoftKeyboardWindow method
topic_type:
- apiref
api_name:
- ISoftKbd.CreateSoftKeyboardWindow
api_location:
- Softkbd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ISoftKbd::CreateSoftKeyboardWindow method

The **ISoftKbd::CreateSoftKeyboardWindow** method creates a soft keyboard window.

## Syntax


```C++
HRESULT CreateSoftKeyboardWindow(
  [in] HWND          hOwner,
  [in] TITLEBAR_TYPE Titlebar_type,
  [in] INT           xPos,
  [in] INT           yPos,
  [in] INT           width,
  [in] INT           height
);
```



## Parameters

<dl> <dt>

*hOwner* \[in\]
</dt> <dd>

Handle of the window to contain the soft keyboard.

</dd> <dt>

*Titlebar\_type* \[in\]
</dt> <dd>

Type of title bar for the soft keyboard window. Possible types are defined by the [**TITLEBAR\_TYPE**](titlebar-type.md) enumeration.

</dd> <dt>

*xPos* \[in\]
</dt> <dd>

The x position of the upper left corner of the soft keyboard window.

</dd> <dt>

*yPos* \[in\]
</dt> <dd>

The y position of the upper left corner of the soft keyboard window.

</dd> <dt>

*width* \[in\]
</dt> <dd>

The width of the soft keyboard window.

</dd> <dt>

*height* \[in\]
</dt> <dd>

The height of the soft keyboard window.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                        | Description                                    |
|----------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The method was successful.<br/>          |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | One or more parameters are invalid.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                        |
| Header<br/>                   | <dl> <dt>Softkbdc.h</dt> </dl>  |
| IDL<br/>                      | <dl> <dt>Softkbd.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Softkbd.dll</dt> </dl> |



## See also

<dl> <dt>

[**ISoftKbd**](isoftkbd.md)
</dt> <dt>

[**ISoftKbd::CreateSoftKeyboardLayoutFromResource**](isoftkbd-createsoftkeyboardlayoutfromresource.md)
</dt> <dt>

[**ISoftKbd::DestroySoftKeyboardWindow**](isoftkbd-destroysoftkeyboardwindow.md)
</dt> <dt>

[**ISoftKbd::ShowSoftKeyboard**](isoftkbd-showsoftkeyboard.md)
</dt> <dt>

[**TITLEBAR\_TYPE**](titlebar-type.md)
</dt> </dl>

 

 





