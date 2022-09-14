---
title: IAgentAudioOutputProperties GetEnabled
description: IAgentAudioOutputProperties GetEnabled
ms.assetid: a1e555e1-98f1-4a3d-b6ba-4cd35348db2b
ms.topic: article
ms.date: 05/31/2018
---

# IAgentAudioOutputProperties::GetEnabled

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT GetEnabled(
long * pbEnabled  // address of variable for audio output Enabled setting 
);                      
```

Retrieves a value indicating whether character speech output is enabled.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="pbEnabled"></span><span id="pbenabled"></span><span id="PBENABLED"></span>*pbEnabled*
</dt> <dd>

Address of a variable that receives **True** if the speech output is currently enabled and **False** if disabled.

</dd> </dl>

Because this setting affects spoken output (TTS and sound file) for all characters, only the user can change this property in the Microsoft Agent property sheet.

 

 




