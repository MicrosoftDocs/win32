---
description: Glossary page
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 26a72de1-24bc-41e6-8d41-61d45f581e51
title: COM+ Glossary
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Glossary

<dl> <dt>

<span id="cos.access_token_gloss"></span><span id="COS.ACCESS_TOKEN_GLOSS"></span>**access token**
</dt> <dd>

An object that describes the security context of a process or thread. The information in a token includes the identity and privileges of the user account associated with the process or thread. When a user logs on, the system verifies the user's password by comparing it with information stored in a security database. If the password is authenticated, the system produces an access token. Every process executed on behalf of this user has a copy of this access token.

</dd> <dt>

<span id="cos.acid_properties_gloss"></span><span id="COS.ACID_PROPERTIES_GLOSS"></span>**ACID properties**
</dt> <dd>

Acronym coined by transaction processing pioneers for atomic, consistent, isolated, and durable. These properties ensure predictable behavior, reinforcing the role of transactions as all-or-none propositions designed to provide consistent and predictable results in a distributed environment when independent failures can occur.

</dd> <dt>

<span id="cos.activation_gloss"></span><span id="COS.ACTIVATION_GLOSS"></span>**activation**
</dt> <dd>

The chain of events that results in the creation of a COM object and the return of a valid pointer to an interface on that object. In COM+, an object gets activated either in its own context or in that of its creator (an object that has requested the object being activated). COM+ services rely on appropriate activation of an object based on the object's configuration. In the course of activation, the system determines the context in which the object runs, initializes the context properties, checks access permissions, and establishes a security identity.

</dd> <dt>

<span id="cos.activation_security_gloss"></span><span id="COS.ACTIVATION_SECURITY_GLOSS"></span>**activation security**
</dt> <dd>

A form of security protection that determines who can launch a server. Activation security is automatically applied by the Service Control Manager (SCM) of a particular computer. Upon receipt of a request from a client to activate an object, the SCM checks the request against activation-security information stored within its registry. Activation security is also checked for same-computer activations. Also called *launch security*.

</dd> <dt>

<span id="cos.activation_type_gloss"></span><span id="COS.ACTIVATION_TYPE_GLOSS"></span>**activation type**
</dt> <dd>

Activation category for a COM+ application that indicates whether the application runs in or out of its client's process space (depending on whether it's a library or server application, respectively) as well as whether the application runs as a service.

</dd> <dt>

<span id="cos.activity_gloss"></span><span id="COS.ACTIVITY_GLOSS"></span>**activity**
</dt> <dd>

In COM+, a logical thread comprising one or more transactions and containing a collection of components that are grouped into a COM+ application. Every COM object belongs to one activity. The association between an object and an activity cannot be changed.

</dd> <dt>

<span id="cos.apartment_model_process_gloss"></span><span id="COS.APARTMENT_MODEL_PROCESS_GLOSS"></span>**apartment model process**
</dt> <dd>

A process that has two or more single-threaded apartments and no multithreaded apartments.

</dd> <dt>

<span id="cos.application_proxy_gloss"></span><span id="COS.APPLICATION_PROXY_GLOSS"></span>**application proxy**
</dt> <dd>

A set of files containing registration information that allows a client to remotely access a COM+ server application. When installed on a client computer, an application proxy file writes information about the server application to the client computer; the client can then remotely access the server application.

</dd> <dt>

<span id="cos.authentication_gloss"></span><span id="COS.AUTHENTICATION_GLOSS"></span>**authentication**
</dt> <dd>

The security process of determining that a caller of an application is actually who it says it is—verifying the authenticity of an identity claim. For COM+ applications, authentication can be turned on and configured administratively, after which it works transparently to the application.

</dd> <dt>

<span id="cos.authorization_gloss"></span><span id="COS.AUTHORIZATION_GLOSS"></span>**authorization**
</dt> <dd>

The security process of determining whether a caller of an application is authorized to do what it is asking to do.

</dd> <dt>

<span id="cos.caching_resource_manager_gloss"></span><span id="COS.CACHING_RESOURCE_MANAGER_GLOSS"></span>**caching resource manager**
</dt> <dd>

A resource manager that acts as a front-end to another resource manager and that caches information locally, reducing the cost of accessing the underlying resource. Unlike a conventional resource manager, a caching resource manager does not participate in recovery because it never permanently stores the underlying data.

</dd> <dt>

<span id="cos.call_security_gloss"></span><span id="COS.CALL_SECURITY_GLOSS"></span>**call security**
</dt> <dd>

A form of security protection that helps control access to a server object's methods after a server has been launched.

</dd> <dt>

<span id="cos.class_gloss"></span><span id="COS.CLASS_GLOSS"></span>**class (COM)**
</dt> <dd>

A named, concrete implementation of one or more interfaces. A COM class is identified by a CLSID and, sometimes, a ProgID.

</dd> <dt>

<span id="cos.cloaking_gloss"></span><span id="COS.CLOAKING_GLOSS"></span>**cloaking**
</dt> <dd>

