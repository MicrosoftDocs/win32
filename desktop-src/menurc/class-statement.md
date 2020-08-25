---
title: CLASS statement
description: Defines the class of the dialog box.
ms.assetid: 7c4325fe-66a4-4bb2-9c99-04b3ff590e7a
keywords:
- CLASS statement Menus and Other Resources
topic_type:
- apiref
api_name:
- CLASS
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# CLASS statement

Defines the class of the dialog box.

The **CLASS** statement appears in the optional section before a [**DIALOG**](dialog-resource.md) statement's main. If no class is given, the standard dialog class is used.

``` syntax
CLASS class
```

<dl> <dt>

<span id="class"></span><span id="CLASS"></span>*class*
</dt> <dd>

A 16-bit unsigned integer or a string, enclosed in double quotation marks ("), that identifies the class of the dialog box. If the window procedure for the class does not process a message sent to it, it must call the [**DefDlgProc**](/windows/win32/api/winuser/nf-winuser-defdlgprocw) function to ensure that all messages are handled properly for the dialog box. A private class can use **DefDlgProc** as the default window procedure. The class must be registered with the **cbWndExtra** member of the [**WNDCLASS**](/windows/win32/api/winuser/ns-winuser-wndclassa) structure set to **DLGWINDOWEXTRA**.

</dd> </dl>

## Remarks

The **CLASS** statement should only be used with special cases, because it overrides the normal processing of a dialog box. The **CLASS** statement converts a dialog box to a window of the specified class; depending on the class, this could give undesirable results. Do not use the redefined control-class names with this statement.

## Examples

The following example demonstrates the use of the **CLASS** statement:

``` syntax
CLASS "myclass" 
```

## See also

<dl> <dt>

[**DefDlgProc**](/windows/win32/api/winuser/nf-winuser-defdlgprocw)
</dt> <dt>

[**DIALOG**](dialog-resource.md)
</dt> </dl>

 

 