---
description: Each new thread or fiber receives its own stack space consisting of both reserved and initially committed memory.
ms.assetid: abb2d5c1-040b-4c36-aae5-3517b6a8c540
title: Thread Stack Size
ms.topic: article
ms.date: 05/31/2018
---

# Thread Stack Size

Each new thread or fiber receives its own stack space consisting of both reserved and initially committed memory. The reserved memory size represents the total stack allocation in virtual memory. As such, the reserved size is limited to the virtual address range. The initially committed pages do not utilize physical memory until they are referenced; however, they do remove pages from the system total commit limit, which is the size of the page file plus the size of the physical memory. The system commits additional pages from the reserved stack memory as they are needed, until either the stack reaches the reserved size minus one page (which is used as a guard page to prevent stack overflow) or the system is so low on memory that the operation fails.

It is best to choose as small a stack size as possible and commit the stack that is needed for the thread or fiber to run reliably. Every page that is reserved for the stack cannot be used for any other purpose.

A stack is freed when its thread exits. It is not freed if the thread is terminated by another thread.

The default size for the reserved and initially committed stack memory is specified in the executable file header. Thread or fiber creation fails if there is not enough memory to reserve or commit the number of bytes requested. The default stack reservation size used by the linker is 1 MB. To specify a different default stack reservation size for all threads and fibers, use the STACKSIZE statement in the module definition (.def) file. The operating system rounds up the specified size to the nearest multiple of the system's allocation granularity (typically 64 KB). To retrieve the allocation granularity of the current system, use the [**GetSystemInfo**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsysteminfo) function.

To change the initially committed stack space, use the *dwStackSize* parameter of the [**CreateThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createthread), [**CreateRemoteThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createremotethread), or [**CreateFiber**](/windows/desktop/api/WinBase/nf-winbase-createfiber) function. This value is rounded up to the nearest page. Generally, the reserve size is the default reserve size specified in the executable header. However, if the initially committed size specified by *dwStackSize* is larger than or equal to the default reserve size, the reserve size is this new commit size rounded up to the nearest multiple of 1 MB.

To change the reserved stack size, set the *dwCreationFlags* parameter of [**CreateThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createthread) or [**CreateRemoteThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createremotethread) to STACK\_SIZE\_PARAM\_IS\_A\_RESERVATION and use the *dwStackSize* parameter. In this case, the initially committed size is the default size specified in the executable header. For fibers, use the *dwStackReserveSize* parameter of [**CreateFiberEx**](/windows/desktop/api/WinBase/nf-winbase-createfiberex). The committed size is specified in the *dwStackCommitSize* parameter.

The [**SetThreadStackGuarantee**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreadstackguarantee) function sets the minimum size of the stack associated with the calling thread or fiber that will be available during any stack overflow exceptions.

 

 
