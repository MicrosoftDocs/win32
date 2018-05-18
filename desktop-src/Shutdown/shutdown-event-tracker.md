---
Description: 'The Shutdown Event Tracker enables the user or application to document the reason for shutting down or restarting the system.'
ms.assetid: '860c014e-1fde-45d1-b366-c279bfcf4079'
title: Shutdown Event Tracker
---

# Shutdown Event Tracker

The *Shutdown Event Tracker* enables the user or application to document the reason for shutting down or restarting the system. The user is prompted to fill in information when selecting **Shut Down** from the **Start** menu, or when using Shutdown.exe. Developers can include a reason code when calling the [**ExitWindowsEx**](exitwindowsex.md) and [**InitiateSystemShutdownEx**](initiatesystemshutdownex.md) functions. The information is stored in the event log.

**Windows XP:** While this feature is enabled by default starting with Windows Server 2003, you must enable it on Windows XP. For more information, see the documentation for the Shutdown Event Tracker included in the system or on TechNet.

The [**ExitWindowsEx**](exitwindowsex.md) and [**InitiateSystemShutdownEx**](initiatesystemshutdownex.md) functions have been updated to support shutdown reason codes in the *dwReason* parameter. Use the values defined in Reason.h to construct a shutdown reason code, or define a custom reason code. A shutdown reason code is constructed from a major flag, a minor flag, and two optional flags. For more information, see [System Shutdown Reason Codes](system-shutdown-reason-codes.md).

## Related topics

<dl> <dt>

[Shutdown Event Tracker (TechNet)](http://go.microsoft.com/fwlink/p/?linkid=103786)
</dt> </dl>

 

 