A server's ability to mask its own identity when making calls on a client's behalf. When cloaking is enabled, calls made by the server impersonating the client can be made under the client's identity. When cloaking is disabled, calls by the server will be made under the server's identity.

</dd> <dt>

<span id="cos.complus_application_gloss"></span><span id="COS.COMPLUS_APPLICATION_GLOSS"></span>**COM+ application**
</dt> <dd>

The primary unit of administration and security for Component Services. A COM+ application is a group of COM components that, generally, perform related functions. These components further consist of COM interfaces and methods.

</dd> <dt>

<span id="cos.complus_application_pooling_gloss"></span><span id="COS.COMPLUS_APPLICATION_POOLING_GLOSS"></span>**COM+ Application Pooling**
</dt> <dd>

A Component Services feature that allows single-threaded processes to scale and can also help you recover from failures in single processes by providing other running processes able to handle activations.

</dd> <dt>

<span id="cos.complus_application_recycling_gloss"></span><span id="COS.COMPLUS_APPLICATION_RECYCLING_GLOSS"></span>**COM+ Application Recycling**
</dt> <dd>

A Component Services feature that significantly increases the overall stability of your applications by allowing you to gracefully shut down a process associated with an application and restart it.

</dd> <dt>

<span id="cos.complus_catalog_gloss"></span><span id="COS.COMPLUS_CATALOG_GLOSS"></span>**COM+ catalog** 
</dt> <dd>

The data store that holds COM+ configuration data. Performance of COM+ administration tasks requires reading and writing data stored in the catalog. The catalog can be accessed only through the Component Services administrative tool or through the COMAdmin library.

</dd> <dt>

<span id="cos.complus_events_gloss"></span><span id="COS.COMPLUS_EVENTS_GLOSS"></span>**COM+ Events**
</dt> <dd>

COM+ Events matches and connects publishers and subscribers through a loosely coupled events system. A publisher makes the method call to initiate an event, and a subscriber receives these calls through the event system rather than directly from the publisher. The COM+ Events service maintains the list of interested subscribers who receive the calls and directs those calls without requiring the knowledge of the publisher.

</dd> <dt>

<span id="cos.complus_library_application_gloss"></span><span id="COS.COMPLUS_LIBRARY_APPLICATION_GLOSS"></span>**COM+ library application**
</dt> <dd>

A COM+ application that runs in the process of the client that creates it. Library applications can use role-based security but do not support remote access or queued components.

</dd> <dt>

<span id="cos.complus_object_pooling_gloss"></span><span id="COS.COMPLUS_OBJECT_POOLING_GLOSS"></span>**COM+ Object Pooling**
</dt> <dd>

An automatic service provided by COM+ that enables you to configure a component to have instances of itself kept active in a pool, ready to be used by any client that requests the component.

</dd> <dt>

<span id="cos.complus_partitions_gloss"></span><span id="COS.COMPLUS_PARTITIONS_GLOSS"></span>**COM+ Partitions**
</dt> <dd>

A COM+ service that enables, on a single computer, the creation of separate execution spaces for applications.

</dd> <dt>

<span id="cos.complus_partition_sets_gloss"></span><span id="COS.COMPLUS_PARTITION_SETS_GLOSS"></span>**COM+ partition sets**
</dt> <dd>

A group of COM+ partitions that is mapped to a particular user ID in Active Directory.

</dd> <dt>

<span id="cos.complus_queued_components_gloss"></span><span id="COS.COMPLUS_QUEUED_COMPONENTS_GLOSS"></span>**COM+ Queued Components**
</dt> <dd>

A COM+ service, based on Microsoft Message Queuing, that provides an easy way to invoke and execute components asynchronously. Message processing can occur without regard to the availability or accessibility of either the sender or the receiver.

</dd> <dt>

<span id="cos.complus_server_application_gloss"></span><span id="COS.COMPLUS_SERVER_APPLICATION_GLOSS"></span>**COM+ server application**
</dt> <dd>

A COM+ application that runs in its own process. Server applications can support all COM+ services.

</dd> <dt>

<span id="cos.complus_soap_gloss"></span><span id="COS.COMPLUS_SOAP_GLOSS"></span>**COM+ SOAP**
</dt> <dd>

A Component Services feature that allows you to expose a COM+ application as an XML web service. COM+ SOAP also enables you to use an XML web service as a COM component.

</dd> <dt>

<span id="cos.com_component_gloss"></span><span id="COS.COM_COMPONENT_GLOSS"></span>**COM component**
</dt> <dd>

A binary unit of code that includes packaging and registration code and that creates COM objects. All COM+ applications consist of one or more COM components.

</dd> <dt>

<span id="cos.commit_tree_gloss"></span><span id="COS.COMMIT_TREE_GLOSS"></span>**commit tree**
</dt> <dd>

In a distributed transaction system, the conceptual representation of a transaction as based on the hierarchical relationships between individual transaction managers participating in a distributed transaction. Included in that hierarchy are the enlisted resource managers associated with the transaction managers.

</dd> <dt>

<span id="cos.com_object_gloss"></span><span id="COS.COM_OBJECT_GLOSS"></span>**COM object**
</dt> <dd>

