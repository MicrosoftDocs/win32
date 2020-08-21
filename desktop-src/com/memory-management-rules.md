---
title: Memory Management Rules
description: Memory Management Rules
ms.assetid: 769127a1-1a14-4ed4-9d38-7cf3e571b661
ms.topic: article
ms.date: 05/31/2018
---

# Memory Management Rules

The lifetime of pointers to interfaces is always managed through the [**AddRef**](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref) and [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) methods on every COM interface. For more information, see [Rules for Managing Reference Counts](rules-for-managing-reference-counts.md).

For all other parameters, it is important to adhere to certain rules for managing memory. The following rules apply to all parameters of interface methodsâ€”including the return valueâ€”that are not passed by value:

-   In-parameters must be allocated and freed by the caller.
-   Out-parameters must be allocated by the one called; they are freed by the caller using the standard COM task memory allocator. See [The OLE Memory Allocator](the-ole-memory-allocator.md) for more information.
-   In/out-parameters are initially allocated by the caller, and then freed and reallocated by the one called, if necessary. As is true for out parameters, the caller is responsible for freeing the final returned value. The standard COM memory allocator must be used.

In the latter two cases, where one piece of code allocates the memory and a different piece of code frees it, using the COM allocator ensures that the two pieces of code are using the same allocation methods.

Another area that needs special attention is the treatment of out and in-out parameters in failure conditions. If a function returns a failure code, the caller typically has no way to clean up the out or in-out parameters. This leads to the following additional rules:

-   In case of an error condition, parameters must always be reliably set to a value that will be cleaned up without any action by the caller.
-   All out pointer parameters must explicitly be set to **NULL**. These are usually passed in a pointer-to-pointer parameter but can also be passed as members of a structure that the caller allocates and the called code fills. The most straightforward way to ensure this is (in part) to set these values to **NULL** on function entry. This rule is important because it promotes more robust application interoperability.
-   Under error conditions, all in-out parameters must either be left alone by the code called (thus remaining at the value to which they were initialized by the caller) or be explicitly set, as in the out parameter error return case.

Remember that these memory management conventions for COM applications apply only across public interfaces and APIsâ€”there is no requirement at all that memory allocation strictly internal to a COM application need be done using these mechanisms.

COM internally uses Remote Procedure Calls (RPC) to communicate between clients and servers. For more information about managing memory in RPC server stubs, see the [Server-stub Memory Management](../rpc/server-stub-memory-management.md) topic.

## Related topics

<dl> <dt>

[Managing Memory Allocation](managing-memory-allocation.md)
</dt> </dl>

 

 