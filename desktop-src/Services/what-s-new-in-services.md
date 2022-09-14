---
description: Windows 7 and Windows Server 2008 R2 include the following new and updated programming elements for services.
ms.assetid: 4be7e244-ad4c-440d-b04e-23afb4c7ddf2
title: Whats New in Services for Windows 7
ms.topic: article
ms.date: 05/31/2018
---

# What's New in Services for Windows 7

Windows 7 and Windows Server 2008 R2 include the following new and updated programming elements for services.

## New Capabilities

A service can register to be started or stopped when a trigger event occurs. This eliminates the need for services to start when the system starts, or for services to poll or actively wait for an event; a service can start when it is needed, instead of starting automatically whether or not there is work to do. For more information, see [Service Trigger Events](service-trigger-events.md).

## Updated Functions



| Function                                                        | Description                                                                                                                                                                                                                                                                                |
|-----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ChangeServiceConfig**](/windows/desktop/api/Winsvc/nf-winsvc-changeserviceconfiga)<br/>   | Changes the configuration parameters of a service. This function supports managed service accounts and virtual accounts. For more information, see [Service Accounts Step-by-Step Guide](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd548356(v=ws.10)).<br/>                                      |
| [**ChangeServiceConfig2**](/windows/desktop/api/Winsvc/nf-winsvc-changeserviceconfig2a)<br/> | Changes the optional configuration parameters of a service. This function supports new configuration information levels for processor groups and service trigger events.<br/>                                                                                                        |
| [**CreateService**](/windows/desktop/api/Winsvc/nf-winsvc-createservicea)<br/>               | Creates a service object and adds it to the specified service control manager database. This function supports managed service accounts and virtual accounts. For more information, see [Service Accounts Step-by-Step Guide](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd548356(v=ws.10)).<br/> |
| [**HandlerEx**](/windows/desktop/api/WinSvc/nc-winsvc-lphandler_function_ex)<br/>                       | An application-defined callback function used with the [**RegisterServiceCtrlHandlerEx**](/windows/desktop/api/Winsvc/nf-winsvc-registerservicectrlhandlerexa) function. This callback function supports new extended control codes for system time changes and service trigger events.<br/>                            |
| [**QueryServiceConfig2**](/windows/desktop/api/Winsvc/nf-winsvc-queryserviceconfig2a)<br/>   | Retrieves the optional configuration parameters of a service. This function supports new configuration information levels for processor groups and service trigger events.<br/>                                                                                                      |
| [**SetServiceStatus**](/windows/desktop/api/Winsvc/nf-winsvc-setservicestatus)<br/>         | Updates the service control manager's status information for the calling service. This function supports new extended control codes for system time changes and service trigger events.<br/>                                                                                         |



 

## New Structures



| Structure                                                                                       | Description                                                            |
|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| [**SERVICE\_TIMECHANGE\_INFO**](/windows/desktop/api/winsvc/ns-winsvc-service_timechange_info)<br/>                         | Contains system time change settings. <br/>                      |
| [**SERVICE\_TRIGGER**](/windows/desktop/api/winsvc/ns-winsvc-service_trigger)<br/>                                          | Represents a service trigger event.<br/>                         |
| [**SERVICE\_TRIGGER\_INFO**](/windows/desktop/api/winsvc/ns-winsvc-service_trigger_info)<br/>                               | Contains trigger event information for a service.<br/>           |
| [**SERVICE\_TRIGGER\_SPECIFIC\_DATA\_ITEM**](/windows/desktop/api/winsvc/ns-winsvc-service_trigger_specific_data_item)<br/> | Contains trigger-specific data for a service trigger event.<br/> |



 

 

