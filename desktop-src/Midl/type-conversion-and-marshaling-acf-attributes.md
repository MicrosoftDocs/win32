---
title: Type-Conversion and Marshaling ACF Attributes
description: Use these attributes to control how your data is transmitted over the network.
ms.assetid: 6af635f6-eeee-4fa6-85db-5d60434a1235
keywords:
- ACF MIDL , attributes, type conversion and marshaling
ms.topic: article
ms.date: 05/31/2018
---

# Type-Conversion and Marshaling ACF Attributes

Use these attributes to control how your data is transmitted over the network.



| Attribute                                        | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**encode**](encode.md)[**decode**](decode.md) | Instructs MIDL to expose the type or procedure serialization (pickling) routines it generates for the stubs. Your client application can call those routines to marshal data by value.                                                                                                                                                                                                                                                                                  |
| [**represent\_as**](represent-as.md)            | Specifies how a data type will be represented on the wire, when the exact nature of a client's data type is unimportant to the server (because it only needs the data itself and not the actual structure), or the actual client type is unknown to MIDL at compile time. For example, if your client application uses a linked list of floating-point numbers, you could specify that the wire-representation of that list be an array of type [**float**](float.md). |
| [**user\_marshal**](user-marshal.md)            | Controls how data is transmitted over the wire by implementing your own marshaling routines. This attribute is useful if you have a data type that is unknown to MIDL or if you are passing information between big-endian and little-endian platforms.                                                                                                                                                                                                                 |



 

The DCE marshaling attributes [**in\_line**](in-line.md) and [**out\_of\_line**](out-of-line.md) are not implemented in Microsoft RPC. The MIDL compiler automatically marshals complex data types out-of-line.

 

 




