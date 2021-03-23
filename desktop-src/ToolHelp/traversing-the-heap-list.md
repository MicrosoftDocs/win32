---
title: Traversing the Heap List
description: The following example obtains a list of heaps for the current process.
ms.assetid: cfa1d2a4-fec0-4089-9351-e0a26f9ecfe3
ms.topic: article
ms.date: 05/31/2018
---

# Traversing the Heap List

The following example obtains a list of heaps for the current process. It takes a snapshot of the heaps using the [**CreateToolhelp32Snapshot**](/windows/desktop/api/TlHelp32/nf-tlhelp32-createtoolhelp32snapshot) function, and then walks through the list using the [**Heap32ListFirst**](/windows/desktop/api/TlHelp32/nf-tlhelp32-heap32listfirst) and [**Heap32ListNext**](/windows/desktop/api/TlHelp32/nf-tlhelp32-heap32listnext) functions. For each heap, it uses the [**Heap32First**](/windows/desktop/api/TlHelp32/nf-tlhelp32-heap32first) and [**Heap32Next**](/windows/desktop/api/TlHelp32/nf-tlhelp32-heap32next) functions to walk the heap blocks.

Note that the
[**Heap32First**](/windows/desktop/api/TlHelp32/nf-tlhelp32-heap32first)
and
[**Heap32Next**](/windows/desktop/api/TlHelp32/nf-tlhelp32-heap32next)
functions
are inefficient, particularly for large heaps.
See the second example for an equivalent, much more efficient, alternative.

```C++
#include <windows.h>
#include <tlhelp32.h>
#include <stdio.h>

int main( void )
{
   HEAPLIST32 hl;
   
   HANDLE hHeapSnap = CreateToolhelp32Snapshot(TH32CS_SNAPHEAPLIST, GetCurrentProcessId());
   
   hl.dwSize = sizeof(HEAPLIST32);
   
   if ( hHeapSnap == INVALID_HANDLE_VALUE )
   {
      printf ("CreateToolhelp32Snapshot failed (%d)\n", GetLastError());
      return 1;
   }
   
   if( Heap32ListFirst( hHeapSnap, &hl ) )
   {
      do
      {
         HEAPENTRY32 he;
         ZeroMemory(&he, sizeof(HEAPENTRY32));
         he.dwSize = sizeof(HEAPENTRY32);

         if( Heap32First( &he, GetCurrentProcessId(), hl.th32HeapID ) )
         {
            printf( "\nHeap ID: %d\n", hl.th32HeapID );
            do
            {
               printf( "Block size: %d\n", he.dwBlockSize );
               
               he.dwSize = sizeof(HEAPENTRY32);
            } while( Heap32Next(&he) );
         }
         hl.dwSize = sizeof(HEAPLIST32);
      } while (Heap32ListNext( hHeapSnap, &hl ));
   }
   else printf ("Cannot list first heap (%d)\n", GetLastError());
   
   CloseHandle(hHeapSnap); 

   return 0;
}
```

The following program uses the
[**HeapWalk**](windows/desktop/api/heapapi/nf-heapapi-heapwalk)
function to walk the process heaps,
producing identical output to the previous program
but much more efficiently:

```C++
#include <windows.h>
#include <stdio.h>

int main( void )
{
    DWORD heapIndex;
    DWORD heapCount = 0;
    PHANDLE heaps = NULL;
    while (TRUE)
    {
        DWORD actualHeapCount = GetProcessHeaps(heapCount, heaps);
        if (actualHeapCount <= heapCount)
        {
            break;
        }
        heapCount = actualHeapCount;
        free(heaps);
        heaps = (HANDLE*)malloc(heapCount * sizeof(HANDLE));
        if (heaps == NULL)
        {
            printf("Unable to allocate memory for list of heaps\n");
            return 1;
        }
    }

    for (heapIndex = 0; heapIndex < heapCount; heapIndex++)
    {
        PROCESS_HEAP_ENTRY entry;

        printf("Heap ID: %d\n", (DWORD)(ULONG_PTR)heaps[heapIndex]);
        entry.lpData = NULL;
        while (HeapWalk(heaps[heapIndex], &entry))
        {
            // Heap32First and Heap32Next ignore entries
            // with the PROCESS_HEAP_REGION flag
            if (!(entry.wFlags & PROCESS_HEAP_REGION))
            {
                printf("Block size: %d\n", entry.cbData + entry.cbOverhead);
            }
        }
    }

    free(heaps);
    return 0;
}
```

Walking a heap with the
[**HeapWalk**](windows/desktop/api/heapapi/nf-heapapi-heapwalk)
function is roughly linear in the size of the heap,
whereas
walking a heap with the
[**Heap32Next**](/windows/desktop/api/TlHelp32/nf-tlhelp32-heap32next)
function is roughly quadratic in the size of the heap.
Even for a modest heap with 10,000 allocations,
[**HeapWalk**](windows/desktop/api/heapapi/nf-heapapi-heapwalk)
runs 10,000 times faster than
[**Heap32Next**](/windows/desktop/api/TlHelp32/nf-tlhelp32-heap32next)
while providing more detailed information.
The difference in performance becomes even more dramatic
as the heap size increases.

For a more detailed example of walking the heap with the
[**HeapWalk**](windows/desktop/api/heapapi/nf-heapapi-heapwalk)
function, see
[Enumerating a Heap](/windows/win32/memory/enumerating-a-heap).
