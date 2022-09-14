---
title: GestureAt Method
description: GestureAt Method
ms.assetid: c84e9363-e905-476a-832b-9acf6ddee5f1
ms.topic: article
ms.date: 05/31/2018
---

# GestureAt Method

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Plays the gesturing animation for the specified character at the specified location.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").GestureAt** *x,y*



| Part  | Description                                                                                                                                                                                               |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *x,y* | Required. An integer value that indicates the horizontal (*x*) screen coordinate and vertical (*y*) screen coordinate to which the character will gesture. These coordinates must be specified in pixels. |



 

</dd> </dl>

## Remarks

The server automatically plays the appropriate animation to gesture toward the specified location. The coordinates are always relative to the screen origin (upper left).

If you declare an object reference and set it to this method, it returns a [**Request**](/windows/desktop/lwef/the-request-object) object. In addition, if the associated animation has not been loaded on the local machine, the server sets the **Request** object's [**Status**](status-property.md) property to "failed" with an appropriate error number. Therefore, if you are using the HTTP protocol to access character animation data, use the [**Get**](get-method.md) method to load the **Gesturing** state animations before calling the **GestureAt** method.

 

 