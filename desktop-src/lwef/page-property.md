---
title: Page Property
description: Page Property
ms.assetid: c3cf07e9-a324-443b-a0c0-2fb80463548f
ms.topic: article
ms.date: 05/31/2018
---

# Page Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets the page displayed in the Microsoft Agent property sheet window.

</dd> <dt>

<span id="Syntax_"></span><span id="syntax_"></span><span id="SYNTAX_"></span>**Syntax** 
</dt> <dd>

*agent***.PropertySheet.Page** \[ = *string*\]



| Part     | Description                                                                                                                                                                                                             |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *string* | A string expression with one of the following values. **"Speech"** Displays the Speech Input page.<br/> **"Output"** Displays the Output page.<br/> **"Copyright"** Displays the Copyright page.<br/> |



 

</dd> </dl>

## Remarks

If no speech engine is installed, setting **Page** to **"Speech"** has no effect. Also, the window's **Visible** property must be set to **True** for the user to see the page.

> [!Note]  
> The user can override this property.

 

 

 





