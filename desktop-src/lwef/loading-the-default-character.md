---
title: Loading the Default Character
description: Loading the Default Character
ms.assetid: 4e91aef5-8402-401d-b09f-83be25011027
ms.topic: article
ms.date: 05/31/2018
---

# Loading the Default Character

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

Instead of loading only a specific character directly by specifying its filename, you can load the *default character*. The default character is a service intended to provide a shared, central Windows assistant that the user chooses. Microsoft Agent includes a property sheet as part of the default character service, known as the Character Properties window, which enables the user to change their selection of the default character.

Selection of the default character is limited to a character that supports the standard animation set, ensuring a basic level of consistency across characters. This does not exclude a character from having additional animations.

However, because the default character is intended for general-purpose use and may be shared by other applications at the same time, avoid loading the default character when you want a character exclusively for your application.

To load the default character, call the [**Load**](load-method.md) method without specifying a filename or path. Microsoft Agent automatically loads the current character set as the default character. If the user has not yet selected a default character, Agent will select the first character that supports the standard animation set. If none is available, the method will fail and report back the cause.

Although a client application can inquire as to the identity of the character, only a user can change its settings. You can use the [**ShowDefaultCharacterProperties**](showdefaultcharacterproperties-method.md) to display the Character Properties window.

The server will notify clients that have loaded the default character when a user changes a character selection, and pass the GUID of the new character. The server automatically unloads the former character and reloads the new character. The queues of any clients that have loaded the default character are halted and flushed. However, the queues of clients that have loaded the character explicitly using the character's filename are not affected. If necessary, the server also handles automatically resetting the text-to-speech (TTS) engine for the new character.

 

 




