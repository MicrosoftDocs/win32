---
title: IAgentUserInput GetCount
description: IAgentUserInput GetCount
ms.assetid: 9c127387-b680-405a-9a62-ee08cc70813a
ms.topic: article
ms.date: 05/31/2018
---

# IAgentUserInput::GetCount

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetCount(
   long * pdwCount  // address of a variable for number of alternatives 
);
```

Retrieves the number of [**Command**](command-event.md) alternatives passed to an [**IAgentNotifySink::Command**](iagentnotifysink--command.md) callback.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pdwCount"></span><span id="pdwcount"></span><span id="PDWCOUNT"></span>*pdwCount*
</dt> <dd>

Address of a variable that receives the count of [**Commands**](command-event.md) alternatives identified by the server.

</dd> </dl>

If voice input was not the source for the command, for example, if the user selected the command from the character's pop-up menu, **GetCount** returns 1. If **GetCount** returns zero (0), the speech recognition engine detected spoken input but determined that there was no matching command.

 

 




