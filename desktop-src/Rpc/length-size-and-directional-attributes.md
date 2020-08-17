---
title: Length, Size, and Directional Attributes
description: In passing arrays between the client and the server, the size-related attributes \ max\_is\ and \ size\_is\ determine how many array elements the server stub allocates.
ms.assetid: 2c95cf47-6fc0-4ccd-bb4f-acf356596e56
ms.topic: article
ms.date: 05/31/2018
---

# Length, Size, and Directional Attributes

In passing arrays between the client and the server, the size-related attributes \[[**max\_is**](/windows/desktop/Midl/max-is)\] and \[[**size\_is**](/windows/desktop/Midl/size-is)\] determine how many array elements the server stub allocates. The length-related attributes \[[**length\_is**](/windows/desktop/Midl/length-is)\], \[[**first\_is**](/windows/desktop/Midl/first-is)\], and \[[**last\_is**](/windows/desktop/Midl/last-is)\] determine how many elements are transmitted to both the server and the client.

Different directional attributes can be applied to parameters. However, some combinations of directional attributes can cause errors. As an example, suppose you are writing an interface that specifies a procedure with two parameters, an array, and the transmitted length of the array. The term *dir\_attr* refers to the directional attribute applied to the parameter as:

``` syntax
Proc1(
    [dir_attr] short *plength;
    [dir_attr, length_is(pLength)] short array[MAX_SIZE]);
```

The MIDL compiler behavior for each combination of directional attributes is described in the following table.



| Array                                          | Length parameter                               | Stub actions during call from client to server                                                                                                                                                                                                                          | Stub actions on return from server to client                                                                                                                                                                         |
|------------------------------------------------|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \[[**in**](/windows/desktop/Midl/in)\]                          | \[[**in**](/windows/desktop/Midl/in)\]                          | Transmit the length and the number of elements indicated by the parameter.                                                                                                                                                                                              | No data transmitted.                                                                                                                                                                                                 |
| \[[**in**](/windows/desktop/Midl/in)\]                          | \[[**out**](/windows/desktop/Midl/out-idl)\]                    | Not legal; MIDL compiler error.                                                                                                                                                                                                                                         | Not legal; MIDL compiler error.                                                                                                                                                                                      |
| \[[**in**](/windows/desktop/Midl/in)\]                          | \[[**in**](/windows/desktop/Midl/in), [**out**](/windows/desktop/Midl/out-idl)\] | Transmit the length and the number of elements indicated by the length parameter.                                                                                                                                                                                       | Transmit the length only.                                                                                                                                                                                            |
| \[[**out**](/windows/desktop/Midl/out-idl)\]                    | \[[**in**](/windows/desktop/Midl/in)\]                          | Transmit the length.<br/> If array size is fixed, allocate the array size on the server, but transmit no elements.<br/> If array size is not bound, not legal: MIDL compiler error.<br/>                                                              | Transmit the number of elements indicated by the length.<br/> Note that the length can be changed and can have a different value from the value on the client. Do not transmit the length.<br/>          |
| \[[**out**](/windows/desktop/Midl/out-idl)\]                    | \[[**out**](/windows/desktop/Midl/out-idl)\]                    | Allocate space for the length parameter on the server but do not transmit the parameter. If the array size is fixed, allocate the array size on the server, but transmit no elements.<br/> If array size is not fixed, not legal: MIDL compiler error.<br/> | Transmit the length and the number of elements indicated by the length as set by the server application.                                                                                                             |
| \[[**out**](/windows/desktop/Midl/out-idl)\]                    | \[[**in**](/windows/desktop/Midl/in), [**out**](/windows/desktop/Midl/out-idl)\] | Transmit the length parameter. If the array size is bound, allocate the array size on the server, but transmit no elements.<br/> If array size is not bound, not legal: MIDL compiler error.<br/>                                                           | Transmit the length. Transmit the number of array elements indicated by the length.<br/>                                                                                                                       |
| \[[**in**](/windows/desktop/Midl/in), [**out**](/windows/desktop/Midl/out-idl)\] | \[[**in**](/windows/desktop/Midl/in)\]                          | Transmit the length and the number of elements indicated by the parameter.                                                                                                                                                                                              | Do not transmit the length. Transmit the number of elements indicated by the length.<br/> Note that the length can be changed and can have a different value from the original value on the client.<br/> |
| \[[**in**](/windows/desktop/Midl/in), [**out**](/windows/desktop/Midl/out-idl)\] | \[[**out**](/windows/desktop/Midl/out-idl)\]                    | Not legal; MIDL compiler error.                                                                                                                                                                                                                                         | Not legal; MIDL compiler error.                                                                                                                                                                                      |
| \[[**in**](/windows/desktop/Midl/in), [**out**](/windows/desktop/Midl/out-idl)\] | \[[**in**](/windows/desktop/Midl/in), [**out**](/windows/desktop/Midl/out-idl)\] | Transmit the length and the number of elements indicated by the parameter.                                                                                                                                                                                              | Transmit the length and the number of elements indicated by the parameter.                                                                                                                                           |



 

In general, you should not modify the length or size parameters on the server side. If you change the length parameter, you can orphan memory. For more information, see [Memory Orphaning](memory-orphaning.md).

 

