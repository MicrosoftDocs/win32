---
title: Directional Attributes Applied to the Parameter
description: The directional attributes \ in\ and \ out\ determine how the client and server allocate and free memory. The following table summarizes the effect of directional attributes on memory allocation.
ms.assetid: 21ab54c4-a707-4ee3-bea8-8ba216e25c16
ms.topic: article
ms.date: 05/31/2018
---

# Directional Attributes Applied to the Parameter

The directional attributes \[ [in](/windows/desktop/Midl/in)\] and \[ [out](/windows/desktop/Midl/out-idl)\] determine how the client and server allocate and free memory. The following table summarizes the effect of directional attributes on memory allocation.



| Directional attribute    | Memory on client                                                                                            | Memory on server                                                                                                                                        |
|--------------------------|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| \[ [in](/windows/desktop/Midl/in)\]       | Client application must allocate before the call.                                                           | Server stub allocates.                                                                                                                                  |
| \[ [out](/windows/desktop/Midl/out-idl)\] | Client stub allocates on return.                                                                            | Server stub allocates top-level pointer only; the server application must allocate all embedded pointers. The server also allocates new data as needed. |
| \[**in**, **out**\]      | Client application must allocate initial data transmitted to server; client stub allocates additional data. | Server stub allocates initial data transmitted from client; the server application allocates new data as needed.                                        |



 

In all of these cases the client stub does not free memory. The client application must free the memory before it terminates. The server stub frees memory when the remote procedure call returns (subject to the \[ [allocate](/windows/desktop/Midl/allocate)\] ACF attribute).

 

 