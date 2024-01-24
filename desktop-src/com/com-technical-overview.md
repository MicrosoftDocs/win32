---
title: COM Technical Overview
ms.assetid: 519c87cc-b442-4187-af2a-124a1e4e8b49
description: "Learn more about: COM Technical Overview"
keywords:
- COM Technical Overview COM
ms.topic: article
ms.date: 05/31/2018
---

# COM Technical Overview

This topic provides an overview of the Microsoft Component Object Model (COM):

-   [Introduction to COM](#introduction-to-com)
-   [Objects and Interfaces](#objects-and-interfaces)
-   [Interface implementation](#interface-implementation)
-   [The IUnknown Interface](#the-iunknown-interface)
-   [The Client/Server Model](#the-clientserver-model)
-   [Service Control Manager](#service-control-manager)
-   [Reusability](#reusability)
-   [Storage and Stream Objects](#storage-and-stream-objects)
-   [Data Transfer](#data-transfer)
-   [Remoting](#remoting)
-   [Security](#security)
-   [Related topics](#related-topics)

## Introduction to COM

The Microsoft Component Object Model (COM) defines a binary interoperability standard for creating reusable software libraries that interact at run time. You can use COM libraries without the requirement of compiling them into your application. COM is the foundation for a number of Microsoft products and technologies, such as Windows Media Player and Windows Server.

COM defines a binary standard that applies to many operating systems and hardware platforms. For network computing, COM defines a standard wire format and protocol for interaction among objects that run on different hardware platforms. COM is independent of implementation language, which means that you can create COM libraries by using different programming languages, such as C++ and those in the .NET Framework.

The COM specification provides all of the fundamental concepts that enable cross-platform software reuse:

-   A binary standard for function calls between components.
-   A provision for strongly-typed groupings of functions into interfaces.
-   A base interface that provides polymorphism, feature discovery, and object lifetime tracking.
-   A mechanism that uniquely identifies components and their interfaces.
-   A component loader that creates component instances from a deployment.

COM has a number of parts that work together to enable the creation of applications that are built from reusable components:

-   A *host system* that provides a run-time environment that conforms to the COM specification.
-   *Interfaces* that define feature contracts, and *components* that implement interfaces.
-   *Servers* that provide components to the system, and *clients* that use the features provided by components.
-   A *registry* that tracks where components are deployed on local and remote hosts.
-   A *Service Control Manager* that locates components on local and remote hosts and connects servers to clients.
-   A *structured storage* protocol that defines how to navigate the contents of files on the host's file system.

Enabling code re-use across hosts and platforms is central to COM. A reusable interface implementation is named a *component*, a *component object*, or a *COM object*. A component implements one or more COM interfaces.

You define a custom COM library by designing the interfaces that your library implements. Consumers of your library can discover and use its features without any knowledge of your library's deployment and implementation details.

## Objects and Interfaces

A COM object exposes its features through an *interface*, which is a collection of member functions. A COM interface defines the expected behavior and responsibilities of a component, and it specifies a strongly-typed contract that provides a small set of related operations. All communication among COM components occurs through interfaces, and all services offered by a component are exposed through its interface. A caller can access only the interface member functions. Internal state is unavailable to a caller unless it is exposed in the interface.

Interfaces are strongly typed. Every interface has its own unique interface identifier, named an IID, which eliminates collisions that could occur with human-readable names. The IID is a globally unique identifier (GUID), which is the same as the Universally Unique ID (UUID) defined by the Open Software Foundation (OSF) Distributed Computing Environment (DCE). When you create a new interface, you must create a new identifier for that interface. When a caller uses an interface, it must use the unique identifier. This explicit identification improves robustness by eliminating naming conflicts that would result in run-time failure.

When you define a new interface, you can create an interface definition by using the interface definition language (IDL). From this interface definition, the Microsoft IDL compiler generates header files for use by applications using the interface, and source code to handle remote procedure calls. The IDL supplied by Microsoft is based on simple extensions to DCE IDL, an industry standard for Remote Procedure Call (RPC)-based distributed computing. IDL is a tool for the convenience of the interface designer and is not central to COM interoperability. With IDL, you do not need to create header files manually for each programming environment. For more information, see [Defining COM Interfaces](defining-com-interfaces.md).

Inheritance is used sparingly in COM interfaces. COM supports interface inheritance only to reuse a contract associated with a base interface. COM does not support selective inheritance; therefore, if one interface inherits from another, it includes all of the functions that the base interface defines. In addition, interfaces use only single inheritance, instead of multiple inheritance, to obtain functions from a base interface.

## Interface implementation

You cannot create an instance of a COM interface by itself. Instead, you create an instance of a class that implements the interface. In C++, a COM interface is modeled as an *abstract base class*, which means that the interface is a C++ class that contains only pure virtual member functions. A C++ library implements COM objects by inheriting the member function signatures from one or more interfaces, overriding each member function, and providing an implementation for each function.

You can use any programming language that supports the concept of function pointers to implement a COM interface. For example, in C, an interface is a structure containing a pointer to a table of function pointers, one for each method in the interface.

When you implement an interface, your class must provide an implementation for every function in the interface. If the class has no work to do in an interface function, the implementation may be a single return statement.

A COM class is identified by using a unique 128-bit Class ID (CLSID) that associates a class with a particular deployment in the file system, which for Windows is a DLL or EXE. A CLSID is a GUID, which means that no other class has the same CLSID. The use of unique class identifiers prevents name collisions among classes. For example, two different vendors can write a class named CStack, but both classes have a unique CLSID, so any possibility of a collision is avoided.

You obtain a new CLSID by using the [**CoCreateGuid**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateguid) function or by using a COM authoring tool, such as Visual Studio, that calls this function internally.

## The IUnknown Interface

All COM interfaces inherit from the [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) interface. The **IUnknown** interface contains the fundamental COM operations for polymorphism and instance lifetime management. The **IUnknown** interface has three member functions, named [**QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q)), [**AddRef**](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref), and [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release). All COM objects are required to implement the **IUnknown** interface.

The [**QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q)) member function provides polymorphism for COM. Call **QueryInterface** to determine at run time whether a COM object supports a particular interface. The COM object returns an interface pointer in the `ppvObject` parameter if it implements the requested interface, otherwise it returns `NULL`. The **QueryInterface** member function enables navigation among all of the interfaces that a COM object supports.

The lifetime of a COM object instance is controlled by its *reference count*. The [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) member functions [**AddRef**](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref) and [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) control the count. **AddRef** increments the count and **Release** decrements the count. When the reference count reaches zero, the **Release** member function may free the instance, because no callers are using it.

## The Client/Server Model

A COM class implements a number of COM interfaces. The implementation consists of binaries that run when a caller interacts with an instance of the COM class. COM enables using a class in different applications, including applications written without knowledge of a particular class. On a Windows platform, classes exist either in a dynamic-linked library (DLL) or in another application (EXE).

On its host system, COM maintains a registration database of all the CLSIDs for the COM objects installed on the system. The registration database is a mapping between each CLSID and the location of the DLL or EXE that houses the corresponding class. COM queries this database whenever a caller wants to create an instance of a COM class. The caller needs to know only the CLSID to request a new instance of the class.

The interaction between a COM object and its callers is modeled as a client/server relationship. The client is the caller that requests a COM object from the system, and the server is the module that houses COM objects that provides services to clients.

A COM client is any caller that passes a CLSID to the system to request an instance of a COM object. The simplest way to create an instance is to call the COM function, [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance).

The [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) function creates one instance of the specified CLSID and returns an interface pointer of the type requested by the client. The client is responsible for managing the lifetime of the instance by calling its [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) function when the client has finished using it. To create multiple objects based on a single CLSID, call the [**CoGetClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-cogetclassobject) function. To connect to an object that is already created and running, call the [**GetActiveObject**](/previous-versions/windows/desktop/api/oleauto/nf-oleauto-getactiveobject) function.

A COM server provides a COM implementation to the system. A server associates a CLSID with a COM class, houses the implementation of the class, implements a class factory for creating instances of the class, and provides for unloading the server.

> [!Note]  
> A COM server is not the same as the COM object that it provides to the system.

 

To enable creating a COM object, a COM server must provide an implementation of the [**IClassFactory**](/windows/win32/api/unknwn/nn-unknwn-iclassfactory) interface. Clients can call the [**CreateInstance**](/windows/desktop/api/Unknwn/nf-unknwn-iclassfactory-createinstance) method to request a new instance of a COM object, but usually such requests are encapsulated in the [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) function.

You can deploy a COM server either as a shared library that is loaded into the client's process at run time (DLL on Windows platforms) or as an executable module (EXE on Windows platforms). For more information, see [Registering COM Applications](registering-com-applications.md).

## Service Control Manager

The Service Control Manager (SCM) handles the client request for an instance of a COM object. The following list shows the sequence of events:

-   A client requests an interface pointer to a COM object from the COM Library by calling a function such as [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) with the CLSID of the COM object.
-   The COM Library queries the SCM to find the server that corresponds with the requested CLSID.
-   The SCM locates the server and requests the creation of the COM object from the class factory that is provided by the server.
-   If successful, the COM Library returns an interface pointer to the client.

After the COM system connects a server object to a client, the client and object communicate directly. There is no added overhead from calling through an intermediary run time.

When you register a COM server with the host system, you can specify different ways for the server to be activated. The following list shows the three ways that the SCM can activate a COM server:

-   In-process: The SCM returns the file path of the DLL that contains the object server implementation. The COM Library loads the DLL and queries it for its class factory interface pointer.
-   Local: The SCM starts the local executable which registers a class factory on startup, and its interface pointer is available to the system and clients.
-   Remote: The local SCM acquires a class factory interface pointer from the SCM that is running on a remote computer.

When a client requests a COM object, the COM Library contacts the SCM on the local host. The SCM locates the appropriate COM server, which may be local or remote, and the server returns an interface pointer to the server's class factory. When the class factory is available, the COM Library or the client can use the class factory to create the requested object. For more information, see [Implementing IClassFactory](implementing-iclassfactory.md).

## Reusability

COM supports *black-box reusability*, which means that the implementation details of a reusable component are not exposed to clients. To achieve black-box reusability, COM supports two mechanisms through which one object may reuse another. The two forms of reuse are named *containment* and *aggregation*. By convention, the object being reused is named the *inner object*, and the object that is making use of the inner object is named the *outer object*.

In containment, the outer object behaves as a client of the inner object. The outer object is a logical container for the inner object, and when the outer object uses the services of the inner object, the outer object delegates implementation to the inner object's interfaces. This means that the outer object is implemented in terms of the inner object's services. The outer object may not support the same interfaces as the inner object, and the outer object may use an inner object's interface to help with implementing parts of a different interface on the outer object.

In aggregation, the outer object exposes interfaces from the inner object as if they were implemented on the outer object. This is useful when the outer object would always delegate every call on one of its interfaces to the same interface of the inner object. Aggregation is a convenience that enables the outer object to avoid extra implementation overhead.

For more information, see [Reusing Objects](reusing-objects.md).

## Storage and Stream Objects

COM objects save state to a file by using *structured storage*, which is a form of persistent storage that enables navigation of a file's contents by using file system semantics. Treating a file's contents in this manner enables features such as incremental access, transactions, and sharing among processes.

The COM persistent storage specification provides for two types of storage elements: storage objects and stream objects. These objects are implemented by the COM Library, and user applications rarely implement these storage elements. Storage objects implement the [**IStorage**](/windows/desktop/api/objidl/nn-objidl-istorage) interface, and stream objects implement the [**IStream**](/windows/desktop/api/objidl/nn-objidl-istream) interface.

A stream object contains data and is conceptually similar to a single file in a file system. Each stream has access rights and a single seek pointer. Through the [**IStream**](/windows/desktop/api/objidl/nn-objidl-istream) interface, you can read, write, seek, and perform other operations on the stream's underlying data. A stream is named by using a text string. It can contain any internal structure, because it is a flat stream of bytes. In addition, the functions in the **IStream** interface are similar to standard file-handle based functions, such as those in the ANSI C run-time library.

A storage object is conceptually similar to a directory in a file system. Each storage can contain any number of sub-storage objects and any number of streams. Each storage has its own access rights. Through the [**IStorage**](/windows/desktop/api/objidl/nn-objidl-istorage) interface, you can perform operations such as enumerating, moving, copying, renaming, creating, and deleting elements. A storage object does not store application-defined data, but it stores implicitly the names of the elements (storages and streams) that it contains.

Storage and stream objects are sharable among processes when they are implemented according to the COM specification on a host platform. This enables objects that are running in-process or out-of-process to have equal incremental access to their file storage. Because COM is loaded into each process separately, it uses operating-system supported shared memory mechanisms to communicate the state of opened elements and their access modes between processes.

Every storage and stream object in a structured file has a name to identify it. The name is a string that follows a particular convention. For more information, see [Storage Object Naming Conventions](/windows/desktop/Stg/storage-object-naming-conventions). The name is passed to [**IStorage**](/windows/desktop/api/objidl/nn-objidl-istorage) functions to specify which element in the storage to operate on. Names of root storage objects are the same as file names in the underlying file system, and these names must follow the file system's conventions and restrictions. Strings passed to storage-related functions which name files are passed through to the file system without interpretation or changes.

Names of elements that are contained within storage objects are managed by the implementation of the particular storage object in question. All implementations of storage objects must support element names that are 32 characters in length, and some implementations may support longer names. Names are stored with case preserved, but they are compared as case-insensitive. Applications that define storage element names must choose names that work in either situation.

You access every element in a structured storage file by using functions and interfaces that are implemented by COM. This means that other applications can browse the file by navigating with the [**IStorage**](/windows/desktop/api/objidl/nn-objidl-istorage) interface functions that provide directory-like services. Also, other applications can use the file's data, without having to run the application that wrote the file. When a COM application accesses the structured storage files of another application, standard Windows access rights apply, and the application must have sufficient privileges.

A COM object can read and write itself to persistent storage. A client queries for one of the persistence-related interfaces on the COM object, depending on the context of the operation. COM objects can implement any combination of the following interfaces:

-   [**IPersistStorage**](/windows/desktop/api/ObjIdl/nn-objidl-ipersiststorage): The COM object reads and writes its persistent state to a storage object. The client provides the object with an [**IStorage**](/windows/desktop/api/objidl/nn-objidl-istorage) pointer through this interface. This is the only persistence interface that includes semantics for incremental access.
-   [**IPersistStream**](/windows/desktop/api/ObjIdl/nn-objidl-ipersiststream): The COM object reads and writes its persistent state to a stream object. The client provides the object with an [**IStream**](/windows/desktop/api/objidl/nn-objidl-istream) pointer through this interface.
-   [**IPersistFile**](/windows/desktop/api/ObjIdl/nn-objidl-ipersistfile): The COM object reads and writes its persistent state directly to a file on the underlying system. This interface does not involve [**IStorage**](/windows/desktop/api/objidl/nn-objidl-istorage) or [**IStream**](/windows/desktop/api/objidl/nn-objidl-istream) unless the underlying file is accessed through these interfaces, but the **IPersistFile** interface has no semantics for storages and streams. The client provides the object with a file name and calls the [**Save**](/windows/desktop/api/ObjIdl/nf-objidl-ipersistfile-save) or [**Load**](/windows/desktop/api/ObjIdl/nf-objidl-ipersistfile-load) functions.

## Data Transfer

Structured storage provides the basis for data exchange between COM objects and processes, which is named *uniform data transfer*. Before COM was implemented in OLE 2, data transfer on Windows was specified by *transfer protocols*, such as the clipboard and drag-drop protocols. Each transfer protocol had its own set of functions that bound the protocol to the query, and specific code was required to handle each different protocol and exchange procedure. Uniform data transfer represents all data transfers by using the [**IDataObject**](/windows/desktop/api/ObjIdl/nn-objidl-idataobject) interface, which separates common data exchange operations from the transfer protocol.

The [**IDataObject**](/windows/desktop/api/ObjIdl/nn-objidl-idataobject) interface encapsulates the standard get and set operations on data, queries and enumerations, and notifications that detect when data changes in an object. Uniform data transfer enables rich descriptions of data formats, as well as the use of different storage media for the data transfer.

During uniform data transfer, all protocols exchange a pointer to an [**IDataObject**](/windows/desktop/api/ObjIdl/nn-objidl-idataobject) interface. The server is the source of the data and implements one data object, which is usable in any data exchange protocol. The client consumes the data and requests data from a data object when it receives an **IDataObject** pointer from any protocol. After the pointer exchange has occurred, both sides handle data exchange in a uniform fashion, through the **IDataObject** interface.

COM defines two data structures that enable uniform data transfer. The [**FORMATETC**](/windows/win32/api/objidl/ns-objidl-formatetc) structure represents a generalized clipboard format, and the [**STGMEDIUM**](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structure represents the transfer medium as a memory handle.

The client creates a [**FORMATETC**](/windows/win32/api/objidl/ns-objidl-formatetc) structure to indicate the type of data that it requests from a data source, and it is used by the data source to describe what formats it provides. The client queries a data source for its available formats by requesting its [**IEnumFORMATETC**](/windows/desktop/api/ObjIdl/nn-objidl-ienumformatetc) interface. For more information, see [The FORMATETC Structure](the-formatetc-structure.md).

The client creates a [**STGMEDIUM**](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structure and passes it to the [**GetData**](/windows/desktop/api/ObjIdl/nf-objidl-idataobject-getdata) method, and the data object returns the data in the provided **STGMEDIUM** structure.

The [**STGMEDIUM**](/windows/win32/api/objidl/ns-objidl-ustgmedium-r1) structure enables both clients and data sources to choose the most efficient exchange medium. For example, if the data to be exchanged is very large, the data source can indicate a disk-based medium as its preferred format, instead of main memory. This flexibility enables efficient data exchanges that can be as fast as passing a pointer to an [**IStorage**](/windows/desktop/api/objidl/nn-objidl-istorage) or an [**IStream**](/windows/desktop/api/objidl/nn-objidl-istream). For more information, see [The STGMEDIUM Structure](the-stgmedium-structure.md).

A client of a data source may require notification when the data changes. COM handles data-change notifications by using an *advise sink* object, which implements the [**IAdviseSink**](/windows/desktop/api/ObjIdl/nn-objidl-iadvisesink) interface. The advise sink object and the **IAdviseSink** interface are implemented by the client, which passes an **IAdviseSink** pointer to the data source. When the data source detects a change in the underlying data, it calls an **IAdviseSink** method to notify the client. For more information, see [Data Notification](data-notification.md).

## Remoting

COM enables remote and distributed computation. *Interface remoting* enables a member function to return an interface pointer to a COM object that is in a different process or on a different host computer. The infrastructure that performs the interface remoting is transparent to both the client and the object server. Neither the client nor the server need one another's deployment details to communicate through a remoted interface. A client calls member functions on the same interface to communicate with a COM object that is in-process, out-of-process on the local host, or on a remote computer. Local and remote calls on the same interface are indistinguishable to the client.

To communicate with a COM object, a client always calls an in-process implementation. If the COM object is in-process, the call is direct. If the COM object is out-of-process or remote, COM provides a *proxy* implementation that forwards the call to the object by using the Remote Procedure Call (RPC) protocol.

A COM object always receives calls from a client through an in-process implementation. If the caller is in-process, the call is direct. If the caller is out-of-process or remote, COM provides a *stub* implementation that receives the remote procedure call from the proxy in the client process.

*Marshaling* is the procedure for packaging the call stack for transmission from proxy to stub. *Unmarshaling* is the unpackaging that occurs at the receiving end. Return values are marshaled and unmarshaled from the stub to the proxy. This kind of communication is also referred to as sending a call *over the wire*.

Each different data type has rules for marshaling. Interface pointers also have a marshaling protocol, which is encapsulated in the [**CoMarshalInterface**](/windows/desktop/api/combaseapi/nf-combaseapi-comarshalinterface) function. In most cases, *standard interface marshaling*, which is provided by the system, is sufficient, but a COM object optionally may implement *custom interface marshaling* to control the creation of remote object proxies to itself. For more information, see [Inter-Object Communication](inter-object-communication.md).

## Security

COM provides two forms of application security. One is *activation security*, which specifies how new objects are created, how clients connect to new and existing objects, and how certain public services, such as the Class Table and the Running Object Table are secured. The other is *call security*, which specifies how security operates in an established connection between a client to a COM object.

Activation security is applied automatically by the Service Control Manager (SCM). When the SCM receives a request to retrieve a COM object, it checks the request against security information that is stored in the registry.

SCM implementations usually offer registry-driven configuration for administering deployed classes and for specific user accounts on the host. For more information, see [Activation Security](activation-security.md).

Call security is applied automatically or is enforced by the application. If the application provides setup information, COM performs the necessary checks to secure the application.

The automatic mechanism checks security for the process, but not for individual objects or methods. If an application requires more fine-grained security, COM provides functions that applications may use do their own security checking.

The automatic and custom mechanisms can be used together, so an application may ask COM to perform automatic security checking and then perform its own.

COM call security services are divided into the following categories:

-   General functions that are called by both clients and servers, which enable the automatic security mechanism to be initialized and automatic authentication services to be registered. The general call security APIs are the [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) and [**CoQueryAuthenticationServices**](/windows/desktop/api/combaseapi/nf-combaseapi-coqueryauthenticationservices) functions.
-   Interfaces on client proxies, which enable the client to control the security on calls to individual interfaces. The [**IClientSecurity**](/windows/desktop/api/ObjIdl/nn-objidl-iclientsecurity) interface and the [**CoQueryProxyBlanket**](/windows/desktop/api/combaseapi/nf-combaseapi-coqueryproxyblanket), [**CoSetProxyBlanket**](/windows/desktop/api/combaseapi/nf-combaseapi-cosetproxyblanket), and [**CoCopyProxy**](/windows/desktop/api/combaseapi/nf-combaseapi-cocopyproxy) functions provide call security on a remote object.
-   Server-side functions and call-context interfaces, which enable the server to retrieve security information about a call and to impersonate the caller. The [**IServerSecurity**](/windows/win32/api/objidlbase/nn-objidlbase-iserversecurity) interface and the [**CoGetCallContext**](/windows/desktop/api/combaseapi/nf-combaseapi-cogetcallcontext), [**CoImpersonateClient**](/windows/desktop/api/combaseapi/nf-combaseapi-coimpersonateclient), and [**CoRevertToSelf**](/windows/desktop/api/combaseapi/nf-combaseapi-coreverttoself) functions provide server-side call security.

Often, the client queries the COM object for the [**IClientSecurity**](/windows/desktop/api/ObjIdl/nn-objidl-iclientsecurity) interface, which is implemented locally by the remoting layer. The client uses this interface to control the security of individual interface proxies on the COM object before making a call on one of the interfaces.

When a call arrives at the server, the server may call the [**CoGetCallContext**](/windows/desktop/api/combaseapi/nf-combaseapi-cogetcallcontext) function to retrieve an [**IServerSecurity**](/windows/win32/api/objidlbase/nn-objidlbase-iserversecurity) interface, which allows the server to check the client's authentication and to impersonate the client, if necessary. The **IServerSecurity** object is valid for the duration of the call.

Call the [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) function to initialize the security layer and set the specified values as the security default. If a process does not call **CoInitializeSecurity**, COM calls it automatically the first time an interface is marshaled or unmarshaled, registering the system default security. The **CoInitializeSecurity** function allows the client to establish default call security for the process, which avoids the use of [**IClientSecurity**](/windows/desktop/api/ObjIdl/nn-objidl-iclientsecurity) on individual proxies. The **CoInitializeSecurity** function enables a server to register automatic authentication services for the process. For more information, see [Setting Process-Wide Security with CoInitializeSecurity](setting-processwide-security-with-coinitializesecurity.md).

## Related topics

<dl> <dt>

[COM Clients and Servers](com-clients-and-servers.md)
</dt> <dt>

[Defining COM Interfaces](defining-com-interfaces.md)
</dt> <dt>

[Registering COM Applications](registering-com-applications.md)
</dt> <dt>

[Security in COM](security-in-com.md)
</dt> <dt>

[Processes, Threads, and Apartments](processes--threads--and-apartments.md)
</dt> </dl>

 

 
