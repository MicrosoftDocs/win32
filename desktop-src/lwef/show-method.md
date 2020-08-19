---
title: Show Method
description: Show Method
ms.assetid: 58adbb55-f4cb-4356-abc4-b85fa3af744d
ms.topic: article
ms.date: 05/31/2018
---

# Show Method

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Makes the specified character visible and plays its associated **Showing** animation.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").Show** \[*Fast*\]



| Part   | Description                                                                                                                                                                                                                              |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Fast* | Optional. A Boolean expression specifying whether the server plays the **Showing** animation. **True** Skips the **Showing** state animation. <br/> **False** (Default) Does not skip the **Showing** state animation. <br/> |



 

</dd> </dl>

## Remarks

If you declare an object reference and set it to this method, it returns a [**Request**](/windows/desktop/lwef/the-request-object) object. In addition, if the associated **Showing** animation has not been loaded and you have not specified the **Fast** parameter as **True**, the server sets the **Request** object's [**Status**](status-property.md) property to "failed" with an appropriate error number. Therefore, if you are using the HTTP protocol to access character animation data, use the [**Get**](get-method.md) method to load the **Showing** state animation before calling the **Show** method.

Avoid setting the **Fast** parameter to **True** without first playing an animation beforehand; otherwise, the character frame may display with no image. In particular, note that if you call [**MoveTo**](moveto-method.md) when the character is not visible, it does not play any animation. Therefore, if you call the **Show** method with **Fast** set to **True**, no image will display. Similarly, if you call [**Hide**](hide-method.md) then **Show** with **Fast** set to **True**, there will be no visible image.

## See Also

[**Hide method**](hide-method.md)


 

