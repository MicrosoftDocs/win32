---
description: Pointer Validation Macros
ms.assetid: 53b080ba-d8cf-48a3-a895-2c14d54f7e21
title: Pointer Validation Macros
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Pointer Validation Macros

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Microsoft DirectShow provides several macros for validating pointers.



| Macro                                                | Description                                                                   |
|------------------------------------------------------|-------------------------------------------------------------------------------|
| [**CheckPointer**](checkpointer.md)                 | Checks whether a pointer is **NULL**.                                         |
| [**ValidateReadPtr**](validatereadptr.md)           | Verifies that the calling process has read access to a memory block.          |
| [**ValidateReadWritePtr**](validatereadwriteptr.md) | Verifies that the calling process has read/write access to a memory block.    |
| [**ValidateStringPtr**](validatestringptr.md)       | Verifies that the calling process has read access to a string.                |
| [**ValidateStringPtrA**](validatestringptra.md)     | Verifies that the calling process has read access to an ANSI string.          |
| [**ValidateStringPtrW**](validatestringptrw.md)     | Verifies that the calling process has read access to a wide-character string. |
| [**ValidateWritePtr**](validatewriteptr.md)         | Verifies that the calling process has write access to a memory block.         |



 

 

 



