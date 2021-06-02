---
description: Handling Unicode in an IME-Aware Application
ms.assetid: fa202c1e-d0af-441f-b878-ed98205a880c
title: Handling Unicode in an IME-Aware Application
ms.topic: article
ms.date: 05/31/2018
---

# Handling Unicode in an IME-Aware Application

Two issues are involved with the IMM and its handling of Unicode. The first issue is that the Unicode versions of IMM functions retrieve the size of a buffer in bytes instead of 16-bit Unicode characters. The second issue is that the IMM normally retrieves Unicode characters (instead of DBCS characters) in the [**WM\_CHAR**](../inputdev/wm-char.md) and [**WM\_IME\_CHAR**](wm-ime-char.md) messages.

Windows supports a Unicode interface for the IMM, in addition to the ANSI interface originally supported.

Your applications should use [**RegisterClassW**](/windows/win32/api/winuser/nf-winuser-registerclassa) to cause the [**WM\_CHAR**](../inputdev/wm-char.md) and [**WM\_IME\_CHAR**](wm-ime-char.md) messages to retrieve Unicode characters instead of DBCS characters in the *wParam* parameter.

## Related topics

<dl> <dt>

[Using Input Method Manager](using-input-method-manager.md)
</dt> </dl>

 

 
