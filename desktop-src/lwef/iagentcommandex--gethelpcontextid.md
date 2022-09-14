---
title: IAgentCommandEx GetHelpContextID
description: IAgentCommandEx GetHelpContextID
ms.assetid: 97b390f3-ab24-4c09-aa87-d76076eba995
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommandEx::GetHelpContextID

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetHelpContextID(
   long * pulID  //  address of command's help topic ID
);
```

Retrieves the [**HelpContextID**](helpcontextid-property-com.md) for a [**Command**](/windows/desktop/lwef/the-command-object) object.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pulID"></span><span id="pulid"></span><span id="PULID"></span>*pulID*
</dt> <dd>

Address of a variable that receives the context number of the help topic associated with the [**Command**](/windows/desktop/lwef/the-command-object) object.

</dd> </dl>

If you've created a Windows Help file for your application and set your character's [**HelpFile**](helpfile-property.md) property to this file, Microsoft Agent automatically calls Help when [**HelpModeOn**](helpmodeon-property.md) is set to **True** and the user selects the command. If there is a context number in the [**HelpContextID**](helpcontextid-property-com.md), Agent calls Help and searches for the topic identified by the current context number. The current context number is the value of **HelpContextID** for the command.

> [!Note]  
> Building a Help file requires the Microsoft Windows Help Compiler.

 

## See Also

[**IAgentCommandEx::SetHelpContextID**](iagentcommandex--sethelpcontextid.md), [**IAgentCharacterEx::SetHelpModeOn**](iagentcharacterex--sethelpmodeon.md), [**IAgentCharacterEx::SetHelpFileName**](iagentcharacterex--sethelpfilename.md)


 

 