---
title: ITsSbResourcePluginStoreEx interface
description: Exposes methods that enable resource plug-ins to store objects such as sessions and targets.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '768a5a4e-8221-417a-ad65-9a213a176eca'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["ITsSbResourcePluginStoreEx interface Remote Desktop Services", "ITsSbResourcePluginStoreEx interface Remote Desktop Services , described"]
topic_type:
- apiref
api_name:
- ITsSbResourcePluginStoreEx
api_type:
- COM
---

# ITsSbResourcePluginStoreEx interface

Exposes methods that enable resource plug-ins to store objects such as sessions and targets. These methods add, delete, and query these objects.

This interface is only available on Windows Server 2012 R2 with [KB3091411](https://support.microsoft.com/kb/3091411) installed. The [**AcquireTargetLock**](itssbresourcepluginstore-acquiretargetlock.md) and [**ReleaseTargetLock**](itssbresourcepluginstore-releasetargetlock.md) methods of the [**ITsSbResourcePluginStore**](itssbresourcepluginstore.md) interface are available starting with Windows Server 2016.

## Members

The **ITsSbResourcePluginStoreEx** interface inherits from [**ITsSbResourcePluginStore**](itssbresourcepluginstore.md). **ITsSbResourcePluginStoreEx** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITsSbResourcePluginStoreEx** interface has these methods.



| Method                                                                                                            | Description                                                                                                     |
|:------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------|
| [**AcquireTargetLock**](itssbresourcepluginstoreex-acquiretargetlock.md)                                         | Locks a target.<br/>                                                                                      |
| [**AddEnvironmentToStore**](itssbresourcepluginstore-addenvironmenttostore.md)                                   | Adds an environment to the resource plug-in store.<br/>                                                   |
| [**AddSessionToStore**](itssbresourcepluginstore-addsessiontostore.md)                                           | Adds a new session to the resource plug-in store.<br/>                                                    |
| [**AddTargetToStore**](itssbresourcepluginstore-addtargettostore.md)                                             | Adds a target to the resource plug-in store.<br/>                                                         |
| [**DeleteTarget**](itssbresourcepluginstore-deletetarget.md)                                                     | Deletes a target.<br/>                                                                                    |
| [**EnumerateEnvironments**](itssbresourcepluginstore-enumerateenvironments.md)                                   | Returns an array that contains the environments present in the resource plug-in store.<br/>               |
| [**EnumerateFarms**](itssbresourcepluginstore-enumeratefarms.md)                                                 | Enumerates all the farms that have been added to the resource plug-in store.<br/>                         |
| [**EnumerateSessions**](itssbresourcepluginstore-enumeratesessions.md)                                           | Enumerates a specified set of sessions.<br/>                                                              |
| [**EnumerateTargets**](itssbresourcepluginstore-enumeratetargets.md)                                             | Returns an array that contains the specified targets that are present in the resource plug-in store.<br/> |
| [**GetFarmProperty**](itssbresourcepluginstore-getfarmproperty.md)                                               | Retrieves a property of a farm.<br/>                                                                      |
| [**QueryEnvironment**](itssbresourcepluginstore-queryenvironment.md)                                             | Returns the specified environment object.<br/>                                                            |
| [**QuerySessionBySessionId**](itssbresourcepluginstore-querysessionbysessionid.md)                               | Returns the session object that has the specified session ID.<br/>                                        |
| [**QueryTarget**](itssbresourcepluginstore-querytarget.md)                                                       | Returns the target that has the specified target name and farm name.<br/>                                 |
| [**ReleaseTargetLock**](itssbresourcepluginstoreex-releasetargetlock.md)                                         | Releases a lock on a target.<br/>                                                                         |
| [**RemoveEnvironmentFromStore**](itssbresourcepluginstore-removeenvironmentfromstore.md)                         | Removes the specified environment from the resource plug-in store.<br/>                                   |
| [**SaveEnvironment**](itssbresourcepluginstore-saveenvironment.md)                                               | Saves an environment.<br/>                                                                                |
| [**SaveSession**](itssbresourcepluginstore-savesession.md)                                                       | Saves a session.<br/>                                                                                     |
| [**SaveTarget**](itssbresourcepluginstore-savetarget.md)                                                         | Saves a target.<br/>                                                                                      |
| [**SetEnvironmentProperty**](itssbresourcepluginstore-setenvironmentproperty.md)                                 | Sets a property on an environment.<br/>                                                                   |
| [**SetEnvironmentPropertyWithVersionCheck**](itssbresourcepluginstore-setenvironmentpropertywithversioncheck.md) | Sets a property on an environment.<br/>                                                                   |
| [**SetSessionState**](itssbresourcepluginstore-setsessionstate.md)                                               | Sets the state of a session.<br/>                                                                         |
| [**SetTargetProperty**](itssbresourcepluginstore-settargetproperty.md)                                           | Sets a property on a target.<br/>                                                                         |
| [**SetTargetPropertyWithVersionCheck**](itssbresourcepluginstore-settargetpropertywithversioncheck.md)           | Sets a property on a target.<br/>                                                                         |
| [**SetTargetState**](itssbresourcepluginstore-settargetstate.md)                                                 | Sets the state of a target.<br/>                                                                          |



 

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                             |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                             |
| IID<br/>                      | IID\_ITsSbResourcePluginStoreEx is defined as 80b83ffd-625d-11e5-bea1-a0481c7e9064<br/> |



## See also

<dl> <dt>

[**ITsSbResourcePluginStore**](itssbresourcepluginstore.md)
</dt> <dt>

[Remote Desktop Virtualization Interfaces](remote-desktop-virtualization-interfaces.md)
</dt> </dl>

 

 





