---
title: Activate Method
description: Activate Method
ms.assetid: 8111139d-1453-416e-8f08-38c06669ff4d
ms.topic: article
ms.date: 05/31/2018
---

# Activate Method

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>[**Description**](../wmformat/description.md)
</dt> <dd>

Sets the active client or character.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").Activate** \[*State*\]



| Part    | Description                                                                                                                                                                           |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *State* | Optional. You can specify the following values for this parameter: 0 Not the active client.<br/> 1 The active client. <br/> 2 (Default) The topmost character.<br/> |



 

</dd> </dl>

## Remarks

When multiple characters are visible, only one of the characters receives speech input at a time. Similarly, when multiple client applications share the same character, only one of the clients receives mouse input (for example, Microsoft Agent control click or drag events). The character set to receive mouse and speech input is the topmost character and the client that receives the input is the active client of that character. (The topmost character's window also appears at the top of the character window's z-order.) Typically, the user determines the topmost character by explicitly selecting the character. However, topmost activation also changes when a character is shown or hidden (the character becomes or is no longer topmost, respectively.)

You can also use this method to explicitly manage when your client receives input directed to the character such as when your application itself becomes active. For example, setting *State* to 2 makes the character topmost and your client receives all mouse and speech input events generated from user interaction with the character. Therefore, it also makes your client the input-active client of the character.

However, you can also set yourself to be the active client for a character without making the character topmost, by setting *State* to 1. This enables your client to receive input directed to that character when the character becomes topmost. Similarly, you can set your client to not be the active client (not to receive input) when the character becomes topmost, by setting *State* to 0.

Avoid calling this method directly after a [**Show**](/previous-versions/visualstudio/foxpro/d79z7xxa(v=vs.71)) method. **Show** automatically sets the input-active client. When the character is hidden, the [**Activate**](/previous-versions/visualstudio/foxpro/01ayxx68(v=vs.71)) call may fail if it gets processed before the **Show** method completes.

If you call this method to a function, it returns a Boolean value that indicates whether the method succeeded. Attempting to call this method with the *State* parameter set to 2 when the specified character is hidden will fail. Similarly, if you set *State* to 0 and your application is the only client, this call fails because a character must always have a topmost client.


```
   Dim Genie as Object

   Sub FormLoad()

   Agent1.Characters.Load "Genie", "Genie.acs"

   Set Genie = Agent1.Characters ("Genie")

   If (Genie. Activate = True) Then
      'I'm active

   Else
      'I must be hidden or something

   End If 
   
   End Sub
```



> [!Note]  
> Calling this method with *State* set to 1 does not typically generate an [**ActivateInput**](https://www.bing.com/search?q=**ActivateInput**) event unless there are no other characters loaded or your application is already input-active.

 

## See Also

[**ActivateInput event**](activateinput-event.md), [**DeactivateInput event**](deactivateinput-event.md)


 

