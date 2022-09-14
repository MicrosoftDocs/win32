---
title: Server Stub Memory Management
description: Server Stub Memory Management
ms.assetid: 99e3ee56-5adb-4b25-bcf2-316d1bbdbdba
keywords:
- Server Stub Memory Management
ms.topic: article
ms.date: 05/31/2018
---

# Server Stub Memory Management

## An Introduction to Server-Stub Memory Management

MIDL-generated stubs act as the interface between a client process and a server process. A client stub marshals all data passed to parameters marked with the [**\[in\]**](../midl/in.md) attribute, and sends it to the server stub. The server stub, upon receiving this data, reconstructs the call stack, and then executes the corresponding user-implemented server function. The server stub also marshals the parameter data marked with the [**\[out\]**](../midl/out-idl.md) attribute and returns it to the client application.

The 32-bit marshaled data format used by MSRPC is a compliant version of the Network Data Representation (NDR) transfer syntax. For more information about this format, see [The Open Group website](https://www.opengroup.org/). For 64-bit platforms, a Microsoft 64-bit extension to NDR transfer syntax called NDR64 can be used for better performance.

## Unmarshaling Inbound Data

In MSRPC, the client stub marshals all of the parameter data tagged as [**\[in\]**](../midl/in.md) in one continuous buffer for transmission to the server stub. Likewise, the server stub marshals all data marked with the [**\[out\]**](../midl/out-idl.md) attribute in a continuous buffer for return to the client stub. While the network protocol layer beneath RPC can fragment and packetize the buffer for transmission, the fragmentation is transparent to the RPC stubs.

Memory allocation for creating the server call frame can be an expensive operation. The server stub will attempt to minimize unnecessary memory usage when possible, and it is assumed that the server routine will not free or reallocate data marked with the [**\[in\]**](../midl/in.md) or **\[in, out\]** attributes. The server stub attempts to reuse data in the buffer whenever possible to avoid unnecessary duplication. The general rule is that if the marshaled data format is the same as the memory format, RPC will use pointers to the marshalled data instead of allocating additional memory for identically formatted data.

For example, the following RPC call is defined with a structure whose marshaled format is identical to its in-memory format.

``` syntax
typedef struct RpcStructure
{
    long val;
    long val2;
}

void ProcessRpcStructure
(
    [in]  RpcStructure *plInStructure;
    [out] RpcStructure *plOutStructure;
);
```

In this case, RPC does not allocate additional memory for the data referenced by *plInStructure*; rather, it simply passes the pointer to the marshaled data to the server-side function implementation. The RPC server stub verifies the buffer during the unmarshaling process if the stub is compiled using the "-robust" flag (which is a default setting in the nmost recent version of the MIDL compiler). RPC guarantees that the data passed to the server-side function implementation is valid.

Be aware that memory is allocated for *plOutStructure*, since no data is passed to the server for it.

## Memory Allocation for Inbound Data

Cases can arise where the server stub allocates memory for parameter data marked with the [**\[in\]**](../midl/in.md) or **\[in, out\]** attributes. This occurs when the marshaled data format differs from the memory format, or when the structures that comprise the marshaled data are sufficient complex and must be read atomically by the RPC server stub. Listed below are several common cases when memory must be allocated for data received by the server stub.

-   The data is a varying array or a conformant varying array. These are arrays (or pointers to arrays) that have the [**\[length\_is()\]**](../midl/length-is.md) or [**\[first\_is()\]**](../midl/first-is.md) attribute set on them. In NDR, only the first element of these arrays are marshaled and transmitted. For example, in the code snippet below, the data passed in the parameter *pv* will have memory allocated for it.

    ``` syntax
    void RpcFunction
    (
        [in] long size,
        [in, out] long *pLength,
        [in, out, size_is(size), length_is(*pLength)] long *pv
    );
    ```

-   The data is a sized string or non-conformant string. These strings are usually pointers to character data tagged with the [**\[size\_is()\]**](../midl/size-is.md) attribute. In the example below, the string passed to the **SizedString** server-side function will have memory allocated, whereas the string passed to the **NormalString** function will be reused.

    ``` syntax
    void SizedString
    (
        [in] long size,
        [in, size_is(size), string] char *str
    );

    void NormalString
    (
        [in, string] char str
    );
    ```

-   The data is a simple type whose memory size differs from its marshaled size, such as **enum16** and **\_\_int3264**.
-   The data is defined by a structure whose memory alignment is smaller than the natural alignment, contains any of the above data types, or has trailing byte padding. For example, the following complex data structure has forced 2-byte alignment and has padding at the end.

    ``` syntax
#pragma pack(2)
    typedef struct ComplexPackedStructure
    {
        char c;  
        long l;   // alignment is forced at the second byte
        char c2;  // there will be a trailing one-byte pad to keep 2-byte alignment
    }
    ```

-   The data contains a structure that must be marshaled field by field. These fields include interface pointers defined in DCOM interfaces; ignored pointers; integer values set with the [**\[range\]**](../midl/range.md) attribute; elements of arrays defined with the [**\[wire\_marshal\]**](../midl/wire-marshal.md), [**\[user\_marshal\]**](../midl/user-marshal.md), [**\[transmit\_as\]**](../midl/transmit-as.md) and [**\[represent\_as\]**](../midl/represent-as.md) attributes; and embedded complex data structures.
-   The data contains a union, a structure containing a union, or an array of unions. Only the specific branch of the union is marshaled on the wire.
-   The data contains a structure with a multidimensional conformant array that has at least one non-fixed dimension.
-   The data contains an array of complex structures.
-   The data contains an array of simple data types such as **enum16** and **\_\_int3264**.
-   The data contains an array of ref and interface pointers.
-   The data has a [**\[force\_allocate\]**](../midl/force-allocate.md) attribute applied to a pointer.
-   The data has a [**\[allocate(all\_nodes)\]**](../midl/allocate.md) attribute applied to a pointer.
-   The data has a [**\[byte\_count\]**](../midl/byte-count.md) attribute applied to a pointer.

## 64-bit Data and NDR64 Transfer Syntax

As mentioned previously, 64-bit data is marshalled using a specific 64-bit transfer syntax called NDR64. This transfer syntax was developed to address the specific issue that arises when pointers are marshaled under 32-bit NDR and transmitted to a server-stub on a 64-bit platform. In this case, a marshaled 32-bit data pointer does not match a 64-bit one, and memory allocation will invariably occur. To create a more consistent behavior on 64-bit platforms, Microsoft developed a new transfer syntax called NDR64.

An example illustrating this problem is as follows:


```C++
typedef struct PtrStruct
{
  long l;
  long *pl;
}
```



This structure, when marshaled, will be reused by the server stub on a 32-bit system. However, if the server stub resides on a 64-bit system, the NDR-marshaled data is 4 bytes in length, but the required memory size will be 8. As a result, memory allocation is forced, and buffer reuse will rarely occur. NDR64 addresses this problem by making the marshaled size of a pointer 64-bit.

In contrast with 32-bit NDR, simple data tyes such as **enum16** and **\_\_int3264** do not make a structure or array complex under NDR64. Likewise, trailing pad values do not make a structure complex. Interface pointers are treated as unique pointers at the top level; as a result, structures and arrays containing interface pointers are not considered complex and will not require specific memory allocation for their use.

## Initializing Outbound Data

After all of the inbound data has been unmarshalled, the server stub needs to initialize the outbound-only pointers marked with the [**\[out\]**](../midl/out-idl.md) attribute.


```C++
typedef struct RpcStructure
{
    long val;
    long val2;
}

void ProcessRpcStructure
(
    [in]  RpcStructure *plInStructure;
    [out] RpcStructure *plOutStructure;
);
```



In the above call, the server stub must initialize *plOutStructure* because it was not present in the marshaled data, and it is an implied [**\[ref\]**](../midl/ref.md) pointer that must be made available to the server function implementation. The RPC server stub initializes and zeroes out any top-level reference-only pointers with the [**\[out\]**](../midl/out-idl.md) attribute. Any **\[out\]** reference pointers beneath it are recursively initialized as well. The recursion stops at any pointers with the [**\[unique\]**](../midl/unique.md) or [**\[ptr\]**](../midl/ptr.md) attributes set on them.

The server function implementation cannot directly alter top-level pointer values, and thus cannot reallocate them. For example, in the implementation of **ProcessRpcStructure** above, the following code is invalid:


```C++
void ProcessRpcStructure(RpcStructure *plInStructure, rpcStructure *plOutStructure)
{
    plOutStructure = MIDL_user_allocate(sizeof(RpcStructure));
    Process(plOutStructure);
}
```



*plOutStructure* is a stack value and its change is not propagated back to RPC. The server function implementation can attempt to avoid allocation by attempting to free *plOutStructure*, which may result in memory corruption. The server stub will then allocate space for the top-level pointer in memory (in the pointer-to-pointer case) and a top-level simple structure whose size on the stack is smaller than expected.

The client can, under certain circumstances, specify the memory allocation size of the server side. In the following example, the client specifies the size of the outbound data in the inbound *size* parameter.

``` syntax
void VariableSizeData
(
    [in] long size,
    [out, size_is(size)] char *pv
);
```

After unmarshalling the inbound data, including *size*, the server stub allocates a buffer for *pv* with a size of "sizeof(char)\*size". After the space has been allocated, the server stub zeroes out the buffer. Note that in this particular case, the stub allocates the memory with **MIDL\_user\_allocate()**, since the size of the buffer is determined at runtime.

Be aware that in the case of DCOM interfaces, MIDL-generated stubs may not be involved at all if the client and server share the same COM apartment, or if **ICallFrame** is implemented. In this case, the server cannot depend on the allocation behavior, and needs to independently verify client-sized memory.

## Server-side Function Implementations and Outbound Data Marshaling

Immediately subsequent to the unmarshalling on inbound data and the initialization of the memory allocated to contain outbound data, the RPC server stub executes the server-side implementation of the function called by the client. At this time, the server can modify the data specifically marked with the **\[in, out\]** attribute, and it can populate the memory allocated for outbound-only data (the data tagged with [**\[out\]**](../midl/out-idl.md)).

The general rules for the manipulation of marshalled parameter data are simple: the server can only allocate new memory or modify the memory specifically allocated by the server stub. Reallocating or releasing existing memory for data can have a negative impact on the results and performance of the function call, and can be very difficult to debug.

Logically, the RPC server lives in a different address space than the client, and it can generally be assumed that they do not share memory. As a result, it is safe for the server function implementation to use the data marked with the [**\[in\]**](../midl/in.md) attribute as "scratch" memory without affecting the client memory addresses. That said, the server should not attempt to reallocate or release **\[in\]** data, leaving the control of those spaces to the RPC server stub itself.

Generally, the server function implementation does not need to reallocate or release data marked with the **\[in, out\]** attribute. For fixed size data, the function implementation logic can directly modify the data. Likewise, for variable-sized data, the function implementation must not modify the field value supplied to the [**\[size\_is()\]**](../midl/size-is.md) attribute, either. Change the field value used to size the data results in a smaller or larger buffer returned to the client which may be ill-equipped to deal with the abnormal length.

If circumstances occur where the server routine has to reallocate the memory used by data marked with the **\[in, out\]** attribute, it is entirely possible that the server-side function implementation will not know if the pointer provided by the stub is to memory allocated with **MIDL\_user\_allocate()** or the marshaled wire buffer. To work around this problem, MS RPC can ensure that no memory leak or corruption occurs if the [**\[force\_allocate\]**](../midl/force-allocate.md) attribute is set on the data. When **\[force\_allocate\]** is set, the server stub will always allocate memory for the pointer, although the caveat is that performance will decrease for every use of it.

When the call returns from the server-side function implementation, the server stub marshals the data marked with the [**\[out\]**](../midl/out-idl.md) attribute and sends it to the client. Be aware that the stub does not marshal the data if the server-side function implementation throws an exception.

## Releasing Allocated Memory

The RPC server stub will release the stack memory after the call has returned from the server-side function, whether an exception occurs or not. The server stub frees all memory allocated by the stub as well as any memory allocated with **MIDL\_user\_allocate()**. The server-side function implementation must always give RPC a consistent state, either by throwing an exception or returning an error code. If the function fails during the population of complicated data structures, it must ensure that all pointers point to valid data or are set to **NULL**.

During this pass, the server stub frees all memory that is not part of the marshaled buffer containing the [**\[in\]**](../midl/in.md) data. One exception to this behavior is data with the [**\[allocate(dont\_free)\]**](../midl/allocate.md) attribute set on them - the server stub does not free any memory associated with these pointers.

After the server stub releases the memory allocated by the stub and the function implementation, the stub calls a specific notification function if the [**\[notify\_flag\]**](../midl/notify-flag.md) attribute is specified for particular data.

## Marshalling a Linked List over RPC -- An Example


```C++
typedef struct _LINKEDLIST
{
    long lSize;
    [size_is(lSize)] char *pData;
    struct _LINKEDLIST *pNext;
} LINKEDLIST, *PLINKEDLIST;

void Test
(
    [in] LINKEDLIST *pIn,
    [in, out] PLINKEDLIST *pInOut,
    [out] LINKEDLIST *pOut
);
```



In the above example, the memory format for **LINKEDLIST** will be identical to the marshaled wire format. As a result, the server stub does not allocate memory for the entire chain of data pointers under *pIn*. Rather, RPC reuses the wire buffer for the entire linked list. Similarly, the stub does not allocate memory for *pInOut*, but instead reuses the wire buffer marshaled by the client.

Because the function signature contains an outbound parameter, *pOut*, the server stub allocates memory to contain the returned data. The allocated memory is initially zeroes out, with **pNext** set to **NULL**. The application can allocate the memory for a new linked list and point *pOut*->**pNext** to it. *pIn* and the linked list it contains can be used as a scratch area, but the application should not change any of the pNext pointers.

The application can freely change the content of the linked list pointed to by *pInOut*, but it must not change any of the **pNext** pointers, let alone the top-level link itself. If the application decides to shorten the linked list, it cannot know if any given **pNext** pointer links tto an RPC internal buffer or a buffer specifically allocated with **MIDL\_user\_allocate()**. To work around this issue, you add a specific type declaration for linked list pointers that forces user allocation, as seen in the code below.

``` syntax
typedef [force_allocate] PLINKEDLIST;
```

This attribute forces the server stub to allocate each node of the linked list separately, and the application can free the shortened part of the linked list by calling **MIDL\_user\_free()**. The application can then safely set the **pNext** pointer at the end of the newly-shortened linked list to **NULL**.

 

 