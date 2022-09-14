---
title: Interface Header Attributes
description: Incorporate these attributes in the interface header to convey information about the entire interface.
ms.assetid: 5e30c902-1a55-4afd-afba-93fcc9e75033
keywords:
- IDL MIDL , attributes, interface header
ms.topic: article
ms.date: 05/31/2018
---

# Interface Header Attributes

Incorporate these attributes in the interface header to convey information about the entire interface.



| Attribute                                   | Usage                                                                                                                                                                                                                                            |
|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**async\_uuid**](async-uuid.md)           | Directs the MIDL compiler to define both synchronous and asynchronous versions of a COM interface.                                                                                                                                               |
| [**uuid**](uuid.md)                        | Designates a 128-bit value that distinguishes a particular interface from all others. The actual value may represent a GUID, a CLSID, or an IID.                                                                                                 |
| [**local**](local.md)                      | Directs the MIDL compiler to generate header files only. An interface must have either a [**uuid**](uuid.md) or a [**local**](local.md) attribute.                                                                                             |
| [**ms\_union**](-ms-union.md)              | Controls the NDR alignment of nonencapsulated unions. Use for backward compatibility with interfaces built on MIDL 1.0 or 2.0.                                                                                                                   |
| [**object**](object.md)                    | Identifies the interface as a COM interface and directs the MIDL compiler to generate proxy/stub code instead of RPC client and server stubs.                                                                                                    |
| [**version**](version.md)                  | Identifies a particular version of an interface in cases where multiple versions of the interface exist. Because COM interfaces are immutable, you cannot use the [**version**](version.md) attribute on an [**object**](object.md) interface. |
| [**pointer\_default**](pointer-default.md) | Specifies the default pointer type for all pointers except for those included in parameter lists. The default type can be [**unique**](unique.md), [**ref**](ref.md), or [**ptr**](ptr.md).                                                   |
| [**endpoint**](endpoint.md)                | Specifies a static (well-known) endpoint on which a server application will listen for remote procedure calls.                                                                                                                                   |



 

See [Type Library Attributes](type-library-attributes.md) for interface attributes, such as [**dual**](dual.md) and [**oleautomation**](oleautomation.md), that are specific to interfaces defined or referenced inside a library statement.

 

 




