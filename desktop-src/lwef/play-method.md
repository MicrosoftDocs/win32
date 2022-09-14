---
title: Play Method (Legacy Windows Environment Features)
description: Play Method
ms.assetid: 7e89341a-b4d3-4bea-8e7f-31c649ff06b3
ms.topic: article
ms.date: 05/31/2018
---

# Play Method (Legacy Windows Environment Features)

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Plays the specified animation for the specified character.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").Play** "*AnimationName*"

</dd> </dl> 

| Part            | Description                                                          |
|-----------------|----------------------------------------------------------------------|
| *AnimationName* | Required. A string that specifies the name of an animation sequence. |



 

## Remarks

An animation's name is defined when the character is compiled with the Microsoft Agent Character Editor. Before playing the specified animation, the server attempts to play the **Return** animation for the previous animation, if one has been assigned.

When accessing a character's animations using a conventional file protocol, you can simply use the **Play** method specifying the name of the animation. However, if you are using the HTTP protocol to access character animation data, use the **Get** method to load the animation before calling the **Play** method.

For more information, see the **Get** method.

To simplify your syntax, you can declare an object reference and set it to reference the [**Character**](/windows/desktop/lwef/the-characters-object) object in the [**Characters**](/windows/desktop/lwef/the-characters-object) collection and use the reference as part of your **Play** statements:


```
   Dim Genie   
   Agent1.Characters.Load "Genie", "https://agent.microsoft.com/characters/v2/genie/genie.acf"

   Set Genie = Agent1.Characters ("Genie")
   
   Genie.Get "state", "Showing"
   Genie.Show

   Genie.Get "animation", "Greet, GreetReturn"
   Genie.Play "Greet"
   Genie.Speak "Hello."
```



If you declare an object reference and set it to this method, it returns a [**Request**](/windows/desktop/lwef/the-request-object) object. In addition, if you specify an animation that is not loaded or if the character has not been successfully loaded, the server sets the [**Status**](status-property.md) property of **Request** object to "failed" with an appropriate error number. However, if the animation does not exist and the character's data has already been successfully loaded, the server raises an error.

The **Play** method does not make the character visible. If the character is not visible, the server plays the animation invisibly, and sets the [**Status**](status-property.md) property of the [**Request**](/windows/desktop/lwef/the-request-object) object.

 

 
