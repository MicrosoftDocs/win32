---
description: Contains an object for each COM+ application installed on the local computer. The properties exposed by these objects hold all settings made at the application level.
ms.assetid: c0c46592-5282-412d-8f54-67637be8218a
title: Applications collection
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Applications
api_type: 
- COM
api_location: 
---

# Applications collection

Contains an object for each COM+ application installed on the local computer. The properties exposed by these objects hold all settings made at the application level.

You set properties for components within an application by using the related [**Components**](components.md) collection. You assign roles to an application by using the related [**Roles**](roles.md) collection.

To install components into an application, use methods on the [**COMAdminCatalog**](comadmincatalog.md) object. To install an application from a file or to shut down or export an application, also use methods on the **COMAdminCatalog** object. Otherwise, to create a new application, you can add an object to the **Applications** collection.

This collection supports the [**Add**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-add) and [**Remove**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-remove) methods of the [**COMAdminCatalogCollection**](comadmincatalogcollection.md) object.

## Members

The **Applications** collection inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**ApplicationInstances**](applicationinstances.md)
-   [**Components**](components.md)
-   [**ErrorInfo**](errorinfo.md)
-   [**LegacyComponents**](legacycomponents.md)
-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)
-   [**Roles**](roles.md)

You can navigate to this collection from the following collections:

-   [**Partitions**](partitions.md)
-   [**Root**](root.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](comadmincatalogobject.md) object within the collection:

