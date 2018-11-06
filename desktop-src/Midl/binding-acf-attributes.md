---
title: Binding ACF Attributes
description: Specify how the client connects to the server for remote procedure calls with the attributes listed in the following table.
ms.assetid: 2a9fdd2f-c646-4ccd-bfa8-66fe973ef911
keywords:
- ACF MIDL , attributes, binding
ms.topic: article
ms.date: 05/31/2018
---

# Binding ACF Attributes

Specify how the client connects to the server for remote procedure calls with the attributes listed in the following table.



| Attribute                                                          | Usage                                                                                                                                                                                                              |
|--------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**async**](async.md)                                             | Defines a handle that allows the caller to make an asynchronous call and return immediately without waiting for results, and then resynchronize with the called function to receive data after the call completes. |
| [**auto\_handle**](auto-handle.md)                                | Tells MIDL to let the stub code control the binding automatically. This is the default if you don't specify any binding handle.                                                                                    |
| [**context\_handle\_noserialize**](context-handle-noserialize.md) | Guarantees that a context handle will never be serialized, regardless of the application's default behavior.                                                                                                       |
| [**context\_handle\_serialize**](context-handle-serialize.md)     | Guarantees that a context handle will always be serialized, regardless of the application's default behavior                                                                                                       |
| [**explicit\_handle**](explicit-handle.md)                        | Lets the client application control the binding with an explicit parameter in each procedure.                                                                                                                      |
| [**implicit\_handle**](implicit-handle.md)                        | Specifies a handle for procedures that do not have an explicit handle parameter. The client application still controls the binding.                                                                                |
| [**strict\_context\_handle**](strict-context-handle.md)           | Guarantees that the methods in the interface will only accept context handles that were created by a method of that interface.                                                                                     |



 

 

 




