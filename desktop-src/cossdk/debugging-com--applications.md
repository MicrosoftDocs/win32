---
description: Debugging techniques for COM+ applications depend on the language in which you choose to write your component.
ms.assetid: 781a0b3f-2bd0-435b-b6fe-4469cc02e8b6
title: Debugging COM+ Applications
ms.topic: article
ms.date: 05/31/2018
---

# Debugging COM+ Applications

Debugging techniques for COM+ applications depend on the language in which you choose to write your component.

If you code in Microsoft Visual C++, you can launch the debugger in C++ or, with a remote client, you can debug by using OLE remote procedure control (RPC) and just-in-time (JIT) debugging. You can always use the Component Services administrative tool to debug your component with the COM+ **Launch in debugger** setting on the **Advanced** tab of the COM+ application's **Properties** dialog box. For more information on debugging components coded in C++, see [Debugging Components Written in Visual C++](debugging-components-written-in-visual-c--.md).

Unless you are currently debugging multithreading, component tracking, remote calls, or process isolation, you can use the Microsoft Visual Basic environment for debugging purposes. [Debugging Components Written in Visual Basic](debugging-components-written-in-visual-basic.md) describes the debugging process within a Visual Basic environment.

The topic [Debugging in the Visual Basic IDE](debugging-in-the-visual-basic-ide.md) provides a general overview with guidelines, tips and a procedure on debugging in the integrated development environment (IDE).

To view more information about debugging advanced processes, see [Debugging Compiled Visual Basic Components](debugging-compiled-visual-basic-components.md).

> [!Note]  
> Several limitations associated with using the Visual Basic environment to debug components with MTS have been resolved for COM+. For more information, see [COM+ Visual Basic Debugging Support Contrasted with MTS](com--visual-basic-debugging-support-contrasted-with-mts.md).

 

## Related topics

<dl> <dt>

[Handling Errors in COM+](handling-errors-in-com-.md)
</dt> </dl>

 

 



