---
title: How ADSI Integrates Extensions
description: Guidelines that describe how ADSI interacts with extensions.
ms.assetid: 00301551-ec56-4cb4-8e77-264c3ad48814
ms.tgt_platform: multiple
keywords:
- extensions ADSI
- adsi and extensions
ms.topic: article
ms.date: 05/31/2018
---

# How ADSI Integrates Extensions

The following guidelines describe how ADSI interacts with extensions:

-   Something binds to an ADSI directory object. For example, "LDAP://CN=JeffSmith,OU=Sales,DC=Fabrikam,DC=COM".
-   ADSI identifies that the object is in the **user** class.
-   ADSI performs a lookup in the registry and identifies the extension CLSIDs for **user**. Be aware that ADSI caches this data.
-   Something calls the **QueryInterface** method for IID\_IMyExtension. ADSI searches the interfaces associated with the **user** object, starting with its own interfaces, then looking at extension interfaces.
-   If a match is found, ADSI creates an instance of the component that supports IID\_IMyExtension, and calls **QueryInterface** for the extension. The resulting interface is returned.
-   The user uses this interface to call the interface methods.
-   Next, the client calls **QueryInterface** for IID\_IYourExtension, which is in a different component. This component delegates this **QueryInterface** call to the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface of the aggregator, which happens to be ADSI itself.
-   Again, ADSI searches the interfaces and creates the component instance.

 

 