In the COM programming model, a programming structure encapsulating both data and functionality, which are defined and allocated as a single unit and for which the only public access is through the programming structure's interfaces. A COM object must support, at a minimum, the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface, which maintains the object's existence while it is being used and provides access to the object's other interfaces.

</dd> <dt>

<span id="cos.compensating_resource_manager_gloss"></span><span id="COS.COMPENSATING_RESOURCE_MANAGER_GLOSS"></span>**Compensating Resource Manager (CRM)**
</dt> <dd>

A COM+ feature that enables non-transactional resources to participate in a two-phase commit transaction with the Microsoft Distributed Transaction Coordinator (DTC). Typically, CRMs do not provide the isolation capabilities of full resource managers, but they do provide transactional atomicity and durability by writing to a log.

</dd> <dt>

<span id="cos.component_services_administrative_tool_gloss"></span><span id="COS.COMPONENT_SERVICES_ADMINISTRATIVE_TOOL_GLOSS"></span>**Component Services administrative tool**
</dt> <dd>

A user-interface snap-in through which administrators and developers can create, configure, and maintain COM+ applications, as well as administer distributed transactions and memory-resident databases. The Component Services administrative tool can also be used to view system events and manage system services local to the computer on which the tool is installed.

</dd> <dt>

<span id="cos.conceptual_model_gloss"></span><span id="COS.CONCEPTUAL_MODEL_GLOSS"></span>**conceptual model**
</dt> <dd>

The first step in the COM+ application design phase, where the developer defines the business problems to be solved and decides what components and services are required.

</dd> <dt>

<span id="cos.concurrency_gloss"></span><span id="COS.CONCURRENCY_GLOSS"></span>**concurrency**
</dt> <dd>

The ability of more than one transaction or process to access the same data at the same time. COM+ generally manages concurrency through synchronization.

</dd> <dt>

<span id="cos.configured_component_gloss"></span><span id="COS.CONFIGURED_COMPONENT_GLOSS"></span>**configured component**
</dt> <dd>

A COM component that has been installed into a COM+ application. After it is installed, the component is configured within the COM+ catalog to make use of the available COM+ services.

</dd> <dt>

<span id="cos.context_gloss"></span><span id="COS.CONTEXT_GLOSS"></span>**context**
</dt> <dd>

A set of run-time properties associated with one or more COM objects that are used to provide services for those objects. Every COM object runs in a single context from activation to deactivation (always within the same apartment). Initialized when an object is activated, context properties, such as security context properties, represent the run-time needs of an object.

</dd> <dt>

<span id="cos.data_tier_gloss"></span><span id="COS.DATA_TIER_GLOSS"></span>**data tier**
</dt> <dd>

In the three-tier architecture model for business applications, the DBMS access layer, which can be accessed through the middle tier, or business services layer, and on occasion through the presentation tier, or user services layer. The data tier consists of data access components (rather than raw DBMS connections) to aid in resource sharing and to allow clients to be configured without installing the DBMS libraries and ODBC drivers on each client. Also called *data services layer*.

</dd> <dt>

<span id="cos.deadlock_gloss"></span><span id="COS.DEADLOCK_GLOSS"></span>**deadlock**
</dt> <dd>

In multithreaded applications, a threading problem that occurs when each member of a set of threads is waiting for another member of the set.

</dd> <dt>

<span id="cos.delegation_gloss"></span><span id="COS.DELEGATION_GLOSS"></span>**delegation**
</dt> <dd>

A form of impersonation that authorizes a server to act on a client's behalf, giving the server the ability to impersonate clients over the network.

</dd> <dt>

<span id="cos.distributed_transaction_gloss"></span><span id="COS.DISTRIBUTED_TRANSACTION_GLOSS"></span>**distributed transaction**
</dt> <dd>

A transaction that involves multiple resource managers, which can be on the same or different computers.

</dd> <dt>

<span id="cos.distributed_transaction_coordinator_gloss"></span><span id="COS.DISTRIBUTED_TRANSACTION_COORDINATOR_GLOSS"></span>**Distributed Transaction Coordinator (DTC)**
</dt> <dd>

A system service that manages transactions and transaction-related communications that are distributed across two or more resource managers on one or more systems to ensure correct ACID transactions.

</dd> <dt>

<span id="cos.dynamic_cloaking_gloss"></span><span id="COS.DYNAMIC_CLOAKING_GLOSS"></span>**dynamic cloaking**
</dt> <dd>

A form of cloaking where the original client identity is discovered as the server thread access token on each method call to the downstream server. Although the identity that is presented can be determined dynamically, the overhead required to do this can be considerably more expensive. For COM+ applications, the default configuration is for dynamic cloaking capability because it provides the flexibility that is usually required by circumstances that necessitate using impersonation in the first place.

</dd> <dt>

<span id="cos.enumerator_object_gloss"></span><span id="COS.ENUMERATOR_OBJECT_GLOSS"></span>**enumerator object**
</dt> <dd>

Enables enumeration of items in a collection.

</dd> <dt>

<span id="cos.event_gloss"></span><span id="COS.EVENT_GLOSS"></span>**event**
</dt> <dd>

