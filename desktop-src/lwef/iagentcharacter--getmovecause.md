---
title: IAgentCharacter GetMoveCause
description: IAgentCharacter GetMoveCause
ms.assetid: 36cdd3bc-65b6-469f-9344-93403c1d24e0
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacter::GetMoveCause

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetMoveCause(
   long * pdwCause  // address of variable for cause of character move
);
```

Retrieves the cause of the character's last move.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pdwCause"></span><span id="pdwcause"></span><span id="PDWCAUSE"></span>*pdwCause*
</dt> <dd>

Address of a variable that receives the cause of the character's last move and will be one of the following:



| Value                                                               | Description                                                                                     |
|----------------------------------------------------------------|--------------------------------------------------------------------------------------|
| **const unsigned short** **NeverMoved = 0;**<br/>        | Character has not been moved.                                                        |
| **const unsigned short** **UserMoved = 1;**<br/>         | User dragged the character.                                                          |
| **const unsigned short** **ProgramMoved = 2;**<br/>      | Your application moved the character.                                                |
| **const unsigned short** **OtherProgramMoved = 3;**<br/> | Another application moved the character.                                             |
| **const unsigned short** **SystemMoved = 4**<br/>        | The server moved the character to keep it onscreen after a screen resolution change. |



 

</dd> </dl>

## See Also

[**IAgentNotifySink::Move**](iagentnotifysink--move.md)


 

 





