---
title: IAgentCharacter GetVisibilityCause
description: IAgentCharacter GetVisibilityCause
ms.assetid: 46f681de-1c99-4f90-a3fe-aae04bb75339
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacter::GetVisibilityCause

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetVisibilityCause(
   long * pdwCause  // address of variable for cause of character visible state
);
```

Retrieves the cause of the character's visible state.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pdwCause"></span><span id="pdwcause"></span><span id="PDWCAUSE"></span>*pdwCause*
</dt> <dd>

Address of a variable that receives the cause of the character's last visibility state change and will be one of the following:



| Value                                                                   | Description                                                                                 |
|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| **const unsigned short** **NeverShown = 0;**<br/>                 | Character has not been shown.                                                               |
| **const unsigned short** **UserHid = 1;**<br/>                    | User hid the character with the character's taskbar icon pop-up menu or using speech input. |
| **const unsigned short** **UserShowed = 2;**<br/>                 | User showed the character.                                                                  |
| **const unsigned short** **ProgramHid = 3;**<br/>                 | Your application hid the character.                                                         |
| **const unsigned short** **ProgramShowed = 4;**<br/>              | Your application showed the character.                                                      |
| **const unsigned short** **OtherProgramHid = 5;**<br/>            | Another application hid the character.                                                      |
| **const unsigned short** **OtherProgramShowed = 6;**<br/>         | Another application showed the character.                                                   |
| **const unsigned short** **UserHidViaCharacterMenu = 7**<br/>     | User hid the character with the character's pop-up menu.                                    |
| **const unsigned short** **UserHidViaTaskbarIcon = UserHid**<br/> | User hid the character with the character's taskbar icon pop-up menu or using speech input. |



 

</dd> </dl>

## See Also

[**IAgentNotifySink::VisibleState**](iagentnotifysink--visiblestate.md)


 

 





