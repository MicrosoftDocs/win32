---
title: Aliasing and Marshaling Attributes
description: Distributed applications almost always pass data between client and server programs when they call interface procedures.
ms.assetid: 64895c64-f16b-47c4-928d-5149808b0476
keywords:
- IDL MIDL , attributes MIDL , aliasing and marshaling
ms.topic: article
ms.date: 05/31/2018
---

# Aliasing and Marshaling Attributes

Distributed applications almost always pass data between client and server programs when they call interface procedures. Developers use MIDL to describe the data that client and server programs pass in a standard way. The MIDL compiler creates application stub, or proxy, programs for the client and the server that convert the data into a standardized form that can be sent over a network. This format, the Network Data Representation (NDR) format, is often called the wire format of the data. The stubs must convert data from its native format in the program's memory space to NDR. This conversion is termed marshaling the data. When a client or server program receives data, it must convert the data from NDR to the native format for that program. This is called unmarshaling the data.

Use aliasing and marshaling attributes to control how your data is packaged into NDR format and transmitted over the network.



| Attribute                             | Usage                                                                                                                         |
|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [**call\_as**](call-as.md)           | Maps a nonremotable function to a remote procedure call.                                                                      |
| [**iid\_is**](iid-is.md)             | Provides the interface identifier of the COM interface that is the object of the pointer.                                     |
| [**transmit\_as**](transmit-as.md)   | Converts a data type to a simpler type for transmission over a network.                                                       |
| [**wire\_marshal**](wire-marshal.md) | Similar to [**transmit\_as**](transmit-as.md) but you implement the routines to size, marshal, unmarshal, and free the data. |



 

## Related topics

<dl> <dt>

[Type Conversion and Marshaling ACF Attributes](type-conversion-and-marshaling-acf-attributes.md)
</dt> </dl>

 

 




