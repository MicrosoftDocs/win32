---
description: When you are ready to debug the COM+ functionality in your Microsoft Visual C++ components, you can configure Visual C++ project or the Component Services administrative tool to launch the debugger.
ms.assetid: 206467ac-108a-49de-a884-66959dc77650
title: Debugging Components Written in Visual C++
ms.topic: article
ms.date: 05/31/2018
---

# Debugging Components Written in Visual C++

When you are ready to debug the COM+ functionality in your Microsoft Visual C++ components, you can configure Visual C++ project or the Component Services administrative tool to launch the debugger. If you are using Visual C++, you can debug with a remote client using OLE RPC and just-in-time (JIT) debugging. If you are unable to run your client under the debugger or if the client is running on another machine, you can use the COM+ **Launch in debugger** setting. You will find this in the Component Services administrative tool as a check box on the **Advanced** tab of the COM+ application **Properties** dialog box.

When you are finished debugging, you should shut down the COM+ applications you are debugging. If a server process is left running, you might get an error message the next time you try to build a DLL when the existing DLL is still loaded in memory. To shut down a COM+ application, right-click the application in the console tree and then click **Shut down**.

> [!Note]  
> If you are using transactions, you might also want to increase the transaction time-out, which defaults to 60 seconds. You can also specify a value of 0, effectively specifying an infinite transaction time-out period. Using the Component Services administrative tool, change the transaction time-out setting on the **Options** tab of the **My Computer Properties** window.

 

## Debugging Server Application Components with Visual C++

When debugging COM+ server applications, you may want to debug remote calls by loading both the client and the server application into the debugger. With Visual C++, you can debug remote calls to your components through the just-in-time (JIT) and OLE RPC settings. The JIT setting causes the compiled component to start the Visual C++ debugger when an error occurs; the OLE RPC setting enables the debugger to step from client to component as you step through your code.

When these features are enabled, you can start your client under the debugger. When the client makes a call to your component, the debugger will step into the component's code in the server process, even if the server is on a different computer on the network. A debugging session is automatically started on the server computer if necessary. Similarly, single stepping past the return statement in the component's code will return debugging to the next statement in the client's code.

> [!Note]  
> You may be able to save a few steps by using the COM+ **Launch in debugger** setting. This allows you to specify the Visual C++ (or other) debugger without having to make special debug settings in the Visual C++ environment. You will find this in the Component Services administrative tool as a check box on the **Advanced** tab of the COM+ application **Properties** dialog box. For more information, see "Debugging Without Visual C++" in this topic.

 

When the COM+ application containing your component is a server application, you must begin by shutting down the application using the Component Services administrative tool. To do this, right-click the COM+ application in the console tree and then click **Shut down**.

**To enable RPC debugging in Visual C++**

1.  In Visual C++, on the **Tools** menu, click **Options**.

2.  In the **Options** dialog box, on the **Debug** tab, select the **OLE RPC debugging** and **Just-in time debugging** check boxes.

3.  Click **OK**.

To begin debugging, start your client project in the debugger.

You can also debug your component without launching your client in the debugger. In this case, your component must launch the debugger on its own. To do this, your component project must specify an executable for the debug session, along with the COM+ application ID.

**To enable a server application component to launch the Visual C++ debugger**

1.  On the **Project** menu, click **Settings**.

2.  In the **Project Settings** dialog box, in the **Settings For** box, select **Win32 Debug**.

3.  On the **Debug** tab, in the **Category** box, select **General**.

4.  In the **Executable for debug session** box, enter the fully qualified path for Dllhost.exe, followed by an argument specifying the application ID of the COM+ application containing the component.

    > [!Note]  
    > Using the Component Services administrative tool, you will find the application ID on the **General** tab of the COM+ application's **Properties** dialog box. Following is an example:

     

    > [!Note]  
    > C:\\Winnt\\System32\\Dllhost.exe /ProcessID:{applicationID}

     

5.  Click **OK**.

You can now set breakpoints, start the debugger, and begin making calls to your component.

## Debugging Library Application Components with Visual C++

To debug components in a library application, you must configure the client's project because the client's process will host the library application.

**To enable library application debugging with Visual C++**

1.  In Visual C++, on the **Project** menu, click **Settings**.

2.  In the **Project Settings** dialog box, in the **Settings For** box, click **Win32 Debug**.

3.  On the **Debug** tab, in the **Category** box, click **Additional DLLs**.

4.  In the **Modules** list, add the component DLLs in your library application. This allows you to set breakpoints before your DLL is actually loaded.

5.  Click **OK**.

## Debugging Without Visual C++

Whether or not you are using Visual C++ for debugging, you can use the **Launch in debugger** setting to specify the debugger in which your components should run.

**To specify a debugger from the Component Services administrative tool**

1.  In the console tree, select the COM+ library application containing the components you wish to debug.

2.  Right-click the application, and then click **Properties**.

3.  In the application's **Properties** dialog box, click the **Advanced** tab.

4.  Under **Debugging**, select the **Launch in debugger** check box.

5.  In the **Debugger path** box, enter path to the debugger you want to use. You can also click **Browse** to locate the debugger. Following is an example: C:\\Winnt\\System32\\Ntsd.exe.

6.  Click **OK**.

## Related topics

<dl> <dt>

[Debugging Components Written in Visual Basic](debugging-components-written-in-visual-basic.md)
</dt> </dl>

 

 