An action recognized by an object, such as clicking the mouse or pressing a key, and for which you can write code to respond.

</dd> <dt>

<span id="cos.event_class_object_gloss"></span><span id="COS.EVENT_CLASS_OBJECT_GLOSS"></span>**event class object**
</dt> <dd>

A configured component that provides a persistent record in the COM+ event system to describe the publishers and the firing interfaces associated with those publishers.

</dd> <dt>

<span id="cos.event_method_gloss"></span><span id="COS.EVENT_METHOD_GLOSS"></span>**event method**
</dt> <dd>

A method in a COM+ interface that identifies a COM+ event. Event methods must be uniquely named and can contain only input parameters. The return value must be an **HRESULT**.

</dd> <dt>

<span id="cos.event_object_gloss"></span><span id="COS.EVENT_OBJECT_GLOSS"></span>**event object**
</dt> <dd>

A COM object that can signal one or more threads that an event has occurred. Any thread within a process can create an event object.

</dd> <dt>

<span id="cos.exception_gloss"></span><span id="COS.EXCEPTION_GLOSS"></span>**exception**
</dt> <dd>

An abnormal condition or error that occurs during the execution of a program and that requires the execution of software outside the normal flow of control.

</dd> <dt>

<span id="cos.failover_gloss"></span><span id="COS.FAILOVER_GLOSS"></span>**failover**
</dt> <dd>

In a cluster network system, the process of relocating an overloaded or failed resource—such as a server, a disk drive, or a network—to its backup component.

</dd> <dt>

<span id="cos.free_threaded_process_gloss"></span><span id="COS.FREE_THREADED_PROCESS_GLOSS"></span>**free-threaded process**
</dt> <dd>

A process that has a multithreaded apartment and no single-threaded apartments.

</dd> <dt>

<span id="cos.global_commit_coordinator_gloss"></span><span id="COS.GLOBAL_COMMIT_COORDINATOR_GLOSS"></span>**global commit coordinator**
</dt> <dd>

On a Microsoft Windows–based distributed transaction system, the root transaction manager of the commit tree. This coordinator makes the decision to either commit or abort a given transaction and is never in doubt.

</dd> <dt>

<span id="cos.impersonation_gloss"></span><span id="COS.IMPERSONATION_GLOSS"></span>**impersonation**
</dt> <dd>

The ability of a thread to execute in a security context different from that of the process owning the thread. The server thread uses an access token representing the client's credentials, and with this, it can access resources that the client can access.

</dd> <dt>

<span id="cos.impersonation_level_gloss"></span><span id="COS.IMPERSONATION_LEVEL_GLOSS"></span>**impersonation level**
</dt> <dd>

The setting used by the client to grant the server a particular level of authority to carry out actions on the client's behalf. In COM+, this can be set only for COM+ server applications.

</dd> <dt>

<span id="cos.interception_gloss"></span><span id="COS.INTERCEPTION_GLOSS"></span>**interception**
</dt> <dd>

For an object activated in a given context, the process of handling calls to that object from across the context boundary. Calls across context are handled with lightweight interface proxies that will handle whatever mediation is required to adjust the run-time environment from one that accommodates the caller to one that accommodates the callee.

</dd> <dt>

<span id="cos.interface_gloss"></span><span id="COS.INTERFACE_GLOSS"></span>**interface**
</dt> <dd>

In COM-based programming, a collection of related public functions that provide access to a COM object. The set of interfaces on a COM object composes a contract that specifies how programs and other objects can interact with the COM object.

</dd> <dt>

<span id="cos.interface_proxy_gloss"></span><span id="COS.INTERFACE_PROXY_GLOSS"></span>**interface proxy**
</dt> <dd>

An interface-specific object that packages (marshals) parameters for that interface in preparation for a remote method call and unpackages (unmarshals) the return values from the interface stub. A proxy runs in the address space of the sender and communicates with a corresponding stub in the receiver's address space.

</dd> <dt>

<span id="cos.interface_stub_gloss"></span><span id="COS.INTERFACE_STUB_GLOSS"></span>**interface stub**
</dt> <dd>

An interface-specific object that unpackages marshaled parameters, calls the required method, and packages (marshals) return values from the called method. The stub runs in the receiver's address space and communicates with a corresponding interface proxy in the sender's address space.

</dd> <dt>

<span id="cos.interior_object_gloss"></span><span id="COS.INTERIOR_OBJECT_GLOSS"></span>**interior object**
</dt> <dd>

In a transactional hierarchy, any object under the root object.

</dd> <dt>

<span id="cos.just_in_time_activation_gloss"></span><span id="COS.JUST_IN_TIME_ACTIVATION_GLOSS"></span>**just-in-time (JIT) activation**
</dt> <dd>

An automatic service provided by COM+ that allows idle server resources to be used more productively. When a component is configured as JIT activated, COM+ can deactivate an instance of it while a client still holds an active reference to the object. The next time the client calls a method on the object, COM+ will reactivate the object transparently to the client, just in time.

</dd> <dt>

<span id="cos.legacy_component_gloss"></span><span id="COS.LEGACY_COMPONENT_GLOSS"></span>**legacy component**
</dt> <dd>

