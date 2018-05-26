---
title: How to Register an MI Provider
description: Once youve successfully built an MI provider, you can register it on the target Windows 8 or Windows Server 2012 machine using the Register-CimProvider tool that ships in Windows. The following steps detail how to do that.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 13295157-C279-4730-8FC2-EF21AFCEB503
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# How to: Register an MI Provider

Once you've successfully built an MI provider, you can register it on the target Windows 8 or Windows Server 2012 machine using the **Register-CimProvider** tool that ships in Windows. The following steps detail how to do that.

1.  Copy the compiled MI provider DLL to a Windows 8 or Windows Server 2012 machine.
2.  On the target machine, open an **elevated** command prompt.
3.  Enter the following at the command prompt - replacing the **ProviderName** parameter with the name of your provider, and the **Path** parameter with the name of your provider's DLL. (You'll need to fully qualify this name if it's not in current directory.) The following also specifies the **Root/StandardCimv2/sample** namespace. You'll want to change that to something more appropriate for production purposes. But, for testing purposes, it's fine.

    > [!Note]  
    > The following call to the **Register-CimProvider** tool is split across multiple lines for display purposes. You should enter this as a single line.

     

    ``` syntax
    Register-CimProvider.exe -Namespace Root/StandardCimv2/sample 
    -ProviderName <your-provider-name> -Path <your-provider-dll> -verbose -ForceUpdate
    ```

4.  To test the provider, see the [How to: Test an MI Provider using PowerShell](how-to-test-an-mi-provider.md).

 

 




