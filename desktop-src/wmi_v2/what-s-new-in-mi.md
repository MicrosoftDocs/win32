---
title: What's New in MI
description: Windows 8 and Windows Server 2012 introduced new ways of creating Windows Management Infrastructure (MI) applications.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1D29C47F-2630-4C5B-86D8-DF13BF02565C
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# What's New in MI?

Windows 8 and Windows Server 2012 introduced new ways of creating Windows Management Infrastructure (MI) applications. This topic highlights these changes and, where appropriate, provides links for more information:

-   [MI Features](#mi-features)
-   [Compatibility with WMI](#compatibility-with-wmi)

## MI Features

<dl> <dt>

<span id="Tight_alignment_with_standards"></span><span id="tight_alignment_with_standards"></span><span id="TIGHT_ALIGNMENT_WITH_STANDARDS"></span>Tight alignment with standards
</dt> <dd>

-   Work across systems using the HTTP-based WS-Man protocol. (DCOM is still supported.)
-   Align with the CIM 2.60 Infrastructure specification, including standard indications (events) and errors.

</dd> <dt>

<span id="New_native-code_provider_APIs"></span><span id="new_native-code_provider_apis"></span><span id="NEW_NATIVE-CODE_PROVIDER_APIS"></span>New native-code provider APIs
</dt> <dd>

-   No more COM coding required! Developers can now focus on developing the business logic, rather than the complex COM coding.
-   New providers contain the MOF & MFL, reducing the number of items developers must install.

</dd> <dt>

<span id="API_support_for_rich__semantics"></span><span id="api_support_for_rich__semantics"></span><span id="API_SUPPORT_FOR_RICH__SEMANTICS"></span>API support for rich PowerShell semantics
</dt> <dd>

-   Enables MI Provider developers to improve the IT pro experience when using PowerShell with MI.
-   Provides scripts and client applications for improved user experiences.

</dd> <dt>

<span id="New_approach_to_creating__cmdlets_from_MI_providers_using_XML"></span><span id="new_approach_to_creating__cmdlets_from_mi_providers_using_xml"></span><span id="NEW_APPROACH_TO_CREATING__CMDLETS_FROM_MI_PROVIDERS_USING_XML"></span>New approach to creating PowerShell cmdlets from MI providers using XML
</dt> <dd>

-   Developers and advanced IT pros can use CDXML to wrap existing CIM classes, creating PowerShell cmdlets without .NET coding.
-   Developers can create cmdlets in native code by implementing a MI provider and writing CDXML to go with it.
-   For more details, see the [CDXML](cmdlet-definition-xml.md) section.

</dd> </dl>

## Compatibility with WMI

The new version of MI maintains full compatibility with the older Windows Management Instrumentation (WMI) implementation.

Both new and existing WMI providers work with the new MI client applications. Existing client applications work with new and existing WMI providers. The new Indications and CIM Errors are mapped to the older Events & WMI error structures automatically.

The new version of MI ships as a downloadable update to Windows 7, Windows Server 2008 R2, and Windows Server 2008 Standard via the [Windows Management Framework 3.0](Http://Go.Microsoft.Com/FWLink/p/?LinkID=269580).

 

 




