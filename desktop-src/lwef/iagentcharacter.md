---
title: IAgentCharacter
description: IAgentCharacter
ms.assetid: 77d0ffc2-76a2-4a21-88e1-1ca85b8c5d2f
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCharacter

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

**IAgentCharacter** defines an interface that allows applications to query character properties and play animations. These functions are also available from [**IAgentCharacterEx**](iagentcharacterex.md). You can use some method return request IDs to track their status in the character's queue and to synchronize your code with the character's current animation state.

**Methods in Vtable Order**



| IAgentCharacter Methods                                           | Description                                                                       |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [**GetVisible**](iagentcharacter--getvisible.md)                 | Returns whether the character (frame) is currently visible.                       |
| [**SetPosition**](iagentcharacter--setposition.md)               | Sets the position of the character frame.                                         |
| [**GetPosition**](iagentcharacter--getposition.md)               | Returns the position of the character frame.                                      |
| [**SetSize**](iagentcharacter--setsize.md)                       | Sets the size of the character frame.                                             |
| [**GetSize**](iagentcharacter--getsize.md)                       | Returns the size of the character frame.                                          |
| [**GetName**](iagentcharacter--getname.md)                       | Returns the name of the character.                                                |
| [**GetDescription**](iagentcharacter--getdescription.md)         | Returns the description for the character.                                        |
| [**GetTTSSpeed**](iagentcharacter--getttsspeed.md)               | Returns the current TTS output speed setting for the character.                   |
| [**GetTTSPitch**](iagentcharacter--getttspitch.md)               | Returns the current TTS pitch setting for the character.                          |
| [**Activate**](iagentcharacter--activate.md)                     | Sets whether a client is active or a character is topmost.                        |
| [**SetIdleOn**](iagentcharacter--setidleon.md)                   | Sets the server's idle processing.                                                |
| [**GetIdleOn**](iagentcharacter--getidleon.md)                   | Returns the setting of the server's idle processing.                              |
| [**Prepare**](iagentcharacter--prepare.md)                       | Retrieves animation data for the character.                                       |
| [**Play**](iagentcharacter--play.md)                             | Plays a specified animation.                                                      |
| [**Stop**](iagentcharacter--stop.md)                             | Stops an animation for a character.                                               |
| [**StopAll**](iagentcharacter--stopall.md)                       | Stops all animations for a character.                                             |
| [**Wait**](iagentcharacter--wait.md)                             | Holds the character's animation queue.                                            |
| [**Interrupt**](iagentcharacter--interrupt.md)                   | Interrupts a character's animation.                                               |
| [**Show**](iagentcharacter--show.md)                             | Displays the character and plays the character's **Showing** state animation.     |
| [**Hide**](iagentcharacter--hide.md)                             | Plays the character's **Hiding** state animation and hides the character's frame. |
| [**Speak**](iagentcharacter--speak.md)                           | Plays spoken output for the character.                                            |
| [**MoveTo**](iagentcharacter--moveto.md)                         | Moves the character frame to the specified location.                              |
| [**GestureAt**](iagentcharacter--gestureat.md)                   | Plays a gesturing animation based on the specified location.                      |
| [**GetMoveCause**](iagentcharacter--getmovecause.md)             | Retrieves the cause of the character's last move.                                 |
| [**GetVisibilityCause**](iagentcharacter--getvisibilitycause.md) | Retrieves the cause of the last change to the character's visibility state.       |
| [**HasOtherClients**](iagentcharacter--hasotherclients.md)       | Retrieves whether the character has other current clients.                        |
| [**SetSoundEffectsOn**](iagentcharacter--setsoundeffectson.md)   | Determines whether a character animation's sound effects play.                    |
| [**GetSoundEffectsOn**](iagentcharacter--getsoundeffectson.md)   | Retrieves whether a character's sound effects setting is enabled.                 |
| [**SetName**](iagentcharacter--setname.md)                       | Sets the character's name.                                                        |
| [**SetDescription**](iagentcharacter--setdescription.md)         | Sets the character's description.                                                 |
| [**GetExtraData**](iagentcharacter--getextradata.md)             | Retrieves additional data stored with the character.                              |



 

 

 




