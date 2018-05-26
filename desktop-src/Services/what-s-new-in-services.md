---
Description: Windows 7 and Windows Server 2008 R2 include the following new and updated programming elements for services.
ms.assetid: 4be7e244-ad4c-440d-b04e-23afb4c7ddf2
title: Whats New in Services for Windows 7
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# What's New in Services for Windows 7

Windows 7 and Windows Server 2008 R2 include the following new and updated programming elements for services.

## New Capabilities

A service can register to be started or stopped when a trigger event occurs. This eliminates the need for services to start when the system starts, or for services to poll or actively wait for an event; a service can start when it is needed, instead of starting automatically whether or not there is work to do. For more information, see [Service Trigger Events](service-trigger-events.md).

## Updated Functions



| Function                                                        | Description                                                                                                                                                                                                                                                                                |
|-----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ChangeServiceConfig**](/windows/win32/Winsvc/nf-winsvc-changeserviceconfiga?branch=master)<br/>   | Changes the configuration parameters of a service. This function supports managed service accounts and virtual accounts. For more information, see [Service Accounts Step-by-Step Guide](http://go.microsoft.com/fwlink/p/?linkid=147314).<br/>                                      |
| [**ChangeServiceConfig2**](/windows/win32/Winsvc/nf-winsvc-changeserviceconfig2a?branch=master)<br/> | Changes the optional configuration parameters of a service. This function supports new configuration information levels for processor groups and service trigger events.<br/>                                                                                                        |
| [**CreateService**](/windows/win32/Winsvc/nf-winsvc-createservicea?branch=master)<br/>               | Creates a service object and adds it to the specified service control manager database. This function supports managed service accounts and virtual accounts. For more information, see [Service Accounts Step-by-Step Guide](http://go.microsoft.com/fwlink/p/?linkid=147314).<br/> |
| [**HandlerEx**](/windows/win32/WinSvc/nc-winsvc-lphandler_function_ex?branch=master)<br/>                       | An application-defined callback function used with the [**RegisterServiceCtrlHandlerEx**](/windows/win32/Winsvc/nf-winsvc-registerservicectrlhandlerexa?branch=master) function. This callback function supports new extended control codes for system time changes and service trigger events.<br/>                            |
| [**QueryServiceConfig2**](/windows/win32/Winsvc/nf-winsvc-queryserviceconfig2a?branch=master)<br/>   | Retrieves the optional configuration parameters of a service. This function supports new configuration information levels for processor groups and service trigger events.<br/>                                                                                                      |
| [**SetServiceStatus**](/windows/win32/Winsvc/nf-winsvc-setservicestatus?branch=master)<br/>         | Updates the service control manager's status information for the calling service. This function supports new extended control codes for system time changes and service trigger events.<br/>                                                                                         |



 

## New Structures



| Structure                                                                                       | Description                                                            |
|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| [**SERVICE\_TIMECHANGE\_INFO**](/windows/win32/winsvc/ns-winsvc-_service_timechange_info?branch=master)<br/>                         | Contains system time change settings. <br/>                      |
| [**SERVICE\_TRIGGER**](/windows/win32/winsvc/ns-winsvc-_service_trigger?branch=master)<br/>                                          | Represents a service trigger event.<br/>                         |
| [**SERVICE\_TRIGGER\_INFO**](/windows/win32/winsvc/ns-winsvc-_service_trigger_info?branch=master)<br/>                               | Contains trigger event information for a service.<br/>           |
| [**SERVICE\_TRIGGER\_SPECIFIC\_DATA\_ITEM**](/windows/win32/winsvc/ns-winsvc-_service_trigger_specific_data_item?branch=master)<br/> | Contains trigger-specific data for a service trigger event.<br/> |



 

 

 




