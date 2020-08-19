---
title: MoveTo Method
description: MoveTo Method
ms.assetid: cca2b1b8-0d44-4272-9f0b-f7afd091d802
ms.topic: article
ms.date: 05/31/2018
---

# MoveTo Method

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Moves the specified character to the specified location.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").MoveTo** *x,y*\[*Speed*\]



| Part    | Description                                                                                                                                                                                     |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *x,y*   | Required. An integer value that indicates the left edge (*x*) and top edge (*y*) of the animation frame. Express these coordinates in pixels.                                                   |
| *Speed* | Optional. A Long integer value specifying in milliseconds how quickly the character's frame moves. The default value is 1000. Specifying zero (0) moves the frame without playing an animation. |



 

</dd> </dl>

## Remarks

The server automatically plays the appropriate animation assigned to the **Moving** states. The location of a character is based on the upper left corner of its frame.

If you declare an object variable and set it to this method, it returns a [**Request**](/windows/desktop/lwef/the-request-object) object. In addition, if the associated animation has not been loaded on the local machine, the server sets the **Request** object's [**Status**](status-property.md) property to "failed" with an appropriate error number. Therefore, if you are using the HTTP protocol to access character or animation data, use the [**Get**](get-method.md) method to load the **Moving** state animations before calling the **MoveTo** method.

Even if the animation is not loaded, the server still moves the frame.

> [!Note]  
> If you call **MoveTo** with a nonzero value before the character is shown, it will return a failure status if you assigned it a [**Request**](/windows/desktop/lwef/the-request-object) object, because the nonzero value indicates that you are attempting to play an animation when the character is not visible.

 

> [!Note]  
> The *Speed* parameter's actual effect may vary based on the speed of the processor of the computer and the priority of other tasks running on the system.

 

 

 