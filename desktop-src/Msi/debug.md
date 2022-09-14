---
description: If this per-machine system policy is set to &\#0034;1&\#0034;, the installer writes common debugging messages to the debugger using the OutputDebugString function.
ms.assetid: 0a9416ca-0535-4595-a4f3-b3ef7c2d3a13
title: Debug
ms.topic: article
ms.date: 05/31/2018
---

# Debug

If this per-machine [system policy](system-policy.md) is set to "1", the installer writes common debugging messages to the debugger using the [**OutputDebugString**](/windows/desktop/api/debugapi/nf-debugapi-outputdebugstringw) function. If this value is set to "2", the installer writes all valid debugging messages to the debugger using the [**OutputDebugString**](/windows/desktop/api/debugapi/nf-debugapi-outputdebugstringw) function. This policy is for debugging purposes only and may not be supported in future versions of Windows Installer.

Windows Installer only writes command lines into the log file if the third (0x04) bit is set in the value of the Debug policy. Therefore, to display command lines in the log, set the Debug policy value to 7. This does not display properties associated with an [Edit Control](edit-control.md) having the [Password Control Attribute](password-control-attribute.md). This will make properties set on the command line visible in the log even if the property is included in the [**MsiHiddenProperties**](msihiddenproperties.md) property. For more information, see [Preventing Confidential Information from Being Written into the Log File](preventing-confidential-information-from-being-written-into-the-log-file.md).

## Registry Key

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Policies**\\**Microsoft**\\**Windows**\\**Installer**

## Data Type

**REG\_DWORD**

 

 
