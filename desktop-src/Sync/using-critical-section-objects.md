---
description: The following example shows how a thread initializes, enters, and releases a critical section. It uses the InitializeCriticalSectionAndSpinCount, EnterCriticalSection, LeaveCriticalSection, and DeleteCriticalSection functions.
ms.assetid: 3c96414b-97e7-4ebb-a629-bfdb7a77c576
title: Using Critical Section Objects
ms.topic: concept-article
ms.date: 07/14/2025
---

# Using Critical Section Objects

The following example shows how a thread initializes, enters, and releases a [critical section](critical-section-objects.md). It uses the [**InitializeCriticalSectionAndSpinCount**](/windows/win32/api/synchapi/nf-synchapi-initializecriticalsectionandspincount), [**EnterCriticalSection**](/windows/win32/api/synchapi/nf-synchapi-entercriticalsection), [**LeaveCriticalSection**](/windows/win32/api/synchapi/nf-synchapi-leavecriticalsection), and [**DeleteCriticalSection**](/windows/win32/api/synchapi/nf-synchapi-deletecriticalsection) functions.

> [!WARNING]
> **Deadlock risk:** If a thread must acquire multiple critical sections, always acquire them in a consistent, documented order across all threads. Acquiring locks in different orders from different threads is the most common cause of deadlocks. Also note that **EnterCriticalSection** blocks indefinitely — use [**TryEnterCriticalSection**](/windows/win32/api/synchapi/nf-synchapi-tryentercriticalsection) for non-blocking acquisition attempts, and implement a bounded retry loop with a deadline if you need timed lock acquisition.

> [!NOTE]
> **Modern C++ alternative:** For new code, consider using `std::mutex` with `std::lock_guard` or `std::scoped_lock` (C++17), which provide RAII-based lock management that ensures release even when exceptions are thrown. For read-heavy workloads, consider [Slim Reader/Writer (SRW) Locks](slim-reader-writer--srw--locks.md) or `std::shared_mutex`.

``` syntax
// Global variable
CRITICAL_SECTION CriticalSection; 

int main( void )
{
    ...

    // Initialize the critical section one time only.
    if (!InitializeCriticalSectionAndSpinCount(&CriticalSection, 
        0x00000400) ) 
        return;
    ...

    // Release resources used by the critical section object.
    DeleteCriticalSection(&CriticalSection);
}

DWORD WINAPI ThreadProc( LPVOID lpParameter )
{
    ...

    // Request ownership of the critical section.
    EnterCriticalSection(&CriticalSection); 

    // Access the shared resource.

    // Release ownership of the critical section.
    LeaveCriticalSection(&CriticalSection);

    ...
return 1;
}
```

 

 
