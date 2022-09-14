---
title: IAgentEx ShowDefaultCharacterProperties
description: IAgentEx ShowDefaultCharacterProperties
ms.assetid: 4817b52a-7168-4008-9cda-0b8d598daea0
ms.topic: article
ms.date: 05/31/2018
---

# IAgentEx::ShowDefaultCharacterProperties

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT ShowDefaultCharacterProperties(
   short x,          // x-coordinate of window
   short y,          // y-coordinate of window
   long bUseDefault  // default position flag
);
```

Displays default character properties window.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="x"></span><span id="X"></span>*x*
</dt> <dd>

The x-coordinate of the window in pixels, relative to the screen origin (upper left).

</dd> <dt>

<span id="y"></span><span id="Y"></span>*y*
</dt> <dd>

The y-coordinate of the window in pixels, relative to the screen origin (upper left).

</dd> <dt>

<span id="bUseDefault"></span><span id="busedefault"></span><span id="BUSEDEFAULT"></span>*bUseDefault*
</dt> <dd>

Default position flag. If this parameter is **True**, Microsoft Agent displays the property sheet window for the default character at the last location it appeared.

> [!Note]  
> For Windows 2000, it may be necessary to call the new [**AllowSetForegroundWindow**](/windows/desktop/api/winuser/nf-winuser-allowsetforegroundwindow) API to ensure that this window becomes the foreground window. For more information about setting the foreground window under Windows 2000, see the Platform SDK documentation.

 

</dd> </dl>

## See Also

[**IAgentNotifySinkEx::DefaultCharacterChange**](iagentnotifysinkex--defaultcharacterchange.md)


 

 