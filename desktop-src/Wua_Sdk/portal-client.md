---
description: The Windows Update Agent (WUA) API is a set of COM interfaces that enable system administrators and programmers to access Windows Update and Windows Server Update Services (WSUS).
ms.assetid: 611dc759-e0fc-472e-bdc2-fb952ba74999
title: Windows Update Agent API
ms.topic: concept-article
ms.date: 05/31/2018
---

# Windows Update Agent API

## Purpose

The Windows Update Agent (WUA) API is a set of COM interfaces that enable system administrators and programmers to access Windows Update and [Windows Server Update Services (WSUS)](/previous-versions/windows/desktop/ms744624(v=vs.85)). Scripts and programs can be written to examine which updates are currently available for a computer, and then you can install or uninstall updates.

> [!NOTE]
> The **Windows Update** page in Windows Settings displays the progress and history of updates managed by the Windows Update orchestrator workflow. The updates handled through WUA APIs will not appear on this page. It is recommended that you disable the Windows Update orchestrator when using the WUA APIs to prevent conflicts. For information about the default Windows Update orchestrator workflow, see [How Windows Update works](/windows/deployment/update/how-windows-update-works). For information on disabling the Windows Update orchestrator, see [Manage connections from Windows 10 and Windows 11 operating system components to Microsoft services](/windows/privacy/manage-connections-from-windows-operating-system-components-to-microsoft-services#bkmk-wu).
> 
> The history of updates that have been installed using the WUA APIs can be viewed in **Event Viewer**. To view WUA update events:
> 1. Right-click **Start** and select **Event Viewer**.
> 2. Navigate to **Windows Logs > System**
> 3. In the **Actions** pane, select **Filter Current Log...**.
> 4. In the **Event sources** drop-down, select **WindowsUpdateClient**.
> 5. Click **Ok** to apply the filter to the results.

## Where applicable

System administrators can use WUA to programmatically determine which updates should be applied to a computer, download those updates, and then install them with little or no user intervention.

Independent software vendors (ISV) and end-user developers can integrate WUA features into computer management or update management software to provide a seamless operating environment.

## Developer audience

You can write WUA applications in several programming languages. WUA defines interfaces and objects that are accessible from Visual Basic, Visual Basic Scripting Edition (VBScript), JScript, and from C and C++. A familiarity with COM programming is useful to the WUA programmer.

## Run-time requirements

WUA is supported starting with Windows XP. WUA is supported on the server starting with Windows Server 2003.

## In this section

-   [Using the Windows Update Agent API](using-the-windows-update-agent-api.md)
-   [WUA API Reference](windows-update-agent--wua--api-reference.md)

 

 
