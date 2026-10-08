---
title: Choosing the Threading Model
description: Choosing the Threading Model
ms.assetid: e8a0286d-1831-454f-8549-1957fd794809
ms.topic: concept-article
ms.date: 01/08/2025
---

# Choosing the Threading Model

Choosing the threading model for an object depends on the object's function. An object that does extensive I/O might support free-threading to provide maximum response to clients by allowing interface calls during I/O latency. On the other hand, an object that interacts with the user might support apartment threading to synchronize incoming COM calls with its window operations.

It is easier to support apartment threading in single-threaded apartments because COM provides synchronization on a per-call basis. Supporting free-threading is more difficult because the object must implement synchronization; however, response to clients may be better because synchronization can be implemented for smaller sections of code.

> [!TIP]
> **Quick decision guide for COM clients:**
>
> ```cpp
> // UI thread or main thread with a message loop → STA
> HRESULT hr = CoInitializeEx(nullptr, COINIT_APARTMENTTHREADED | COINIT_DISABLE_OLE1DDE);
>
> // Background/worker thread with no message loop → MTA
> HRESULT hr = CoInitializeEx(nullptr, COINIT_MULTITHREADED);
> ```
>
> **For COM servers (in-process DLLs)**, set the `ThreadingModel` registry value under the `InprocServer32` key:
> - `Apartment` — Object runs in caller's STA (most common for UI-related objects)
> - `Free` — Object runs in the MTA
> - `Both` — Object runs in the caller's apartment (best for general-purpose objects)
> - `Neutral` — Object runs in the Neutral Apartment (COM+ only)
>
> If unsure, start with `Both` and ensure your object is thread-safe. This reduces cross-apartment marshaling by letting COM create the object in the caller's apartment, though marshaling may still occur for cross-apartment callbacks or access from other apartments.

## Related topics

<dl> <dt>

[Accessing Interfaces Across Apartments](accessing-interfaces-across-apartments.md)
</dt> <dt>

[Multithreaded Apartments](multithreaded-apartments.md)
</dt> <dt>

[In-Process Server Threading Issues](in-process-server-threading-issues.md)
</dt> <dt>

[Processes, Threads, and Apartments](processes--threads--and-apartments.md)
</dt> <dt>

[Single-Threaded and Multithreaded Communication](single-threaded-and-multithreaded-communication.md)
</dt> <dt>

[Single-Threaded Apartments](single-threaded-apartments.md)
</dt> </dl>

 

 




