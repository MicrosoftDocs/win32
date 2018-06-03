---
Description: This API enables developer tools to debug Windows apps using JavaScript running in the app host.
ms.assetid: 43996903-E0B8-440B-88CA-610D859B340B
title: Debugging and authoring support for Windows apps using JavaScript
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Debugging and authoring support for Windows apps using JavaScript

This API enables developer tools to debug Windows apps using JavaScript running in the app host.

## In this section



| Topic                                                                                             | Description                                                                                                                                                                                                                                         |
|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWebApplicationActivation**](/previous-versions/windows/desktop/api/WebApplication/nn-webapplication-iwebapplicationactivation)<br/>                         | Enables debugging applications to manage activations.<br/>                                                                                                                                                                                    |
| [**IWebApplicationAuthoringMode**](/previous-versions/windows/desktop/api/webapplication/nn-webapplication-iwebapplicationauthoringmode)<br/>                   | Provides the full local path to the authoring binary to be loaded into the WWAHost process.<br/>                                                                                                                                              |
| [**IWebApplicationHost**](/previous-versions/windows/desktop/api/webapplication/nn-webapplication-iwebapplicationhost)<br/>                                     | Exposes methods and properties that are implemented by the WWAHost.<br/>                                                                                                                                                                      |
| [**IWebApplicationNavigationEvents**](/previous-versions/windows/desktop/api/webapplication/nn-webapplication-iwebapplicationnavigationevents)<br/>             | Enables a debugging or authoring app to receive notification of navigation events.<br/>                                                                                                                                                       |
| [**IWebApplicationScriptEvents**](/previous-versions/windows/desktop/api/webapplication/nn-webapplication-iwebapplicationscriptevents)<br/>                     | Enables a debugging or authoring app to receive notification of scripting engine events.<br/>                                                                                                                                                 |
| [**IWebApplicationUIEvents**](/previous-versions/windows/desktop/api/webapplication/nn-webapplication-iwebapplicationuievents)<br/>                             | Enables a debugging or authoring app to receive notification of user interface events and respond to events that require user interaction.<br/>                                                                                               |
| [**IWebApplicationUpdateEvents**](/previous-versions/windows/desktop/api/webapplication/nn-webapplication-iwebapplicationupdateevents)<br/>                     | Enables an authoring app to receive notification of designer events and respond to those events.<br/>                                                                                                                                         |
| [**RegisterAuthoringClientFunctionType**](/previous-versions/windows/desktop/api/webapplication/nc-webapplication-registerauthoringclientfunctiontype)<br/>     | Defines a pointer to an application-defined function in a dynamic-link library (DLL) that will be used as the authoring binary. When the app host starts in authoring mode, this function is called to initialize the authoring binary. <br/> |
| [**UnregisterAuthoringClientFunctionType**](/previous-versions/windows/desktop/api/webapplication/nc-webapplication-unregisterauthoringclientfunctiontype)<br/> | Unregisters the application-defined function that was registered with the [**RegisterAuthoringClientFunctionType**](/previous-versions/windows/desktop/api/webapplication/nc-webapplication-registerauthoringclientfunctiontype) function. This function is called when the app host terminates.<br/>             |



 

 

 




