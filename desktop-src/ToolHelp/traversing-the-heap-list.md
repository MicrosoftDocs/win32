---
title: Traversing the Heap List
description: The following example obtains a list of heaps for the current process.
ms.assetid: cfa1d2a4-fec0-4089-9351-e0a26f9ecfe3
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Traversing the Heap List

The following example obtains a list of heaps for the current process. It takes a snapshot of the heaps using the [**CreateToolhelp32Snapshot**](/windows/win32/TlHelp32/nf-tlhelp32-createtoolhelp32snapshot?branch=master) function, and then walks through the list using the [**Heap32ListFirst**](/windows/win32/TlHelp32/nf-tlhelp32-heap32listfirst?branch=master) and [**Heap32ListNext**](/windows/win32/TlHelp32/nf-tlhelp32-heap32listnext?branch=master) functions. For each heap, it uses the [**Heap32First**](/windows/win32/TlHelp32/nf-tlhelp32-heap32first?branch=master) and [**Heap32Next**](/windows/win32/TlHelp32/nf-tlhelp32-heap32next?branch=master) functions to walk the heap blocks.


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
   
   if( Heap32ListFirst( hHeapSnap, &amp;hl ) )
   {
      do
      {
         HEAPENTRY32 he;
         ZeroMemory(&amp;he, sizeof(HEAPENTRY32));
         he.dwSize = sizeof(HEAPENTRY32);

         if( Heap32First( &amp;he, GetCurrentProcessId(), hl.th32HeapID ) )
         {
            printf( "\nHeap ID: %d\n", hl.th32HeapID );
            do
            {
               printf( "Block size: %d\n", he.dwBlockSize );
               
               he.dwSize = sizeof(HEAPENTRY32);
            } while( Heap32Next(&amp;he) );
         }
         hl.dwSize = sizeof(HEAPLIST32);
      } while (Heap32ListNext( hHeapSnap, &amp;hl ));
   }
   else printf ("Cannot list first heap (%d)\n", GetLastError());
   
   CloseHandle(hHeapSnap); 

   return 0;
}
```



 

 




