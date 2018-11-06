---
title: ShowDefaultCharacterProperties Method
description: ShowDefaultCharacterProperties Method
ms.assetid: a3b109c0-5701-4a72-baae-bcbb97b025a3
ms.topic: article
ms.date: 05/31/2018
---

# ShowDefaultCharacterProperties Method

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Displays the default character's properties.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.ShowDefaultCharacterProperties** \[ *X* , *Y* \]



| Part | Description                                                                                                                                                |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *X*  | Optional. A short integer value that indicates the horizontal (*X* ) screen coordinate to display the window. This coordinate must be specified in pixels. |
| *Y*  | Optional. A short integer value that indicates the vertical (*Y*) screen coordinate to display the window. This coordinate must be specified in pixels.    |



 

</dd> </dl>

## Remarks

Calling this method displays the default character properties window (not the Microsoft Agent property sheet). If you do not specify the X and Y coordinates, the window appears at the last location it was displayed.

## See Also

[**DefaultCharacterChange event**](defaultcharacterchange-event.md)


 

 




