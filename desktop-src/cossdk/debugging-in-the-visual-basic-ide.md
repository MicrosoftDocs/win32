---
description: Using the Microsoft Visual Basic integrated development environment (IDE) for debugging gives Visual Basic developers access to familiar tools and ease-of-use.
ms.assetid: d31efc97-c286-434d-93f5-77b34ec16205
title: Debugging in the Visual Basic IDE
ms.topic: article
ms.date: 05/31/2018
---

# Debugging in the Visual Basic IDE

Using the Microsoft Visual Basic integrated development environment (IDE) for debugging gives Visual Basic developers access to familiar tools and ease-of-use. While many components will eventually need to be more fully debugged using the Microsoft Visual C++ environment, one strategy might be to first debug as much functionality as possible with Visual Basic. For example, you might want to use the Visual Basic IDE for debugging within COM+ when you aren't yet debugging multithreading, component tracking, remote calls, or process isolation.

In general, when using the Visual Basic environment for debugging, you first compile the project and add the DLL to a COM+ application. Then you set binary compatibility for the project, referencing the DLL you made, and start the project to begin debugging.

## General Guidelines for Debugging in the Visual Basic Environment

-   While you are debugging using Visual Basic, COM+ treats the Visual Basic components as if they belong to a library application, even if the components are registered as belonging to a server application. Because it runs as a library application, the component icons in the Component Services administrative tool do not spin as the components are debugged.
-   If you change transaction attributes on a component during debugging or make a source code change that requires Visual Basic to generate a new CLSID or ProgID, be sure to delete and reinstall the COM+ application containing the component. If you have set binary compatibility for the component, you will be warned that changes have occurred.

## Notes on Debugging Within a COM+ Application

-   If you make changes in the Visual Basic IDE in your component's interfaces, class names, project names, transactional support or other settings, there may be mismatches between the configuration data in the Component Services explorer and the actual configuration running in the Visual Basic debugger.
-   Do not export a COM+ application while you are debugging a component in the application. COM+ will treat the Visual Basic development environment as the component.
-   If you are running a component outside the debugger and then decide to begin debugging, an instance of the component may still be running in COM+ when you start it in the debugger. COM+ will detect this condition and attempt to silently shut down the instance it controls. To avoid this problem, remove the component from the Component Services administrative tool before you begin debugging.

**To debug using the Visual Basic environment**

1.  Open the component project in Visual Basic.

2.  Compile your component, and then set binary compatibility in your project to the compiled component.

3.  Set the MTSTransactionMode property to a value other than 0 - NotAnMTSObject. When you start the project, this setting prompts Visual Basic to activate your component within COM+.

4.  From the **Project** menu, click **Properties**, and then enter the start program on the **Debugging** tab. The start program is the client executable that calls this component.

    > [!Note]  
    > The start program must be local to the component you are debugging.

     

5.  Press the F5 key to begin debugging the component.

After you press F5, Visual Basic launches the client application and runs the component in debug mode. You can place breakpoints in the component's code and set watches on variables.

## Related topics

<dl> <dt>

[COM+ Visual Basic Debugging Support Contrasted with MTS](com--visual-basic-debugging-support-contrasted-with-mts.md)
</dt> <dt>

[Debugging Compiled Visual Basic Components](debugging-compiled-visual-basic-components.md)
</dt> </dl>

 

 



