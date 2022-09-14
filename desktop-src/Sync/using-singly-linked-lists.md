---
description: The following example uses the InitializeSListHead function to initialize a singly linked list and the InterlockedPushEntrySList function to insert 10 items.
ms.assetid: 5608f84f-9211-4043-bb53-60339191ee29
title: Using Singly Linked Lists
ms.topic: article
ms.date: 05/31/2018
---

# Using Singly Linked Lists

The following example uses the [**InitializeSListHead**](/windows/win32/api/interlockedapi/nf-interlockedapi-initializeslisthead) function to initialize a [singly linked list](interlocked-singly-linked-lists.md) and the [**InterlockedPushEntrySList**](/windows/win32/api/interlockedapi/nf-interlockedapi-interlockedpushentryslist) function to insert 10 items. The example uses the [**InterlockedPopEntrySList**](/windows/win32/api/interlockedapi/nf-interlockedapi-interlockedpopentryslist) function to remove 10 items and the [**InterlockedFlushSList**](/windows/win32/api/interlockedapi/nf-interlockedapi-interlockedflushslist) function to verify that the list is empty.


```C++
#include <windows.h>
#include <malloc.h>
#include <stdio.h>

// Structure to be used for a list item; the first member is the 
// SLIST_ENTRY structure, and additional members are used for data.
// Here, the data is simply a signature for testing purposes. 


typedef struct _PROGRAM_ITEM {
    SLIST_ENTRY ItemEntry;
    ULONG Signature; 
} PROGRAM_ITEM, *PPROGRAM_ITEM;

int main( )
{
    ULONG Count;
    PSLIST_ENTRY pFirstEntry, pListEntry;
    PSLIST_HEADER pListHead;
    PPROGRAM_ITEM pProgramItem;

    // Initialize the list header to a MEMORY_ALLOCATION_ALIGNMENT boundary.
    pListHead = (PSLIST_HEADER)_aligned_malloc(sizeof(SLIST_HEADER),
       MEMORY_ALLOCATION_ALIGNMENT);
    if( NULL == pListHead )
    {
        printf("Memory allocation failed.\n");
        return -1;
    }
    InitializeSListHead(pListHead);

    // Insert 10 items into the list.
    for( Count = 1; Count <= 10; Count += 1 )
    {
        pProgramItem = (PPROGRAM_ITEM)_aligned_malloc(sizeof(PROGRAM_ITEM),
            MEMORY_ALLOCATION_ALIGNMENT);
        if( NULL == pProgramItem )
        {
            printf("Memory allocation failed.\n");
            return -1;
        }
        pProgramItem->Signature = Count;
        pFirstEntry = InterlockedPushEntrySList(pListHead, 
                       &(pProgramItem->ItemEntry)); 
    }

    // Remove 10 items from the list and display the signature.
    for( Count = 10; Count >= 1; Count -= 1 )
    {
        pListEntry = InterlockedPopEntrySList(pListHead);

        if( NULL == pListEntry )
        {
            printf("List is empty.\n");
            return -1;
        }
  
        pProgramItem = (PPROGRAM_ITEM)pListEntry;
        printf("Signature is %d\n", pProgramItem->Signature);

    // This example assumes that the SLIST_ENTRY structure is the 
    // first member of the structure. If your structure does not 
    // follow this convention, you must compute the starting address 
    // of the structure before calling the free function.

        _aligned_free(pListEntry);
    }

    // Flush the list and verify that the items are gone.
    pListEntry = InterlockedFlushSList(pListHead);
    pFirstEntry = InterlockedPopEntrySList(pListHead);
    if (pFirstEntry != NULL)
    {
        printf("Error: List is not empty.\n");
        return -1;
    }

    _aligned_free(pListHead);

    return 1;
}

```



 

 
