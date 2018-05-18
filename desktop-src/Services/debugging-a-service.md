---
Description: 'You can use any one of the following methods to debug your service.'
ms.assetid: '6f4ae117-2120-4c1e-b69f-641ce2e633fa'
title: Debugging a Service
---

# Debugging a Service

You can use any one of the following methods to debug your service.

-   Use your debugger to debug the service while it is running. First, obtain the process identifier (PID) of the service process. After you have obtained the PID, attach to the running process. For syntax information, see the documentation included with your debugger.
-   Call the [**DebugBreak**](https://msdn.microsoft.com/library/windows/desktop/ms679297) function to invoke the debugger for just-in-time debugging.
-   Specify a debugger to use when starting a program. To do so, create a key called **Image File Execution Options** in the following registry location:

    **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion**

    Create a subkey with the same name as your service (for example, MYSERV.EXE). To this subkey, add a value of type **REG\_SZ**, named **Debugger**. Use the full path to the debugger as the string value. In the Services control panel applet, select your service, click **Startup** and check **Allow Service to Interact with Desktop**. The service must be an interactive service, or else the debugger cannot run on the default desktop. Note that this technique is no longer supported as of Windows Vista because all services are run in session that is reserved exclusively for services and does not support displaying a user interface.

-   Use [Event Tracing](https://msdn.microsoft.com/library/windows/desktop/bb968803) to log information.

To debug the initialization code of an auto-start service, you will have to temporarily install and run the service as a demand-start service.

At times, it may be necessary to run a service as a console application for debugging purposes. In this scenario, the [**StartServiceCtrlDispatcher**](startservicectrldispatcher.md) function will return **ERROR\_FAILED\_SERVICE\_CONTROLLER\_CONNECT**. Therefore, be sure to structure your code such that service-specific code is not called when this error is returned.

## Related topics

<dl> <dt>

[Debugging a Service Application](http://go.microsoft.com/fwlink/p/?linkid=160257)
</dt> <dt>

[Debugging Tools for Windows](http://go.microsoft.com/fwlink/p/?linkid=116392)
</dt> </dl>

 

 



