---
description: Other Microsoft Tools for Building Distributed Applications
ms.assetid: 518ca5b5-4285-4d69-abfe-bf6444a1deb5
title: Other Microsoft Tools for Building Distributed Applications
ms.topic: article
ms.date: 05/31/2018
---

# Other Microsoft Tools for Building Distributed Applications

In addition to the tools in COM+, Microsoft provides the following tools to assist the developer in creating distributed applications:

-   Microsoft Data Access Components (MDAC). Microsoft provides several avenues for retrieving data from a myriad of sources. For example, OLE DB offers a set of COM interfaces for building database components. The interfaces are defined so that data providers can implement different levels of support, based on the capabilities of the underlying data store. Because OLE DB is COM-based, it can easily be extended, and extensions are implemented as new interfaces. OLE DB also includes an application-level programming interface, called ActiveX Data Objects (ADO). ADO exposes dual interfaces, so it can easily be used from scripting languages as well as Microsoft Visual C++, Visual Basic, and other developer tools.

    > [!Note]  
    > Developers can also choose to use a generic, vendor-neutral API such as the Microsoft Open Database Connectivity (ODBC) application programming interface (API). The ODBC API is a C language interface for accessing data in a DBMS by using Structured Query Language (SQL). An ODBC driver manager provides the programming interface and run-time components to locate DBMS-specific drivers. ODBC drivers, typically supplied by the DBMS vendor, translate generic calls from the ODBC driver manager into calls to the native data access method. The primary advantage of using the ODBC API is that you need to learn only one API to access a wide range of DBMSs.

     

-   Microsoft SQL Server. In addition to providing a robust and eloquent relational database system, Microsoft SQL Server can provide a distributed application with connection pooling and security that can integrate with the Windows security model.

-   COM Transaction Integration (COMTI). COMTI can be used to integrate mainframe systems into Windows systems, including COM+ applications. COMTI uses standard communication protocols (for example, LU 6.2) for communicating between Windows computers and mainframe and minicomputers.

## Related topics

<dl> <dt>

[COM+ Design Assumptions and Principles](com--design-assumptions-and-principles.md)
</dt> <dt>

[Designing the COM+ Application Using UML](designing-the-com--application-using-uml.md)
</dt> <dt>

[General Design Tips for Using COM+](general-design-tips-for-using-com-.md)
</dt> <dt>

[Optimizing Interactions with the COM+ Business Logic Tier](optimizing-interactions-with-the-com--business-logic-tier.md)
</dt> </dl>

 

 



