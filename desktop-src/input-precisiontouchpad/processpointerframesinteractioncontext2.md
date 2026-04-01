---
title: ProcessPointerFramesInteractionContext2 and BufferPointerPacketsInteractionContext2 functions (InteractionContext.h)
description: Processes pointer frames or buffers pointer packets with extended pointer type information for an Interaction Context, enabling touchpad gesture recognition.
ms.topic: reference
ms.date: 03/28/2026
---

# ProcessPointerFramesInteractionContext2 and BufferPointerPacketsInteractionContext2 functions

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Processes pointer frames or buffers pointer packets with extended pointer type information for an Interaction Context.

## Syntax

```cpp
HRESULT
WINAPI
ProcessPointerFramesInteractionContext2(
    _In_ HINTERACTIONCONTEXT interactionContext,
    _In_ UINT32 entriesCount,
    _In_ UINT32 pointerCount,
    _In_reads_(entriesCount * pointerCount) const POINTER_TYPE_INFO *pointerInfo);

HRESULT
WINAPI
BufferPointerPacketsInteractionContext2(
    _In_ HINTERACTIONCONTEXT interactionContext,
    _In_ UINT32 entriesCount,
    _In_reads_(entriesCount) const POINTER_TYPE_INFO *pointerInfo);
```

## Parameters

<dl>
<dt><em>interactionContext</em></dt>
<dd>

A handle to the Interaction Context.

</dd>
<dt><em>entriesCount</em></dt>
<dd>

The number of entries (frames) in the *pointerInfo* array. For **ProcessPointerFramesInteractionContext2**, the total number of elements is *entriesCount* × *pointerCount*. For **BufferPointerPacketsInteractionContext2**, this is the total number of elements.

</dd>
<dt><em>pointerCount</em></dt>
<dd>

(**ProcessPointerFramesInteractionContext2** only.) The number of pointers per frame.

</dd>
<dt><em>pointerInfo</em></dt>
<dd>

A pointer to an array of [**POINTER_TYPE_INFO**](/windows/win32/api/winuser/ns-winuser-pointer_type_info) structures containing the pointer input data.

</dd>
</dl>

## Return value

If the function succeeds, it returns **S_OK**.

If the function fails, it returns an **HRESULT** error code.

## Remarks

These APIs function identically to their counterparts [**ProcessPointerFramesInteractionContext**](/windows/win32/api/interactioncontext/nf-interactioncontext-processpointerframesinteractioncontext) and [**BufferPointerPacketsInteractionContext**](/windows/win32/api/interactioncontext/nf-interactioncontext-bufferpointerpacketsinteractioncontext). Their only difference is in taking a **POINTER_TYPE_INFO** buffer instead of a **POINTER_INFO** buffer. These APIs enable the Interaction Context to use the extended pointer info payload when appropriate.

For touchpad input, these APIs must be used instead of their counterparts. The extended information in the **POINTER_TYPE_INFO** structure is required for proper touchpad gesture recognition.

## Requirements

| Requirement | Value |
|-----|-----|
| Minimum supported client | Windows 11 \[desktop apps only\] |
| Minimum supported server | None supported |
| Header | InteractionContext.h |
| Library | Ninput.lib |
| DLL | Ninput.dll (ordinal 2507 for ProcessPointerFramesInteractionContext2, ordinal 2508 for BufferPointerPacketsInteractionContext2) |

## See also

- [**RegisterTouchpadCapableWindow**](registertouchpadcapable.md)
- [**GetPointerTouchpadInfo**](getpointertouchpadinfo.md)
- [Precision Touchpad Programming Guide](precision-touchpad-guide.md)
- [Precision Touchpad Reference](precision-touchpad-reference.md)
