---
description: The following example shows how a thread initializes, enters, and releases a critical section. It uses the InitializeCriticalSectionAndSpinCount, EnterCriticalSection, LeaveCriticalSection, and DeleteCriticalSection functions.
ms.assetid: 3c96414b-97e7-4ebb-a629-bfdb7a77c576
title: Using Critical Section Objects
ms.topic: article
ms.date: 05/31/2018
---

# Using Critical Section Objects

The following example shows how a thread initializes, enters, and releases a [critical section](critical-section-objects.md). It uses the [**InitializeCriticalSectionAndSpinCount**](/windows/win32/api/synchapi/nf-synchapi-initializecriticalsectionandspincount), [**EnterCriticalSection**](/windows/win32/api/synchapi/nf-synchapi-entercriticalsection), [**LeaveCriticalSection**](/windows/win32/api/synchapi/nf-synchapi-leavecriticalsection), and [**DeleteCriticalSection**](/windows/win32/api/synchapi/nf-synchapi-deletecriticalsection) functions.

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

 

 
