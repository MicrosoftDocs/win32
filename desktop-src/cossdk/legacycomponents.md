---
description: Contains an object for each unconfigured component in the Applications collection. Unconfigured components cannot make use of COM+ services. The properties exposed by these objects hold settings made at the component level.
ms.assetid: 87f3b93f-71aa-4187-88d2-889c13d8bd06
title: LegacyComponents collection
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LegacyComponents
api_type: 
- COM
api_location: 
---

# LegacyComponents collection

Contains an object for each unconfigured component in the Applications collection. Unconfigured components cannot make use of COM+ services. The properties exposed by these objects hold settings made at the component level.

This collection supports the [**Remove**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-remove) method of the [**COMAdminCatalogCollection**](comadmincatalogcollection.md) object, but not the [**Add**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-add) method. To install or import components into an application, use methods on the [**COMAdminCatalog**](comadmincatalog.md) object.

## Members

The **LegacyComponents** collection inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**ErrorInfo**](errorinfo.md)
-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)

You can navigate to this collection from the following collections:

-   [**Applications**](applications.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](comadmincatalogobject.md) object within the collection:

-   [AccessPermissions](#accesspermissions)
-   [ActivateAtStorage](#activateatstorage)
-   [AppID](#appid)
-   [AppName](#appname)
-   [AuthenticationLevel](#authenticationlevel)
-   [Bitness](#bitness)
-   [ClassName](#classname)
-   [CLSID](#clsid)
-   [DllSurrogate](#dllsurrogate)
-   [InprocHandler32](#inprochandler32)
-   [InprocServer32](#inprocserver32)
-   [IsEnabled](#isenabled)
-   [LaunchPermissions](#launchpermissions)
-   [LocalServer32](#localserver32)
-   [LocalService](#localservice)
-   [Password](#password)
-   [ProgID](#progid)
-   [RemoteServer](#remoteserver)
-   [RunAs](#runas)
-   [ServiceParameter](#serviceparameter)
-   [SRPTrustLevel](#srptrustlevel)
-   [ThreadingModel](#threadingmodel)

### AccessPermissions



| Entry | Value |
|----------------|---------------------------------------------------------------------------------|
| Description    | Specifies the user accounts that are allowed or denied access to the component. |
| Access         | ReadWrite                                                                       |
| Type           | String                                                                          |
| Default        | N/A                                                                             |
| Minimum system | Windows XP                                                                      |



 

### ActivateAtStorage



| Entry | Value |
|----------------|------------------------------------------------------------------|
| Description    | Specifies whether to run the server on the data storage machine. |
| Access         | ReadWrite                                                        |
| Type           | String Possible values:"N""Y"                                    |
| Default        | "N"                                                              |
| Minimum system | Windows XP                                                       |



 

### AppID



| Entry | Value |
|----------------|---------------------|
| Description    | The application ID. |
| Access         | ReadOnly            |
| Type           | String              |
| Default        | N/A                 |
| Minimum system | Windows XP          |



 

### AppName



| Entry | Value |
|----------------|------------------------------|
| Description    | The name of the application. |
| Access         | ReadOnly                     |
| Type           | String                       |
| Default        | N/A                          |
| Minimum system | Windows XP                   |



 

### AuthenticationLevel



| Entry | Value |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Sets authentication level for calls, with values corresponding to the Remote Procedure Call (RPC) authentication settings. When COMAdminAuthenticationDefault is chosen, the setting in the DefaultAuthenticationLevel property within the [**LocalComputer**](localcomputer.md) collection is used. |
| Access         | ReadWrite                                                                                                                                                                                                                                                                                             |
| Type           | Long Possible values:COMAdminAuthenticationDefault (0)COMAdminAuthenticationNone (1) COMAdminAuthenticationConnect (2)COMAdminAuthenticationCall (3)COMAdminAuthenticationPacket (4)COMAdminAuthenticationIntegrity (5)COMAdminAuthenticationPrivacy (6)                                              |
| Default        | COMAdminAuthenticationDefault (0)                                                                                                                                                                                                                                                                     |
| Minimum system | Windows XP                                                                                                                                                                                                                                                                                            |



 

> [!Note]  
> It is recommended that you use the constants in the enumeration and not the numeric values.

 

### Bitness



| Entry | Value |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Represents the binary bitness type of the component. On systems that use 64-bit Windows, this property distinguishes between 64-bit components and 32-bit components. |
| Access         | ReadOnly                                                                                                                                                              |
| Type           | Long Possible values:COMAdmin32BitComponent (0x1)COMAdmin64BitComponent (0x2)                                                                                         |
| Default        | N/A                                                                                                                                                                   |
| Minimum system | Windows XP                                                                                                                                                            |



 

### ClassName



| Entry | Value |
|----------------|------------------------|
| Description    | The name of the class. |
| Access         | ReadOnly               |
| Type           | String                 |
| Default        | N/A                    |
| Minimum system | Windows XP             |



 

### CLSID



| Entry | Value |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | A GUID for the component. This property is returned when the [**Key**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_key) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                                  |
| Type           | String                                                                                                                                                    |
| Default        | N/A                                                                                                                                                       |
| Minimum system | Windows XP                                                                                                                                                |



 

### DllSurrogate



| Entry | Value |
|----------------|------------------------------------------------------------|
| Description    | Specifies the full path to a surragate server application. |
| Access         | ReadWrite                                                  |
| Type           | String                                                     |
| Default        | N/A                                                        |
| Minimum system | Windows XP                                                 |



 

### InprocHandler32



| Entry | Value |
|----------------|--------------------------------------------------------------------|
| Description    | Specifies the full path to a 32-bit in-process custom handler DLL. |
| Access         | ReadWrite                                                          |
| Type           | String                                                             |
| Default        | N/A                                                                |
| Minimum system | Windows XP                                                         |



 

### InprocServer32



| Entry | Value |
|----------------|------------------------------------------------------------|
| Description    | Specifies the full path to a 32-bit in-process server DLL. |
| Access         | ReadWrite                                                  |
| Type           | String                                                     |
| Default        | N/A                                                        |
| Minimum system | Windows XP                                                 |



 

### IsEnabled



| Entry | Value |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | If the COM+ application or component is disabled, IsEnabled is False. If the COM+ application or component is enabled, IsEnabled is True. |
| Access         | ReadWrite                                                                                                                                 |
| Type           | Bool                                                                                                                                      |
| Default        | True                                                                                                                                      |
| Minimum system | Windows XP                                                                                                                                |



 

### LaunchPermissions



| Entry | Value |
|----------------|----------------------------------------------------------------------------------------|
| Description    | Specifies user accounts that are allowed or denied permission to start this component. |
| Access         | ReadWrite                                                                              |
| Type           | String                                                                                 |
| Default        | N/A                                                                                    |
| Minimum system | Windows XP                                                                             |



 

### LocalServer32



| Entry | Value |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Specifies the full path to a 32-bit local server application. To help protect system security, use quoted strings in the path to indicate where the executable filename ends and the arguments begin. For example, "\\"C:\\Program Files\\Company Files\\Application.exe\\" param1 param2". |
| Access         | ReadWrite                                                                                                                                                                                                                                                                                   |
| Type           | String                                                                                                                                                                                                                                                                                      |
| Default        | N/A                                                                                                                                                                                                                                                                                         |
| Minimum system | Windows XP                                                                                                                                                                                                                                                                                  |



 

### LocalService



| Entry | Value |
|----------------|-----------------------------------------------------|
| Description    | Specifies the full path to the service application. |
| Access         | ReadWrite                                           |
| Type           | String                                              |
| Default        | N/A                                                 |
| Minimum system | Windows XP                                          |



 

### Password



| Entry | Value |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Sets the password used by the server process to log on under the specified RunAs identity. Password should be set at the same time as the RunAs identity, prior to using [**SaveChanges**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-savechanges), because the password and identity are validated before being saved. If the password and identity get out of sync, the component cannot be launched until they are reset by an administrator. |
| Access         | WriteOnly                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Type           | String                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Default        | NULL                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Minimum system | Windows XP                                                                                                                                                                                                                                                                                                                                                                                                                   |



 

### ProgID



| Entry | Value |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Description    | A name identifying the component. This property is returned when the Name property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                             |
| Type           | String                                                                                                                               |
| Default        | N/A                                                                                                                                  |
| Minimum system | Windows XP                                                                                                                           |



 

### RemoteServer



| Entry | Value |
|----------------|---------------------------------------|
| Description    | Specifies the remote server computer. |
| Access         | ReadWrite                             |
| Type           | String                                |
| Default        | N/A                                   |
| Minimum system | Windows XP                            |



 

### RunAs



| Entry | Value |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Specifies the user under whose identity the component will run. Password should be set at the same time as the RunAs identity, prior to using [**SaveChanges**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-savechanges), because the password and identity are validated before being saved. If the password and identity get out of sync, the component cannot be launched until they are reset by an administrator. |
| Access         | ReadWrite                                                                                                                                                                                                                                                                                                                                                                                         |
| Type           | String                                                                                                                                                                                                                                                                                                                                                                                            |
| Default        | N/A                                                                                                                                                                                                                                                                                                                                                                                               |
| Minimum system | Windows XP                                                                                                                                                                                                                                                                                                                                                                                        |



 

### ServiceParameter



| Entry | Value |
|----------------|-------------------------------------------------------------------------------------------|
| Description    | Specifies the parameters passed to the application when invoked as a service application. |
| Access         | ReadWrite                                                                                 |
| Type           | String                                                                                    |
| Default        | N/A                                                                                       |
| Minimum system | Windows XP                                                                                |



 

### SRPTrustLevel



| Entry | Value |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Indicates the software restriction policy (SRP) trust level of the component. The SRP trust level refers to the level of trust that you are willing to give to a component. An Unrestricted SRP trust level corresponds to the SAFER\_LEVELID\_FULLYTRUSTED enum value, while a Disallowed SRP trust level corresponds to the SAFER\_LEVELID\_DISALLOWED enum value. The enumeration for the trust levels is defined in Winsafer.h. |
| Access         | ReadWrite                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Type           | Long Possible values:SAFER\_LEVELID\_DISALLOWED (0x0)SAFER\_LEVELID\_FULLYTRUSTED (0x40000)                                                                                                                                                                                                                                                                                                                                         |
| Default        | SAFER\_LEVELID\_FULLYTRUSTED                                                                                                                                                                                                                                                                                                                                                                                                        |
| Minimum system | Windows XP                                                                                                                                                                                                                                                                                                                                                                                                                          |



 

A component that you are willing to trust with Unrestricted access should have the most stringent security attached to it. Applications that are Unrestricted can load only unrestricted components, while Disallowed applications will not be allowed to run and therefore cannot load any components.

### ThreadingModel



| Entry | Value |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Determines how instances of the component are assigned to threads for method execution. Values correspond to COM threading models.                                                  |
| Access         | ReadOnly                                                                                                                                                                            |
| Type           | Long Possible values:COMAdminThreadingModelApartment (0)COMAdminThreadingModelFree (1)COMAdminThreadingModelMain (2)COMAdminThreadingModelBoth (3)COMAdminThreadingModelNeutral (4) |
| Default        | N/A                                                                                                                                                                                 |
| Minimum system | Windows XP                                                                                                                                                                          |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 
