---
description: The following functions are used or implemented by services.
ms.assetid: 63666848-cbac-4853-8b91-89303f9854c0
title: Service Functions
ms.topic: article
ms.date: 05/31/2018
---

# Service Functions

The following functions are used or implemented by services.



| Function                                                             | Description                                                                                                                           |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**Handler**](/windows/desktop/api/Winsvc/nc-winsvc-lphandler_function)                                           | An application-defined callback function used with the [**RegisterServiceCtrlHandler**](/windows/desktop/api/Winsvc/nf-winsvc-registerservicectrlhandlera) function.     |
| [**HandlerEx**](/windows/desktop/api/WinSvc/nc-winsvc-lphandler_function_ex)                                       | An application-defined callback function used with the [**RegisterServiceCtrlHandlerEx**](/windows/desktop/api/Winsvc/nf-winsvc-registerservicectrlhandlerexa) function. |
| [**RegisterServiceCtrlHandler**](/windows/desktop/api/Winsvc/nf-winsvc-registerservicectrlhandlera)     | Registers a function to handle service control requests.                                                                              |
| [**RegisterServiceCtrlHandlerEx**](/windows/desktop/api/Winsvc/nf-winsvc-registerservicectrlhandlerexa) | Registers a function to handle extended service control requests.                                                                     |
| [**ServiceMain**](/windows/win32/api/winsvc/nc-winsvc-lpservice_main_functiona)                                   | An application-defined function that serves as the starting point for a service.                                                      |
| [**SetServiceBits**](/windows/desktop/api/Lmserver/nf-lmserver-setservicebits)                             | Registers a service type with the service control manager and the Server service.                                                     |
| [**SetServiceStatus**](/windows/desktop/api/Winsvc/nf-winsvc-setservicestatus)                         | Updates the service control manager's status information for the calling service.                                                     |
| [**StartServiceCtrlDispatcher**](/windows/desktop/api/Winsvc/nf-winsvc-startservicectrldispatchera)     | Connects the main thread of a service process to the service control manager.                                                         |



 

The following functions are used by programs that control, configure, or interact with services.



| Function                                                                 | Description                                                                                                                                 |
|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [**ChangeServiceConfig**](/windows/desktop/api/Winsvc/nf-winsvc-changeserviceconfiga)                       | Changes the configuration parameters of a service.                                                                                          |
| [**ChangeServiceConfig2**](/windows/desktop/api/Winsvc/nf-winsvc-changeserviceconfig2a)                     | Changes the optional configuration parameters of a service.                                                                                 |
| [**CloseServiceHandle**](/windows/desktop/api/Winsvc/nf-winsvc-closeservicehandle)                         | Closes the specified handle to a service control manager object or a service object.                                                        |
| [**ControlService**](/windows/desktop/api/Winsvc/nf-winsvc-controlservice)                                 | Sends a control code to a service.                                                                                                          |
| [**ControlServiceEx**](/windows/desktop/api/Winsvc/nf-winsvc-controlserviceexa)                             | Sends a control code to a service.                                                                                                          |
| [**CreateService**](/windows/desktop/api/Winsvc/nf-winsvc-createservicea)                                   | Creates a service object and adds it to the specified service control manager database.                                                     |
| [**DeleteService**](/windows/desktop/api/Winsvc/nf-winsvc-deleteservice)                                   | Marks the specified service for deletion from the service control manager database.                                                         |
| [**EnumDependentServices**](/windows/desktop/api/Winsvc/nf-winsvc-enumdependentservicesa)                   | Retrieves the name and status of each service that depends on the specified service.                                                        |
| [**EnumServicesStatusEx**](/windows/desktop/api/Winsvc/nf-winsvc-enumservicesstatusexa)                     | Enumerates services in the specified service control manager database based on the specified information level.                             |
| [**GetServiceDisplayName**](/windows/desktop/api/Winsvc/nf-winsvc-getservicedisplaynamea)                   | Retrieves the display name of the specified service.                                                                                        |
| [**GetServiceKeyName**](/windows/desktop/api/Winsvc/nf-winsvc-getservicekeynamea)                           | Retrieves the service name of the specified service.                                                                                        |
| [**NotifyBootConfigStatus**](/windows/desktop/api/Winsvc/nf-winsvc-notifybootconfigstatus)                 | Reports the boot status to the service control manager.                                                                                     |
| [**NotifyServiceStatusChange**](/windows/desktop/api/Winsvc/nf-winsvc-notifyservicestatuschangea)           | Enables an application to receive notification when the specified service is created or deleted or when its status changes.                 |
| [**OpenSCManager**](/windows/desktop/api/Winsvc/nf-winsvc-openscmanagera)                                   | Establishes a connection to the service control manager on the specified computer and opens the specified service control manager database. |
| [**OpenService**](/windows/desktop/api/Winsvc/nf-winsvc-openservicea)                                       | Opens an existing service.                                                                                                                  |
| [**QueryServiceConfig**](/windows/desktop/api/Winsvc/nf-winsvc-queryserviceconfiga)                         | Retrieves the configuration parameters of the specified service.                                                                            |
| [**QueryServiceConfig2**](/windows/desktop/api/Winsvc/nf-winsvc-queryserviceconfig2a)                       | Retrieves the optional configuration parameters of the specified service.                                                                   |
| [**QueryServiceDynamicInformation**](/windows/desktop/api/Winsvc/nf-winsvc-queryservicedynamicinformation) | Retrieves dynamic information related to the current service start.                                                                         |
| [**QueryServiceObjectSecurity**](/windows/desktop/api/winsvc/nf-winsvc-queryserviceobjectsecurity)    | Retrieves a copy of the security descriptor associated with a service object.                                                               |
| [**QueryServiceStatusEx**](/windows/desktop/api/Winsvc/nf-winsvc-queryservicestatusex)                     | Retrieves the current status of the specified service based on the specified information level.                                             |
| [**SetServiceObjectSecurity**](/windows/desktop/api/winsvc/nf-winsvc-setserviceobjectsecurity)        | Sets the security descriptor of a service object.                                                                                           |
| [**StartService**](/windows/desktop/api/Winsvc/nf-winsvc-startservicea)                                     | Starts a service.                                                                                                                           |



 

## Obsolete Functions

The following functions are obsolete.<dl>

[**EnumServicesStatus**](/windows/desktop/api/Winsvc/nf-winsvc-enumservicesstatusa)  
[**LockServiceDatabase**](/windows/desktop/api/Winsvc/nf-winsvc-lockservicedatabase)  
[**QueryServiceLockStatus**](/windows/desktop/api/Winsvc/nf-winsvc-queryservicelockstatusa)  
[**QueryServiceStatus**](/windows/desktop/api/Winsvc/nf-winsvc-queryservicestatus)  
[**UnlockServiceDatabase**](/windows/desktop/api/Winsvc/nf-winsvc-unlockservicedatabase)  
</dl>

 

 
