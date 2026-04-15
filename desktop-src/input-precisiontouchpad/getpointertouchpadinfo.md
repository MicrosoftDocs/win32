---
title: GetPointerTouchpadInfo functions (Winuser.h)
description: Retrieves touchpad-specific information for pointer input, including single-pointer and frame variants with optional history.
ms.topic: reference
ms.date: 03/28/2026
---

# GetPointerTouchpadInfo functions

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Retrieves touchpad-specific pointer information. Four variants are available depending on whether you need a single pointer or an entire frame, and whether you need the current state or full history.

## Syntax

```cpp
WINUSERAPI
BOOL
WINAPI
GetPointerTouchpadInfo(
    _In_ UINT32 pointerId,
    _Out_writes_(1) POINTER_TOUCH_INFO *touchpadInfo);

WINUSERAPI
BOOL
WINAPI
GetPointerTouchpadInfoHistory(
    _In_ UINT32 pointerId,
    _Inout_ UINT32 *entriesCount,
    _Out_writes_opt_(*entriesCount) POINTER_TOUCH_INFO *touchpadInfo);

WINUSERAPI
BOOL
WINAPI
GetPointerFrameTouchpadInfo(
    _In_ UINT32 pointerId,
    _Inout_ UINT32 *pointerCount,
    _Out_writes_opt_(*pointerCount) POINTER_TOUCH_INFO *touchpadInfo);

WINUSERAPI
BOOL
WINAPI
GetPointerFrameTouchpadInfoHistory(
    _In_ UINT32 pointerId,
    _Inout_ UINT32 *entriesCount,
    _Inout_ UINT32 *pointerCount,
    _Out_writes_opt_(*entriesCount * *pointerCount) POINTER_TOUCH_INFO *touchpadInfo);
```

## Parameters

<dl>
<dt><em>pointerId</em></dt>
<dd>

The identifier of the pointer for which to retrieve information.

</dd>
<dt><em>entriesCount</em> (History variants)</dt>
<dd>

A pointer to a value that specifies the number of entries in the buffer. On input, specifies the size of the buffer. On output, receives the number of entries written.

</dd>
<dt><em>pointerCount</em> (Frame variants)</dt>
<dd>

A pointer to a value that specifies the number of pointers in the frame. On input, specifies the size of the buffer. On output, receives the number of pointers written.

</dd>
<dt><em>touchpadInfo</em></dt>
<dd>

A pointer to a [**POINTER_TOUCH_INFO**](/windows/win32/api/winuser/ns-winuser-pointer_touch_info) structure that receives the touchpad information. Can be **NULL** to query the required buffer sizes.

</dd>
</dl>

## Return value

If the function succeeds, the return value is nonzero.

If the function fails, the return value is zero. To get extended error information, call [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror).

## Remarks

Retrieves the requested touchpad pointer input associated with the specified pointer ID. The "frame" includes all currently-active contacts delivered to the same target as the input associated with the pointer ID. The "history" includes any input that was coalesced with the current input due to the target not dequeuing the earlier input promptly.

The pointer input is returned in a [**POINTER_TOUCH_INFO**](/windows/win32/api/winuser/ns-winuser-pointer_touch_info) structure, just like the touch equivalents of these APIs, due to the extended pointer fields being identical for touch and touchpad input.

These functions should only be called when processing **WM_POINTER** messages for touchpad input (after registering as touchpad-capable via [**RegisterTouchpadCapableWindow**](registertouchpadcapable.md) or [**RegisterTouchpadCapableThread**](registertouchpadcapable.md)).

Pointer input for touchpads has some functional differences when compared to other pointer device types:

- The **ptPixelLocation** and **ptPixelLocationRaw** fields are identical and contain the position of the mouse pointer at the time the gesture began and do not change over the duration of the gesture.
- The **ptHimetricLocation** and **ptHimetricLocationRaw** fields are identical and contain the position of the contact relative to the device.
- [**GetPointerDeviceRects**](/windows/win32/api/winuser/nf-winuser-getpointerdevicerects) returns the virtual desktop for the screen rect and the touchpad's dimensions for the device rect. While the above positions will be located within the bounds of these rects, there is no relationship between the two. For other pointer device types, the respective positions are at the same relative location within their corresponding rects, but that is not the case for touchpad input.
- When initially receiving an input stream, there may be a significant spatial and temporal gap for each contact between the first and second input frames. While the system is still performing disambiguation on the touchpad input, the input frames are discarded. If the system determines a gesture is occurring, it synthesizes an earlier frame for the contacts' **POINTER_FLAG_DOWN** input and delivers it first, so that the input target can use the information when determining if the input has met its gesture recognition thresholds. If the input is used for content manipulation, care should be taken to avoid the content "jumping" at the beginning, which could happen if the contacts' spatial motion is directly applied as content manipulation as the input arrives.
- If the pointer input is fed to the Interaction Context APIs for gesture recognition:
  - [**ProcessPointerFramesInteractionContext2**](processpointerframesinteractioncontext2.md) and [**BufferPointerPacketsInteractionContext2**](processpointerframesinteractioncontext2.md) must be used when feeding input to the interaction context.
  - Only manipulation gesture output can occur (taps and holds cannot be recognized, because the system will only generate touchpad **WM_POINTER** input once these gestures can no longer occur).
  - If the interaction context is configured to return its output in screen coordinates, then the output is scaled by the scale factor of the display containing the mouse pointer, so that the same gesture on the touchpad results in the same effective gesture output regardless of display scale.
  - If configured for himetric output, then the same gesture will produce the same results regardless of the mouse pointer's display. The output is scaled based on the velocity of the input so that faster finger motion results in larger output magnitudes for the same physical finger distance.
  - The output will avoid "jumping" as described above and can be directly applied to content for manipulation.

## Requirements

| Requirement | Value |
|-----|-----|
| Minimum supported client | Windows 11 \[desktop apps only\] |
| Minimum supported server | None supported |
| Header | Winuser.h (include Windows.h) |
| Library | User32.lib |
| DLL | User32.dll (ordinal 2691 for GetPointerTouchpadInfo, ordinal 2692 for GetPointerTouchpadInfoHistory, ordinal 2693 for GetPointerFrameTouchpadInfo, ordinal 2694 for GetPointerFrameTouchpadInfoHistory) |

## See also

- [**RegisterTouchpadCapableWindow**](registertouchpadcapable.md)
- [**GetPointerTouchInfo**](/windows/win32/api/winuser/nf-winuser-getpointertouchinfo)
- [Precision Touchpad Programming Guide](precision-touchpad-guide.md)
- [Precision Touchpad Reference](precision-touchpad-reference.md)
