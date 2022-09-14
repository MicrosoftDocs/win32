---
title: IDL Techniques for Better Interface and Method Design
description: Consider using the following IDL-specific techniques to improve security and performance when you are developing RPC interfaces and methods that handle both conformant and variant data.
ms.assetid: 651bdb5c-ad56-4526-9b7d-7165141e7ceb
ms.topic: article
ms.date: 05/31/2018
---

# IDL Techniques for Better Interface and Method Design

Consider using the following IDL-specific techniques to improve security and performance when you are developing RPC interfaces and methods that handle both conformant and variant data. The attributes referred to in this topic are the IDL attributes set on method parameters that handle either conformant data (for example, the \[**size\_is**\] and \[**max\_is**\] attributes) or variant data (for example, the \[**length\_is**\] and \[**string**\] attributes).

## Using the \[range\] Attribute with Conformant Data Parameters

The \[**range**\] attribute instructs the RPC run-time to perform additional size validation during the data unmarshaling process. Specifically, it verifies that the supplied size of the data passed as the associated parameter is within the specified range.

The \[**range**\] attribute does not affect wire format.

If the value on wire is outside of the allowed range, RPC will throw an RPC\_X\_INVALID\_BOUND or RPC\_X\_BAD\_STUB\_DATA exception. This provides an additional level of data validation, and can help prevent common security errors like buffer overruns. Likewise, using \[**range**\] can improve application performance, since conformant data marked with it has clearly-defined constraints available for consideration by the RPC service.

## RPC Server Stub Memory Management Rules

It is important to understand RPC server stub memory management rules when creating the IDL files for an RPC-enabled application. Applications can improve server resource utilization by using \[**range**\] in conjunction with conformant data as indicated above, as well as deliberately avoiding the application of variable-length data IDL attributes like like \[**length\_is**\] to conformant data.

The application of \[**length\_is**\] to data structure fields defined in an IDL file is not recommended.

## Best Practices for Variable-length Data Parameters

The following are several best practices to consider when defining the IDL attributes for variable-sized data structures, method parameters and fields.

-   Use early correlation. It is generally better to define the variable size parameter or field such that it occurs immediately after the controlling integral type.

    For example,

    ``` syntax
    earlyCorr
    (
    [in, range(MIN_COUNT, MAX_COUNT)] long size, 
    [in,size_is(size)] char *pv
    );
    ```

    is better than

    ``` syntax
    lateCorr
    (
    [in,size_is(size)] char *pv, 
    [in, range(MIN_COUNT, MAX_COUNT)] long size)
    );
    ```

    wherein **earlyCorr** declares the size parameter immediately before the variable-length data parameter, and **lateCorr** declares the size parameter after it. Using early correspondence improves performance overall, especially in cases where the method is called frequently.

-   For parameters marked with the \[**out, size\_is**\] attribute tuple, and where the data length is known on the client side or where the client has a reasonable upper bound, the method definition should be similar to the following in terms of parameter attribution and sequence:

    ``` syntax
    outKnownSize
    (
    [in,range(MIN_COUNT, MAX_COUNT)] long lSize,
    [out,size_is(lSize)] UserDataType * pArr
    );
    ```

    In this case, the client provides a fixed size buffer for *pArr*, allowing the server-side RPC service to allocate a reasonably-sized buffer with a good degree of assurance. Note that in the example the data is received from the server (\[**out**\]). The definition is similar for data passed to the server (\[**in**\]).

-   For situations where the server-side component of an RPC application decides the data length, the method definition should be similar to the following:

    ``` syntax
    typedef [range(MIN_COUNT,MAX_COUNT)] long RANGED_LONG;

    outUnknownSize
    (
    [out] RANGED_LONG *pSize,
    [out,size_is(,*pSize)] UserDataType **ppArr
    );
    ```

    **RANGED\_LONG** is a type defined for both the client and server stubs, and of a specified size the client can correctly anticipate. In the example, the client passes *ppArr* as **NULL**, and the RPC server application component allocates the correct amount of memory. Upon return, the RPC service on the client side allocates the memory for the returned data.

-   If the client wants to send a subset of a large conformant array to the server, the application can specify the size of the subset as demonstrated in the following example:

    ``` syntax
    inConformantVaryingArray
    (
    [in,range(MIN_COUNT,MAX_COUNT)] long lSize,
    [in] long lLength, 
    [in,size_is(lSize), length_is(lLength)] UserDataType *pArr
    );
    ```

    This way RPC will only transmit *lLength* elements of the array across the wire. However, this definition forces the RPC service to allocate memory of size *lSize* on the server side.

-   If the client application component determines the maximum size of an array the server can return, but allows the server to transmit a subset of that array, the application can specify such a behavior by defining the IDL similar to the following example:

    ``` syntax
    inMaxSizeOutLength
    (
    [in, range(MIN_COUNT, MAX_COUNT)] long lSize,
    [out] long *pLength,
    [out,size_is(lSize), length_is(*pLength)] UserDataType *pArr
    );
    ```

    The client application component specifies the maximum size of the array, and the server specifies how many elements it transmits back to the client.

-   If the server application component needs to return a string to the client application component, and if the client knows the maximum size to be returned from the server, the application can use a conformant string type as demonstrated in the following example:

    ``` syntax
    outStringKnownSize
    (
    [in,range(MIN_COUNT, MAX_STRING)] long lSize,
    [out,size_is(lSize),string] wchar_t *pString
    );
    ```

-   If the client application component should not control the size of the string, the RPC service can specifically allocate the memory as demonstrated in the following example:

    ``` syntax
    outStringUnknownSize
    (
    [out] LPWSTR *ppStr
    );
    ```

    The client application component must set *ppStr* to **NULL** on when calling the RPC method.

 

 




