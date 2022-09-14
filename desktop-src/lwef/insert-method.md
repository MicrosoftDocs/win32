---
title: Insert Method
description: Insert Method
ms.assetid: d58cfe50-ace7-4b0f-8539-c2e13a180c96
ms.topic: article
ms.date: 05/31/2018
---

# Insert Method

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Inserts a **Command** object in the **Commands** collection.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").Commands.Insert** *Name*, *RefName*, *Before*\_

*Caption*, *Voice, Enabled, Visible*



| Part      | Description                                                                                                                                                                                                                                                                                          |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Name*    | Required. A string value corresponding to the ID you assign to the [**Command**](/windows/desktop/lwef/the-command-object).                                                                                                                                                                                               |
| *RefName* | Required. A string value corresponding to the name (ID) of the command just above or below where you want to insert the new command.                                                                                                                                                                 |
| *Before*  | Optional. A Boolean value indicating whether to insert the new command before the command specified by *RefName*. **True** (Default). The new command will be inserted before the referenced command.<br/> **False** The new command will be inserted after the referenced command.<br/> |
| *Caption* | Optional. A string value corresponding to the name that will appear in the character's pop-up menu and in the Commands Window when the client application is input-active. For more information, see the [**Command**](/windows/desktop/lwef/the-command-object) object's [**Caption**](caption-property.md)property.    |
| *Voice*   | Optional. A string value corresponding to the words or phrase to be used by the speech engine for recognizing this command. For more information on formatting alternatives for the string, see the [**Command**](/windows/desktop/lwef/the-command-object) object's **Voice** property.                                  |
| *Enabled* | Optional. A Boolean value indicating whether the command is enabled. The default value is **True**. For more information, see the [**Command**](/windows/desktop/lwef/the-command-object) object's **Enabled** property.                                                                                                  |
| *Visible* | Optional. A Boolean value indicating whether the command is visible in the Commands Window when the client application is input-active. The default value is **True**. For more information, see the [**Command**](/windows/desktop/lwef/the-command-object) object's [**Visible**](visible-property.md) property.       |



 

</dd> </dl>

## Remarks

The value of a [**Command**](/windows/desktop/lwef/the-command-object) object's [**Name**](name-property.md) property must be unique within its [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection. You must remove a **Command** before you can create a new **Command** with the same **Name** property setting. Attempting to create a **Command** with a **Name** property that already exists raises an error.

This method also returns a [**Command**](/windows/desktop/lwef/the-command-object) object. This enables you to declare an object and assign a **Command** to it when you call the **Insert** method.


```
   Dim Cmd2 as IAgentCtlCommandEx
   Set Cmd2 = Genie.Commands.Insert ("my second command", "my first command",_ True, "Test", "Test", True, True)
   Cmd2.VoiceCaption = "this is a test"
```



## See Also

[**Add method**](add-method.md), [**Remove method**](remove-method.md), [**RemoveAll method**](removeall-method.md)


 

