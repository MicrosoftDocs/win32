---
description: The following example illustrates the use of the HeapWalk function to enumerate a heap.
ms.assetid: ef37d644-473f-4e51-9785-5b44fe0dce42
title: Enumerating a Heap
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating a Heap

The following example illustrates the use of the [**HeapWalk**](/windows/desktop/api/HeapApi/nf-heapapi-heapwalk) function to enumerate a heap.

First, the example creates a private heap with the [**HeapCreate**](/windows/desktop/api/HeapApi/nf-heapapi-heapcreate) function. Then it uses [**HeapLock**](/windows/desktop/api/HeapApi/nf-heapapi-heaplock) to lock the heap so other threads cannot access the heap while it is being enumerated. The example then calls [**HeapWalk**](/windows/desktop/api/HeapApi/nf-heapapi-heapwalk) with a pointer to a [**PROCESS\_HEAP\_ENTRY**](/windows/win32/api/minwinbase/ns-minwinbase-process_heap_entry) structure and iterates through the heap, printing each entry to the console.

After enumeration is finished, the example uses [**HeapUnlock**](/windows/desktop/api/HeapApi/nf-heapapi-heapunlock) to unlock the heap so that other threads can access it. Finally, the example calls [**HeapDestroy**](/windows/desktop/api/HeapApi/nf-heapapi-heapdestroy) to destroy the private heap.


```C++
#include <windows.h>
#include <tchar.h>
#include <stdio.h>

int __cdecl _tmain()
{
    DWORD LastError;
    HANDLE hHeap;
    PROCESS_HEAP_ENTRY Entry;

    //
    // Create a new heap with default parameters.
    //
    hHeap = HeapCreate(0, 0, 0);
    if (hHeap == NULL) {
        _tprintf(TEXT("Failed to create a new heap with LastError %d.\n"),
                 GetLastError());
        return 1;
    }

    //
    // Lock the heap to prevent other threads from accessing the heap 
    // during enumeration.
    //
    if (HeapLock(hHeap) == FALSE) {
        _tprintf(TEXT("Failed to lock heap with LastError %d.\n"),
                 GetLastError());
        return 1;
    }

    _tprintf(TEXT("Walking heap %#p...\n\n"), hHeap);

    Entry.lpData = NULL;
    while (HeapWalk(hHeap, &Entry) != FALSE) {
        if ((Entry.wFlags & PROCESS_HEAP_ENTRY_BUSY) != 0) {
            _tprintf(TEXT("Allocated block"));

            if ((Entry.wFlags & PROCESS_HEAP_ENTRY_MOVEABLE) != 0) {
                _tprintf(TEXT(", movable with HANDLE %#p"), Entry.Block.hMem);
            }

            if ((Entry.wFlags & PROCESS_HEAP_ENTRY_DDESHARE) != 0) {
                _tprintf(TEXT(", DDESHARE"));
            }
        }
        else if ((Entry.wFlags & PROCESS_HEAP_REGION) != 0) {
            _tprintf(TEXT("Region\n  %d bytes committed\n") \
                     TEXT("  %d bytes uncommitted\n  First block address: %#p\n") \
                     TEXT("  Last block address: %#p\n"),
                     Entry.Region.dwCommittedSize,
                     Entry.Region.dwUnCommittedSize,
                     Entry.Region.lpFirstBlock,
                     Entry.Region.lpLastBlock);
        }
        else if ((Entry.wFlags & PROCESS_HEAP_UNCOMMITTED_RANGE) != 0) {
            _tprintf(TEXT("Uncommitted range\n"));
        }
        else {
            _tprintf(TEXT("Block\n"));
        }

        _tprintf(TEXT("  Data portion begins at: %#p\n  Size: %d bytes\n") \
                 TEXT("  Overhead: %d bytes\n  Region index: %d\n\n"),
                 Entry.lpData,
                 Entry.cbData,
                 Entry.cbOverhead,
                 Entry.iRegionIndex);
    }
    LastError = GetLastError();
    if (LastError != ERROR_NO_MORE_ITEMS) {
        _tprintf(TEXT("HeapWalk failed with LastError %d.\n"), LastError);
    }

    //
    // Unlock the heap to allow other threads to access the heap after 
    // enumeration has completed.
    //
    if (HeapUnlock(hHeap) == FALSE) {
        _tprintf(TEXT("Failed to unlock heap with LastError %d.\n"),
                 GetLastError());
    }

    //
    // When a process terminates, allocated memory is reclaimed by the operating
    // system so it is not really necessary to call HeapDestroy in this example.
    // However, it may be advisable to call HeapDestroy in a longer running
    // application.
    //
    if (HeapDestroy(hHeap) == FALSE) {
        _tprintf(TEXT("Failed to destroy heap with LastError %d.\n"),
                 GetLastError());
    }

    return 0;
}
```



The following output shows typical results for a newly created heap.

``` syntax
Walking heap 0X00530000...

Region
  4096 bytes committed
  258048 bytes uncommitted
  First block address: 0X00530598
  Last block address: 0X00570000
  Data portion begins at: 0X00530000
  Size: 1416 bytes
  Overhead: 0 bytes
  Region index: 0

Block
  Data portion begins at: 0X005307D8
  Size: 2056 bytes
  Overhead: 16 bytes
  Region index: 0

Uncommitted range
  Data portion begins at: 0X00531000
  Size: 258048 bytes
  Overhead: 0 bytes
  Region index: 0
```

 

 
