---
title: Serialization Services
description: Microsoft RPC supports two methods for encoding and decoding data, collectively called serializing data.
ms.assetid: 36d6ea16-7d01-436e-ac32-610c3ddb8b8d
keywords:
- Remote Procedure Call RPC , described, serialization
ms.topic: article
ms.date: 05/31/2018
---

# Serialization Services

Microsoft RPC supports two methods for encoding and decoding data, collectively called *serializing data*. Serialization means that the data is marshaled to and unmarshaled from buffers that you control. This differs from the traditional usage of RPC, in which the stubs and the RPC run-time library have full control of the marshaling buffers, and the process is transparent. You can use the buffer for storage on permanent media, encryption, and so on. When you encode data, the RPC stubs marshal the data to a buffer and pass the buffer to you. When you decode data, you supply a marshaling buffer with data in it, and the data is unmarshaled from the buffer to memory. You can serialize on a procedure or type basis.

> [!Note]  
> The term *pickling* is commonly used among developers to describe serialization. In fact, the Windows SDK samples contains a directory called *pickle* that preserves the RPC serialization sample programs.

 

Serialization leverages the RPC mechanisms for marshaling and unmarshaling data for other purposes. For example, instead of using several I/O operations to serialize a group of objects to a stream, an application can optimize performance by serializing several objects of different types into a buffer and then writing the entire buffer in a single operation. The functions that manipulate serialization handles are independent of the type of serialization you are using.

As another example, if you need to use a network transport mechanism besides RPC, such as Microsoft Windows Sockets (Winsock). With RPC serialization, your program can make calls to functions that marshal your data into buffers and then transmit this data using Winsock. When your application receives data, it can use the RPC serialization mechanism to unmarshal data from buffers filled by the Winsock routines. This provides you with many of the advantages of RPC-style applications, and at the same time, it enables you to use non-RPC transport mechanisms.

You can also use serialization for purposes unrelated to network communications. For example, once you use the RPC encoding functions to marshal data to a buffer, you can store it in a file for use by another application. You can also encrypt it. You can even use it to store a hardware- and operating system-independent representation of data in a database.

The following topics present a discussion of the serialization services that Microsoft RPC supports:

-   [Using Serialization Services](using-serialization-services.md)
-   [Procedure Serialization](procedure-serialization.md)
-   [Type Serialization](type-serialization.md)
-   [Serialization Handles](serialization-handles.md)

 

 




