---
description: "Learn more about: Extensible Storage Engine Managed Reference"
title: Extensible Storage Engine Managed Reference
TOCTitle: Extensible Storage Engine Managed Reference
ms:assetid: b6dc69d0-82be-478d-b47f-37d7569cd200
ms:mtpsurl: https://msdn.microsoft.com/library/Dn375980(v=EXCHG.10)
ms:contentKeyID: 56355772
ms.date: 09/02/2015
ms.topic: article
---

# Extensible Storage Engine Managed Reference

Find reference information for the ManagedESENT library. The ManagedESENT library provides managed access to ESENT, the embeddable database engine that is native to Windows.


_**Applies to:** Windows | Windows Server_

**In this article**  
How is the ManagedESENT library different than ESENT?  
Requirements  
In this section  

## How is the ManagedESENT library different than ESENT?

ESENT is an embeddable, transactional database engine that allows you to create custom applications that need reliable, high-performance, low-overhead storage of data. The ESENT engine can help with data needs that range from something as simple as a hash table that is too large to store in memory, to something more complex, such as an application with tables, columns, and indexes. To create an application with ESENT, you use the esent.dll DLL that is part of the Windows operating system and write your code with C/C++. For more information about ESENT, see [Extensible Storage Engine Reference](./extensible-storage-engine-reference.md).

ManagedESENT is built on top of esent.dll, which is part of Windows, so there are no extra unmanaged binaries to download and install. With the ManagedESENT library, you can create your application by using a managed language such as C\# instead of C/C++. The library uses the same type and member names to expose the ESE API, so if you are already familiar with the structure of this API, you can easily transition to this managed library.

## Requirements

This managed library requires the following:

  - A computer running a version of Windows starting with Windows Vista

  - Visual Studio 2012

  - The .NET Framework 4.5

## In this section

  - [Microsoft.Isam.Esent](./microsoft.isam.esent-namespace.md)

  - [Microsoft.Isam.Esent.Interop](./microsoft.isam.esent.interop-namespace.md)

  - [Microsoft.Isam.Esent.Interop.Server2003](./microsoft.isam.esent.interop.server2003-namespace.md)

  - [Microsoft.Isam.Esent.Interop.Vista](./microsoft.isam.esent.interop.vista-namespace.md)

  - [Microsoft.Isam.Esent.Interop.Windows7](./microsoft.isam.esent.interop.windows7-namespace.md)

  - [Microsoft.Isam.Esent.Interop.Windows8](./microsoft.isam.esent.interop.windows8-namespace.md)
