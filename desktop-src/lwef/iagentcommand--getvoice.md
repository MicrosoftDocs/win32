---
title: IAgentCommand GetVoice
description: IAgentCommand GetVoice
ms.assetid: 69f3c91b-2ccf-4bea-8034-0c3e0a5e4ec4
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IAgentCommand::GetVoice

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetVoice(
   BSTR * pbszVoice  // address of Voice setting for Command
);
```

Retrieves the value of the [**Voice**](voice-property.md) text property for a [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441).

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbszVoice"></span><span id="pbszvoice"></span><span id="PBSZVOICE"></span>*pbszVoice*
</dt> <dd>

The address of a BSTR that receives the [**Voice**](voice-property.md) text property for a [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441).

</dd> </dl>

A [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) with its [**Voice**](voice-property.md) property set and its [**Enabled**](enabled-property.md) property set to **True** will be voice-accessible. If its [**Caption**](caption-property.md) property is also set it appears in the Voice Commands Window. If its [**Visible**](visible-property.md) property is set to **True**, it appears in the character's pop-up menu.

## See Also

[**IAgentCommand::SetVoice**](iagentcommand--setvoice.md), [**IAgentCommands::Add**](iagentcommands--add.md), [**IAgentCommands::Insert**](iagentcommands--insert.md)


 

 




