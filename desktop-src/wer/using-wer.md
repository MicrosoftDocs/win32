---
title: Using WER
description: Beginning with Windows Vista, Windows provides crash, non-response, and kernel fault error reporting by default without requiring changes to your application.
ms.assetid: c096cd89-e3a7-4959-a35f-40e6168f277e
keywords:
- Windows error reporting Windows Error Reporting , using
ms.topic: article
ms.date: 05/31/2018
---

# Using WER

Beginning with Windows Vista, Windows provides crash, non-response, and kernel fault error reporting by default without requiring changes to your application. The report will include minidump and heap dump information if required. Applications instead use the WER API to send application-specific problem reports to Microsoft.

Because Windows automatically reports unhandled exceptions, application should not handle fatal exceptions. If the faulting or not-responding process is interactive, WER displays a user interface informing the user of the problem. An application is considered unresponsive if it does not respond to Windows messages for five seconds while the user is trying to interact with the application.

## Windows Error Reporting flow for crashes, non-response, and kernel faults

The following shows the steps that occur for an application crash, non-response, or kernel fault.

1.  The problem event occurs.
2.  The operating system invokes WER.
3.  WER collects the data, builds a report, and prompts the user for consent (if needed).
4.  WER sends the report to Microsoft (Watson Server) if the user consented.
5.  If the Watson server requests additional data, WER collects the data and prompts the user for consent (if needed).
6.  If the application has registered for recovery and restart, WER executes the registered callback functions while the data is compressed and sent to Microsoft (if the user consented).
7.  If a response to the problem is available from Microsoft, the user is notified.

Applications can use the following functions to customize the contents of the report that is sent to Microsoft. The registration functions tell WER to include the specific files and memory blocks in the error report that it creates.

-   [**WerRegisterFile**](/windows/desktop/api/Werapi/nf-werapi-werregisterfile)
-   [**WerRegisterMemoryBlock**](/windows/desktop/api/Werapi/nf-werapi-werregistermemoryblock)
-   [**WerSetFlags**](/windows/desktop/api/Werapi/nf-werapi-wersetflags)
-   [**WerUnregisterFile**](/windows/desktop/api/Werapi/nf-werapi-werunregisterfile)
-   [**WerUnregisterMemoryBlock**](/windows/desktop/api/Werapi/nf-werapi-werunregistermemoryblock)
-   [**WerGetFlags**](/windows/desktop/api/Werapi/nf-werapi-wergetflags)

## Windows Error Reporting flow for generic event reporting

The following steps show how applications can get an error report for a non-fatal error condition.

1.  The non-fatal problem event occurs.
2.  The application recognizes the event and uses the following sequence of function calls to generate the report.
    1.  Call the [**WerReportCreate**](/windows/desktop/api/Werapi/nf-werapi-werreportcreate) function to create the report.
    2.  Call the [**WerReportSetParameter**](/windows/desktop/api/Werapi/nf-werapi-werreportsetparameter) function to set the report parameters.
    3.  Call the [**WerReportAddFile**](/windows/desktop/api/Werapi/nf-werapi-werreportaddfile) function to add files to the report.
    4.  Call the [**WerReportAddDump**](/windows/desktop/api/Werapi/nf-werapi-werreportadddump) function to add a minidump to the report (if needed).
    5.  Call the [**WerReportSubmit**](/windows/desktop/api/Werapi/nf-werapi-werreportsubmit) function to send the report.
    6.  Call the [**WerReportCloseHandle**](/windows/desktop/api/Werapi/nf-werapi-werreportclosehandle) to free resources.
3.  Depending on the specific options used when calling the functions in step 2, WER will finish the error reporting. WER will ensure that the reporting is done in accordance with the policies set by the user. For example, WER will send the report to Microsoft, queue the report, and show the appropriate user interfaces to the user.

## Excluding an application from Windows Error Reporting

To exclude your application from Windows error reporting, use the [**WerAddExcludedApplication**](/windows/desktop/api/Werapi/nf-werapi-weraddexcludedapplication) function. To restore error reporting for your application, use the [**WerRemoveExcludedApplication**](/windows/desktop/api/Werapi/nf-werapi-werremoveexcludedapplication) function.

## Automatically recovering data and restarting a faulted application

An application can use Application Recovery and Restart to save data and state information before the application exits due to an unhandled exception or when the application stops responding. The application is also restarted, if requested. For details, see [Application Recovery and Restart](/windows/desktop/Recovery/application-recovery-and-restart-portal).

## Legacy API

An application can report a fault by calling the [**ReportFault**](/windows/desktop/api/ErrorRep/nf-errorrep-reportfault) function. However, you should not use the **ReportFault** function unless you have a very specific requirement that the operating system's default error reporting behavior cannot fulfill.

If error reporting is enabled, the system displays a dialog box to the user indicating that the application has encountered a problem and will close. If there is a debugger configured in the **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\AeDebug** key, the user is given the option to launch the debugger. The user is also given the option to send a report to Microsoft. If the user sends the report, the system displays another dialog box thanking the user for the report and providing a link to more information.

The error reporting system supports the following operation modes.



| Operation mode          | Description                                                                                                                                                                                                                                                                                                                                  |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Shared memory reporting | If the application's security context is the same as the security context of the logged-on user, the error reporting system uses a block of shared memory for communication. This mode cannot be used with manifest reporting mode.<br/>                                                                                               |
| Manifest reporting      | If the application's security context is not the same as the security context of the logged-on user, the error reporting system uses a file for communication. This mode is also used for reporting unresponsive applications and kernel faults. This mode cannot be used with shared memory reporting mode.<br/>                      |
| Internet reporting      | The error reporting system sends all data to Microsoft through the Internet. This is the default mode of operation. It cannot be used with corporate reporting mode. This mode is used when there is no corporate upload path specified by the administrator.<br/>                                                                     |
| Corporate reporting     | The error reporting system sends all data to a file share instead of uploading it directly to Microsoft. This allows corporate IT managers to review data before it is sent to Microsoft. This mode is used when there is a corporate upload path specified by the administrator. It cannot be used with Internet reporting mode.<br/> |
| Headless reporting      | The error reporting system will not display any dialog boxes to the user. This allows corporate IT managers to collect error reports from their employees at all times. This mode is used when reporting is enabled by the administrator, but notification is disabled. It can be used only with corporate reporting mode.<br/>        |



 

To exclude your application from error reporting, use the [**AddERExcludedApplication**](/windows/desktop/api/ErrorRep/nf-errorrep-adderexcludedapplicationa) function.

 

