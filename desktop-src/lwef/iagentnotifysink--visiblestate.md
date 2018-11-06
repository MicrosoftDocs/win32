---
title: IAgentNotifySink VisibleState
description: IAgentNotifySink VisibleState
ms.assetid: b0346296-74e9-448f-aa6d-a9fb1e645f05
ms.topic: article
ms.date: 05/31/2018
---

# IAgentNotifySink::VisibleState

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT VisibleState(
   long dwCharID,  // character ID
   long bVisible,  // visibility flag
   long dwCause,   // cause of visible state
);                          
```

Notifies a client application when the visibility state of the character changes.

-   No return value.

<dl> <dt>

<span id="dwCharID"></span><span id="dwcharid"></span><span id="DWCHARID"></span>*dwCharID*
</dt> <dd>

Identifier of the character whose visibility state is changed.

</dd> <dt>

<span id="bVisible"></span><span id="bvisible"></span><span id="BVISIBLE"></span>*bVisible*
</dt> <dd>

Visibility flag. This Boolean value is **True** when character becomes visible and **False** when the character becomes hidden.

</dd> <dt>

<span id="dwCause"></span><span id="dwcause"></span><span id="DWCAUSE"></span>*dwCause*
</dt> <dd>

Cause of last change to the character's visibility state. The parameter may be one of the following:



| Value                                                                   | Description                                                                                 |
|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| **const unsigned short** **NeverShown = 0;**<br/>                 | Character has not been shown.                                                               |
| **const unsigned short** **UserHid = 1;**<br/>                    | User hid the character with the character's taskbar icon pop-up menu or with speech input.. |
| **const unsigned short** **UserShowed = 2;**<br/>                 | User showed the character.                                                                  |
| **const unsigned short** **ProgramHid = 3;**<br/>                 | Your application hid the character.                                                         |
| **const unsigned short** **ProgramShowed = 4;**<br/>              | Your application showed the character.                                                      |
| **const unsigned short** **OtherProgramHid = 5;**<br/>            | Another application hid the character.                                                      |
| **const unsigned short** **OtherProgramShowed = 6;**<br/>         | Another application showed the character.                                                   |
| **const unsigned short** **UserHidViaCharacterMenu = 7**<br/>     | User hid the character with the character's pop-up menu.                                    |
| **const unsigned short** **UserHidViaTaskbarIcon = UserHid**<br/> | User hid the character with the character's taskbar icon pop-up menu or using speech input. |



 

</dd> </dl>

## See Also

[**IAgentCharacter::GetVisible**](iagentcharacter--getvisible.md), [**IAgentCharacter::GetVisibilityCause**](iagentcharacter--getvisibilitycause.md)


 

 