An unconfigured component that has been installed into a COM+ application.

</dd> <dt>

<span id="cos.listener_gloss"></span><span id="COS.LISTENER_GLOSS"></span>**listener**
</dt> <dd>

An architectural element of the COM+ Queued Components service. The listener is a COM object that opens the message queue associated with its host application and waits for messages to arrive. As messages arrive, the listener dispatches threads that process messages.

</dd> <dt>

<span id="cos.logical_model_gloss"></span><span id="COS.LOGICAL_MODEL_GLOSS"></span>**logical model**
</dt> <dd>

The second step in a COM+ application design process, where the conceptual model is broken out into the logical tiers of the three-tier architecture, as follows: the presentation tier, or user services; the middle tier, or business services; and the data tier, or data services.

</dd> <dt>

<span id="cos.loosely_couple_event_gloss"></span><span id="COS.LOOSELY_COUPLE_EVENT_GLOSS"></span>**loosely coupled event**
</dt> <dd>

An event whose sender (publisher) and receiver (subscriber) are not closely bound. In a loosely coupled event system, such as COM+ Events, event information from different publishers is persisted in an event store. Subscribers query this store and select the events that they want to receive. Selecting event information from the event store creates a subscription. When an event occurs, the event system looks in this database and finds the interested subscribers, creates a new object of each interested class, and calls a method on that object.

</dd> <dt>

<span id="cos.marshaling_gloss"></span><span id="COS.MARSHALING_GLOSS"></span>**marshaling**
</dt> <dd>

The process of packaging and unpackaging interface method parameters across thread or process boundaries so that a remote procedure call can take place.

</dd> <dt>

<span id="cos.message_mover_gloss"></span><span id="COS.MESSAGE_MOVER_GLOSS"></span>**message mover**
</dt> <dd>

The architectural element of the COM+ Queued Components service that moves failed messages back to their input queue so that they can be retried.

</dd> <dt>

<span id="cos.meta_event_gloss"></span><span id="COS.META_EVENT_GLOSS"></span>**meta-event**
</dt> <dd>

A type of event used by the COM+ Events system to notify interested subscribers whenever event class objects or subscriptions are created, modified, or removed.

</dd> <dt>

<span id="cos.method_gloss"></span><span id="COS.METHOD_GLOSS"></span>**method**
</dt> <dd>

In COM-based programming, a process performed by a COM object when it receives a message.

</dd> <dt>

<span id="cos.middle_tier_gloss"></span><span id="COS.MIDDLE_TIER_GLOSS"></span>**middle tier**
</dt> <dd>

In the three-tier architecture model for business applications, the layer comprising the business logic and data rules. The components that make up the middle tier can be used to enforce business rules, such as business algorithms, legal or governmental regulations, and data rules, which are designed to keep the data structures consistent within either specific or multiple databases. Because these middle-tier components are not tied to a specific client, they can be used by all applications and can be moved to different locations as response time and other rules require. Also called *business services layer* or *business logic tier*.

</dd> <dt>

<span id="cos.mixed_model_process_gloss"></span><span id="COS.MIXED_MODEL_PROCESS_GLOSS"></span>**mixed model process**
</dt> <dd>

A process that has a multithreaded apartment and one or more single-threaded apartments.

</dd> <dt>

<span id="cos.moniker_gloss"></span><span id="COS.MONIKER_GLOSS"></span>**moniker**
</dt> <dd>

A name that uniquely identifies a COM object. In the same way that a path identifies a file in the file system, a moniker identifies a COM object in the directory namespace.

</dd> <dt>

<span id="cos.msi_file_gloss"></span><span id="COS.MSI_FILE_GLOSS"></span>**.msi file**
</dt> <dd>

A file created by the Component Services administrative tool when you export a COM+ application or application proxy for installation on another computer. The .msi file can be installed on any Windows-based client using Windows Installer.

</dd> <dt>

<span id="cos.multithreaded_apartment_model_gloss"></span><span id="COS.MULTITHREADED_APARTMENT_MODEL_GLOSS"></span>**multithreaded apartment model**
</dt> <dd>

An apartment model in which all the threads in the process that have been initialized as free-threaded reside in a single apartment. Therefore, there is no need to marshal between threads. The threads need not retrieve and dispatch messages because COM does not use window messages in this model.

</dd> <dt>

<span id="cos.nested_transaction_gloss"></span><span id="COS.NESTED_TRANSACTION_GLOSS"></span>**nested transaction**
</dt> <dd>

A secondary transaction initiated from within an existing primary or parent transaction boundary. The primary transaction does not commit until all of its subordinate, or nested, transactions commit. COM+ does not support nested transactions.

</dd> <dt>

<span id="cos.neutral_apartment_model_gloss"></span><span id="COS.NEUTRAL_APARTMENT_MODEL_GLOSS"></span>**neutral apartment model**
</dt> <dd>

A threading model in which objects follow the guidelines for multithreaded apartments but can execute on any kind of thread. The neutral apartment model is the recommended threading model for COM components and COM+ applications.

</dd> <dt>

