---
Description: 'The following functions are used or implemented by services.'
ms.assetid: '63666848-cbac-4853-8b91-89303f9854c0'
title: Service Functions
---

# Service Functions

The following functions are used or implemented by services.



| Function                                                             | Description                                                                                                                           |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**Handler**](handler.md)                                           | An application-defined callback function used with the [**RegisterServiceCtrlHandler**](registerservicectrlhandler.md) function.     |
| [**HandlerEx**](handlerex.md)                                       | An application-defined callback function used with the [**RegisterServiceCtrlHandlerEx**](registerservicectrlhandlerex.md) function. |
| [**RegisterServiceCtrlHandler**](registerservicectrlhandler.md)     | Registers a function to handle service control requests.                                                                              |
| [**RegisterServiceCtrlHandlerEx**](registerservicectrlhandlerex.md) | Registers a function to handle extended service control requests.                                                                     |
| [**ServiceMain**](servicemain.md)                                   | An application-defined function that serves as the starting point for a service.                                                      |
| [**SetServiceBits**](setservicebits.md)                             | Registers a service type with the service control manager and the Server service.                                                     |
| [**SetServiceStatus**](setservicestatus.md)                         | Updates the service control manager's status information for the calling service.                                                     |
| [**StartServiceCtrlDispatcher**](startservicectrldispatcher.md)     | Connects the main thread of a service process to the service control manager.                                                         |



 

The following functions are used by programs that control, configure, or interact with services.



| Function                                                                 | Description                                                                                                                                 |
|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [**ChangeServiceConfig**](changeserviceconfig.md)                       | Changes the configuration parameters of a service.                                                                                          |
| [**ChangeServiceConfig2**](changeserviceconfig2.md)                     | Changes the optional configuration parameters of a service.                                                                                 |
| [**CloseServiceHandle**](closeservicehandle.md)                         | Closes the specified handle to a service control manager object or a service object.                                                        |
| [**ControlService**](controlservice.md)                                 | Sends a control code to a service.                                                                                                          |
| [**ControlServiceEx**](controlserviceex.md)                             | Sends a control code to a service.                                                                                                          |
| [**CreateService**](createservice.md)                                   | Creates a service object and adds it to the specified service control manager database.                                                     |
| [**DeleteService**](deleteservice.md)                                   | Marks the specified service for deletion from the service control manager database.                                                         |
| [**EnumDependentServices**](enumdependentservices.md)                   | Retrieves the name and status of each service that depends on the specified service.                                                        |
| [**EnumServicesStatusEx**](enumservicesstatusex.md)                     | Enumerates services in the specified service control manager database based on the specified information level.                             |
| [**GetServiceDisplayName**](getservicedisplayname.md)                   | Retrieves the display name of the specified service.                                                                                        |
| [**GetServiceKeyName**](getservicekeyname.md)                           | Retrieves the service name of the specified service.                                                                                        |
| [**NotifyBootConfigStatus**](notifybootconfigstatus.md)                 | Reports the boot status to the service control manager.                                                                                     |
| [**NotifyServiceStatusChange**](notifyservicestatuschange.md)           | Enables an application to receive notification when the specified service is created or deleted or when its status changes.                 |
| [**OpenSCManager**](openscmanager.md)                                   | Establishes a connection to the service control manager on the specified computer and opens the specified service control manager database. |
| [**OpenService**](openservice.md)                                       | Opens an existing service.                                                                                                                  |
| [**QueryServiceConfig**](queryserviceconfig.md)                         | Retrieves the configuration parameters of the specified service.                                                                            |
| [**QueryServiceConfig2**](queryserviceconfig2.md)                       | Retrieves the optional configuration parameters of the specified service.                                                                   |
| [**QueryServiceDynamicInformation**](queryservicedynamicinformation.md) | Retrieves dynamic information related to the current service start.                                                                         |
| [**QueryServiceObjectSecurity**](https://msdn.microsoft.com/library/windows/desktop/aa379312)    | Retrieves a copy of the security descriptor associated with a service object.                                                               |
| [**QueryServiceStatusEx**](queryservicestatusex.md)                     | Retrieves the current status of the specified service based on the specified information level.                                             |
| [**SetServiceObjectSecurity**](https://msdn.microsoft.com/library/windows/desktop/aa379589)        | Sets the security descriptor of a service object.                                                                                           |
| [**StartService**](startservice.md)                                     | Starts a service.                                                                                                                           |



 

## Obsolete Functions

The following functions are obsolete.<dl>

[**EnumServicesStatus**](enumservicesstatus.md)  
[**LockServiceDatabase**](lockservicedatabase.md)  
[**QueryServiceLockStatus**](queryservicelockstatus.md)  
[**QueryServiceStatus**](queryservicestatus.md)  
[**UnlockServiceDatabase**](unlockservicedatabase.md)  
</dl>

 

 



