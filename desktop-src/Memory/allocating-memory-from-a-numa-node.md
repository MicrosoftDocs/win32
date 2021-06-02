---
description: The following sample code demonstrates the use of the NUMA functions GetNumaHighestNodeNumber, GetNumaProcessorNode, and VirtualAllocExNuma.
ms.assetid: df025b35-fb6b-4987-806e-9c76e6b130a1
title: Allocating Memory from a NUMA Node
ms.topic: article
ms.date: 05/31/2018
---

# Allocating Memory from a NUMA Node

The following sample code demonstrates the use of the NUMA functions [**GetNumaHighestNodeNumber**](/windows/win32/api/systemtopologyapi/nf-systemtopologyapi-getnumahighestnodenumber), [**GetNumaProcessorNode**](/windows/win32/api/winbase/nf-winbase-getnumaprocessornode), and [**VirtualAllocExNuma**](/windows/win32/api/memoryapi/nf-memoryapi-virtualallocexnuma). It also demonstrates the use of the [**QueryWorkingSetEx**](/windows/win32/api/psapi/nf-psapi-queryworkingsetex) function to retrieve the NUMA node on which pages are allocated.


```C++
#define _WIN32_WINNT 0x0600

#include <windows.h>
#include <stdlib.h>
#include <stdio.h>
#include <psapi.h>
#include <tchar.h>

SIZE_T AllocationSize;
DWORD  PageSize;

void DumpNumaNodeInfo (PVOID Buffer, SIZE_T Size);

void __cdecl wmain (int argc, const wchar_t* argv[])
{
    ULONG HighestNodeNumber;
    ULONG NumberOfProcessors;
    PVOID* Buffers = NULL;

    if (argc > 1)
    {
        (void)swscanf_s (argv[1], L"%Ix", &AllocationSize);
    }

    if (AllocationSize == 0)
    {
        AllocationSize = 16*1024*1024;
    }

    //
    // Get the number of processors and system page size.
    //

    SYSTEM_INFO SystemInfo;
    GetSystemInfo (&SystemInfo);
    NumberOfProcessors = SystemInfo.dwNumberOfProcessors;
    PageSize = SystemInfo.dwPageSize;

    //
    // Get the highest node number.
    //

    if (!GetNumaHighestNodeNumber (&HighestNodeNumber))
    {
        _tprintf (_T("GetNumaHighestNodeNumber failed: %d\n"), GetLastError());
        goto Exit;
    }

    if (HighestNodeNumber == 0)
    {
        _putts (_T("Not a NUMA system - exiting"));
        goto Exit;
    }

    //
    // Allocate array of pointers to memory blocks.
    //

    Buffers = (PVOID*) malloc (sizeof(PVOID)*NumberOfProcessors);

    if (Buffers == NULL)
    {
        _putts (_T("Allocating array of buffers failed"));
        goto Exit;
    }

    ZeroMemory (Buffers, sizeof(PVOID)*NumberOfProcessors);

    //
    // For each processor, get its associated NUMA node and allocate some memory from it.
    //

    for (UCHAR i = 0; i < NumberOfProcessors; i++)
    {
        UCHAR NodeNumber;

        if (!GetNumaProcessorNode (i, &NodeNumber))
        {
            _tprintf (_T("GetNumaProcessorNode failed: %d\n"), GetLastError());
            goto Exit;
        }

        _tprintf (_T("CPU %u: node %u\n"), (ULONG)i, NodeNumber);

        PCHAR Buffer = (PCHAR)VirtualAllocExNuma(
            GetCurrentProcess(),
            NULL,
            AllocationSize,
            MEM_RESERVE | MEM_COMMIT,
            PAGE_READWRITE,
            NodeNumber
        );

        if (Buffer == NULL)
        {
            _tprintf (_T("VirtualAllocExNuma failed: %d, node %u\n"), GetLastError(), NodeNumber);
            goto Exit;
        }

        PCHAR BufferEnd = Buffer + AllocationSize - 1;
        SIZE_T NumPages = ((SIZE_T)BufferEnd)/PageSize - ((SIZE_T)Buffer)/PageSize + 1;

        _putts (_T("Allocated virtual memory:"));
        _tprintf (_T("%p - %p (%6Iu pages), preferred node %u\n"), Buffer, BufferEnd, NumPages, NodeNumber);

        Buffers[i] = Buffer;

        //
        // At this point, virtual pages are allocated but no valid physical
        // pages are associated with them yet.
        //
        // The FillMemory call below will touch every page in the buffer, faulting
        // them into our working set. When this happens physical pages will be allocated
        // from the preferred node we specified in VirtualAllocExNuma, or any node
        // if the preferred one is out of pages.
        //

        FillMemory (Buffer, AllocationSize, 'x');

        //
        // Check the actual node number for the physical pages that are still valid
        // (if system is low on physical memory, some pages could have been trimmed already).
        //

        DumpNumaNodeInfo (Buffer, AllocationSize);

        _putts(_T(""));
    }

Exit:
    if (Buffers != NULL)
    {
        for (UINT i = 0; i < NumberOfProcessors; i++)
        {
            if (Buffers[i] != NULL)
            {
                VirtualFree (Buffers[i], 0, MEM_RELEASE);
            }
        }

        free (Buffers);
    }
}

void DumpRegion (PVOID StartPtr, PVOID EndPtr, BOOL Valid, DWORD Node)
{
    DWORD_PTR StartPage = ((DWORD_PTR)StartPtr)/PageSize;
    DWORD_PTR EndPage   = ((DWORD_PTR)EndPtr)/PageSize;
    DWORD_PTR NumPages  = (EndPage - StartPage) + 1;

    if (!Valid)
    {
        _tprintf (_T("%p - %p (%6Iu pages): no valid pages\n"), StartPtr, EndPtr, NumPages);
    }
    else
    {
        _tprintf (_T("%p - %p (%6Iu pages): node %u\n"), StartPtr, EndPtr, NumPages, Node);
    }
}

void DumpNumaNodeInfo (PVOID Buffer, SIZE_T Size)
{
    DWORD_PTR StartPage = ((DWORD_PTR)Buffer)/PageSize;
    DWORD_PTR EndPage   = ((DWORD_PTR)Buffer + Size - 1)/PageSize;
    DWORD_PTR NumPages  = (EndPage - StartPage) + 1;

    PCHAR StartPtr = (PCHAR)(PageSize*StartPage);

    _putts (_T("Checking NUMA node:"));

    PPSAPI_WORKING_SET_EX_INFORMATION WsInfo = (PPSAPI_WORKING_SET_EX_INFORMATION)
        malloc (NumPages*sizeof(PSAPI_WORKING_SET_EX_INFORMATION));

    if (WsInfo == NULL)
    {
        _putts (_T("Could not allocate array of PSAPI_WORKING_SET_EX_INFORMATION structures"));
        return;
    }

    for (DWORD_PTR i = 0; i < NumPages; i++)
    {
        WsInfo[i].VirtualAddress = StartPtr + i*PageSize;
    }

    BOOL bResult = QueryWorkingSetEx(
        GetCurrentProcess(),
        WsInfo,
        (DWORD)NumPages*sizeof(PSAPI_WORKING_SET_EX_INFORMATION)
    );

    if (!bResult)
    {
        _tprintf (_T("QueryWorkingSetEx failed: %d\n"), GetLastError());
        free (WsInfo);
        return;
    }

    PCHAR RegionStart   = NULL;
    BOOL  RegionIsValid = false;
    DWORD RegionNode    = 0;

    for (DWORD_PTR i = 0; i < NumPages; i++)
    {
        PCHAR Address = (PCHAR)WsInfo[i].VirtualAddress;
        BOOL  IsValid = WsInfo[i].VirtualAttributes.Valid;
        DWORD Node    = WsInfo[i].VirtualAttributes.Node;

        if (i == 0)
        {
            RegionStart   = Address;
            RegionIsValid = IsValid;
            RegionNode    = Node;
        }

        if (IsValid != RegionIsValid || Node != RegionNode)
        {
            DumpRegion (RegionStart, Address - 1, RegionIsValid, RegionNode);

            RegionStart   = Address;
            RegionIsValid = IsValid;
            RegionNode    = Node;
        }

        if (i == (NumPages - 1))
        {
            DumpRegion (RegionStart, Address + PageSize - 1, IsValid, Node);
        }
    }

    free (WsInfo);
}
```



## Related topics

<dl> <dt>

[NUMA Support](../procthread/numa-support.md)
</dt> </dl>

 

 
