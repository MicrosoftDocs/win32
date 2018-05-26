---
title: ITsSbResourcePluginStoreEx interface
description: Exposes methods that enable resource plug-ins to store objects such as sessions and targets.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 768a5a4e-8221-417a-ad65-9a213a176eca
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- ITsSbResourcePluginStoreEx interface Remote Desktop Services
- ITsSbResourcePluginStoreEx interface Remote Desktop Services , described
topic_type:
- apiref
api_name:
- ITsSbResourcePluginStoreEx
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# ITsSbResourcePluginStoreEx interface

Exposes methods that enable resource plug-ins to store objects such as sessions and targets. These methods add, delete, and query these objects.

This interface is only available on Windows Server 2012 R2 with [KB3091411](https://support.microsoft.com/kb/3091411) installed. The [**AcquireTargetLock**](/windows/win32/sbtsv/nf-sbtsv-itssbresourcepluginstore-acquiretargetlock?branch=master) and [**ReleaseTargetLock**](/windows/win32/sbtsv/nf-sbtsv-itssbresourcepluginstore-releasetargetlock?branch=master) methods of the [**ITsSbResourcePluginStore**](/windows/win32/sbtsv/nn-sbtsv-itssbresourcepluginstore?branch=master) interface are available starting with Windows Server 2016.

## Members

The **ITsSbResourcePluginStoreEx** interface inherits from [**ITsSbResourcePluginStore**](/windows/win32/sbtsv/nn-sbtsv-itssbresourcepluginstore?branch=master). **ITsSbResourcePluginStoreEx** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITsSbResourcePluginStoreEx** interface has these methods.



| Method                                                                                                            | Description                                                                                                     |
|:------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------|
| [**AcquireTargetLock**](itssbresourcepluginstoreex-acquiretargetlock.md)                                         | Locks a target.<br/>                                                                                      |
| [**AddEnvironmentToStore**](/windows/win32/sbtsv/nf-sbtsv-itssbresourcepluginstore-addenvironmenttostore?branch=master)                                   | Adds an environment to the resource plug-in store.<br/>                                                   |
| [**AddSessionToStore**](/windows/win32/sbtsv/nf-sbtsv-itssbresourcepluginstore-addsessiontostore?branch=master)                                           | Adds a new session to the resource plug-in store.<br/>                                                    |
| [**AddTargetToStore**](/windows/win32/sbtsv/nf-sbtsv-itssbresourcepluginstore-addtargettostore?branch=master)                                             | Adds a target to the resource plug-in store.<br/>                                                         |
| [**DeleteTarget**](/windows/win32/sbtsv/nf-sbtsv-itssbresourcepluginstore-deletetarget?branch=master)                                                     | Deletes a target.<br/>                                                                                    |
| [**EnumerateEnvironments**](/windows/win32/sbtsv/nf-sbtsv-itssbresourcepluginstore-enumerateenvironments?branch=master)                                   | Returns an array that contains the environments present in the resource plug-in store.<br/>               |
| [**EnumerateFarms**](/windows/win32/sbtsv/nf-sbtsv-itssbresourcepluginstore-enumeratefarms?branch=master)                                                 | Enumerates all the farms that have been added to the resource plug-in store.<br/>                         |
| [**EnumerateSessions**](/windows/win32/sbtsv/nf-sbtsv-itssbresourcepluginstore-enumeratesessions?branch=master)                                           | Enumerates a specified set of sessions.<br/>                                                              |
| [**EnumerateTargets**](/windows/win32/sbtsv/nf-sbtsv-itssbresourcepluginstore-enumeratetargets?branch=master)                                             | Returns an array that contains the specified targets that are present in the resource plug-in store.<br/> |
| [**GetFarmProperty**](/windows/win32/sbtsv/nf-sbtsv-itssbresourcepluginstore-getfarmproperty?branch=master)                                               | Retrieves a property of a farm.<br/>                                                                      |
| [**QueryEnvironment**](/windows/win32/sbtsv/nf-sbtsv-itssbresourcepluginstore-queryenvironment?branch=master)                                             | Returns the specified environment object.<br/>                                                            |
| [**QuerySessionBySessionId**](/windows/win32/sbtsv/nf-sbtsv-itssbresourcepluginstore-querysessionbysessionid?branch=master)                               | Returns the session object that has the specified session ID.<br/>                                        |
| [**QueryTarget**](/windows/win32/sbtsv/nf-sbtsv-itssbresourcepluginstore-querytarget?branch=master)                                                       | Returns the target that has the specified target name and farm name.<br/>                                 |
| [**ReleaseTargetLock**](itssbresourcepluginstoreex-releasetargetlock.md)                                         | Releases a lock on a target.<br/>                                                                         |
| [**RemoveEnvironmentFromStore**](/windows/win32/sbtsv/nf-sbtsv-itssbresourcepluginstore-removeenvironmentfromstore?branch=master)                         | Removes the specified environment from the resource plug-in store.<br/>                                   |
| [**SaveEnvironment**](/windows/win32/sbtsv/nf-sbtsv-itssbresourcepluginstore-saveenvironment?branch=master)                                               | Saves an environment.<br/>                                                                                |
| [**SaveSession**](/windows/win32/sbtsv/nf-sbtsv-itssbresourcepluginstore-savesession?branch=master)                                                       | Saves a session.<br/>                                                                                     |
| [**SaveTarget**](/windows/win32/sbtsv/nf-sbtsv-itssbresourcepluginstore-savetarget?branch=master)                                                         | Saves a target.<br/>                                                                                      |
| [**SetEnvironmentProperty**](/windows/win32/sbtsv/nf-sbtsv-itssbresourcepluginstore-setenvironmentproperty?branch=master)                                 | Sets a property on an environment.<br/>                                                                   |
| [**SetEnvironmentPropertyWithVersionCheck**](/windows/win32/sbtsv/nf-sbtsv-itssbresourcepluginstore-setenvironmentpropertywithversioncheck?branch=master) | Sets a property on an environment.<br/>                                                                   |
| [**SetSessionState**](/windows/win32/sbtsv/nf-sbtsv-itssbresourcepluginstore-setsessionstate?branch=master)                                               | Sets the state of a session.<br/>                                                                         |
| [**SetTargetProperty**](/windows/win32/sbtsv/nf-sbtsv-itssbresourcepluginstore-settargetproperty?branch=master)                                           | Sets a property on a target.<br/>                                                                         |
| [**SetTargetPropertyWithVersionCheck**](/windows/win32/sbtsv/nf-sbtsv-itssbresourcepluginstore-settargetpropertywithversioncheck?branch=master)           | Sets a property on a target.<br/>                                                                         |
| [**SetTargetState**](/windows/win32/sbtsv/nf-sbtsv-itssbresourcepluginstore-settargetstate?branch=master)                                                 | Sets the state of a target.<br/>                                                                          |



 

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                             |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                             |
| IID<br/>                      | IID\_ITsSbResourcePluginStoreEx is defined as 80b83ffd-625d-11e5-bea1-a0481c7e9064<br/> |



## See also

<dl> <dt>

[**ITsSbResourcePluginStore**](/windows/win32/sbtsv/nn-sbtsv-itssbresourcepluginstore?branch=master)
</dt> <dt>

[Remote Desktop Virtualization Interfaces](remote-desktop-virtualization-interfaces.md)
</dt> </dl>

 

 





