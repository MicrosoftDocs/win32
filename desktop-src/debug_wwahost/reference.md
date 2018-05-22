---
Description: 'This API enables developer tools to debug Windows apps using JavaScript running in the app host.'
ms.assetid: '43996903-E0B8-440B-88CA-610D859B340B'
title: Debugging and authoring support for Windows apps using JavaScript
---

# Debugging and authoring support for Windows apps using JavaScript

This API enables developer tools to debug Windows apps using JavaScript running in the app host.

## In this section



| Topic                                                                                             | Description                                                                                                                                                                                                                                         |
|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IWebApplicationActivation**](iwebapplicationactivation.md)<br/>                         | Enables debugging applications to manage activations.<br/>                                                                                                                                                                                    |
| [**IWebApplicationAuthoringMode**](iwebapplicationauthoringmode.md)<br/>                   | Provides the full local path to the authoring binary to be loaded into the WWAHost process.<br/>                                                                                                                                              |
| [**IWebApplicationHost**](iwebapplicationhost.md)<br/>                                     | Exposes methods and properties that are implemented by the WWAHost.<br/>                                                                                                                                                                      |
| [**IWebApplicationNavigationEvents**](iwebapplicationnavigationevents.md)<br/>             | Enables a debugging or authoring app to receive notification of navigation events.<br/>                                                                                                                                                       |
| [**IWebApplicationScriptEvents**](iwebapplicationscriptevents.md)<br/>                     | Enables a debugging or authoring app to receive notification of scripting engine events.<br/>                                                                                                                                                 |
| [**IWebApplicationUIEvents**](iwebapplicationuievents.md)<br/>                             | Enables a debugging or authoring app to receive notification of user interface events and respond to events that require user interaction.<br/>                                                                                               |
| [**IWebApplicationUpdateEvents**](iwebapplicationupdateevents.md)<br/>                     | Enables an authoring app to receive notification of designer events and respond to those events.<br/>                                                                                                                                         |
| [**RegisterAuthoringClientFunctionType**](registerauthoringclientfunctiontype.md)<br/>     | Defines a pointer to an application-defined function in a dynamic-link library (DLL) that will be used as the authoring binary. When the app host starts in authoring mode, this function is called to initialize the authoring binary. <br/> |
| [**UnregisterAuthoringClientFunctionType**](unregisterauthoringclientfunctiontype.md)<br/> | Unregisters the application-defined function that was registered with the [**RegisterAuthoringClientFunctionType**](registerauthoringclientfunctiontype.md) function. This function is called when the app host terminates.<br/>             |



 

 

 




