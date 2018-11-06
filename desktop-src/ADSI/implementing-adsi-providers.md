---
title: Implementing Active Directory Service Interfaces Providers
description: Active Directory Service Interfaces (ADSI) are COM interfaces that wrap directory service objects to expose them to clients of directory services. By supplying an implementation of ADSI, you expand your client-base to the set of ADSI client applications.
ms.assetid: f86f36f0-44ff-41b7-8cf6-b97b721a8572
ms.tgt_platform: multiple
keywords:
- Implementing Active Directory Service Interfaces Providers ADSI
- Implementing ADSI Providers ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Implementing Active Directory Service Interfaces Providers

Active Directory Service Interfaces (ADSI) are COM interfaces that wrap directory service objects to expose them to clients of directory services. By supplying an implementation of ADSI, you expand your client-base to the set of ADSI client applications.

As with any COM implementation, you can write an ADSI provider in many languages. The ADSI COM interfaces are defined as dual interfaces that allow both run-time and compile-time name resolution and can be called by Automation-compliant languages such as Visual Basic, Visual Basic Scripting Edition, and also the more performance and efficiency-conscious languages such as C and C++. ADSI clients also include web applications using Active Server Pages and administration snap-ins through the Microsoft Management Console.

Because ADSI supplies its own OLE DB provider, implementing the search features defined by [**IDirectorySearch**](/windows/desktop/api/Iads/nn-iads-idirectorysearch) also enables ADSI clients to query your directory service for data.

All directory service objects can be represented through a generic ADSI object supporting [**IDirectoryObject**](/windows/desktop/api/Iads/nn-iads-idirectoryobject). ADSI supplies the building blocks necessary to represent the features and services of any directory service.

In addition, the ADSI meta-interfaces represent common objects used by directory administrators. You map the properties of the meta-interfaces to the properties supported by your directory service. ADSI clients programming to the Active Directory Service Interfaces gain access to your directory service as soon as the provider is installed and the system restarted.

If your directory service supports a schema representation, supporting the schema management interfaces makes your namespace directly accessible to directory service browsers. By publishing your features through the schema, clients can query your directory service online and take advantage of the services you offer. Because of the online schema availability and the COM interface advantage, you can continue to make new features available to your client software while supporting down-level versions.

 

 




