---
title: IAgentCommand GetID
description: IAgentCommand GetID
ms.assetid: '4d8d8be7-7003-4ef3-abba-b5232267c993'
---

# IAgentCommand::GetID

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetID(
   long * pdwID  // address of ID for Command
);
```

Retrieves the ID for a [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441).

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pdwID"></span><span id="pdwid"></span><span id="PDWID"></span>*pdwID*
</dt> <dd>

The address of a variable that receives the ID of a [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441).

</dd> </dl>

## See Also

[**IAgentCommands::Add**](iagentcommands--add.md), [**IAgentCommands::Insert**](iagentcommands--insert.md), [**IAgentCommands::Remove**](iagentcommands--remove.md)


 

 




