---
description: Given that in many cases you will be able to debug only a portion of your components functionality within the Microsoft Visual Basic environment, there will be situations in which you will need to debug components built with Visual Basic after they have been compiled. Since the Visual Basic environment doesnt enable this, you must instead use the Microsoft Visual C++ environment.
ms.assetid: a58c5884-3c2d-4699-8b19-277003912dfd
title: Debugging Compiled Visual Basic Components
ms.topic: article
ms.date: 05/31/2018
---

# Debugging Compiled Visual Basic Components

Given that in many cases you will be able to debug only a portion of your component's functionality within the Microsoft Visual Basic environment, there will be situations in which you will need to debug components built with Visual Basic after they have been compiled. Since the Visual Basic environment doesn't enable this, you must instead use the Microsoft Visual C++ environment.

**To debug a Visual Basic component in the Visual C++ environment**

1.  In Visual Basic 6.0, open the Visual Basic project that you want to debug.

2.  On the **File** menu, click **Make YourProject.dll**.

3.  In the **Make Project** dialog box, click **Options**.

4.  In the **Project Properties** dialog box, on the **Compile** tab, click **Compile to Native Code** and **No Optimization** and select the **Create Symbolic Debug Info** check box.

5.  Click **OK**, and then click **OK** again to compile your project.

6.  Move the compiled DLL to the location where COM+ applications are normally installed.

    > [!Note]  
    > If you don't move the DLL, you may get an error message informing you that symbolic debugging information for the DLL could not be located. If you have trouble getting the debugger to stop at breakpoints in your component, confirm that the DLL is in the standard packages directory, delete the component from its package, and re-add the component.

     

7.  Start Visual C++.

8.  On the **File** menu, click **Open Workspace**.

9.  In the **Open Workspace** dialog box, set **Files of Type** to **All files(\*.\*)**, select your compiled component, and click **Open**.

10. From the **File** menu, click **Open** (not **Open Workspace**) and open the Visual Basic module (.bas), form (.frm), or class (.cls) that you want to debug.

11. On the **Project** menu, click **Settings**.

12. In the **Project Settings** dialog box, on the **Debug** tab, select **General** in the **Category** box.

13. In the **Executable for debug session** box, enter the fully qualified path for Dllhost.exe, followed by an argument specifying the process ID of the COM+ application containing the component. You will find the process ID on the **General** tab of the COM+ application's **Properties** dialog box. Following is an example: C:\\Winnt\\System32\\Dllhost.exe /ProcessID:{&lt;processID&gt;}.

14. Click **OK**.

## Related topics

<dl> <dt>

[COM+ Visual Basic Debugging Support Contrasted with MTS](com--visual-basic-debugging-support-contrasted-with-mts.md)
</dt> <dt>

[Debugging in the Visual Basic IDE](debugging-in-the-visual-basic-ide.md)
</dt> </dl>

 

 



