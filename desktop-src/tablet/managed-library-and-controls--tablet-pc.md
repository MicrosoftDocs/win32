---
description: To build Tablet PC applications in C\# and Visual Basic .NET, your project in Microsoft Visual Studio .NET must include a reference to the Tablet PC managed library assemblies. This provides access to the managed object model and controls.
ms.assetid: d9c491c9-d341-4189-9a41-45c4d78322fa
title: Managed Library and Controls (Tablet PC)
ms.topic: article
ms.date: 05/31/2018
---

# Managed Library and Controls (Tablet PC)

To build Tablet PC applications in C\# and Visual Basic .NET, your project in Microsoft Visual Studio .NET must include a reference to the Tablet PC managed library assemblies. This provides access to the managed object model and controls.

## Microsoft Visual C\# and Visual Basic.NET

In Windows Vista, the Tablet PC managed library assemblies are installed by default in two directories:

-   <systemdrive>:\\Program Files\\Common Files\\Microsoft Shared\\Ink directory
-   <systemdrive>:\\Program Files\\Microsoft SDKs\\Windows\\v6.0\\Bin

To add a reference to the Tablet PC platform managed libraries in Microsoft Visual Studio .NET:

1.  Open your Visual Studio .NET project.
2.  On the **Project** menu, click **Add Reference**.
3.  On the **.NET** tab in the **Add Reference** dialog box, on the components list, select **Microsoft Tablet PC API**.
4.  Click **Select**, and then click **OK**.

To add a reference to the ink analysis APIs in Visual Studio .NET:

1.  Open your Microsoft Visual Studio .NET project.
2.  On the **Project** menu, click **Add Reference**.
3.  On the **.NET** tab in the **Add Reference** dialog box, on the components list, select **Microsoft Tablet PC Ink Analysis Managed Library**.
4.  Click **Select**, and then click **OK**.

> [!Note]  
> When compiling applications that use Microsoft.Ink on Visual Studio 2005, you must select **Project**, select **Properties**, select **Build** and set Platform target=x86. This option is not available in Microsoft Visual Studio Express products.

 

 

 



