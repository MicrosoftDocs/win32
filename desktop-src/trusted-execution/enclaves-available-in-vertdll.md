---
description: Enclaves are used to create trusted execution environments. These Vertdll APIs are available to developers in VBS enclaves.
ms.assetid: 8e5588b6-0b1a-4ba6-9729-33f4e41e867c
title: Vertdll APIs available in VBS enclaves
titleSuffix: Secure Enclaves
ms.topic: reference
ms.date: 11/20/2024
---

# Vertdll APIs available in VBS enclaves

[!INCLUDE [enclaves-os-reqs.md](../includes/enclaves-os-reqs.md)]

Enclaves are used to create trusted execution environments. These Vertdll APIs are available to developers in VBS enclaves.

## Functions exported by Vertdll.dll

The following APIs exported by Vertdll.dll are available to be called in VBS enclaves.

| API | Header | Description |
|--------|--------|--------|
| [IsProcessorFeaturePresent](/windows/win32/api/processthreadsapi/nf-processthreadsapi-isprocessorfeaturepresent) | processthreadsapi.h | Determines whether the specified processor feature is supported by the current computer. |
| [LdrDisableThreadCalloutsForDll](../DevNotes/ldrdisablethreadcalloutsfordll.md) | - | Disables thread attach and detach callouts to a DLL. |
| **NtTerminateProcess**<br>See [TerminateProcess](/windows/win32/api/processthreadsapi/nf-processthreadsapi-terminateprocess) | processthreadsapi.h | Terminates the specified process and all of its threads. |
| [RtlCaptureContext](/windows/win32/api/winnt/nf-winnt-rtlcapturecontext) | winnt.h | Retrieves a context record in the context of the caller. |
| **RtlGetLastNtStatus**<br>See [GetLastError](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) | - | Gets the last NTSTATUS value. |
| [RtlLookupFunctionEntry](/windows/win32/api/winnt/nf-winnt-rtllookupfunctionentry) | winnt.h | Searches the active function tables for an entry that corresponds to the specified PC value. |
| [RtlPcToFileHeader](/windows/win32/api/winnt/nf-winnt-rtlpctofileheader) | winnt.h | Retrieves the base address of the image that contains the specified PC value. |
| **RtlRaiseStatus**<br>See [RaiseException](/windows/win32/api/errhandlingapi/nf-errhandlingapi-raiseexception) | - | Raises an exception, with only a *dwExceptionCode* parameter. **RtlRaiseStatus** invokes **RaiseException**, passing **EXCEPTION_NONCONTINUABLE** to indicate a noncontinuable exception has been encountered. |
| [RtlTimeFieldsToTime](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtltimefieldstotime) | wdm.h | Converts **TIME_FIELDS** information to a system time value. |
| **RtlUnhandledExceptionFilter**<br>See [UnhandledExceptionFilter](/windows/win32/api/errhandlingapi/nf-errhandlingapi-unhandledexceptionfilter) | - | An application-defined function that passes unhandled exceptions to the debugger, if the process is being debugged. |
| [RtlUnwind](/windows/win32/api/winnt/nf-winnt-rtlunwind) | winnt.h | Initiates an unwind of procedure call frames. |
| [RtlUnwindEx](/windows/win32/api/winnt/nf-winnt-rtlunwindex) | winnt.h | Initiates an unwind of procedure call frames. |
| [RtlVirtualUnwind](/windows/win32/api/winnt/nf-winnt-rtlvirtualunwind) | winnt.h | Retrieves the invocation context of the function that precedes the specified function context. |
| [RtlGetSystemGlobalData](../DevNotes/rtlgetsystemglobaldata.md) | - | Gets the address of the system global data area. |
| [memcmp](/cpp/c-runtime-library/reference/memcmp-wmemcmp) | memory.h *or*<br>string.h | Compares characters in two buffers. |
| [memcpy](/cpp/c-runtime-library/reference/memcpy-wmemcpy) | memory.h *or*<br>string.h | Copies bytes between buffers. |
| [memmove](/cpp/c-runtime-library/reference/memmove-wmemmove) | string.h | Moves one buffer to another. |
| [memset](/cpp/c-runtime-library/reference/memset-wmemset) | memory.h *or*<br>string.h | Sets a buffer to a specified character. |
| [OutputDebugStringW](/windows/win32/api/debugapi/nf-debugapi-outputdebugstringw) | debugapi.h | Sends a string to the debugger for display. |
| [CallEnclave](/windows/win32/api/enclaveapi/nf-enclaveapi-callenclave) | enclaveapi.h | Calls a function within an enclave. |
| [EnclaveGetEnclaveInformation](/windows/win32/api/winenclaveapi/nf-winenclaveapi-enclavegetenclaveinformation) | winenclaveapi.h | Gets information about the currently executing enclave. |
| [GetCurrentProcess](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentprocess) | processthreadsapi.h | Retrieves a pseudo handle for the current process. |
| [TerminateEnclave](/windows/win32/api/enclaveapi/nf-enclaveapi-terminateenclave) | enclaveapi.h | Ends the execution of the threads that are running within an enclave. |
| [TerminateProcess](/windows/win32/api/processthreadsapi/nf-processthreadsapi-terminateprocess) | processthreadsapi.h | Terminates the specified process and all of its threads. |
| [GetLastError](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) | errhandlingapi.h | Retrieves the calling thread's last-error code value. |
| [SetLastError](/windows/win32/api/errhandlingapi/nf-errhandlingapi-setlasterror) | errhandlingapi.h | Sets the last-error code for the calling thread. |
| [RaiseException](/windows/win32/api/errhandlingapi/nf-errhandlingapi-raiseexception) | errhandlingapi.h | Raises an exception in the calling thread. |
| [SetUnhandledExceptionFilter](/windows/win32/api/errhandlingapi/nf-errhandlingapi-setunhandledexceptionfilter) | errhandlingapi.h | Enables an application to supersede the top-level exception handler of each thread of a process. |
| [GetProcessHeap](/windows/win32/api/heapapi/nf-heapapi-getprocessheap) | heapapi.h | Retrieves a handle to the default heap of the calling process. |
| [GetProcessHeaps](/windows/win32/api/heapapi/nf-heapapi-getprocessheaps) | heapapi.h | Returns the number of active heaps and retrieves handles to all of the active heaps for the calling process. |
| [HeapAlloc](/windows/win32/api/heapapi/nf-heapapi-heapalloc) | heapapi.h | Allocates a block of memory from a heap. The allocated memory is not movable. |
| [HeapCompact](/windows/win32/api/heapapi/nf-heapapi-heapcompact) | heapapi.h | Returns the size of the largest committed free block in the specified heap. |
| [HeapCreate](/windows/win32/api/heapapi/nf-heapapi-heapcreate) | heapapi.h | Creates a private heap object that can be used by the calling process. |
| [HeapDestroy](/windows/win32/api/heapapi/nf-heapapi-heapdestroy) | heapapi.h | Destroys the specified heap object. It decommits and releases all the pages of a private heap object, and it invalidates the handle to the heap. |
| [HeapFree](/windows/win32/api/heapapi/nf-heapapi-heapfree) | heapapi.h | Frees a memory block allocated from a heap by the **HeapAlloc** or **HeapReAlloc** function. |
| [HeapLock](/windows/win32/api/heapapi/nf-heapapi-heaplock) | heapapi.h | Attempts to acquire the critical section object, or lock, that is associated with a specified heap. |
| [HeapReAlloc](/windows/win32/api/heapapi/nf-heapapi-heaprealloc) | heapapi.h | Reallocates a block of memory from a heap. This function enables you to resize a memory block and change other memory block properties. |
| [HeapSize](/windows/win32/api/heapapi/nf-heapapi-heapsize) | heapapi.h | Retrieves the size of a memory block allocated from a heap by the **HeapAlloc** or **HeapReAlloc** function. |
| [HeapUnlock](/windows/win32/api/heapapi/nf-heapapi-heapunlock) | heapapi.h | Releases ownership of the critical section object, or lock, that is associated with a specified heap. It reverses the action of the **HeapLock** function. |
| [InitializeSListHead](/windows/win32/api/interlockedapi/nf-interlockedapi-initializeslisthead) | interlockedapi.h | Initializes the head of a singly linked list. |
| [InterlockedFlushSList](/windows/win32/api/interlockedapi/nf-interlockedapi-interlockedflushslist) | interlockedapi.h | Removes all items from a singly linked list. |
| [InterlockedPopEntrySList](/windows/win32/api/interlockedapi/nf-interlockedapi-interlockedpopentryslist) | interlockedapi.h | Removes an item from the front of a singly linked list. |
| [InterlockedPushEntrySList](/windows/win32/api/interlockedapi/nf-interlockedapi-interlockedpushentryslist) | interlockedapi.h | Inserts an item at the front of a singly linked list. |
| [InterlockedPushListSList](/windows/win32/sync/interlockedpushlistslist) | interlockedapi.h | Inserts a singly-linked list at the front of another singly linked list. |
| [InterlockedPushListSListEx](/windows/win32/api/interlockedapi/nf-interlockedapi-interlockedpushlistslistex)  | interlockedapi.h | Inserts a singly-linked list at the front of another singly linked list. |
| [QueryDepthSList](/windows/win32/api/interlockedapi/nf-interlockedapi-querydepthslist) | interlockedapi.h | Retrieves the number of entries in the specified singly linked list. |
| [DisableThreadLibraryCalls](/windows/win32/api/libloaderapi/nf-libloaderapi-disablethreadlibrarycalls) | libloaderapi.h | Disables the **DLL_THREAD_ATTACH** and **DLL_THREAD_DETACH** notifications for the specified DLL. |
| [GetModuleHandleExW](/windows/win32/api/libloaderapi/nf-libloaderapi-getmodulehandleexw) | libloaderapi.h | Retrieves a module handle for the specified module and increments the module's reference count unless **GET_MODULE_HANDLE_EX_FLAG_UNCHANGED_REFCOUNT** is specified. |
| [GetProcAddress](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) | libloaderapi.h | Retrieves the address of an exported function or variable from the specified DLL. |
| [SetThreadStackGuarantee](/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreadstackguarantee) | processthreadsapi.h | Sets the minimum size of the stack associated with the calling thread or fiber that will be available during any stack overflow exceptions. |
| [VirtualAlloc](/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc) | memoryapi.h | Reserves, commits, or changes the state of a region of pages in the virtual address space of the calling process. |
| [VirtualFree](/windows/win32/api/memoryapi/nf-memoryapi-virtualfree) | memoryapi.h | Releases, decommits, or releases and decommits a region of pages within the virtual address space of the calling process. |
| [VirtualProtect](/windows/win32/api/memoryapi/nf-memoryapi-virtualprotect) | memoryapi.h | Changes the protection on a region of committed pages in the virtual address space of the calling process. |
| [VirtualQuery](/windows/win32/api/memoryapi/nf-memoryapi-virtualquery) | memoryapi.h | Retrieves information about a range of pages in the virtual address space of the calling process. |
| [AcquireSRWLockExclusive](/windows/win32/api/synchapi/nf-synchapi-acquiresrwlockexclusive) | synchapi.h | Acquires a slim reader/writer (SRW) lock in exclusive mode. |
| [AcquireSRWLockShared](/windows/win32/api/synchapi/nf-synchapi-acquiresrwlockshared) | synchapi.h | Acquires a slim reader/writer (SRW) lock in shared mode. |
| [DeleteCriticalSection](/windows/win32/api/synchapi/nf-synchapi-deletecriticalsection) | synchapi.h | Releases all resources used by an unowned critical section object. |
| [DeleteSynchronizationBarrier](/windows/win32/api/synchapi/nf-synchapi-deletesynchronizationbarrier) | synchapi.h | Deletes a synchronization barrier. |
| [EnterCriticalSection](/windows/win32/api/synchapi/nf-synchapi-entercriticalsection) | synchapi.h | Waits for ownership of the specified critical section object. The function returns when the calling thread is granted ownership. |
| [EnterSynchronizationBarrier](/windows/win32/api/synchapi/nf-synchapi-entersynchronizationbarrier) | synchapi.h | Causes the calling thread to wait at a synchronization barrier until the maximum number of threads have entered the barrier. |
| [InitializeConditionVariable](/windows/win32/api/synchapi/nf-synchapi-initializeconditionvariable) | synchapi.h | Initializes a condition variable. |
| [InitializeCriticalSection](/windows/win32/api/synchapi/nf-synchapi-initializecriticalsection) | synchapi.h | Initializes a critical section object. |
| [InitializeCriticalSectionAndSpinCount](/windows/win32/api/synchapi/nf-synchapi-initializecriticalsectionandspincount) | synchapi.h | Initializes a critical section object and sets the spin count for the critical section. |
| [InitializeCriticalSectionEx](/windows/win32/api/synchapi/nf-synchapi-initializecriticalsectionex) | synchapi.h | Initializes a critical section object with a spin count and optional flags. |
| [InitializeSRWLock](/windows/win32/api/synchapi/nf-synchapi-initializesrwlock) | synchapi.h | Initialize a slim reader/writer (SRW) lock. |
| [InitializeSynchronizationBarrier](/windows/win32/api/synchapi/nf-synchapi-initializesynchronizationbarrier) | synchapi.h | Initializes a new synchronization barrier. |
| [LeaveCriticalSection](/windows/win32/api/synchapi/nf-synchapi-leavecriticalsection) | synchapi.h | Releases ownership of the specified critical section object. |
| [ReleaseSRWLockExclusive](/windows/win32/api/synchapi/nf-synchapi-releasesrwlockexclusive) | synchapi.h | Releases a slim reader/writer (SRW) lock that was acquired in exclusive mode. |
| [ReleaseSRWLockShared](/windows/win32/api/synchapi/nf-synchapi-releasesrwlockshared) | synchapi.h | Releases a slim reader/writer (SRW) lock that was acquired in shared mode. |
| [SetCriticalSectionSpinCount](/windows/win32/api/synchapi/nf-synchapi-setcriticalsectionspincount) | synchapi.h | Sets the spin count for the specified critical section. |
| [SleepConditionVariableCS](/windows/win32/api/synchapi/nf-synchapi-sleepconditionvariablecs) | synchapi.h | Sleeps on the specified condition variable and releases the specified critical section as an atomic operation. |
| [SleepConditionVariableSRW](/windows/win32/api/synchapi/nf-synchapi-sleepconditionvariablesrw) | synchapi.h | Sleeps on the specified condition variable and releases the specified lock as an atomic operation. |
| [TryAcquireSRWLockExclusive](/windows/win32/api/synchapi/nf-synchapi-tryacquiresrwlockexclusive) | synchapi.h | Attempts to acquire a slim reader/writer (SRW) lock in exclusive mode. If the call is successful, the calling thread takes ownership of the lock. |
| [TryAcquireSRWLockShared](/windows/win32/api/synchapi/nf-synchapi-tryacquiresrwlockshared) | synchapi.h | Attempts to acquire a slim reader/writer (SRW) lock in shared mode. If the call is successful, the calling thread takes ownership of the lock. |
| [TryEnterCriticalSection](/windows/win32/api/synchapi/nf-synchapi-tryentercriticalsection) | synchapi.h | Attempts to enter a critical section without blocking. If the call is successful, the calling thread takes ownership of the critical section. |
| [WaitOnAddress](/windows/win32/api/synchapi/nf-synchapi-waitonaddress) | synchapi.h | Waits for the value at the specified address to change. |
| [WakeAllConditionVariable](/windows/win32/api/synchapi/nf-synchapi-wakeallconditionvariable) | synchapi.h | Wake all threads waiting on the specified condition variable. |
| [WakeByAddressAll](/windows/win32/api/synchapi/nf-synchapi-wakebyaddressall) | synchapi.h | Wakes all threads that are waiting for the value of an address to change. |
| [WakeByAddressSingle](/windows/win32/api/synchapi/nf-synchapi-wakebyaddresssingle) | synchapi.h | Wakes one thread that is waiting for the value of an address to change. |
| [WakeConditionVariable](/windows/win32/api/synchapi/nf-synchapi-wakeconditionvariable) | synchapi.h | Wake a single thread waiting on the specified condition variable. |
| [GetCurrentThread](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentthread) | processthreadsapi.h | Retrieves a pseudo handle for the calling thread. |
| [GetCurrentThreadId](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentthreadid) | processthreadsapi.h | Retrieves the thread identifier of the calling thread. |
| [TlsAlloc](/windows/win32/api/processthreadsapi/nf-processthreadsapi-tlsalloc) | processthreadsapi.h | Allocates a thread local storage (TLS) index. |
| [TlsFree](/windows/win32/api/processthreadsapi/nf-processthreadsapi-tlsfree) | processthreadsapi.h | Releases a TLS index, making it available for reuse. |
| [TlsGetValue](/windows/win32/api/processthreadsapi/nf-processthreadsapi-tlsgetvalue) | processthreadsapi.h | Retrieves the value in the calling thread's TLS slot for the specified TLS index. |
| [TlsSetValue](/windows/win32/api/processthreadsapi/nf-processthreadsapi-tlssetvalue) | processthreadsapi.h | Stores a value in the calling thread's TLS slot for the specified TLS index. |
| [EnclaveCopyIntoEnclave](/windows/win32/api/winenclaveapi/nf-winenclaveapi-enclavecopyintoenclave) | winenclaveapi.h | Copies data from an untrusted address (outside of the enclave) into the enclave. |
| [EnclaveCopyOutOfEnclave](/windows/win32/api/winenclaveapi/nf-winenclaveapi-enclavecopyoutofenclave) | winenclaveapi.h | Copies data from the enclave to an untrusted address (outside of the enclave). |
| [EnclaveGetAttestationReport](/windows/win32/api/winenclaveapi/nf-winenclaveapi-enclavegetattestationreport) | winenclaveapi.h | Gets an enclave attestation report that describes the current enclave and is signed by the authority that is responsible for the type of the enclave. |
| [EnclaveRestrictContainingProcessAccess](/windows/win32/api/winenclaveapi/nf-winenclaveapi-enclaverestrictcontainingprocessaccess) | winenclaveapi.h | Restricts (or restores) access by an enclave to the address space of its containing process. |
| [EnclaveSealData](/windows/win32/api/winenclaveapi/nf-winenclaveapi-enclavesealdata) | winenclaveapi.h | Generates an encrypted binary large object (blob) from unencypted data. |
| [EnclaveUnsealData](/windows/win32/api/winenclaveapi/nf-winenclaveapi-enclaveunsealdata) | winenclaveapi.h | Decrypts an encrypted binary large object (blob). |
| [EnclaveVerifyAttestationReport](/windows/win32/api/winenclaveapi/nf-winenclaveapi-enclaveverifyattestationreport) | winenclaveapi.h | Verifies an attestation report that was generated on the current system. |
| [WideCharToMultiByte](/windows/win32/api/stringapiset/nf-stringapiset-widechartomultibyte) | stringapiset.h | Maps a UTF-16 (wide character) string to a new character string.<br><br>**Note:** The only code page available to VBS Enclaves is **CP_UTF8**. |
| [MultiByteToWideChar](/windows/win32/api/stringapiset/nf-stringapiset-multibytetowidechar) | stringapiset.h | Maps a character string to a UTF-16 (wide character) string.<br><br>**Note:** The only code page available to VBS Enclaves is **CP_UTF8**. |
| LdrResolveDelayLoadedAPI<br>See [ResolveDelayLoadedAPI](/windows/win32/devnotes/resolvedelayloadedapi) | - | Locates the target function of the specified import and replaces the function pointer in the import thunk with the target of the function implementation. |

## See also

- [Secure Enclaves (Trusted Execution)](enclaves.md)
- [UCRT APIs Available in VBS Enclaves](enclaves-available-in-ucrt.md)
- [Bcrypt APIs Available in VBS Enclaves](enclaves-available-in-bcrypt.md)
- [libvcruntime APIs Available in VBS Enclaves](enclaves-available-in-libvcruntime.md)
