---
title: IAgentCharacterEx GetHelpFileName
description: IAgentCharacterEx GetHelpFileName
ms.assetid: 52d5a874-ad3e-4833-9e3e-ff485414c54c
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacterEx::GetHelpFileName

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetHelpFileName(
   BSTR * pbszName  // address of Help filename
);
```

Retrieves the HelpFileName for a character.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbszName"></span><span id="pbszname"></span><span id="PBSZNAME"></span>*pbszName*
</dt> <dd>

Address of a variable that receives the Help filename for the character.

</dd> </dl>

If you've created a Windows Help file for your application and set the character's [**HelpFile**](helpfile-property.md) property, Microsoft Agent automatically calls Help when [**HelpModeOn**](helpmodeon-property.md) is set to **True** and the user clicks the character or selects a command from its pop-up menu. If there is a context number in the selected command's [**HelpContextID**](helpcontextid-property.md) property, Help displays a topic corresponding to the current Help context; otherwise it displays "No Help topic associated with this item."

This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

> [!Note]  
> Building a Help file requires the Microsoft Windows Help Compiler.

 

## See Also

[**IAgentCommandsEx::SetHelpContextID**](iagentcommandsex--sethelpcontextid.md), [**IAgentCharacterEx::SetHelpModeOn**](iagentcharacterex--sethelpmodeon.md), [**IAgentCharacterEx::SetHelpFileName**](iagentcharacterex--sethelpfilename.md)


 

 