<span id="cos.persistent_object_gloss"></span><span id="COS.PERSISTENT_OBJECT_GLOSS"></span>**persistent object**
</dt> <dd>

A COM object that can save its internal state when asked to do so by a client and that conforms to COM-defined standards through which clients can request objects to be initialized, loaded, and saved to and from a data store (for example, flat file, structured storage, or memory). It is the client's responsibility to manage the location where the object's persistent data is stored but not the format of the data.

</dd> <dt>

<span id="cos.persistent_object_interface_gloss"></span><span id="COS.PERSISTENT_OBJECT_INTERFACE_GLOSS"></span>**persistent object interface**
</dt> <dd>

A COM interface implemented by a persistent object. Clients use persistent object interfaces to tell those persistent objects when and where to store their state.

</dd> <dt>

<span id="cos.phase_zero_notification_interface_gloss"></span><span id="COS.PHASE_ZERO_NOTIFICATION_INTERFACE_GLOSS"></span>**phase zero notification interface**
</dt> <dd>

COM+ interface that allows applications to detect when a transaction is ready to proceed with a two-phase commit protocol so that it can perform the necessary notification operations and communicate to the transaction manager when the operations have been completed.

</dd> <dt>

<span id="cos.physical_model_gloss"></span><span id="COS.PHYSICAL_MODEL_GLOSS"></span>**physical model**
</dt> <dd>

The third and final step in the COM+ application design process, where the developer determines where the components reside physically and how they are to be coded.

</dd> <dt>

<span id="cos.player_gloss"></span><span id="COS.PLAYER_GLOSS"></span>**player**
</dt> <dd>

The architectural element of the COM+ Queued Components service that retrieves the message from a queue and then loads the server object and the standard interface stubs to unmarshal data and invoke server methods. The player unmarshals the client's security context at the server side and then invokes the server component and makes the same method calls. The method calls are not played back by the player until the client component completes and the transaction that recorded the method calls commits.

</dd> <dt>

<span id="cos.presentation_tier_gloss"></span><span id="COS.PRESENTATION_TIER_GLOSS"></span>**presentation tier**
</dt> <dd>

In the three-tier architecture model for business applications, the layer that presents data to the user and optionally permits data manipulation and data entry. The two main types of user interface for the presentation tier are the traditional application and the Web-based application. Also called *user services layer*.

</dd> <dt>

<span id="cos.primary_access_token_gloss"></span><span id="COS.PRIMARY_ACCESS_TOKEN_GLOSS"></span>**primary access token**
</dt> <dd>

Describes the security context of the user account associated with a process.

</dd> <dt>

<span id="cos.proxy_manager_gloss"></span><span id="COS.PROXY_MANAGER_GLOSS"></span>**proxy manager**
</dt> <dd>

In standard marshaling, a component that manages all the interface proxies for a single object.

</dd> <dt>

<span id="cos.pseudo_object_gloss"></span><span id="COS.PSEUDO_OBJECT_GLOSS"></span>**pseudo-object**
</dt> <dd>

A type of contained object, such as a user selection in a document, a range of cells in a spreadsheet, or a range of characters in a text document. This type of object is called a pseudo-object because it isn't treated as a distinct object until a user marks the selection.

</dd> <dt>

<span id="cos.publisher_gloss"></span><span id="COS.PUBLISHER_GLOSS"></span>**publisher**
</dt> <dd>

The sender of an event. In the COM+ Events architecture, the publisher makes the method call to initiate an event.

</dd> <dt>

<span id="cos.queue_moniker_gloss"></span><span id="COS.QUEUE_MONIKER_GLOSS"></span>**queue moniker**
</dt> <dd>

The moniker used to activate a queued component.

</dd> <dt>

<span id="cos.race_condition_gloss"></span><span id="COS.RACE_CONDITION_GLOSS"></span>**race condition**
</dt> <dd>

In a multithreaded application, a condition that occurs when multiple threads access a data item without coordination, possibly causing inconsistent results, depending on which thread reaches the data item first. COM supplies some functions specifically designed to help avoid race conditions in out-of-process servers.

</dd> <dt>

<span id="cos.recorder_gloss"></span><span id="COS.RECORDER_GLOSS"></span>**recorder**
</dt> <dd>

The architectural element of the COM+ Queued Components service that marshals the client's security context into a message and records all of the method calls for an object. The recorder is a system-provided proxy manager that selects interfaces from the queuable interfaces in the COM+ catalog.

</dd> <dt>

<span id="cos.resource_dispenser_gloss"></span><span id="COS.RESOURCE_DISPENSER_GLOSS"></span>**resource dispenser**
</dt> <dd>

In the COM+ programming model, a component that manages nondurable shared state on behalf of the application components within a process. Resource dispensers are similar to resource managers but without the guarantee of durability.

</dd> <dt>

<span id="cos.resource_manager_gloss"></span><span id="COS.RESOURCE_MANAGER_GLOSS"></span>**resource manager**
</dt> <dd>

