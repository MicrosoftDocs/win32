---
Description: This API enables developer tools to debug Windows apps using JavaScript running in the app host.
ms.assetid: 43996903-E0B8-440B-88CA-610D859B340B
title: Debugging and authoring support for Windows apps using JavaScript
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Debugging and authoring support for Windows apps using JavaScript

This API enables developer tools to debug Windows apps using JavaScript running in the app host.

## In this section



| Topic                                                                                             | Description                                                                                                                                                                                                                                         |
|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWebApplicationActivation**](/windows/previous-versions/WebApplication/nn-webapplication-iwebapplicationactivation?branch=master)<br/>                         | Enables debugging applications to manage activations.<br/>                                                                                                                                                                                    |
| [**IWebApplicationAuthoringMode**](/windows/previous-versions/webapplication/nn-webapplication-iwebapplicationauthoringmode?branch=master)<br/>                   | Provides the full local path to the authoring binary to be loaded into the WWAHost process.<br/>                                                                                                                                              |
| [**IWebApplicationHost**](/windows/previous-versions/webapplication/nn-webapplication-iwebapplicationhost?branch=master)<br/>                                     | Exposes methods and properties that are implemented by the WWAHost.<br/>                                                                                                                                                                      |
| [**IWebApplicationNavigationEvents**](/windows/previous-versions/webapplication/nn-webapplication-iwebapplicationnavigationevents?branch=master)<br/>             | Enables a debugging or authoring app to receive notification of navigation events.<br/>                                                                                                                                                       |
| [**IWebApplicationScriptEvents**](/windows/previous-versions/webapplication/nn-webapplication-iwebapplicationscriptevents?branch=master)<br/>                     | Enables a debugging or authoring app to receive notification of scripting engine events.<br/>                                                                                                                                                 |
| [**IWebApplicationUIEvents**](/windows/previous-versions/webapplication/nn-webapplication-iwebapplicationuievents?branch=master)<br/>                             | Enables a debugging or authoring app to receive notification of user interface events and respond to events that require user interaction.<br/>                                                                                               |
| [**IWebApplicationUpdateEvents**](/windows/previous-versions/webapplication/nn-webapplication-iwebapplicationupdateevents?branch=master)<br/>                     | Enables an authoring app to receive notification of designer events and respond to those events.<br/>                                                                                                                                         |
| [**RegisterAuthoringClientFunctionType**](/windows/previous-versions/webapplication/nc-webapplication-registerauthoringclientfunctiontype?branch=master)<br/>     | Defines a pointer to an application-defined function in a dynamic-link library (DLL) that will be used as the authoring binary. When the app host starts in authoring mode, this function is called to initialize the authoring binary. <br/> |
| [**UnregisterAuthoringClientFunctionType**](/windows/previous-versions/webapplication/nc-webapplication-unregisterauthoringclientfunctiontype?branch=master)<br/> | Unregisters the application-defined function that was registered with the [**RegisterAuthoringClientFunctionType**](/windows/previous-versions/webapplication/nc-webapplication-registerauthoringclientfunctiontype?branch=master) function. This function is called when the app host terminates.<br/>             |



 

 

 




