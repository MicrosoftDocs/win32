---
title: IAgentCharacterEx SetHelpFileName
description: IAgentCharacterEx SetHelpFileName
ms.assetid: 1f8d2bd7-5821-46c0-b371-7ecbc526df72
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacterEx::SetHelpFileName

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetHelpFileName(
   BSTR bszName  // Help filename
);
```

Sets the HelpFileName for a character.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="bszName"></span><span id="bszname"></span><span id="BSZNAME"></span>*bszName*
</dt> <dd>

The Help filename for the character.

</dd> </dl>

If you've created a Windows Help file for your application and set the character's [**HelpFile**](helpfile-property.md) property, Microsoft Agent automatically calls Help when [**HelpModeOn**](helpmodeon-property.md) is set to **True** and the user clicks the character or selects a command from its pop-up menu. If there is a context number in the [**HelpContextID**](helpcontextid-property.md) property of the selected command, Help displays a topic corresponding to the current Help context; otherwise it displays "No Help topic associated with this item."

This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

> [!Note]  
> Building a Help file requires the Microsoft Windows Help Compiler.

 

## See Also

[**IAgentCommandsEx::SetHelpContextID**](iagentcommandsex--sethelpcontextid.md), [**IAgentCharacterEx::SetHelpModeOn**](iagentcharacterex--sethelpmodeon.md), [**IAgentCharacterEx::GetHelpFileName**](iagentcharacterex--gethelpfilename.md)


 

 




