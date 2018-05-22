---
title: Why Use MI
description: The Windows Management Infrastructure (MI) features represent the latest version of the Windows Management Instrumentation (WMI) technologies, which are based on the CIM standard from DMTF (Distributed Management Task Force).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '12E5D856-D1B7-44CA-8860-CE73A8A8C824'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
---

# Why Use MI?

The Windows Management Infrastructure (MI) features represent the latest version of the Windows Management Instrumentation (WMI) technologies, which are based on the CIM standard from DMTF (Distributed Management Task Force). MI is fully compatible with previous versions of WMI and provides a host of features and benefits that make designing and developing providers and clients easier than ever.

<dl> <dt>

<span id="Reduced_development_time"></span><span id="reduced_development_time"></span><span id="REDUCED_DEVELOPMENT_TIME"></span>Reduced development time
</dt> <dd>

MI reduces development time by providing new native provider APIs, native client APIs, and .NET APIs that no longer require complex COM coding to interact with WMI. In addition, there are in-box and SDK tools that ease the development process.

</dd> <dt>

<span id="Tighter_integration_with_"></span><span id="tighter_integration_with_"></span><span id="TIGHTER_INTEGRATION_WITH_"></span>Tighter integration with PowerShell
</dt> <dd>

MI introduces a new way of creating PowerShell cmdlets (called "CIM-based cmdlets") that use XML to map PowerShell commands and parameters to any new or existing MI classes, methods, and properties. The new APIs also include support for rich PowerShell semantics such as **PromptUser** and **Warning.**

</dd> <dt>

<span id="Standards-based"></span><span id="standards-based"></span><span id="STANDARDS-BASED"></span>Standards-based
</dt> <dd>

The MI APIs have been updated to align with the DMTF standards. The default machine-to-machine communication now goes over [WinRM](https://msdn.microsoft.com/library/ee309369) (the Microsoft implementation of the WS-Man standard), and the MI APIs also expose standard error and event classes ([**CIM\_Error**](https://msdn.microsoft.com/library/mt130388) and [**CIM\_Indication**](https://msdn.microsoft.com/library/mt130426)). Combined with the new PowerShellextensions, this alignment with standards enables IHVs to provide IT pros the ability to manage CIM-compliant devices from Windows using PowerShell over WS-Man.

</dd> </dl>

 

 




