---
title: The AudioOutput Object
description: The AudioOutput Object
ms.assetid: 7c1c6079-f445-4980-9559-8d26b6014e89
ms.topic: article
ms.date: 05/31/2018
---

# The AudioOutput Object

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

This object provides access to audio output properties maintained by the server. The properties are read-only, but the user can change them in the Microsoft Agent property sheet.

If you declare an object variable of type [**IAgentCtlAudioObjectEx**](https://www.bing.com/search?q=**IAgentCtlAudioObjectEx**), you will not be able to access all properties for the [**AudioOutput**](/windows/desktop/lwef/the-audiooutput-object) object. While Agent also supports [**IAgentCtlAudioObject**](https://www.bing.com/search?q=**IAgentCtlAudioObject**), this latter interface is provided only for backward compatibility and supports only those properties in previous releases.

-   [**Enabled**](enabled-property-ao.md)
-   [**SoundEffects**](soundeffects-property.md)
-   [**Status**](status-property.md)

 

 