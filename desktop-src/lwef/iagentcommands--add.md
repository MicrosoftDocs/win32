---
title: IAgentCommands Add
description: IAgentCommands Add
ms.assetid: f6be7773-77fa-4c59-8feb-c2ebf54fd2e0
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommands::Add

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT Add(
   BSTR bszCaption,  // Caption setting for Command
   BSTR bszVoice,    // Voice setting for Command
   long bEnabled,    // Enabled setting for Command
   long bVisible,    // Visible setting for Command
   long * pdwID      // address for variable for ID
);
```

Adds a [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) to a [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms695971) collection.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="bszCaption"></span><span id="bszcaption"></span><span id="BSZCAPTION"></span>*bszCaption*
</dt> <dd>

A BSTR that specifies the value of the [**Caption**](caption-property.md) text displayed for a [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) in a [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms695971) collection.

</dd> <dt>

<span id="bszVoice"></span><span id="bszvoice"></span><span id="BSZVOICE"></span>*bszVoice*
</dt> <dd>

A BSTR that specifies the value of the [**Voice**](voice-property.md) text setting for a [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) in a [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms695971) collection.

</dd> <dt>

<span id="bEnabled"></span><span id="benabled"></span><span id="BENABLED"></span>*bEnabled*
</dt> <dd>

A Boolean expression that specifies the [**Enabled**](enabled-property.md) setting for a [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) in a [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms695971) collection. If the parameter is **True**, the **Command** is enabled and can be selected; if **False**, the **Command** is disabled.

</dd> <dt>

<span id="bVisible"></span><span id="bvisible"></span><span id="BVISIBLE"></span>*bVisible*
</dt> <dd>

A Boolean expression that specifies the [**Visible**](visible-property.md) setting for a [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) in a [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms695971) collection. If the parameter is **True**, the **Command** will be visible in the character's pop-up menu (if the [**Caption**](caption-property.md) property is also set).

</dd> <dt>

<span id="pdwID_"></span><span id="pdwid_"></span><span id="PDWID_"></span>*pdwID* 
</dt> <dd>

Address of a variable that receives the ID for the added [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441).

</dd> </dl>

## See Also

[**IAgentCommand::SetCaption**](iagentcommand--setcaption.md), [**IAgentCommand::SetEnabled**](iagentcommand--setenabled.md), [**IAgentCommand::SetVisible**](iagentcommand--setvisible.md), [**IAgentCommand::SetVoice**](iagentcommand--setvoice.md), [**IAgentCommands::Insert**](iagentcommands--insert.md), [**IAgentCommands::Remove**](iagentcommands--remove.md), [**IAgentCommands::RemoveAll**](iagentcommands--removeall.md)


 

 




