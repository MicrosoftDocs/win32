---
title: IAgentCommandEx SetHelpContextID
description: IAgentCommandEx SetHelpContextID
ms.assetid: 861d55dc-f584-495c-a148-016af8f7a3e2
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommandEx::SetHelpContextID

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetHelpContextID(
   long ulID  //  ID for help topic
);
```

Sets the [**HelpContextID**](helpcontextid-property-com.md) for a [**Command**](/windows/desktop/lwef/the-command-object) object.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="ulID"></span><span id="ulid"></span><span id="ULID"></span>*ulID*
</dt> <dd>

The context number of the help topic associated with the [**Command**](/windows/desktop/lwef/the-command-object) object; used to provide context-sensitive Help for the command.

</dd> </dl>

If you've created a Windows Help file for your application and set this in the character's [**HelpFile**](helpfile-property.md) property. Microsoft Agent automatically calls Help when [**HelpModeOn**](helpmodeon-property.md) is set to **True** and the user selects the command. If there is a context number in the [**HelpContextID**](helpcontextid-property-com.md), Agent calls Help and searches for the topic identified by the current context number. The current context number is the value of **HelpContextID** for the command.

> [!Note]  
> Building a Help file requires the Microsoft Windows Help Compiler.

 

## See Also

[**IAgentCommandEx::GetHelpContextID**](iagentcommandex--gethelpcontextid.md), [**IAgentCharacterEx::SetHelpModeOn**](iagentcharacterex--sethelpmodeon.md), [**IAgentCharacterEx::SetHelpFileName**](iagentcharacterex--sethelpfilename.md)


 

 