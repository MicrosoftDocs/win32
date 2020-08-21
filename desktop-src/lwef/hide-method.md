---
title: Hide Method
description: Hide Method
ms.assetid: c30eda78-0951-43b4-8ae1-daccbd41170d
ms.topic: article
ms.date: 05/31/2018
---

# Hide Method

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Hides the specified character.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").Hide** \[*Fast*\]



| Part   | Description                                                                                                                                                                                                                                      |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Fast* | Optional. A Boolean value that indicates whether to skip the animation associated with the character's Hiding state **True** Does not play the **Hiding** animation. <br/> **False** (Default) Plays the **Hiding** animation. <br/> |



 

</dd> </dl>

## Remarks

The server queues the actions of the **Hide** method in the character's queue, so you can use it to hide the character after a sequence of other animations. You can play the action immediately by using the [**Stop**](stop-method.md) method before calling this method.

If you declare an object reference and set it to this method, it returns a [**Request**](/windows/desktop/lwef/the-request-object) object. In addition, if the associated **Hiding** animation has not been loaded and you have not specified the **Fast** parameter as **True**, the server sets the **Request** object [**Status**](status-property.md) property to "failed" with an appropriate error number. Therefore, if you are using the HTTP protocol to access character or animation data, use the [**Get**](get-method.md) method and specify the **Hiding** state to load the animation before calling the **Hide** method.

Hiding a character can also result in triggering the [**ActivateInput**](activateinput-event.md) event of another client.

> [!Note]  
> Hidden characters cannot access the audio channel. The server will pass back a failure status in the [**RequestComplete**](requestcomplete-event.md) event if you generate an animation request and the character is hidden.

 

## See Also

[**Show method**](show-method.md)


 

