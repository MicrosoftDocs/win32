---
description: Debugging Components Written in Visual Basic
ms.assetid: 2b00ed29-8b48-4a54-83e8-d5e69e5f883e
title: Debugging Components Written in Visual Basic
ms.topic: article
ms.date: 05/31/2018
---

# Debugging Components Written in Visual Basic

You can use the Microsoft Visual Basic 6.0 development environment for debugging within certain scenarios. Using Visual Basic for debugging allows access to tools familiar to Visual Basic programmers. On the other hand, because during debugging Visual Basic components run within the Visual Basic environment's process, it may be necessary to debug your component after it has been compiled by using the Microsoft Visual C++ development environment.

For more information about debugging within the Visual Basic integrated development environment (IDE), see [Debugging in the Visual Basic IDE](debugging-in-the-visual-basic-ide.md). For more on debugging Visual Basic components after they're compiled using the Visual C++ development environment, see [Debugging Compiled Visual Basic Components](debugging-compiled-visual-basic-components.md).

Also, several limitations associated with using the Visual Basic environment to debug components with MTS have been resolved for COM+. For more information, see [COM+ Visual Basic Debugging Support Contrasted with MTS](com--visual-basic-debugging-support-contrasted-with-mts.md).

> [!Note]  
> If you have already used Visual Basic on the same computer as COM+, you may have noticed the Component Services add-in available in the Visual Basic environment. Originally in MTS, this feature was designed to update the registry each time you recompiled a component in a COM+ application. However, given the nature of the interaction of the Microsoft Windows Registry and the COM+ registration database, some settings may not be completely updated. Therefore, instead of using the commands available with this add-in, you should remove and reinstall your components to update settings after recompiling.

 

## Related topics

<dl> <dt>

[Debugging Components Written in Visual C++](debugging-components-written-in-visual-c--.md)
</dt> </dl>

 

 



