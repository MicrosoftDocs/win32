---
title: IAgentAudioOutputProperties GetUsingSoundEffects
description: IAgentAudioOutputProperties GetUsingSoundEffects
ms.assetid: 3ccf90b1-a2aa-482a-9f96-85d735532c11
ms.topic: article
ms.date: 05/31/2018
---

# IAgentAudioOutputProperties::GetUsingSoundEffects

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetUsingSoundEffects(
long * pbUsingSoundEffects  // address of variable sound effects output 
);                          // setting 
```

Retrieves a value indicating whether sound effects output is enabled.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbUsingSoundEffects"></span><span id="pbusingsoundeffects"></span><span id="PBUSINGSOUNDEFFECTS"></span>*pbUsingSoundEffects*
</dt> <dd>

Address of a variable that receives **True** if the sound effects output is currently enabled and **False** if disabled.

</dd> </dl>

Sound effects for a character's animation are assigned in the Microsoft Agent Character Editor. Because this setting affects sound effects output for all characters, only the user can change this property in the Microsoft Agent property sheet.

 

 




