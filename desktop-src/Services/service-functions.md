---
Description: The following functions are used or implemented by services.
ms.assetid: 63666848-cbac-4853-8b91-89303f9854c0
title: Service Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Service Functions

The following functions are used or implemented by services.



| Function                                                             | Description                                                                                                                           |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**Handler**](/windows/win32/Winsvc/nc-winsvc-lphandler_function?branch=master)                                           | An application-defined callback function used with the [**RegisterServiceCtrlHandler**](/windows/win32/Winsvc/nf-winsvc-registerservicectrlhandlera?branch=master) function.     |
| [**HandlerEx**](/windows/win32/WinSvc/nc-winsvc-lphandler_function_ex?branch=master)                                       | An application-defined callback function used with the [**RegisterServiceCtrlHandlerEx**](/windows/win32/Winsvc/nf-winsvc-registerservicectrlhandlerexa?branch=master) function. |
| [**RegisterServiceCtrlHandler**](/windows/win32/Winsvc/nf-winsvc-registerservicectrlhandlera?branch=master)     | Registers a function to handle service control requests.                                                                              |
| [**RegisterServiceCtrlHandlerEx**](/windows/win32/Winsvc/nf-winsvc-registerservicectrlhandlerexa?branch=master) | Registers a function to handle extended service control requests.                                                                     |
| [**ServiceMain**](servicemain.md)                                   | An application-defined function that serves as the starting point for a service.                                                      |
| [**SetServiceBits**](/windows/win32/Lmserver/nf-lmserver-setservicebits?branch=master)                             | Registers a service type with the service control manager and the Server service.                                                     |
| [**SetServiceStatus**](/windows/win32/Winsvc/nf-winsvc-setservicestatus?branch=master)                         | Updates the service control manager's status information for the calling service.                                                     |
| [**StartServiceCtrlDispatcher**](/windows/win32/Winsvc/nf-winsvc-startservicectrldispatchera?branch=master)     | Connects the main thread of a service process to the service control manager.                                                         |



 

The following functions are used by programs that control, configure, or interact with services.



| Function                                                                 | Description                                                                                                                                 |
|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [**ChangeServiceConfig**](/windows/win32/Winsvc/nf-winsvc-changeserviceconfiga?branch=master)                       | Changes the configuration parameters of a service.                                                                                          |
| [**ChangeServiceConfig2**](/windows/win32/Winsvc/nf-winsvc-changeserviceconfig2a?branch=master)                     | Changes the optional configuration parameters of a service.                                                                                 |
| [**CloseServiceHandle**](/windows/win32/Winsvc/nf-winsvc-closeservicehandle?branch=master)                         | Closes the specified handle to a service control manager object or a service object.                                                        |
| [**ControlService**](/windows/win32/Winsvc/nf-winsvc-controlservice?branch=master)                                 | Sends a control code to a service.                                                                                                          |
| [**ControlServiceEx**](/windows/win32/Winsvc/nf-winsvc-controlserviceexa?branch=master)                             | Sends a control code to a service.                                                                                                          |
| [**CreateService**](/windows/win32/Winsvc/nf-winsvc-createservicea?branch=master)                                   | Creates a service object and adds it to the specified service control manager database.                                                     |
| [**DeleteService**](/windows/win32/Winsvc/nf-winsvc-deleteservice?branch=master)                                   | Marks the specified service for deletion from the service control manager database.                                                         |
| [**EnumDependentServices**](/windows/win32/Winsvc/nf-winsvc-enumdependentservicesa?branch=master)                   | Retrieves the name and status of each service that depends on the specified service.                                                        |
| [**EnumServicesStatusEx**](/windows/win32/Winsvc/nf-winsvc-enumservicesstatusexa?branch=master)                     | Enumerates services in the specified service control manager database based on the specified information level.                             |
| [**GetServiceDisplayName**](/windows/win32/Winsvc/nf-winsvc-getservicedisplaynamea?branch=master)                   | Retrieves the display name of the specified service.                                                                                        |
| [**GetServiceKeyName**](/windows/win32/Winsvc/nf-winsvc-getservicekeynamea?branch=master)                           | Retrieves the service name of the specified service.                                                                                        |
| [**NotifyBootConfigStatus**](/windows/win32/Winsvc/nf-winsvc-notifybootconfigstatus?branch=master)                 | Reports the boot status to the service control manager.                                                                                     |
| [**NotifyServiceStatusChange**](/windows/win32/Winsvc/nf-winsvc-notifyservicestatuschangea?branch=master)           | Enables an application to receive notification when the specified service is created or deleted or when its status changes.                 |
| [**OpenSCManager**](/windows/win32/Winsvc/nf-winsvc-openscmanagera?branch=master)                                   | Establishes a connection to the service control manager on the specified computer and opens the specified service control manager database. |
| [**OpenService**](/windows/win32/Winsvc/nf-winsvc-openservicea?branch=master)                                       | Opens an existing service.                                                                                                                  |
| [**QueryServiceConfig**](/windows/win32/Winsvc/nf-winsvc-queryserviceconfiga?branch=master)                         | Retrieves the configuration parameters of the specified service.                                                                            |
| [**QueryServiceConfig2**](/windows/win32/Winsvc/nf-winsvc-queryserviceconfig2a?branch=master)                       | Retrieves the optional configuration parameters of the specified service.                                                                   |
| [**QueryServiceDynamicInformation**](/windows/win32/Winsvc/nf-winsvc-queryservicedynamicinformation?branch=master) | Retrieves dynamic information related to the current service start.                                                                         |
| [**QueryServiceObjectSecurity**](https://msdn.microsoft.com/library/windows/desktop/aa379312)    | Retrieves a copy of the security descriptor associated with a service object.                                                               |
| [**QueryServiceStatusEx**](/windows/win32/Winsvc/nf-winsvc-queryservicestatusex?branch=master)                     | Retrieves the current status of the specified service based on the specified information level.                                             |
| [**SetServiceObjectSecurity**](https://msdn.microsoft.com/library/windows/desktop/aa379589)        | Sets the security descriptor of a service object.                                                                                           |
| [**StartService**](/windows/win32/Winsvc/nf-winsvc-startservicea?branch=master)                                     | Starts a service.                                                                                                                           |



 

## Obsolete Functions

The following functions are obsolete.<dl>

[**EnumServicesStatus**](/windows/win32/Winsvc/nf-winsvc-enumservicesstatusa?branch=master)  
[**LockServiceDatabase**](/windows/win32/Winsvc/nf-winsvc-lockservicedatabase?branch=master)  
[**QueryServiceLockStatus**](/windows/win32/Winsvc/nf-winsvc-queryservicelockstatusa?branch=master)  
[**QueryServiceStatus**](/windows/win32/Winsvc/nf-winsvc-queryservicestatus?branch=master)  
[**UnlockServiceDatabase**](/windows/win32/Winsvc/nf-winsvc-unlockservicedatabase?branch=master)  
</dl>

 

 



