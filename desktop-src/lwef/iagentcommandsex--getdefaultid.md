---
title: IAgentCommandsEx GetDefaultID
description: IAgentCommandsEx GetDefaultID
ms.assetid: 14079ae0-ad2c-4f38-9371-9914f8402e49
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommandsEx::GetDefaultID

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetDefaultID(
   long * pdwID  // address of default command's ID
);
```

Retrieves the ID of the default command in a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pdwID"></span><span id="pdwid"></span><span id="PDWID"></span>*pdwID*
</dt> <dd>

Address of a variable that receives the ID of the [**Command**](/windows/desktop/lwef/the-command-object) set as the default.

</dd> </dl>

This property returns the current default [**Command**](/windows/desktop/lwef/the-command-object) object in your [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection. The default command is bold in the character's pop-up menu. However, setting the default command does not change command handling or double-click events.

This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

## See Also

[**IAgentCommandsEx::SetDefaultID**](iagentcommandsex--setdefaultid.md)


 

 