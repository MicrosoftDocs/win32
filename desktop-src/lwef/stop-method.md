---
title: Stop Method (Legacy Windows Environment Features)
description: Stop Method
ms.assetid: 68372f72-db9c-447c-a3e4-488940c730d7
ms.topic: article
ms.date: 05/31/2018
---

# Stop Method (Legacy Windows Environment Features)

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Stops the animation for the specified character.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").Stop** \[*Request*\]



| Part      | Description                                                                                   |
|-----------|-----------------------------------------------------------------------------------------------|
| *Request* | Optional. A [**Request**](/windows/desktop/lwef/the-request-object) object specifying a particular animation call. |



 

</dd> </dl>

## Remarks

To specify the request parameter, you must create a variable and assign the animation request you want to stop. If you don't set the **Request** parameter, the server stops all animations for the character, including queued [**Get**](get-method.md) calls, and clears its animation queue unless the character is currently playing its **Hiding** or **Showing** animation. This method does not stop non-queued **Get** calls.

To stop a specific animation or [**Get**](get-method.md) call, declare an object variable and assign your animation request to that variable:


```
   Dim MyRequest
   Dim Genie

   Agent1.Characters.Load "Genie", "https://agent.microsoft.com/characters/v2/genie/genie.acf"

   Set Genie = Agent1.Characters ("Genie")

   Genie.Get "state", "Showing"
   Genie.Get "animation", "Greet, GreetReturn"

   Genie.Show
   
   'This animation will never play
   Set MyRequest = Genie.Play ("Greet")
   
   Genie.Stop MyRequest
```



This method will not generate a [**Request**](/windows/desktop/lwef/the-request-object) object.

## See Also

[**StopAll method**](stopall-method.md)


 

 
