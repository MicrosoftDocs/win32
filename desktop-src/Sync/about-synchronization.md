---
description: To synchronize access to a resource, use one of the synchronization objects in one of the wait functions.
ms.assetid: 0930bf12-6d5f-4f2c-914d-53e6e862d3bd
title: About Synchronization
ms.topic: concept-article
ms.date: 07/18/2025
---

# About Synchronization

To synchronize access to a resource, use one of the [synchronization objects](synchronization-objects.md) in one of the [wait functions](wait-functions.md). The state of a synchronization object is either *signaled* or *nonsignaled*. The wait functions allow a thread to block its own execution until a specified nonsignaled object is set to the signaled state. For more information, see [Interprocess Synchronization](interprocess-synchronization.md).

## Choosing the right synchronization primitive

| Primitive | Scope | Performance | Reentrant | When to use |
|-----------|-------|-------------|-----------|-------------|
| [Slim Reader/Writer (SRW) Lock](slim-reader-writer--srw--locks.md) | Single process | Fast (typically user-mode; may enter kernel under contention) | No | Default choice for reader-heavy workloads in modern code. Smallest memory footprint (pointer-sized). |
| [Critical Section](critical-section-objects.md) | Single process | Fast (spins then kernel wait) | Yes | Use when you need reentrant/recursive locking within one process. Slightly larger than SRW. |
| [Mutex](mutex-objects.md) | Cross-process (named) | Slower (always kernel object) | Yes | Required for synchronization between processes via a named mutex. Also useful with `WaitForMultipleObjects`. |
| [Semaphore](semaphore-objects.md) | Cross-process (named) | Kernel object | N/A | Limits concurrent access to a resource pool (e.g., connection pool of N items). |
| [Event](event-objects.md) | Cross-process (named) | Kernel object | N/A | Signaling between threads/processes. Use for "something happened" notifications, not for protecting data. |
| C++ `std::mutex` / `std::shared_mutex` | Single process | Implementation-defined | No | Preferred for portable C++ code and RAII. Use when you don't need Win32 wait APIs or cross-process synchronization. |

> [!NOTE]
> **SRW locks vs Critical Sections**: For new code that doesn't require recursive locking, prefer SRW locks (`AcquireSRWLockExclusive`/`AcquireSRWLockShared`). They are smaller, faster, and support reader/writer semantics. Critical sections are still appropriate when you need reentrant (recursive) acquisition by the same thread.

> [!IMPORTANT]
> **Common mistake**: Using a Mutex for intra-process synchronization when a Critical Section or SRW lock would suffice. Mutexes always involve a kernel mode transition, making them significantly slower for high-frequency operations within a single process.

The following are other synchronization mechanisms:

-   [overlapped input and output](synchronization-and-overlapped-input-and-output.md)
-   [asynchronous procedure calls](asynchronous-procedure-calls.md)
-   [critical section objects](critical-section-objects.md)
-   [condition variables](condition-variables.md)
-   [slim reader/writer locks](slim-reader-writer--srw--locks.md)
-   [one-time initialization](one-time-initialization.md)
-   [interlocked variable access](interlocked-variable-access.md)
-   [interlocked singly linked lists](interlocked-singly-linked-lists.md)
-   [timer queues](timer-queues.md)
-   the [**MemoryBarrier**](/windows/win32/api/winnt/nf-winnt-memorybarrier) macro

For additional information on synchronization, see [Synchronization and Multiprocessor Issues](synchronization-and-multiprocessor-issues.md).

 

 
