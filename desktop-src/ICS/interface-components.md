---
title: Interface Components
description: Interface Components
ms.assetid: '1827a554-4153-42f6-b39f-97cece8cd1c2'
---

# Interface Components

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. It is unavailable in subsequent versions. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The IPv6 Internet Connection Firewall APIs consist of two core interfaces, a subsidiary interface, and a number of enumeration and collection interfaces.

The core interfaces include:

-   A manager interface that provides access to individual connections. All clients of this API must start with this interface.
-   A connection interface is the main interface for performing actual configuration tasks. This interface enables enumeration of the set of open ports and includes methods to open a port, close a port, and query if a port is open with the use of direct arguments.

The subsidiary interface represents an open port on a connection and is intended only for use by the open port enumerations and collections.

The enumeration interfaces for connections and open ports are provided in two forms: one that returns the native interface, and one that returns a **VARIANT**. The native interface is for use by C++ clients; the interface that returns a **VARIANT** is for use by scripting clients that are making use of the collection functionality present in the scripting language, for example, the for-each construct in Visual Basic. The collection interfaces are for use by scripting clients.

There are also two means provided to obtain enumerations or collections: a method that returns the native enumeration interface and a property that yields the collection. Again, the native enumeration interface is for C++ clients and the property that yields the collection is for scripting clients.

 

 




