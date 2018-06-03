---
title: Preparing the Environment
description: Preparing the Environment
ms.assetid: 0091f714-8b2b-4cd6-b8bf-1d901aae5013
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Preparing the Environment

1.  In order to identify drivers that allocate contiguous memory, it is necessary to ensure that security update MS09-012 (KB 956572) is properly installed. This security update must be installed using the **/B:SQP2QFE** option.
    -   Install a hotfix version of NTOSKRNL.EXE greater than or equal to file version 5.2.3790.4173 as indicated in [Knowledge Base Article 938486](http://go.microsoft.com/fwlink/p/?linkid=3100&amp;ID=938486).

    -   Review [Knowledge Base Article 956572](http://go.microsoft.com/fwlink/p/?linkid=3100&amp;ID=956572). This article discusses security update MS09-012.

    -   If security update MS09-012 is installed on your system, this security update must be uninstalled and reinstalled using the **/B:SQP2QFE** option. Be sure to restart your system after uninstalling MS09-012.

    -   Install MS09-012 using the **/B:SP2QFE** option. For example:

        ```
        WindowsServer2003.WindowsXP-KB952004-x64-ENU.exe /B:SP2QFE
        ```

        

    -   Restart your server.

2.  Update the Register by setting HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management DisablePagingExecutive (dword) from 0 (hex) to 1 (hex).

    > [!Note]  
    > Be sure to set this value to 0 when the data collection is done. If this value is not set to 0 performance can be negatively impacted.

     

3.  Download and install the latest version of Windows Performance Toolkit from the [WPT web site](http://go.microsoft.com/fwlink/p/?linkid=141497). Please see [Installation](installation.md) section of this document for more information.

 

 




