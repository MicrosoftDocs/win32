---
title: IAgentBalloon GetEnabled
description: IAgentBalloon GetEnabled
ms.assetid: 1a5ea6c0-6150-459f-95eb-a9c7598c1d94
ms.topic: article
ms.date: 05/31/2018
---

# IAgentBalloon::GetEnabled

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetEnabled(
  long * pbEnabled  // address of variable for Enabled setting 
);                  // for word balloon
```

Retrieves the value of the [**Enabled**](enabled-property.md) property for a word balloon.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbEnabled"></span><span id="pbenabled"></span><span id="PBENABLED"></span>*pbEnabled*
</dt> <dd>

The address of a variable that receives **True** when the word balloon is enabled and **False** when it is disabled.

</dd> </dl>

The Microsoft Agent server automatically displays the word balloon for spoken output, unless it is disabled. The word balloon can be disabled for a character in the Microsoft Agent Character Editor, or (by the user) for all characters in the Microsoft Agent property sheet. If the user disables the word balloon, the client cannot restore it.

 

 




