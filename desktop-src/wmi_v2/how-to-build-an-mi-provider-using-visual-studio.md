---
title: How to Build an MI Provider Using Visual Studio
description: Once you've created an empty Microsoft Visual Studio project to house your MI provider and generated the source code files from your MOF file, you can insert the generated source code files into the Visual Studio project.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '290FDDC8-B97C-4679-B302-B9C34DC80BFB'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
---

# How to: Build an MI Provider Using Visual Studio

Once you've created an empty Microsoft Visual Studio project to house your MI provider and generated the source code files from your MOF file, you can insert the generated source code files into the Visual Studio project. This topic provides step-by-step instructions detailing how to accomplish that task.

1.  Start Visual Studio and open the provider project you created.
2.  Open the Solution Explorer by clicking **&lt;Ctrl&gt;&lt;Alt&gt;L**.
3.  Right-click the **Header Files** folder and, when the context menu displays, select the **Add** and then **Existing item...** menu options.
4.  When the **Add Existing Item** dialog displays, browse to the folder containing the generated provider source code files, select all of the header files (.h), and click **Add**.
5.  Right-click the **Source Files** folder and, when the context menu displays, select the **Add** and then **Existing item...** menu options.
6.  When the **Add Existing Item** dialog displays, browse to the folder containing the generated provider source code files, select all of the C source code files (.c), and click **Add**.
7.  **\[Optional\]** If you did not specify the **SkipLocalize** parameter when you ran the **Convert-MofToProvider** tool, you will have a resource file (.rc) generated on your behalf called **strings.rc**. To add it to the project, right-click the **Resources Files** folder and, when the context menu displays, select the **Add** and then **Existing item...** menu options. When the **Add Existing Item** dialog displays, browse to the folder containing the generated provider source code files, select the **strings.rc** file, and click **Add**.
8.  Right-click the project name and, when the context menu displays, select the **Add** and then **Existing item...** menu options.
9.  When the **Add Existing Item** dialog displays, browse to the folder containing the generated provider source code files, select the MOF file (**process.mof**) and DEF file (**provider.def**), and click **Add**. (Holding down the &lt;Ctrl&gt; key will enable you to select multiple files.)
10. In the Solution Explorer, locate the **provider.def** file and double-click it to open it in the editor.
11. When the DEF file is open, change **%ProviderName%** to the name of your Visual Studio project's output, which is typically the same name as your project. In the following example, the project name is **ProcessProvider** and produces a DLL called **ProcessProvider.DLL**. Therefore, the **LIBRARY** record indicates this.

    ``` syntax
    LIBRARY         ProcessProvider.DLL

    EXPORTS
        DllMain             = DllMain             PRIVATE
        GetProviderClassID  = GetProviderClassID  PRIVATE
        DllGetClassObject   = DllGetClassObject   PRIVATE
        DllCanUnloadNow     = DllCanUnloadNow     PRIVATE
        DllRegisterServer   = DllRegisterServer   PRIVATE
        DllUnregisterServer = DllUnregisterServer PRIVATE
    ```

12. Right-click the project name and, when the context menu displays, select the **Properties** menu option to display the project's **Property Pages** dialog.
13. In the **Configuration** combo box, select the **All Configurations** item.
14. On the left side of the dialog, expand **Configuration Properties**, then expand **Linker**, and click **Input**.
15. For the **Module Definition File**, enter **provider.def** and click **OK**.
16. Now that you have a skeleton MI provider, you can code your own business logic into the provider. If you're new to MI provider development, download the [MI API Samples](Http://Go.Microsoft.Com/FWLink/p/?LinkID=306594) and look at the **Provider** sample (under the **Process** directory). For that sample, the key files of note are the following.

    

    | File(s)                                                                                                                                                 | Notes                                                                                                                                                                                                                                                                 |
    |---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | MSFT\_WindowsProcess.c<br/> MSFT\_WindowsProcess.h<br/> WindowsProcess.c<br/> WindowsProcess.h<br/>                             | The **MSFT\_WindowsProcess.c** and **MSFT\_WindowsProcess.h** files were generated using the sample's MOF file and make calls to functions defined and implemented in the **WindowsProcess.c** and **WindowsProcess.h** files.<br/>                             |
    | MSFT\_WindowsServiceProcess.c<br/> MSFT\_WindowsServiceProcess.h<br/> WindowsServiceProcess.c<br/> WindowsServiceProcess.h<br/> | The **MSFT\_WindowsServiceProcess.c** and **MSFT\_WindowsServiceProcess.h** files were generated using the sample's MOF file and make calls to functions defined and implemented in the **WindowsServiceProcess.c** and **WindowsServiceProcess.h** files.<br/> |
    | helper.c<br/> helper.h<br/>                                                                                                                 | The **helper.c** and **helper.h** files define a handy function - **ResultFromWin32Error** - for converting Win32 error codes to [MI\_Result](Http://Go.Microsoft.Com/FWLink/p/?LinkID=308964) values.<br/>                                                     |

    

     

17. Build the project by clicking **&lt;Ctrl&gt;&lt;Shift&gt;B**. The Output window will show you the build's progress and should display a success message when the build has completed.
18. Once the provider builds successfully, you can [register](how-to-register-an-mi-provider.md) and [test](how-to-test-an-mi-provider.md) it.

 

 





