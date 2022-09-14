---
title: Using Application Recovery and Restart
description: An application can use Application Recovery and Restart (ARR) to save data and state information before the application exits due to an unhandled exception or when the application stops responding. The application is also restarted, if requested.
ms.assetid: 28cbb4c0-a287-4302-b3a9-daddc69adb40
ms.topic: article
ms.date: 05/31/2018
---

# Using Application Recovery and Restart

An application can use Application Recovery and Restart (ARR) to save data and state information before the application exits due to an unhandled exception or when the application stops responding. The application is also restarted, if requested.

When you register for recovery or restart, the registration information is added to the process. [Windows Error Reporting (WER)](/windows/desktop/wer/windows-error-reporting) uses the registration information to call your recovery callback and restart your application. For example, if you register for recovery and your application encounters an unhandled exception, WER displays a dialog to the user that gives the user the option of checking for a solution online, closing the program, or debugging the program. If the user chooses to either check for a solution or close the program, WER calls the registered callback and gives the application the chance to save data and state information. When the recovery is complete, the application is terminated.

If you register for restart and your application encounters an unhandled exception, WER displays the same dialog to the user but gives the option of restarting the program instead of closing the program. If you register for both recovery and restart, recovery occurs first; the application is then terminated and restarted.

An unresponsive application is handled in a similar fashion. An application is considered unresponsive if it does not respond to Windows messages for five seconds and the user then tries to interact with the application; the user will see (Not Responding) in the title bar. WER is activated when the user clicks the system close button.

You must register for recovery or restart, or remove the registration, before the application becomes unresponsive or encounters an unhandled exception. However, in your recovery callback, you can change the restart command line.

For details on registering for recovery or restart, see the following topics:

-   [Registering for Application Recovery](registering-for-application-recovery.md)
-   [Registering for Application Restart](registering-for-application-restart.md)

For samples that implement the recovery and restart features, see the AppRecovery and AppRestart samples in the Windows SDK located in the WinBase\\WindowsErrorReporting folder.

 

 