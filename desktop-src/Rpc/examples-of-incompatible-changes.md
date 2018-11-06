---
title: Examples of Incompatible Changes
description: When dealing with incompatible changes, the unfortunate rule of thumb is as follows any change can be backward incompatible, unless it is very well understood.
ms.assetid: 5b893d79-b81d-4ede-8d49-71d85219c497
ms.topic: article
ms.date: 05/31/2018
---

# Examples of Incompatible Changes

When dealing with incompatible changes, the unfortunate rule of thumb is as follows: any change can be backward incompatible, unless it is very well understood. This rule requires knowledge of NDR rules. If you do not know what the NDR is, do not make modifications. Examples of changes that typically result in an access violation in the application, or a BAD\_STUB\_DATA\_EXCEPTION raised by the marshaling engine, are as follows:

-   Adding a new method in the middle of old methods.
-   Adding or removing parameters from a method.
-   Changing an attribute, for example a pointer attribute: changing \[ref\] to \[unique\] or \[ptr\] or vice versa. Each pointer type has a different wire representation.
-   Changing the size of the data: from short to long, from char to wchar\_t (unicode), adding a field to a structure, changing the size of a fixed size array.
-   Adding union arms to a union with a default clause.

Some insidious changes or unintended mismatches between a client and a server may occur as follows:

-   Modifying a member of a compound type, like a structure or an array. For example, if a CLIENT\_ID changes from an integral to a GUID, a CLIENT\_RECORD structure with the CLIENT\_ID field becomes incompatible. This may be difficult to detect if cascaded through several levels of embedding to an actual remote parameter type.
-   Modifying an imported type. The type may be coming from a different component that does not remote directly, hence the change was thought to be compatible.
-   Using \#ifdef in an IDL file is a bad idea to ifdef type definitions in an IDL file—it is disaster waiting to happen. Inevitably, due to build or other glitches, a client is compiled with a different set of defines than the server, and they end up being incompatible.

 

 




