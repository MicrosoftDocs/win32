---
description: Assert and Breakpoint Macros
ms.assetid: c34db182-1f65-4a2f-9534-268638c2502d
title: Assert and Breakpoint Macros
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Assert and Breakpoint Macros

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The [DirectShow Base Classes](directshow-base-classes.md) provide several macros that perform asserts or cause breakpoints.



| Macro                                        | Description                                                                                                                        |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| [**ASSERT**](assert.md)                     | Evaluates an expression, and displays a diagnostic message if the expression is **FALSE**.                                         |
| [**DbgAssertAligned**](dbgassertaligned.md) | Tests whether a pointer is aligned to a specified boundary.                                                                        |
| [**DbgBreak**](dbgbreak.md)                 | Displays a message box with the specified string, the name of the source file, and the line number.                                |
| [**EXECUTE\_ASSERT**](execute-assert.md)    | Evaluates an expression in debug and retail builds. In debug builds, displays a diagnostic message if the expression is **FALSE**. |
| [**KASSERT**](kassert.md)                   | Evaluates an expression, and causes a breakpoint exception if the expression is **FALSE**.                                         |
| [**KDbgBreak**](kdbgbreak.md)               | Causes a breakpoint exception, and logs the specified string.                                                                      |



 

## Related topics

<dl> <dt>

[Debugging Utilities](debugging-utilities.md)
</dt> </dl>

 

 



