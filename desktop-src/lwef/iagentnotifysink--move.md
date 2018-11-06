---
title: IAgentNotifySink Move
description: IAgentNotifySink Move
ms.assetid: d1809fdb-df4b-4884-b9e8-2877a814dc9a
ms.topic: article
ms.date: 05/31/2018
---

# IAgentNotifySink::Move

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT Move(
   long dwCharID,  // character ID
   long x,         // x-coordinate of new location
   long y,         // y-coordinate of new location
   long dwCause    // cause of move state
);                          
```

Notifies a client application when the character has been moved.

-   No return value.

<dl> <dt>

<span id="dwCharID"></span><span id="dwcharid"></span><span id="DWCHARID"></span>*dwCharID*
</dt> <dd>

Identifier of the character that has been moved.

</dd> <dt>

<span id="x"></span><span id="X"></span>*x*
</dt> <dd>

The x-coordinate of the new position in pixels, relative to the screen origin (upper left). The location of a character is based on the upper left corner of its animation frame.

</dd> <dt>

<span id="y"></span><span id="Y"></span>*y*
</dt> <dd>

The y-coordinate of the new position in pixels, relative to the screen origin (upper left). The location of a character is based on the upper left corner of its animation frame.

</dd> <dt>

<span id="dwCause"></span><span id="dwcause"></span><span id="DWCAUSE"></span>*dwCause*
</dt> <dd>

The cause of the character move. The parameter may be one of the following:



| Value                                                          | Description                                                                          |
|----------------------------------------------------------------|--------------------------------------------------------------------------------------|
| **const unsigned short** **NeverMoved = 0;**<br/>        | Character has not been moved.                                                        |
| **const unsigned short** **UserMoved = 1;**<br/>         | User dragged the character.                                                          |
| **const unsigned short** **ProgramMoved = 2;**<br/>      | Your application moved the character.                                                |
| **const unsigned short** **OtherProgramMoved = 3;**<br/> | Another application moved the character.                                             |
| **const unsigned short** **SystemMoved = 4**<br/>        | The server moved the character to keep it onscreen after a screen resolution change. |



 

</dd> </dl>

This event is sent to all clients of the character.

## See Also

[**IAgentCharacter::GetMoveCause**](iagentcharacter--getmovecause.md), [**IAgentCharacter::MoveTo**](iagentcharacter--moveto.md)


 

 





