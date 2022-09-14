---
title: Add Method
description: Add Method
ms.assetid: dd258294-33d6-45f5-a6a1-a3a56b12a7df
ms.topic: article
ms.date: 05/31/2018
---

# Add Method

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Adds a [Command](the-command-object.md) object to the [Commands](the-commands-collection-object.md) collection.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").Commands.Add** *Name*, *Caption*, *Voice*, *Enabled*, *Visible*



| Part      | Description                                                                                                                                                                                                                                                                                                         |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Name*    | Required. A string value corresponding to the ID you assign for the command.                                                                                                                                                                                                                                        |
| *Caption* | Optional. A string value corresponding to the name that will appear in the character's pop-up menu and in the Commands Window when the client application is input-active. For more information, see the [Command](the-command-object.md) object's [Caption](caption-property.md) property.                       |
| *Voice*   | Optional. A string value corresponding to the words or phrase to be used by the speech engine for recognizing this command. For more information on formatting alternatives for the string, see the [Command](the-command-object.md) object's [Voice](voice-property.md) property.                                |
| *Enabled* | Optional. A Boolean value indicating whether the command is enabled. The default value is **True**. For more information, see the [Command](the-command-object.md) object's [Enabled](enabled-property.md) property.                                                                                              |
| *Visible* | Optional. A Boolean value indicating whether the command is visible in the character's pop-up menu for the character when the client application is input-active. The default value is **True**. For more information, see the [Command](the-command-object.md) object's [Visible](visible-property.md) property. |



 

</dd> </dl>

## Remarks

The value of a [Command](the-command-object.md) object's [Name](name-property.md) property must be unique within its [Commands](the-commands-collection-object.md) collection. You must remove a Command before you can create a new Command with the same Name property setting. Attempting to create a Command with a Name property that already exists raises an error.

This method also returns a [Command](the-command-object.md) object. This enables you to declare an object and assign a Command to it when you call the Addmethod.


```
   Dim Cmd1 as IAgentCtlCommandEx
   Set Cmd1 = Genie.Commands.Add ("my first command", "Test", "Test", True, True)
   Cmd1.VoiceCaption = "this is a test"
```



## Related topics

<dl> <dt>

[**Insert method**](insert-method.md)
</dt> <dt>

[**RemoveAll method**](removeall-method.md)
</dt> <dt>

[**Remove method**](remove-method.md)
</dt> </dl>

 

 




