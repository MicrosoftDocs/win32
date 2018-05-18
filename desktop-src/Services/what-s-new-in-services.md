---
Description: 'Windows 7 and Windows Server 2008 R2 include the following new and updated programming elements for services.'
ms.assetid: '4be7e244-ad4c-440d-b04e-23afb4c7ddf2'
title: 'What's New in Services for Windows 7'
---

# What's New in Services for Windows 7

Windows 7 and Windows Server 2008 R2 include the following new and updated programming elements for services.

## New Capabilities

A service can register to be started or stopped when a trigger event occurs. This eliminates the need for services to start when the system starts, or for services to poll or actively wait for an event; a service can start when it is needed, instead of starting automatically whether or not there is work to do. For more information, see [Service Trigger Events](service-trigger-events.md).

## Updated Functions



| Function                                                        | Description                                                                                                                                                                                                                                                                                |
|-----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ChangeServiceConfig**](changeserviceconfig.md)<br/>   | Changes the configuration parameters of a service. This function supports managed service accounts and virtual accounts. For more information, see [Service Accounts Step-by-Step Guide](http://go.microsoft.com/fwlink/p/?linkid=147314).<br/>                                      |
| [**ChangeServiceConfig2**](changeserviceconfig2.md)<br/> | Changes the optional configuration parameters of a service. This function supports new configuration information levels for processor groups and service trigger events.<br/>                                                                                                        |
| [**CreateService**](createservice.md)<br/>               | Creates a service object and adds it to the specified service control manager database. This function supports managed service accounts and virtual accounts. For more information, see [Service Accounts Step-by-Step Guide](http://go.microsoft.com/fwlink/p/?linkid=147314).<br/> |
| [**HandlerEx**](handlerex.md)<br/>                       | An application-defined callback function used with the [**RegisterServiceCtrlHandlerEx**](registerservicectrlhandlerex.md) function. This callback function supports new extended control codes for system time changes and service trigger events.<br/>                            |
| [**QueryServiceConfig2**](queryserviceconfig2.md)<br/>   | Retrieves the optional configuration parameters of a service. This function supports new configuration information levels for processor groups and service trigger events.<br/>                                                                                                      |
| [**SetServiceStatus**](setservicestatus.md)<br/>         | Updates the service control manager's status information for the calling service. This function supports new extended control codes for system time changes and service trigger events.<br/>                                                                                         |



 

## New Structures



| Structure                                                                                       | Description                                                            |
|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| [**SERVICE\_TIMECHANGE\_INFO**](service-timechange-info.md)<br/>                         | Contains system time change settings. <br/>                      |
| [**SERVICE\_TRIGGER**](service-trigger.md)<br/>                                          | Represents a service trigger event.<br/>                         |
| [**SERVICE\_TRIGGER\_INFO**](service-trigger-info.md)<br/>                               | Contains trigger event information for a service.<br/>           |
| [**SERVICE\_TRIGGER\_SPECIFIC\_DATA\_ITEM**](service-trigger-specific-data-item.md)<br/> | Contains trigger-specific data for a service trigger event.<br/> |



 

 

 




