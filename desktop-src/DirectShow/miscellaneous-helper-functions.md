---
description: Miscellaneous Helper Functions
ms.assetid: 6d022907-6838-4d22-81ca-57c35bcb8b0d
title: Miscellaneous Helper Functions
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Miscellaneous Helper Functions

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following are miscellaneous helper functions.



| Function                                                   | Description                                                                                                   |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [**EqualPins**](equalpins.md)                             | Checks if two pins are on the same object.                                                                    |
| [**Int64x32Div32**](int64x32div32.md)                     | Implements the formula `((a*b)+rnd)/c` where `a` is a 64-bit value and `b`, `c`, and `rnd` are 32-bit values. |
| [**IsEqualObject**](isequalobject.md)                     | Checks if two interfaces are on the same object.                                                              |
| [**llMulDiv**](llmuldiv.md)                               | Implements the formula `((a*b)+rnd)/c` where each term is a 64-bit value.                                     |
| [**WaitDispatchingMessages**](waitdispatchingmessages.md) | Waits for an object to be signaled, while dispatching window messages.                                        |



 

 

 



