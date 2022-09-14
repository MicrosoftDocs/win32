---
description: Contains an object for each component in the related application.
ms.assetid: f502ba60-b2b1-4556-8f91-22a474e60e0d
title: Components collection
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Components
api_type: 
- COM
api_location: 
---

# Components collection

Contains an object for each component in the related application. The **Components** collection is always related to an object in the [**Applications**](applications.md) collection. The properties exposed by these objects hold settings made at the component level.

This collection supports the [**Remove**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-remove) method of the [**COMAdminCatalogCollection**](comadmincatalogcollection.md) object, but not the [**Add**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-add) method. To install or import components into an application, use methods on the [**COMAdminCatalog**](comadmincatalog.md) object.

## Members

The **Components** collection inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**ErrorInfo**](errorinfo.md)
-   [**InterfacesForComponent**](interfacesforcomponent.md)
-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)
-   [**RolesForComponent**](rolesforcomponent.md)
-   [**SubscriptionsForComponent**](subscriptionsforcomponent.md)

You can navigate to this collection from the following collections:

-   [**Applications**](applications.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](comadmincatalogobject.md) object within the collection:

-   [AllowInprocSubscribers](#allowinprocsubscribers)
-   [ApplicationID](#applicationid)
-   [Bitness](#bitness)
-   [CLSID](#multiinterfacepublisherfilterclsid)
-   [ComponentAccessChecksEnabled](#componentaccesschecksenabled)
-   [ComponentTransactionTimeout](#componenttransactiontimeoutenabled)
-   [ComponentTransactionTimeoutEnabled](#componenttransactiontimeoutenabled)
-   [COMTIIntrinsics](#comtiintrinsics)
-   [ConstructionEnabled](#constructionenabled)
-   [ConstructorString](#constructorstring)
-   [CreationTimeout](#creationtimeout)
-   [Description](#description)
-   [DLL](#dll)
-   [EventTrackingEnabled](#eventtrackingenabled)
-   [ExceptionClass](#exceptionclass)
-   [FireInParallel](#fireinparallel)
-   [IISIntrinsics](#iisintrinsics)
-   [InitializeServerApplication](#initializeserverapplication)
-   [IsEnabled](#isenabled)
-   [IsEventClass](#iseventclass)
-   [IsInstalled](#isinstalled)
-   [IsPrivateComponent](#isprivatecomponent)
-   [JustInTimeActivation](#justintimeactivation)
-   [LoadBalancingSupported](#loadbalancingsupported)
-   [MaxPoolSize](#maxpoolsize)
-   [MinPoolSize](#minpoolsize)
-   [MultiInterfacePublisherFilterCLSID](#multiinterfacepublisherfilterclsid)
-   [MustRunInClientContext](#mustruninclientcontext)
-   [MustRunInDefaultContext](#mustrunindefaultcontext)
-   [ObjectPoolingEnabled](#objectpoolingenabled)
-   [ProgID](#progid)
-   [PublisherID](#publisherid)
-   [SoapAssemblyName](#soapassemblyname)
-   [SoapTypeName](#soaptypename)
-   [Synchronization](#synchronization)
-   [ThreadingModel](#threadingmodel)
-   [Transaction](#componenttransactiontimeout)
-   [TxIsolationLevel](#txisolationlevel)
-   [VersionBuild](#versionbuild)
-   [VersionMajor](#versionmajor)
-   [VersionMinor](#versionminor)
-   [VersionSubBuild](#versionsubbuild)

### AllowInprocSubscribers



| Entry | Value |
|----------------|--------------------------------------------------------------------|
| Description    | Enables in process subscribers if the component is an event class. |
| Access         | ReadWrite                                                          |
| Type           | Bool                                                               |
| Default        | True                                                               |
| Minimum system | Windows 2000                                                       |



 

### ApplicationID



| Entry | Value |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The GUID for the application containing the component. Must be a valid application's GUID, which is verified before [**SaveChanges**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-savechanges) is called. If this value is changed to be a GUID for a different application, the component moves to that application. |
| Access         | ReadWrite                                                                                                                                                                                                                                                                                        |
| Type           | String                                                                                                                                                                                                                                                                                           |
| Default        | N/A                                                                                                                                                                                                                                                                                              |
| Minimum system | Windows 2000                                                                                                                                                                                                                                                                                     |



 

### Bitness



| Entry | Value |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Represents the binary bitness type of a component. On systems that use 64-bit Windows, this property distinguishes between 64-bit components and 32-bit components. |
| Access         | ReadOnly                                                                                                                                                            |
| Type           | Long Possible values:COMAdmin32BitComponent (0x1)COMAdmin64BitComponent (0x2)                                                                                       |
| Default        | N/A                                                                                                                                                                 |
| Minimum system | Windows XP                                                                                                                                                          |



 

### CLSID



| Entry | Value |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | A GUID for the component. This property is returned when the [**Key**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_key) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                                  |
| Type           | String                                                                                                                                                    |
| Default        | N/A                                                                                                                                                       |
| Minimum system | Windows 2000                                                                                                                                              |



 

### ComponentAccessChecksEnabled



| Entry | Value |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Indicates whether role-based access checks are performed on calls into the component and works in conjunction with the AccessChecksLevel and ApplicationAccessChecksEnabled properties on the application. |
| Access         | ReadWrite                                                                                                                                                                                                  |
| Type           | Bool                                                                                                                                                                                                       |
| Default        | False                                                                                                                                                                                                      |
| Minimum system | Windows 2000                                                                                                                                                                                               |



 

### ComponentTransactionTimeout



| Entry | Value |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | When used in a transaction, specifies the time period in which this component causes the transaction to time out. The default is 60 seconds and cannot be longer than 3600 seconds (1 hour). The time-out value can be set to 0, specifying an infinite transaction time-out period. For this property to be used, ComponentTransactionTimeoutEnabled must be True. The value of this property overrides the global transaction time-out specified by the TransactionTimeout property of the [**LocalComputer**](localcomputer.md) collection. |
| Access         | ReadWrite                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Type           | Long (0-3600)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Default        | 60                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Minimum system | Windows 2000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |



 

### ComponentTransactionTimeoutEnabled



| Entry | Value |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Specifies whether the transaction time-out period is enabled for this component. By default, the transaction time-out feature is disabled. When this property is True, the time-out specified by ComponentTransactionTimeout is used. When this property is False, the time-out specified by the TransactionTimeout property of the [**LocalComputer**](localcomputer.md) collection is used. |
| Access         | ReadWrite                                                                                                                                                                                                                                                                                                                                                                                      |
| Type           | Bool                                                                                                                                                                                                                                                                                                                                                                                           |
| Default        | False                                                                                                                                                                                                                                                                                                                                                                                          |
| Minimum system | Windows 2000                                                                                                                                                                                                                                                                                                                                                                                   |



 

### COMTIIntrinsics



| Entry | Value |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Enables passing of context properties from the COM Transaction Integrator (COMTI) into the context for this class. The COMTI eases the task of wrapping mainframe transactions and business logic as COM components. |
| Access         | ReadWrite                                                                                                                                                                                                            |
| Type           | Bool                                                                                                                                                                                                                 |
| Default        | False                                                                                                                                                                                                                |
| Minimum system | Windows 2000                                                                                                                                                                                                         |



 

### ConstructionEnabled



| Entry | Value |
|----------------|------------------------------------------------------------------------------------------|
| Description    | Determines whether the ConstructorString is passed to the object when it is constructed. |
| Access         | ReadWrite                                                                                |
| Type           | Bool                                                                                     |
| Default        | False                                                                                    |
| Minimum system | Windows 2000                                                                             |



 

### ConstructorString



| Entry | Value |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Initialization string for component construction. You can create different objects from the same generic component by using object constructor strings. If ConstructionEnabled is False, this property is ignored. |
| Access         | ReadWrite                                                                                                                                                                                                          |
| Type           | String                                                                                                                                                                                                             |
| Default        | ""                                                                                                                                                                                                                 |
| Minimum system | Windows 2000                                                                                                                                                                                                       |



 

### CreationTimeout



| Entry | Value |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | When creating the object, number of milliseconds before a time-out error is returned. The maximum time-out is 2147483647 milliseconds (about 25 days). |
| Access         | ReadWrite                                                                                                                                              |
| Type           | Long (0-2147483647)                                                                                                                                    |
| Default        | 0                                                                                                                                                      |
| Minimum system | Windows 2000                                                                                                                                           |



 

### Description



| Entry | Value |
|----------------|--------------------------|
| Description    | Describes the component. |
| Access         | ReadWrite                |
| Type           | String                   |
| Default        | ""                       |
| Minimum system | Windows 2000             |



 

### DLL



| Entry | Value |
|----------------|---------------------------------------------------------|
| Description    | The name and path of the file containing the component. |
| Access         | ReadOnly                                                |
| Type           | String                                                  |
| Default        | N/A                                                     |
| Minimum system | Windows 2000                                            |



 

### EventTrackingEnabled



| Entry | Value |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Determines whether events are tracked. Events include actions such as application shutdown; object creation and release; object references, consistency, activation, and deactivation; method calls, returns, and exceptions; transaction startup, preparing to commit, and abort; resource dispenser connection, allocation, and recycling; thread allocation and recycling. |
| Access         | ReadWrite                                                                                                                                                                                                                                                                                                                                                                     |
| Type           | Bool                                                                                                                                                                                                                                                                                                                                                                          |
| Default        | True                                                                                                                                                                                                                                                                                                                                                                          |
| Minimum system | Windows 2000                                                                                                                                                                                                                                                                                                                                                                  |



 

### ExceptionClass



| Entry | Value |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The CLSID, which can be a GUID or a moniker string, to activate an alternative program during the process of dealing with a repeatedly failing queued components program. |
| Access         | ReadWrite                                                                                                                                                                 |
| Type           | String                                                                                                                                                                    |
| Default        | ""                                                                                                                                                                        |
| Minimum system | Windows 2000                                                                                                                                                              |



 

### FireInParallel



| Entry | Value |
|----------------|----------------------------------------------------------------------------|
| Description    | Enables events to be fired in parallel if the component is an event class. |
| Access         | ReadWrite                                                                  |
| Type           | Bool                                                                       |
| Default        | False                                                                      |
| Minimum system | Windows 2000                                                               |



 

### IISIntrinsics



| Entry | Value |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Enables passing of IIS context properties, such as an application session object or a user session object, into the context for this class. |
| Access         | ReadWrite                                                                                                                                   |
| Type           | Bool                                                                                                                                        |
| Default        | False                                                                                                                                       |
| Minimum system | Windows 2000                                                                                                                                |



 

### InitializeServerApplication



| Entry | Value |
|----------------|-----------------------------------------------------------------------------|
| Description    | Indicates whether the component is used to initialize a server application. |
| Access         | ReadWrite                                                                   |
| Type           | Bool                                                                        |
| Default        | False                                                                       |
| Minimum system | Windows Server 2003                                                         |



 

### IsEnabled



| Entry | Value |
|----------------|-----------------------------------------------------------------------------------------------------------------------------|
| Description    | False if the COM+ application or component is disabled. If the COM+ application or component is enabled, IsEnabled is True. |
| Access         | ReadWrite                                                                                                                   |
| Type           | Bool                                                                                                                        |
| Default        | True                                                                                                                        |
| Minimum system | Windows XP                                                                                                                  |



 

### IsEventClass



| Entry | Value |
|----------------|----------------------------------------------------|
| Description    | Indicates whether the component is an event class. |
| Access         | ReadOnly                                           |
| Type           | Bool                                               |
| Default        | False                                              |
| Minimum system | Windows 2000                                       |



 

### IsInstalled



| Entry | Value |
|----------------|-----------------------------------------------------------------|
| Description    | Indicates whether the component is installed in an application. |
| Access         | ReadOnly                                                        |
| Type           | Bool                                                            |
| Default        | False                                                           |
| Minimum system | Windows Server 2003                                             |



 

### IsPrivateComponent



| Entry | Value |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Determines whether a server application is a private component. A private component in a server application can be activated only from within the application. For example, if you call [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) on a private component, it fails from out-of-process but succeeds in-process. In contrast, if you call **CoCreateInstance** on a public component, it succeeds both in-process and out-of-process. |
| Access         | ReadWrite                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Type           | Bool                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Default        | False                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Minimum system | Windows XP                                                                                                                                                                                                                                                                                                                                                                                                                              |



 

### JustInTimeActivation



| Entry | Value |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Determines whether [JIT activation](enabling-jit-activation-for-a-component.md) is enabled for the component. This property is set to True when [transaction support](setting-the-transaction-attribute.md) is set to Required, Requires New, or Supported. When JustInTimeActivation is set to True, [synchronization support](setting-the-synchronization-attribute.md) must be set to Required (the default) or Requires New. |
| Access         | ReadWrite                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Type           | Bool                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Default        | False                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Minimum system | Windows 2000                                                                                                                                                                                                                                                                                                                                                                                                                        |



 

### LoadBalancingSupported



| Entry | Value |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | If the component load balancing service is installed and enabled on the server, determines whether the component participates in load balancing. |
| Access         | ReadWrite                                                                                                                                        |
| Type           | Bool                                                                                                                                             |
| Default        | False                                                                                                                                            |
| Minimum system | Windows 2000                                                                                                                                     |



 

### MaxPoolSize



| Entry | Value |
|----------------|-----------------------------------|
| Description    | Maximum number of objects pooled. |
| Access         | ReadWrite                         |
| Type           | Long (1-1048576)                  |
| Default        | 1048576                           |
| Minimum system | Windows 2000                      |



 

### MinPoolSize



| Entry | Value |
|----------------|-----------------------------------|
| Description    | Minimum number of objects pooled. |
| Access         | ReadWrite                         |
| Type           | Long (0-1048576)                  |
| Default        | 0                                 |
| Minimum system | Windows 2000                      |



 

### MultiInterfacePublisherFilterCLSID



| Entry | Value |
|----------------|-------------------------------------------------------------------------|
| Description    | CLSID for the publisher filter used if the component is an event class. |
| Access         | ReadWrite                                                               |
| Type           | String                                                                  |
| Default        | N/A                                                                     |
| Minimum system | Windows 2000                                                            |



 

### MustRunInClientContext



| Entry | Value |
|----------------|-----------------------------------------------------------------------------------------------------------|
| Description    | Indicates that component must be activated in its original caller's context. Otherwise, activation fails. |
| Access         | ReadWrite                                                                                                 |
| Type           | Bool                                                                                                      |
| Default        | False                                                                                                     |
| Minimum system | Windows XP                                                                                                |



 

### MustRunInDefaultContext



| Entry | Value |
|----------------|--------------------------------------------------------------------------------------------------------------|
| Description    | Indicates that the component must be activated in the default caller's context. Otherwise, activation fails. |
| Access         | ReadWrite                                                                                                    |
| Type           | Bool                                                                                                         |
| Default        | False                                                                                                        |
| Minimum system | Windows 2000                                                                                                 |



 

### ObjectPoolingEnabled



| Entry | Value |
|----------------|-------------------------------------------------------------------------------------------------|
| Description    | Determines whether [COM+ object pooling](com--object-pooling.md) is enabled for the component. |
| Access         | ReadWrite                                                                                       |
| Type           | Bool                                                                                            |
| Default        | False                                                                                           |
| Minimum system | Windows 2000                                                                                    |



 

### ProgID



| Entry | Value |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | A friendly name used for identifying the component. This property is returned when the [**Name**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_name) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                                                              |
| Type           | String                                                                                                                                                                                |
| Default        | N/A                                                                                                                                                                                   |
| Minimum system | Windows 2000                                                                                                                                                                          |



 

### PublisherID



| Entry | Value |
|----------------|------------------------------------------------------------------------|
| Description    | Identifier for the event publisher if the component is an event class. |
| Access         | ReadWrite                                                              |
| Type           | String                                                                 |
| Default        | ""                                                                     |
| Minimum system | Windows 2000                                                           |



 

### SoapAssemblyName



| Entry | Value |
|----------------|--------------------------------------------------------------------------------------------------|
| Description    | A GUID identifying the GAC assembly that is run when the component is invoked as a SOAP service. |
| Access         | ReadWrite                                                                                        |
| Type           | String                                                                                           |
| Default        | NULL                                                                                             |
| Minimum system | Windows Server 2003                                                                              |



 

### SoapTypeName



| Entry | Value |
|----------------|------------------------------------------------------------------------------|
| Description    | The managed type name for a component that can be invoked as a SOAP service. |
| Access         | ReadWrite                                                                    |
| Type           | String                                                                       |
| Default        | NULL                                                                         |
| Minimum system | Windows Server 2003                                                          |



 

### Synchronization



| Entry | Value |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Determines call [synchronization](setting-the-synchronization-attribute.md) for the component.                                                                                                     |
| Access         | ReadWrite                                                                                                                                                                                           |
| Type           | Long Possible values:COMAdminSynchronizationIgnored (0)COMAdminSynchronizationNone (1)COMAdminSynchronizationSupported (2)COMAdminSynchronizationRequired (3)COMAdminSynchronizationRequiresNew (4) |
| Default        | COMAdminSynchronizationIgnored (0)                                                                                                                                                                  |
| Minimum system | Windows 2000                                                                                                                                                                                        |



 

### ThreadingModel



| Entry | Value |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Determines how instances of the component are assigned to threads for method execution. Values correspond to COM threading models.                                                                                        |
| Access         | ReadOnly                                                                                                                                                                                                                  |
| Type           | Long Possible values:COMAdminThreadingModelApartment (0)COMAdminThreadingModelFree (1)COMAdminThreadingModelMain (2)COMAdminThreadingModelBoth (3)COMAdminThreadingModelNeutral (4)COMAdminThreadingModelNotSpecified (5) |
| Default        | N/A                                                                                                                                                                                                                       |
| Minimum system | Windows 2000                                                                                                                                                                                                              |



 

### Transaction



| Entry | Value |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Determines how a component supports [transactions](setting-the-transaction-attribute.md). It is recommended that you use the constants in the enumeration and not the numeric values. |
| Access         | ReadWrite                                                                                                                                                                              |
| Type           | Long Possible values:COMAdminTransactionIgnored (0)COMAdminTransactionNone (1)COMAdminTransactionSupported (2)COMAdminTransactionRequired (3)COMAdminTransactionRequiresNew (4)        |
| Default        | COMAdminTransactionNone (1)                                                                                                                                                            |
| Minimum system | Windows 2000                                                                                                                                                                           |



 

### TxIsolationLevel



| Entry | Value |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Indicates the transaction isolation levels. There are five isolation levels: none, read uncommitted, read committed, repeatable read, and serialized. The default isolation level is serialized.                           |
| Access         | ReadWrite                                                                                                                                                                                                                  |
| Type           | Long Possible values:COMAdminTxIsolationLevelAny (0)COMAdminTxIsolationLevelReadUnCommitted (1)COMAdminTxIsolationLevelReadCommitted (2)COMAdminTxIsolationLevelRepeatableRead (3)COMAdminTxIsolationLevelSerializable (4) |
| Default        | COMAdminTxIsolationLevelSerializable (4)                                                                                                                                                                                   |
| Minimum system | Windows XP                                                                                                                                                                                                                 |



 

### VersionBuild



| Entry | Value |
|----------------|---------------------------|
| Description    | Version build identifier. |
| Access         | ReadOnly                  |
| Type           | String                    |
| Default        | ""                        |
| Minimum system | Windows 2000              |



 

### VersionMajor



| Entry | Value |
|----------------|---------------------|
| Description    | Version identifier. |
| Access         | ReadOnly            |
| Type           | String              |
| Default        | ""                  |
| Minimum system | Windows 2000        |



 

### VersionMinor



| Entry | Value |
|----------------|-------------------------|
| Description    | Version sub-identifier. |
| Access         | ReadOnly                |
| Type           | String                  |
| Default        | ""                      |
| Minimum system | Windows 2000            |



 

### VersionSubBuild



| Entry | Value |
|----------------|-------------------------------|
| Description    | Version sub-build identifier. |
| Access         | ReadOnly                      |
| Type           | String                        |
| Default        | ""                            |
| Minimum system | Windows 2000                  |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 
