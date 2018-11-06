---
title: Using Active Directory Service Interfaces
description: Active Directory Service Interfaces (ADSI) provides the means for client applications of directory services to use one set of interfaces to communicate with any namespace that provides an ADSI implementation.
ms.assetid: 58bde1ea-30d1-4601-a6fb-df0bb837e2ab
ms.tgt_platform: multiple
keywords:
- Using Active Directory Service Interfaces ADSI
- ADSI ADSI , Using
- Active Directory Service Interfaces ADSI , Using
ms.topic: article
ms.date: 05/31/2018
---

# Using Active Directory Service Interfaces

Active Directory Service Interfaces (ADSI) provides the means for client applications of directory services to use one set of interfaces to communicate with any namespace that provides an ADSI implementation. ADSI clients use the well-defined Active Directory Service Interfaces in place of the network-specific API calls to gain simpler access to the services for a namespace.

Active Directory Service Interfaces conform to the Component Object Model (COM) and support standard COM features.

ADSI supplies interfaces that are compliant with Automation for name-bound controllers like Java, Microsoft Visual Basic development system, and Visual Basic Scripting Edition (VBScript). ADSI can also provide an interface that can optimize performance for interfaces that are not compliant with Automation, to use with language environments like C and C++.

ADSI also provides the non-automation interfaces, [**IDirectoryObject**](/windows/desktop/api/Iads/nn-iads-idirectoryobject) and [**IDirectorySearch**](/windows/desktop/api/Iads/nn-iads-idirectorysearch), to support directory object management and queries.

In addition, ADSI supplies its own OLE DB provider, so that any client already using OLE DB, including those using ActiveX Data Objects, can query directory services directly.

Web applications using Active Server Pages also can program access to directory services through ADSI.

ADSI clients can programmatically discover all the ADSI providers at a site and use the same interfaces to communicate with each namespace. As additional providers are installed, the ADSI clients can communicate, without recompiling, with the new namespaces as well.

This programming guide describes how ADSI works and provides information for performing specific tasks in ADSI. The following topics are discussed:

-   [Binding to an ADSI Object](binding-to-an-adsi-object.md)
-   [Creating and Deleting Objects](creating-and-deleting-objects.md)
-   [Accessing and Manipulating Data with ADSI](accessing-and-manipulating-data-with-adsi.md)
-   [Using the ADSI Schema](using-the-adsi-schema.md)
-   [Collections and Groups](collections-and-groups.md)
-   [Enumerating ADSI Objects](enumerating-adsi-objects.md)
-   [Searching Active Directory](searching-active-directory.md)
-   [ADSI Security Model](adsi-security-model.md)
-   [ADSI Extensions](adsi-extensions.md)
-   [Using ADSI with Exchange](using-adsi-with-exchange.md)
-   [ADSI Utility Interfaces](adsi-utility-interfaces.md)
-   [Programming ADSI with Java/COM](programming-adsi-with-javacom.md)

 

 