A service that manages persistent or durable data in databases, durable message queues, or transactional file systems. It is the resource manager that knows how to store data and perform disaster recovery. COM+ server applications use resource managers to maintain the durable state of an application, such as the record of inventory on hand, pending orders, and accounts receivable. Resource managers work in cooperation with the Microsoft Distributed Transaction Coordinator (DTC) to guarantee atomicity and isolation to an application.

</dd> <dt>

<span id="cos.role_baed_security_gloss"></span><span id="COS.ROLE_BAED_SECURITY_GLOSS"></span>**role-based security**
</dt> <dd>

A COM+ security service provided for COM+ applications. A role represents a category of users defined for a COM+ application for the purpose of determining access permissions to the application's resources. Roles are assigned by a developer to components, interfaces, and methods. Users are assigned by an administrator to appropriate roles, enabling a user within a given role to access any resources to which that role is assigned.

</dd> <dt>

<span id="cos.root_object_gloss"></span><span id="COS.ROOT_OBJECT_GLOSS"></span>**root object**
</dt> <dd>

The first object of a transaction, called the root of the transaction, and always placed in a new transactional boundary. There can be only one root object in a transaction. All other objects in the transactional hierarchy under the root object are called interior objects.

</dd> <dt>

<span id="cos.root_transaction_manager_gloss"></span><span id="COS.ROOT_TRANSACTION_MANAGER_GLOSS"></span>**root transaction manager**
</dt> <dd>

The transaction manager on the system that initiates a transaction. The transaction is not finalized until the root transaction manager determines the transaction's status (either committed or aborted).

</dd> <dt>

<span id="cos.semaphore_gloss"></span><span id="COS.SEMAPHORE_GLOSS"></span>**semaphore**
</dt> <dd>

A kernel object used to arbitrate access to a shared resource.

</dd> <dt>

<span id="cos.service_control_manager_gloss"></span><span id="COS.SERVICE_CONTROL_MANAGER_GLOSS"></span>**service control manager (SCM)**
</dt> <dd>

A Microsoft Windows server process that manages all the services in the Windows registry.

</dd> <dt>

<span id="cos.shared_property_manager_gloss"></span><span id="COS.SHARED_PROPERTY_MANAGER_GLOSS"></span>**shared property manager (SPM)**
</dt> <dd>

In Com+, a resource dispenser that you can use to share nonpersistent state among multiple objects within a server process.

</dd> <dt>

<span id="cos.single_threaded_process_gloss"></span><span id="COS.SINGLE_THREADED_PROCESS_GLOSS"></span>**single-threaded process**
</dt> <dd>

A process that consists of just one single-threaded apartment, which in turn consists of exactly one thread. All COM objects that live in a single-threaded apartment can receive method calls from only the one thread that belongs to that apartment.

</dd> <dt>

<span id="cos.soap_gloss"></span><span id="COS.SOAP_GLOSS"></span>**SOAP**
</dt> <dd>

A simple, XML-based protocol for exchanging structured and type information on the Web. The protocol contains no application or transport semantics, which makes it highly modular and extensible.

</dd> <dt>

<span id="cos.split_registration_gloss"></span><span id="COS.SPLIT_REGISTRATION_GLOSS"></span>**split registration**
</dt> <dd>

For components that are already existing COM components and are used in the COM+ services environment, the registration arrangement in which the basic COM aspect of the registration is stored in the Windows registry and new COM+ services and attributes (for example, Queued Components) are stored in the COM+ Registration Database. Each component attribute is stored in either the Windows registry or the COM+ Registration Database. New COM components are registered exclusively in the COM+ Registration Database, with some duplication in the Windows registry so that existing tools can use them.

</dd> <dt>

<span id="cos.stateful_gloss"></span><span id="COS.STATEFUL_GLOSS"></span>**stateful**
</dt> <dd>

Of or pertaining to a system or process that monitors all details of the state of an activity in which it participates.

</dd> <dt>

<span id="cos.stateless_gloss"></span><span id="COS.STATELESS_GLOSS"></span>**stateless**
</dt> <dd>

Of or pertaining to a system or process that participates in activity without monitoring all details of its state.

</dd> <dt>

<span id="cos.static_cloaking_gloss"></span><span id="COS.STATIC_CLOAKING_GLOSS"></span>**static cloaking**
</dt> <dd>

A form of cloaking where the original client identity can be presented once to a downstream server, setting the original client identity once on the proxy. This client identity is presented as a server thread token that will be used on subsequent method calls.

</dd> <dt>

<span id="cos.subscriber_gloss"></span><span id="COS.SUBSCRIBER_GLOSS"></span>**subscriber**
</dt> <dd>

The receiver of an event. In the COM+ Events architecture, the subscriber receives the calls made by the publisher.

</dd> <dt>

<span id="cos.subscription_object_gloss"></span><span id="COS.SUBSCRIPTION_OBJECT_GLOSS"></span>**subscription object**
</dt> <dd>

In the COM+ Events system, an object created by a subscriber to request and manage the delivery of events.

</dd> <dt>

<span id="cos.synchronization_gloss"></span><span id="COS.SYNCHRONIZATION_GLOSS"></span>**synchronization**
</dt> <dd>

