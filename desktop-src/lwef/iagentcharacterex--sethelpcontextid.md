---
title: IAgentCharacterEx SetHelpContextID
description: IAgentCharacterEx SetHelpContextID
ms.assetid: 218e970e-825e-441d-8947-30ec6a2845bd
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacterEx::SetHelpContextID

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetHelpContextID(
   long ulHelpID  // ID for help topic
);
```

Sets the [**HelpContextID**](helpcontextid-property.md) for the character.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="ulHelpID"></span><span id="ulhelpid"></span><span id="ULHELPID"></span>*ulHelpID*
</dt> <dd>

The context number of the help topic for associated with a character; used to provide context-sensitive Help for the character.

</dd> </dl>

If you've created a Windows Help file for your application and set this in the character's [**HelpFile**](helpfile-property.md) property, Microsoft Agent automatically calls Help when [**HelpModeOn**](helpmodeon-property.md) is set to **True** and the user selects the character. If there is a context number in the [**HelpContextID**](helpcontextid-property.md), Agent calls Help and searches for the topic identified by the current context number. The current context number is the value of **HelpContextID** for the character. If there is a context number in the **HelpContextID** property, Help displays a topic corresponding to the current Help context; otherwise it displays "No Help topic associated with this item."

This setting applies only when your client application is the active client of the topmost character. It does not affect other clients of the character or other characters that your client application is using.

> [!Note]  
> Building a Help file requires the Microsoft Windows Help Compiler.

 

## See Also

[**IAgentCharacterEx::GetHelpContextID**](iagentcharacterex--gethelpcontextid.md), [**IAgentCharacterEx::SetHelpModeOn**](iagentcharacterex--sethelpmodeon.md), [**IAgentCharacterEx::SetHelpFileName**](iagentcharacterex--sethelpfilename.md)


 

 




