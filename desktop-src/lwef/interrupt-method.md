---
title: Interrupt Method
description: Interrupt Method
ms.assetid: b8442e25-a629-47c7-acdd-1d28e74d78a2
ms.topic: article
ms.date: 05/31/2018
---

# Interrupt Method

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Interrupts the animation for the specified character.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").Interrupt** *Request*



| Part      | Description                                                                  |
|-----------|------------------------------------------------------------------------------|
| *Request* | A [**Request**](/windows/desktop/lwef/the-request-object) object for a particular animation call. |



 

</dd> </dl>

## Remarks

You can use this to sync up animation between characters. For example, if another character is in a looping animation, this method will stop the loop and move to the next animation in the character's queue. You cannot interrupt a character animation that you are not using (that you have not loaded).

To specify the request parameter, you must create a variable and assign the animation request you want to interrupt:


```
   Dim GenieRequest as Object
   Dim RobbyRequest as Object
   Dim Genie as Object
   Dim Robby as Object

   Sub FormLoad()

      MyAgent1.Characters.Load "Genie", "Genie.acs"

      MyAgent1.Characters.Load "Robby", "Robby.acs"

      Set Genie = MyAgent1.Characters ("Genie")
      Set Robby = MyAgent1.Characters ("Robby")

      Genie.Show

      Genie.Speak "Just a moment"

      Set GenieRequest = Genie.Play ("Processing")

      Robby.Show
      Robby.Play "confused"
      Robby.Speak "Hey, Genie. What are you doing?"
      Robby.Interrupt GenieRequest

      Genie.Speak "I was just checking on something."

   End Sub
```



You cannot interrupt the animation of the same character you specify in this method because the server queues the **Interrupt** method in that character's animation queue. Therefore, you can only use **Interrupt** to halt the animation of another character you have loaded.

If you declare an object reference and set it to this method, it returns a [**Request**](/windows/desktop/lwef/the-request-object) object.

> [!Note]  
> **Interrupt** does not flush the character's queue; it halts the existing animation and moves on to the next animation in the character's queue. To halt and flush a character's queue, use the [**Stop**](stop-method.md) method.

 

## See Also

[**Stop method**](stop-method.md)


 

 