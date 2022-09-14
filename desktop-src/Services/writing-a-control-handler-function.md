---
description: When a Handler function is called by the dispatcher thread, it handles the control code passed in the Opcode parameter and then calls the ReportSvcStatus function to update the service status.
ms.assetid: bf1932bd-496b-46a1-95f4-1581da98299f
title: Writing a Control Handler Function
ms.topic: article
ms.date: 05/31/2018
---

# Writing a Control Handler Function

When a [**Handler**](/windows/desktop/api/Winsvc/nc-winsvc-lphandler_function) function is called by the dispatcher thread, it handles the control code passed in the *Opcode* parameter and then calls the ReportSvcStatus function to update the service status. When a [**Handler**](/windows/desktop/api/Winsvc/nc-winsvc-lphandler_function) function receives a control code, it should report the service status only if handling the control code causes the service status to change. If the service does not act on the control, it should not report status to the service control manager. For the source code for ReportSvcStatus, see [Writing a ServiceMain Function](writing-a-servicemain-function.md).

In the following example, the SvcCtrlHandler function is an example of a [**Handler**](/windows/desktop/api/Winsvc/nc-winsvc-lphandler_function) function. Note that the ghSvcStopEvent variable is a global variable that should be initialized and used as demonstrated in [Writing a ServiceMain function](writing-a-servicemain-function.md).


```C++
//
// Purpose: 
//   Called by SCM whenever a control code is sent to the service
//   using the ControlService function.
//
// Parameters:
//   dwCtrl - control code
// 
// Return value:
//   None
//
VOID WINAPI SvcCtrlHandler( DWORD dwCtrl )
{
   // Handle the requested control code. 

   switch(dwCtrl) 
   {  
      case SERVICE_CONTROL_STOP: 
         ReportSvcStatus(SERVICE_STOP_PENDING, NO_ERROR, 0);

         // Signal the service to stop.

         SetEvent(ghSvcStopEvent);
         ReportSvcStatus(gSvcStatus.dwCurrentState, NO_ERROR, 0);
         
         return;
 
      case SERVICE_CONTROL_INTERROGATE: 
         break; 
 
      default: 
         break;
   } 
   
}
```



## Related topics

<dl> <dt>

[Service Control Handler Function](service-control-handler-function.md)
</dt> <dt>

[The Complete Service Sample](the-complete-service-sample.md)
</dt> </dl>

 

 