-   [3GigSupportEnabled](#3gigsupportenabled)
-   [AccessChecksLevel](#accesscheckslevel)
-   [Activation](#recycleactivationlimit)
-   [ApplicationAccessChecksEnabled](#applicationaccesschecksenabled)
-   [ApplicationDirectory](#applicationdirectory)
-   [ApplicationProxy](#applicationproxyservername)
-   [ApplicationProxyServerName](#applicationproxyservername)
-   [AppPartitionID](#apppartitionid)
-   [Authentication](#authenticationcapability)
-   [AuthenticationCapability](#authenticationcapability)
-   [Changeable](#changeable)
-   [CommandLine](#commandline)
-   [ConcurrentApps](#concurrentapps)
-   [CreatedBy](#createdby)
-   [CRMEnabled](#crmenabled)
-   [CRMLogFile](#crmlogfile)
-   [Deleteable](#deleteable)
-   [Description](#description)
-   [DumpEnabled](#dumpenabled)
-   [DumpOnException](#dumponexception)
-   [DumpOnFailfast](#dumponfailfast)
-   [DumpPath](#dumppath)
-   [EventsEnabled](#eventsenabled)
-   [ID](#applications-collection)
-   [Identity](#identity)
-   [ImpersonationLevel](#impersonationlevel)
-   [IsEnabled](#isenabled)
-   [IsSystem](#issystem)
-   [MaxDumpCount](#maxdumpcount)
-   [Name](#applicationproxyservername)
-   [Password](#password)
-   [QCAuthenticateMsgs](#qcauthenticatemsgs)
-   [QCListenerMaxThreads](#qclistenermaxthreads)
-   [QueueListenerEnabled](#queuelistenerenabled)
-   [QueuingEnabled](#queuingenabled)
-   [RecycleActivationLimit](#recycleactivationlimit)
-   [RecycleCallLimit](#recyclecalllimit)
-   [RecycleExpirationTimeout](#recycleexpirationtimeout)
-   [RecycleLifetimeLimit](#recyclelifetimelimit)
-   [RecycleMemoryLimit](#recyclememorylimit)
-   [Replicable](#replicable)
-   [RunForever](#runforever)
-   [ServiceName](#servicename)
-   [ShutdownAfter](#shutdownafter)
-   [SoapActivated](#soapactivated)
-   [SoapBaseUrl](#soapbaseurl)
-   [SoapMailTo](#soapmailto)
-   [SoapVRoot](#soapvroot)
-   [SRPEnabled](#srpenabled)
-   [SRPTrustLevel](#srptrustlevel)

### 3GigSupportEnabled



| Entry | Value |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Indicates whether the application can use 3 GB of memory in its process. If this is not enabled, the application can use only 2 GB of memory. |
| Access         | ReadWrite                                                                                                                                     |
| Type           | Bool                                                                                                                                          |
| Default        | False                                                                                                                                         |
| Minimum system | Windows 2000                                                                                                                                  |



 

### AccessChecksLevel



| Entry | Value |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Indicates whether access checks are performed at only the process level or at both the process and component level. It is recommended that you use the constants in the enumeration and not the numeric values. |
| Access         | ReadWrite                                                                                                                                                                                                       |
| Type           | Long Possible values: COMAdminAccessChecksApplicationLevel (0) COMAdminAccessChecksApplicationComponentLevel (1)                                                                                                |
| Default        | COMAdminAccessChecksApplicationComponentLevel (1)                                                                                                                                                               |
| Minimum system | Windows 2000                                                                                                                                                                                                    |



 

### Activation



| Entry | Value |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Local activation indicates that objects within the application run within a dedicated local server process (server application). In-process activation indicates that objects run in their creator's process (library application). |
| Access         | ReadWrite                                                                                                                                                                                                                           |
| Type           | Long Possible values:COMAdminActivationInproc (0)COMAdminActivationLocal (1)                                                                                                                                                        |
| Default        | COMAdminActivationLocal (1)                                                                                                                                                                                                         |
| Minimum system | Windows 2000                                                                                                                                                                                                                        |



 

### ApplicationAccessChecksEnabled



| Entry | Value |
|----------------|----------------------------------------------------------------------------------------------------|
| Description    | Indicates whether access checks are performed for the application when clients make calls into it. |
| Access         | ReadWrite                                                                                          |
| Type           | Bool                                                                                               |
| Default        | True                                                                                               |
| Minimum system | Windows 2000                                                                                       |



 

### ApplicationDirectory



| Entry | Value |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The full path to the application. This information is needed when you configure Side-by-Side (SxS) assemblies. Side-by-side (SxS) assemblies allow ASP applications to specify which version of an SxS-supported system DLL to use, such as MSVCRT, MSXML, COMCTL, GDIPLUS, and so on. For example, if your ASP application relies on MSVCRT version 2.0, you can ensure that your application still uses MSVCRT version 2.0 even after service packs are applied to the server. Any new version of MSVCRT is still installed on the computer, but version 2.0 remains and is used by your application. SxS-supported DLLs are stored in %WINDIR%\\WinSxS. |
| Access         | ReadWrite                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Type           | String                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Default        | ""                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Minimum system | Windows XP                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |



 

> [!Note]  
> Only one version of a system DLL can be used in any application pool, even though this feature is configurable at the application level. For example, if application App1 uses MSVCRT, version 2.5 and application App2 uses MSVCRT, version 2.4, then App1 and App2 should not be in the same application pool. If they are, the application that is loaded first has its version of MSVCRT loaded, and the other application is forced to use it until the applications are unloaded.

 

For more information, see "Side-by-Side Assemblies" in [Changes in COM+ Services in IIS 6.0](/previous-versions/iis/6.0-sdk/ms526018(v=vs.90)).

### ApplicationProxy



| Entry | Value |
|----------------|------------------------------------------------------------|
| Description    | Indicates whether the application is an application proxy. |
| Access         | ReadOnly                                                   |
| Type           | Bool                                                       |
| Default        | False                                                      |
| Minimum system | Windows 2000                                               |



 

### ApplicationProxyServerName



| Entry | Value |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | A remote server name used when exporting the application proxy. It is this server name that the application proxy points to when it is installed on a client computer. |
| Access         | ReadWrite                                                                                                                                                              |
| Type           | String                                                                                                                                                                 |
| Default        | ""                                                                                                                                                                     |
| Minimum system | Windows 2000                                                                                                                                                           |



 

### AppPartitionID



| Entry | Value |
|----------------|---------------------------------------------------|
| Description    | A GUID representing the application partition ID. |
| Access         | ReadOnly                                          |
| Type           | String                                            |
| Default        | &lt;Generated&gt;                                 |
| Minimum system | Windows Server 2003                               |



 

### Authentication



| Entry | Value |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Sets authentication level for calls, with values corresponding to the Remote Procedure Call (RPC) authentication settings. When COMAdminAuthenticationDefault is chosen, the setting in the DefaultAuthenticationLevel property within the [**LocalComputer**](localcomputer.md) collection is used. |
| Access         | ReadWrite                                                                                                                                                                                                                                                                                             |
| Type           | Long Possible values:COMAdminAuthenticationDefault (0)COMAdminAuthenticationNone (1) COMAdminAuthenticationConnect (2)COMAdminAuthenticationCall (3)COMAdminAuthenticationPacket (4)COMAdminAuthenticationIntegrity (5)COMAdminAuthenticationPrivacy (6)                                              |
| Default        | COMAdminAuthenticationPacket (4)                                                                                                                                                                                                                                                                      |
| Minimum system | Windows 2000                                                                                                                                                                                                                                                                                          |



 

> [!Note]  
> For library (in-process) applications, the only valid settings here are COMAdminAuthenticationDefault and COMAdminAuthenticationNone . It is recommended that you use the constants in the enumeration and not the numeric values.

 

### AuthenticationCapability



| Entry | Value |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Determines what identity is presented when calls are impersonated.                                                                                                                                                                      |
| Access         | ReadWrite                                                                                                                                                                                                                               |
| Type           | Long Possible values:COMAdminAuthenticationCapabilitiesNone (0x0)COMAdminAuthenticationCapabilitiesSecureReference (0x2)COMAdminAuthenticationCapabilitiesStaticCloaking (0x20)COMAdminAuthenticationCapabilitiesDynamicCloaking (0x40) |
| Default        | COMAdminAuthenticationCapabilitiesDynamicCloaking (0x40)                                                                                                                                                                                |
| Minimum system | Windows 2000                                                                                                                                                                                                                            |



 

### Changeable



| Entry | Value |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Determines whether changes to the application settings or those of its components are allowed, either programmatically or through the Component Services administration tool. |
| Access         | ReadWrite                                                                                                                                                                     |
| Type           | Bool                                                                                                                                                                          |
| Default        | True                                                                                                                                                                          |
| Minimum system | Windows 2000                                                                                                                                                                  |



 

### CommandLine



| Entry | Value |
|----------------|----------------------------------------------------------------------------------------------------------------------------|
| Description    | A command-line string for use in debugging. The application can be launched in a debugger with the specified command line. |
| Access         | ReadWrite                                                                                                                  |
| Type           | String                                                                                                                     |
| Default        | ""                                                                                                                         |
| Minimum system | Windows 2000                                                                                                               |



 

### ConcurrentApps



| Entry | Value |
|----------------|----------------------------------------------------------------------------------|
| Description    | Specifies the maximum number of poolable applications that can run concurrently. |
| Access         | ReadWrite                                                                        |
| Type           | Long (1-1048576)                                                                 |
| Default        | 1                                                                                |
| Minimum system | Windows XP                                                                       |



 

### CreatedBy



| Entry | Value |
|----------------|---------------------------------------------------------------|
| Description    | Informational string to describe who created the application. |
| Access         | ReadWrite                                                     |
| Type           | String                                                        |
| Default        | ""                                                            |
| Minimum system | Windows 2000                                                  |



 

### CRMEnabled



| Entry | Value |
|----------------|------------------------------------------------------------------|
| Description    | Determines whether the Compensating Resource Manager is enabled. |
| Access         | ReadWrite                                                        |
| Type           | Bool                                                             |
| Default        | False                                                            |
| Minimum system | Windows 2000                                                     |



 

### CRMLogFile



| Entry | Value |
|----------------|----------------------------------------------------------------------------------------|
| Description    | Name and path of file for keeping the log for the compensating resource manager (CRM). |
| Access         | ReadWrite                                                                              |
| Type           | String                                                                                 |
| Default        | ""                                                                                     |
| Minimum system | Windows 2000                                                                           |



 

### Deleteable



| Entry | Value |
|----------------|-----------------------------------------------------------------------------------------------------------------------------|
| Description    | Sets whether the application can be deleted, either programmatically or through the Component Services administration tool. |
| Access         | ReadWrite                                                                                                                   |
| Type           | Bool                                                                                                                        |
| Default        | True                                                                                                                        |
| Minimum system | Windows 2000                                                                                                                |



 

### Description



| Entry | Value |
|----------------|----------------------------|
| Description    | Describes the application. |
| Access         | ReadWrite                  |
| Type           | String                     |
| Default        | ""                         |
| Minimum system | Windows 2000               |



 

### DumpEnabled



| Entry | Value |
|----------------|-------------------------------------------------------------------------------------------------------|
| Description    | Enables the dump of the state of a COM+ application at the time of failure to a designated directory. |
| Access         | ReadWrite                                                                                             |
| Type           | Bool                                                                                                  |
| Default        | False                                                                                                 |
| Minimum system | Windows XP                                                                                            |



 

> [!Note]  
> As of Windows Server 2003, only administrators have read access privileges to the COM+ dump files.

 

### DumpOnException



| Entry | Value |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Enables the dump of the state of a COM+ application when the application causes an unhandled exception and is terminated by the COM+ runtime. |
| Access         | ReadWrite                                                                                                                                     |
| Type           | Bool                                                                                                                                          |
| Default        | False                                                                                                                                         |
| Minimum system | Windows XP                                                                                                                                    |



 

### DumpOnFailfast



| Entry | Value |
|----------------|---------------------------------------------------------------------------------|
| Description    | Enables the dump of the state of a COM+ application when the application fails. |
| Access         | ReadWrite                                                                       |
| Type           | Bool                                                                            |
| Default        | False                                                                           |
| Minimum system | Windows XP                                                                      |



 

### DumpPath



| Entry | Value |
|----------------|--------------------------------------------------------------|
| Description    | The path of the directory in which the dump files are saved. |
| Access         | ReadWrite                                                    |
| Type           | String                                                       |
| Default        | "%systemroot%\\system32\\com\\dmp"                           |
| Minimum system | Windows XP                                                   |



 

> [!Note]  
> As of Windows Server 2003, only administrators have read access privileges to the COM+ dump files.

 

### EventsEnabled



| Entry | Value |
|----------------|-----------------------------------------------------------|
| Description    | Indicates whether events are enabled for the application. |
| Access         | ReadWrite                                                 |
| Type           | Bool                                                      |
| Default        | True                                                      |
| Minimum system | Windows 2000                                              |



 

### ID



| Entry | Value |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | A GUID representing the application. This property is returned when the [**Key**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_key) property method is called on an object of this collection. |
| Access         | WriteOnce                                                                                                                                                            |
| Type           | String                                                                                                                                                               |
| Default        | &lt;Generated&gt;                                                                                                                                                    |
| Minimum system | Windows 2000                                                                                                                                                         |



 

### Identity



| Entry | Value |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Sets the server process identity for the application. Specify a valid user account or "Interactive User" to have the application assume the identity of the current logged-on user. You can also specify the strings "nt authority\\localservice", "nt authority\\networkservice", and "nt authority\\system". The default password for these three accounts is "" (empty string). |
| Access         |                                                                                                                                                                                                                                                                                                                                                                                    |
| Type           |                                                                                                                                                                                                                                                                                                                                                                                    |
| Default        |                                                                                                                                                                                                                                                                                                                                                                                    |
| Minimum system | Windows 2000                                                                                                                                                                                                                                                                                                                                                                       |



 

The Identity property is not enabled for library applications, which run in the client process.

The Password property should be set at the same time as Identity, prior to using [**SaveChanges**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-savechanges), because the password and identity are validated before being saved. If the password and identity get out of sync, the application cannot be launched until they are reset by an administrator.

### ImpersonationLevel



| Entry | Value |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Sets impersonation level used for calls made to other applications.                                                                                           |
| Access         | ReadWrite                                                                                                                                                     |
| Type           | Long Possible values:COMAdminImpersonationAnonymous (1)COMAdminImpersonationIdentify (2)COMAdminImpersonationImpersonate (3)COMAdminImpersonationDelegate (4) |
| Default        | COMAdminImpersonationImpersonate (3)                                                                                                                          |
| Minimum system | Windows 2000                                                                                                                                                  |



 

### IsEnabled



| Entry | Value |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | If the COM+ application or component is disabled, IsEnabled is False. If the COM+ application or component is enabled, IsEnabled is True. |
| Access         | ReadWrite                                                                                                                                 |
| Type           | Bool                                                                                                                                      |
| Default        | True                                                                                                                                      |
| Minimum system | Windows XP                                                                                                                                |



 

### IsSystem



| Entry | Value |
|----------------|--------------------------------------|
| Description    | Identifies COM+ system applications. |
| Access         | ReadOnly                             |
| Type           | Bool                                 |
| Default        | False                                |
| Minimum system | Windows 2000                         |



 

### MaxDumpCount



| Entry | Value |
|----------------|----------------------------------------------------------------------------------|
| Description    | Indicates the maximum number of files to be generated before overwriting occurs. |
| Access         | ReadWrite                                                                        |
| Type           | Long (1-200)                                                                     |
| Default        | 5                                                                                |
| Minimum system | Windows XP                                                                       |



 

### Name



| Entry | Value |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The name of the application. Extra spaces at the beginning and end of the string are stripped out. This property is returned when the [**Name**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_name) property method is called on an object of this collection. |
| Access         | ReadWrite                                                                                                                                                                                                                            |
| Type           | String                                                                                                                                                                                                                               |
| Default        | "New Application"                                                                                                                                                                                                                    |
| Minimum system | Windows 2000                                                                                                                                                                                                                         |



 

> [!Note]  
> Unique names should be chosen for applications. If multiple applications are created with the same name, it can interfere with referencing the applications by name, resulting in unpredictable behavior.

 

### Password



| Entry | Value |
|----------------|----------------------------------------------------------------------------|
| Description    | Sets the password used by the server process to log on under the identity. |
| Access         | WriteOnly                                                                  |
| Type           | String                                                                     |
| Default        | ""                                                                         |
| Minimum system | Windows 2000                                                               |



 

Password should be set at the same time as Identity, prior to using [**SaveChanges**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-savechanges), because the password and identity are validated before being saved. If the password and identity get out of sync, the application cannot be launched until they are reset by an administrator.

### QCAuthenticateMsgs



| Entry | Value |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Indicates under what circumstances queued requests to an application are authenticated.                                                 |
| Access         | ReadWrite                                                                                                                               |
| Type           | Long Possible values:COMAdminQCMessageAuthenticateSecureApps (0)COMAdminQCMessageAuthenticateOff (1)COMAdminQCMessageAuthenticateOn (2) |
| Default        | COMAdminQCMessageAuthenticateSecureApps (0)                                                                                             |
| Minimum system | Windows XP                                                                                                                              |



 

### QCListenerMaxThreads



| Entry | Value |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Indicates the maximum number of concurrent listener threads. The valid range for this property is 0 to 1000. For a newly created application, the setting is derived from the algorithm currently used for determining the default number of listener threads: 16 times the number of CPUs in the server. |
| Access         | ReadWrite                                                                                                                                                                                                                                                                                                 |
| Type           | Long (0-1000)                                                                                                                                                                                                                                                                                             |
| Default        | 0                                                                                                                                                                                                                                                                                                         |
| Minimum system | Windows XP                                                                                                                                                                                                                                                                                                |



 

> [!Note]  
> This property is also available with read/write capability from the **Queuing** tab of the Component Services administrative tool.

 

### QueueListenerEnabled



| Entry | Value |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Indicates whether the queued components listener is enabled for the application. If enabled, the listener is launched when the application starts. This property takes effect only if QueuingEnabled is set to True. |
| Access         | ReadWrite                                                                                                                                                                                                            |
| Type           | Bool                                                                                                                                                                                                                 |
| Default        | False                                                                                                                                                                                                                |
| Minimum system | Windows 2000                                                                                                                                                                                                         |



 

### QueuingEnabled



| Entry | Value |
|----------------|--------------------------------------------------------------------------------------|
| Description    | Indicates whether the COM+ Queued Components service is enabled for the application. |
| Access         | ReadWrite                                                                            |
| Type           | Bool                                                                                 |
| Default        | False                                                                                |
| Minimum system | Windows 2000                                                                         |



 

### RecycleActivationLimit



| Entry | Value |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Indicates the maximum number of activations of configured objects in the application to accept before recycling the process. The default number of activations is 0. |
| Access         | ReadWrite                                                                                                                                                            |
| Type           | Long (0-1048576)                                                                                                                                                     |
| Default        | 0                                                                                                                                                                    |
| Minimum system | Windows XP                                                                                                                                                           |



 

### RecycleCallLimit



| Entry | Value |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Indicates the maximum number of calls to allow configured objects in the application to accept before recycling the process. The default number of calls is 0. |
| Access         | ReadWrite                                                                                                                                                      |
| Type           | Long (0-1048576)                                                                                                                                               |
| Default        | 0                                                                                                                                                              |
| Minimum system | Windows XP                                                                                                                                                     |



 

### RecycleExpirationTimeout



| Entry | Value |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Indicates the amount of time (in minutes) to allow a recycled process to run before shutting it down. The countdown begins immediately after the process is recycled. The maximum expiration time-out is 1440 minutes (24 hours), and the default is 15 minutes. |
| Access         | ReadWrite                                                                                                                                                                                                                                                        |
| Type           | Long (1-1440)                                                                                                                                                                                                                                                    |
| Default        | 15                                                                                                                                                                                                                                                               |
| Minimum system | Windows XP                                                                                                                                                                                                                                                       |



 

### RecycleLifetimeLimit



| Entry | Value |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Indicates the maximum number of minutes to allow a process to run before recycling it. The maximum lifetime limit is 30240 minutes (21 days), and the default is 0 minutes. |
| Access         | ReadWrite                                                                                                                                                                   |
| Type           | Long (0-30240)                                                                                                                                                              |
| Default        | 0                                                                                                                                                                           |
| Minimum system | Windows XP                                                                                                                                                                  |



 

### RecycleMemoryLimit



| Entry | Value |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Indicates the maximum amount of memory usage (in kilobytes) allowed a process before it's recycled. If the process memory usage exceeds the specified number for a period longer than one minute, the process is recycled. The default amount of memory usage is 0 KB. |
| Access         | ReadWrite                                                                                                                                                                                                                                                              |
| Type           | Long (0-1048576)                                                                                                                                                                                                                                                       |
| Default        | 0                                                                                                                                                                                                                                                                      |
| Minimum system | Windows XP                                                                                                                                                                                                                                                             |



 

### Replicable



| Entry | Value |
|----------------|------------------------------------------------------|
| Description    | Indicates whether the application can be replicated. |
| Access         | ReadWrite                                            |
| Type           | Bool                                                 |
| Default        | True                                                 |
| Minimum system | Windows XP                                           |



 

### RunForever



| Entry | Value |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Enables a server process to continue if an application is idle. If set to True, the server process does not shut down when left idle. If set to False, the process shuts down according to the value set by the ShutdownAfter property. RunForever is not enabled for library (in-process) applications. |
| Access         | ReadWrite                                                                                                                                                                                                                                                                                                |
| Type           | Bool                                                                                                                                                                                                                                                                                                     |
| Default        | False                                                                                                                                                                                                                                                                                                    |
| Minimum system | Windows 2000                                                                                                                                                                                                                                                                                             |



 

### ServiceName



| Entry | Value |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The service name corresponding to the application configured to run as a service application. If this value is **NULL**, the application is not configured to run as a service. Otherwise, the configuration information for the service can be found by using the service name. |
| Access         | ReadOnly                                                                                                                                                                                                                                                                         |
| Type           | String                                                                                                                                                                                                                                                                           |
| Default        | ""                                                                                                                                                                                                                                                                               |
| Minimum system | Windows XP                                                                                                                                                                                                                                                                       |



 

### ShutdownAfter



| Entry | Value |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Sets the delay before shutting down a server process after it becomes idle. Shutdown latency ranges from 0 to 1440 minutes (24 hours). If RunForever is set to True, this property is ignored. ShutdownAfter is not enabled for library (in-process) applications. |
| Access         | ReadWrite                                                                                                                                                                                                                                                          |
| Type           | Long (0-1440)                                                                                                                                                                                                                                                      |
| Default        | 3                                                                                                                                                                                                                                                                  |
| Minimum system | Windows 2000                                                                                                                                                                                                                                                       |



 

### SoapActivated



| Entry | Value |
|----------------|--------------------------------------------------------------------------------------|
| Description    | Indicates whether this application is exposed for consumption via the SOAP protocol. |
| Access         | ReadWrite                                                                            |
| Type           | Bool                                                                                 |
| Default        | False                                                                                |
| Minimum system | Windows Server 2003                                                                  |



 

### SoapBaseUrl



| Entry | Value |
|----------------|------------------------------------------------------------------------------|
| Description    | The URL endpoint at which this application is exposed via the SOAP protocol. |
| Access         | ReadWrite                                                                    |
| Type           | String                                                                       |
| Default        | ""                                                                           |
| Minimum system | Windows Server 2003                                                          |



 

### SoapMailTo



| Entry | Value |
|----------------|-------------------------------------------------------------------------------|
| Description    | The email address at which this application is exposed via the SOAP protocol. |
| Access         | ReadWrite                                                                     |
| Type           | String                                                                        |
| Default        | ""                                                                            |
| Minimum system | Windows Server 2003                                                           |



 

### SoapVRoot



| Entry | Value |
|----------------|----------------------------------------------------------------------------------------------------------------------|
| Description    | The IIS virtual root directory in which the access scripts that expose the application via the SOAP protocol reside. |
| Access         | ReadWrite                                                                                                            |
| Type           | String                                                                                                               |
| Default        | ""                                                                                                                   |
| Minimum system | Windows Server 2003                                                                                                  |



 

### SRPEnabled



| Entry | Value |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Determines the software restriction policy (SRP) for the application. If set to True, the SRPTrustLevel property for the application is used. If set to False, the software restriction policies from the local security settings are used. The local security settings are controlled through the Local Security Policy snap-in of the Microsoft Management Console. |
| Access         | ReadWrite                                                                                                                                                                                                                                                                                                                                                             |
| Type           | Bool                                                                                                                                                                                                                                                                                                                                                                  |
| Default        | False                                                                                                                                                                                                                                                                                                                                                                 |
| Minimum system | Windows XP                                                                                                                                                                                                                                                                                                                                                            |



 

### SRPTrustLevel



| Entry | Value |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Indicates the software restriction policy (SRP) trust level of the application. This property is used only if the SRPEnabled property is set to True. The SRP trust level refers to the level of trust that you are willing to give to an application. An Unrestricted SRP trust level corresponds to the SAFER\_LEVELID\_FULLYTRUSTED enum value, while a Disallowed SRP trust level corresponds to the SAFER\_LEVELID\_DISALLOWED enum value. The enumeration for the trust levels is defined in Winsafer.h. |
| Access         | ReadWrite                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Type           | Long Possible values:SAFER\_LEVELID\_DISALLOWED (0x0)SAFER\_LEVELID\_FULLYTRUSTED (0x40000)                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Default        | SAFER\_LEVELID\_FULLYTRUSTED (0x40000)                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Minimum system | Windows XP                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |



 

An application that you are willing to trust with Unrestricted access should have the most stringent security attached to it. Applications that are Unrestricted can load only unrestricted components, while Disallowed applications will not be allowed to run and therefore cannot load any components.

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 
