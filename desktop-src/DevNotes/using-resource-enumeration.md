---
description: The following example shows how to use the VerifierEnumerateResource function and related programming elements to abstract and categorize process-specific resource information.
ms.assetid: e0c2c795-2960-44f9-8b63-2329f5b42e15
title: Using Resource Enumeration
ms.topic: article
ms.date: 05/31/2018
---

# Using Resource Enumeration

The following example shows how to use the [**VerifierEnumerateResource**](/windows/desktop/api/Avrfsdk/nf-avrfsdk-verifierenumerateresource) function and related programming elements to abstract and categorize process-specific resource information.


```C++
#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <avrfsdk.h>
 
//
// helper class for local cleanup
//
template <typename T, typename FT, FT F> class OnDelete
{
private:
    T Val_;
public:
    OnDelete(T Val) :Val_(Val) {};
    ~OnDelete() { F(Val_); };
};
 
//
// prototype for the API
//
typedef ULONG (WINAPI * VerifierEnumResourceFn)(
    HANDLE Process,
    ULONG  Flags,
    ULONG  ResourceType,
    AVRF_RESOURCE_ENUMERATE_CALLBACK ResourceCallback,
    PVOID  EnumerationContext
    );
 
//
// enumeration context for heap allocations
//
typedef struct _HEAP_ENUM_CONTEXT 
{
    ULONG64 AddressToSearch;
} HEAP_ENUM_CONTEXT,*PHEAP_ENUM_CONTEXT;
 
ULONG WINAPI FindHeapAllocationCallback(
    PAVRF_HEAP_ALLOCATION HeapAllocation,
    PVOID EnumerationContext,
    PULONG EnumerationLevel
    )
/*++
 
Description:
 
    callback function for the handle trace enumeration function
 
--*/
{
    UNREFERENCED_PARAMETER(EnumerationLevel);
 
    PHEAP_ENUM_CONTEXT HeapEnumCtx = (PHEAP_ENUM_CONTEXT)EnumerationContext;
 
    //
    // shik the heap metadata allocations
    //
    if (HeapAllocation->HeapState & HeapMetadata) 
    {
        return 0;
    }
 
    if ((HeapEnumCtx->AddressToSearch >= HeapAllocation->UserAllocation &&
         HeapEnumCtx->AddressToSearch < (HeapAllocation->UserAllocation + 
                                         HeapAllocation->UserAllocationSize)) ||
        (HeapEnumCtx->AddressToSearch >= HeapAllocation->Allocation &&
         HeapEnumCtx->AddressToSearch < (HeapAllocation->Allocation + 
                                         HeapAllocation->AllocationSize)))
    {
 
        //
        // print the "boundaries" of the user allocation
        //
        printf("          %I64p - %I64p\n",
               HeapAllocation->UserAllocation,
               HeapAllocation->UserAllocationSize);
 
        //
        // print the stack trace information, if any
        //
        if (HeapAllocation->BackTraceInformation)
        {
        
            PAVRF_BACKTRACE_INFORMATION BackTrace = 
                HeapAllocation->BackTraceInformation;
            
            if (BackTrace->Depth) 
            {
 
                printf("--------- BackTrace %04x Depth %04x\n",
                       BackTrace->Index,
                       BackTrace->Depth);
                //
                // display the address from the stack trace
                //
                ULONG Iter;                
                for (Iter = 0;Iter < BackTrace->Depth ; Iter++)
                {
                    printf("          %I64p\n",
                    BackTrace->ReturnAddresses[Iter]);
                }
            } 
            else 
            {
                printf("--------- BackTrace with 0 Depth\n");
            }
        } 
        else 
        {
            printf("--------- NO BackTrace\n");
        }
         
    }
    
    return ERROR_SUCCESS;
}
 
//
// enumeration context for handle operations
//
typedef struct _HANDLE_ENUM_CONTEXT 
{
    ULONG64 HandleToSearch;
} HANDLE_ENUM_CONTEXT,*PHANDLE_ENUM_CONTEXT;
 
ULONG WINAPI FindHandleOperationCallback(
    PAVRF_HANDLE_OPERATION HandleOperation,
    PVOID EnumerationContext,
    PULONG EnumerationLevel
    )
/*++
 
Description:
 
    callback function for the handle trace enumeration function
 
--*/
{
    UNREFERENCED_PARAMETER(EnumerationLevel);
 
    PHANDLE_ENUM_CONTEXT HandleEnum = (PHANDLE_ENUM_CONTEXT)EnumerationContext;
 
    if (HandleOperation->Handle == HandleEnum->HandleToSearch)
    {
 
        printf("PID.TID %x.%x - operation %d on handle %I64x\n",
               HandleOperation->ProcessId,
               HandleOperation->ThreadId,
               HandleOperation->OperationType,
               HandleEnum->HandleToSearch);    
    }
 
    return ERROR_SUCCESS;
}        
 

int __cdecl wmain(
    /* __in */ int argc, 
    /* __in_ecount(argc) */ LPWSTR * argv
    )
/*++
 
Description:
 
    This function takes a process identifier, 
    the kind of resource to enumerate, and the address of 
    a resource. Resource here is the entity used by APIs instrumented
    by Verifier (handles and heap allocations for now) 
    and for which there is additional information
    useful to debug and diagnose an issue flagged by Verifier.
    This code sample uses the Enumeration API to find additional
    information about a given resource. The additional information
    is printed on the console.
 
--*/
{
 
    if (argc < 4)
    {
        printf("usage: verifenum PID ProcessId Handle|Heap Resource\n"
               "\n"
               "Sample:\n"
               "  verifenum.exe 1289 Handle 0x4\n"
               "  - finds all the operations for handle 4 in process 1289\n"
               "  verifenum.exe 1289 Heap 0x123456\n"
               "  - finds all the details of heap allocation at address\n"
               "    0x123456 in process 1289\n");
        return 1;
    }
 
    WCHAR * StringPid  = argv[1];
    WCHAR * StringType = argv[2];
    WCHAR * StringRes  = argv[3];
 
    //
    // convert the command line param to a Process Id
    //
    ULONG   Pid = wcstoul(StringPid,0,10);
    //
    // convert the command line param to a resource address
    //    
    ULONG64 Resource = _wcstoui64(StringRes,0,0x10);
 
    //
    // Load verifier.dll 
    //
    HMODULE hMod = LoadLibraryExW(L"verifier.dll",0,0);
    if (NULL == hMod)
    {
        return GetLastError();
    }
    OnDelete<HMODULE,BOOL(WINAPI *)(HMODULE),FreeLibrary> fm(hMod);
 
    //
    // discover the entry point VerifierEnumResource
    //
    VerifierEnumResourceFn VerifierEnumResource_;
    *(FARPROC *)&VerifierEnumResource_ = GetProcAddress(
                                             hMod,
                                             "VerifierEnumerateResource"
                                         );
    if (NULL == VerifierEnumResource_) 
    {
        printf("could not find entry point %s in verifier.dll\n",
               "VerifierEnumerateResource");
        return GetLastError();
    }
 
    //
    // open the process with the required access for the operation
    //
    HANDLE hProcess = OpenProcess(PROCESS_VM_READ|PROCESS_QUERY_INFORMATION,
                                  FALSE,
                                  Pid);
    if (NULL == hProcess) 
    {
        return GetLastError();
    }
    OnDelete<HANDLE,BOOL(WINAPI *)(HANDLE),CloseHandle> cm(hProcess);        
 
    //
    // dispatch the enumeration to the proper resource type
    //
    if (0 == _wcsicmp(StringType,L"Heap"))
    {
 
        HEAP_ENUM_CONTEXT HeapEnumCtx = { Resource };
 
        VerifierEnumResource_(
            hProcess,
            0,
            AvrfResourceHeapAllocation,
            (AVRF_RESOURCE_ENUMERATE_CALLBACK)FindHeapAllocationCallback,
            &HeapEnumCtx
        );
    
    } 
    else if (0 == _wcsicmp(StringType,L"Handle")) 
    {
 
        HANDLE_ENUM_CONTEXT HandleEnumCtx = { Resource };
 
        VerifierEnumResource_(
            hProcess,
            0,
            AvrfResourceHandleTrace,
            (AVRF_RESOURCE_ENUMERATE_CALLBACK)FindHandleOperationCallback,
            &HandleEnumCtx
        );
    
    } 
    else 
    {
        printf("Unrecognized resource type\n");
        return 1;
    }
 
    return 0;
}
```



 

 