In COM+, a service that flows from component to component and prohibits more than one caller from entering the component at any given time. Synchronization determines when threads can dispatch calls to an object.

</dd> <dt>

<span id="cos.three_tier_architectural_model_gloss"></span><span id="COS.THREE_TIER_ARCHITECTURAL_MODEL_GLOSS"></span>**three-tier architectural model**
</dt> <dd>

The fundamental framework for the logical design model, segments an application's components into three tiers of services as follows: the presentation tier, or user services; the middle tier, or business services; and the data tier, or data services. These tiers do not necessarily correspond to physical locations on various computers on a network, but rather to logical layers of the application.

</dd> <dt>

<span id="cos.tightly_couple_event_gloss"></span><span id="COS.TIGHTLY_COUPLE_EVENT_GLOSS"></span>**tightly coupled event**
</dt> <dd>

An event whose sender (publisher) and receiver (subscriber) are closely bound. In a tightly coupled event system, the publisher is provided with an interface on which to call a method when a change occurs. The subscriber knows which publisher to request notification from and the interfaces that are exposed. A tightly coupled event system requires that both the publisher and the subscriber are running at all times.

</dd> <dt>

<span id="cos.trace_log_gloss"></span><span id="COS.TRACE_LOG_GLOSS"></span>**trace log**
</dt> <dd>

A log file automatically generated by the Microsoft Distributed Transaction Coordinator that shows data related to one or more distributed transactions. Examples of data in a trace log are transaction ID, transaction time, and messages indicating the transaction outcome.

</dd> <dt>

<span id="cos.transaction_gloss"></span><span id="COS.TRANSACTION_GLOSS"></span>**transaction**
</dt> <dd>

A unit of work in which a series of related operations occur during an application process. A transaction executes exactly once and is atomic—either all of the work is done or none of it is.

</dd> <dt>

<span id="cos.transaction_internet_protocol_gloss"></span><span id="COS.TRANSACTION_INTERNET_PROTOCOL_GLOSS"></span>**Transaction Internet Protocol (TIP)**
</dt> <dd>

Transaction Internet Protocol is a standard two-phase commit protocol that enables heterogeneous transaction managers to coordinate distributed transactions, especially over the Internet. The TIP two-phase commit protocol is simple to implement and is independent of the application-to-application communications protocol, such that it may be used with any application protocol but especially HTTP.

</dd> <dt>

<span id="cos.transaction_manager_gloss"></span><span id="COS.TRANSACTION_MANAGER_GLOSS"></span>**transaction manager**
</dt> <dd>

The part of the Microsoft Distributed Transaction Coordinator (DTC) that executes on each computer participating in a distributed transaction and manages the activities related to committing or aborting that part of the transaction.

</dd> <dt>

<span id="cos.transaction_processing_application_gloss"></span><span id="COS.TRANSACTION_PROCESSING_APPLICATION_GLOSS"></span>**transaction processing application**
</dt> <dd>

A collection of transaction operations that automate a given business task.

</dd> <dt>

<span id="cos.transaction_processing_system_gloss"></span><span id="COS.TRANSACTION_PROCESSING_SYSTEM_GLOSS"></span>**transaction processing system**
</dt> <dd>

A complete system, comprising both computer hardware and software, that hosts a transaction processing application to perform routine transactions necessary to conduct business.

</dd> <dt>

<span id="cos.two_phase_commit_protocol_gloss"></span><span id="COS.TWO_PHASE_COMMIT_PROTOCOL_GLOSS"></span>**two-phase commit protocol**
</dt> <dd>

A protocol used only in distributed transactions, ensures that the outcome of a transaction is consistent across all transaction managers participating in the transaction. The protocol operates in two distinct phases to ultimately commit or abort a transaction: phase one evaluates the condition of each resource manager, and phase two completes the transaction.

</dd> <dt>

<span id="cos.unconfigured_component_gloss"></span><span id="COS.UNCONFIGURED_COMPONENT_GLOSS"></span>**unconfigured component**
</dt> <dd>

A COM component that has not been configured within the COM+ catalog. Unconfigured components cannot make use of COM+ services.

</dd> <dt>

<span id="cos.whereabouts_gloss"></span><span id="COS.WHEREABOUTS_GLOSS"></span>**whereabouts**
</dt> <dd>

For DTC transactions, an opaque data structure that represents the address of the resource manager's transaction manager.

</dd> <dt>

<span id="cos.xa_interfaces_gloss"></span><span id="COS.XA_INTERFACES_GLOSS"></span>**XA interfaces**
</dt> <dd>

A standard set of programming interfaces that allow COM+ application developers to access XA-compliant databases and create resource managers that operate with relational databases, message queuing, transactional files, and object-oriented databases. Although Microsoft does not directly support the XA protocol, Microsoft does support translation facilities between OLE transactions and XA.

</dd> <dt>

<span id="cos.xml_web_services_gloss"></span><span id="COS.XML_WEB_SERVICES_GLOSS"></span>**XML web services**
</dt> <dd>

Units of application logic providing data and services to other applications. Applications access XML web services through standard Web protocols, such as SOAP.

</dd> </dl>

 

 
