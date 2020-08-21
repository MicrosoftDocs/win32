---
title: Microsoft Agent Animations for Genie Character
description: Microsoft Agent Animations for Genie Character
ms.assetid: 56c42d7a-32af-47cb-8578-0a89507a41ed
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft Agent Animations for Genie Character

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

The [Microsoft Agent Genie Character](https://www.microsoft.com/downloads/details.aspx?FamilyID=da86ba4e-bc2d-4c1d-b5a0-3183fe206414) is a copyrighted work of Microsoft Corporation.

Genie supports the animations listed in the table below. Refer to [Programming the Microsoft Agent Server Interface](/windows/desktop/lwef/programming-the-microsoft-agent-server-interface) and [Programming the Microsoft Agent Control](programming-the-microsoft-agent-control.md) for information on how to call the character's animations.

If accessing these character animations using the HTTP protocol and the control's [**Get**](get-method.md) or server's [**Prepare**](/windows/desktop/lwef/iagentcharacter--prepare) method, consider how you will download them. Instead of downloading all the animations at once, you may want to retrieve the **Showing** and **Speaking** state animations first. This will enable you to display the character quickly and have it speak while bringing down other animations asynchronously. In addition, to ensure that character and animation data load successfully, use the [**RequestComplete**](requestcomplete-event.md) event. If a load request fails, you can retry loading the data or display an appropriate message.

If an animation's **Return** animations is defined using Exit branches, you do not need to call it explicitly; Agent automatically plays the **Return** animation before the next animation. However, if a **Return** animation is listed, you must call the animation using the [**Play**](play-method.md) method before another animation to provide a smooth transition. If no **Return** animation is listed, the animation typically ends without needing a transitional animation.

The character file includes sound effects for some animation as noted in the following table. Sound effects play only if this option is enabled in the Microsoft Agent property sheet. You can also disable sound effects in your application.



| Animation                 | Return Animation         | Supports Speaking | Sound Effects | Assigned to State                            | Description                                                    |
|---------------------------|--------------------------|-------------------|---------------|----------------------------------------------|----------------------------------------------------------------|
| **Acknowledge**           | None                     | No                | **No**        | None                                         | Nods head                                                      |
| **Alert**                 | Yes, using Exit branches | Yes               | **No**        | **Listening**                                | Straightens and raises eyebrows                                |
| **Announce**              | Yes, using Exit branches | Yes               | **No**        | None                                         | Raises hand                                                    |
| **Blink**                 | None                     | No                | **No**        | **IdlingLevel1** **IdlingLevel2**<br/> | Blinks eyes                                                    |
| **Confused**              | Yes, using Exit branches | Yes               | **No**        | None                                         | Scratches head                                                 |
| **Congratulate**          | Yes, using Exit branches | Yes               | **Yes**       | None                                         | Applauds                                                       |
| **Congratulate\_2**       | Yes, using Exit branches | Yes               | **No**        | None                                         | Gives thumbs-up gesture                                        |
| **Decline**               | Yes, using Exit branches | Yes               | **No**        | None                                         | Raises hands and shakes head                                   |
| **DoMagic1**              | None                     | Yes               | **No**        | None                                         | Turns to side and raises hands                                 |
| **DoMagic2**              | Yes, using Exit branches | No                | **Yes**       | None                                         | Lowers hands, clouds appear                                    |
| **DontRecognize**         | Yes, using Exit branches | Yes               | **No**        | None                                         | Holds hand to ear                                              |
| **Explain**               | Yes, using Exit branches | Yes               | **No**        | None                                         | Extends arms to side                                           |
| **GestureDown**           | Yes, using Exit branches | Yes               | **No**        | **GesturingDown**                            | Gestures down                                                  |
| **GestureLeft**           | Yes, using Exit branches | Yes               | **No**        | **GesturingLeft**                            | Gestures left                                                  |
| **GestureRight**          | Yes, using Exit branches | Yes               | **No**        | **GesturingRight**                           | Gestures right                                                 |
| **GestureUp**             | Yes, using Exit branches | Yes               | **No**        | **GesturingUp**                              | Gestures up                                                    |
| **GetAttention**          | **GetAttentionReturn**   | Yes               | **No**        | None                                         | Waves arms                                                     |
| **GetAttentionContinued** | **GetAttentionReturn**   | Yes               | **No**        | None                                         | Waves arms again                                               |
| **GetAttentionReturn**    | None                     | No                | **No**        | None                                         | Returns to neutral position                                    |
| **Greet**                 | Yes, using Exit branches | Yes               | **No**        | None                                         | Bows                                                           |
| **Hearing\_1**            | None                     | No                | **No**        | **Hearing**                                  | Ears extend (\*looping animation)                              |
| **Hearing\_2**            | None                     | No                | **No**        | **Hearing**                                  | Tilts head left (\*looping animation)                          |
| **Hearing\_3**            | None                     | No                | **No**        | **Hearing**                                  | Turns head left (\*looping animation)                          |
| **Hearing\_4**            | None                     | No                | **No**        | **Hearing**                                  | Turns head right (\*looping animation)                         |
| **Hide**                  | None                     | No                | **Yes**       | **Hiding**                                   | Disappears into smoke                                          |
| **Idle1\_1**              | None                     | No                | **No**        | **IdlingLevel1** IdlingLevel2                | Takes breath                                                   |
| **Idle1\_2**              | None                     | No                | **No**        | **IdlingLevel1** **IdlingLevel2**<br/> | Glances right and blinks                                       |
| **Idle1\_3**              | Yes, using Exit branches | No                | **No**        | **IdlingLevel1** **IdlingLevel2**<br/> | Glances left and blinks                                        |
| **Idle1\_4**              | None                     | No                | **No**        | **IdlingLevel1** **IdlingLevel2**<br/> | Glances up to the right and blinks                             |
| **Idle1\_5**              | Yes, using Exit branches | No                | **No**        | **IdlingLevel1** **IdlingLevel2**<br/> | Glances down and blinks                                        |
| **Idle1\_6**              | None                     | No                | **No**        | **IdlingLevel1** **IdlingLevel2**<br/> | Glances up and blinks                                          |
| **Idle2\_1**              | None                     | No                | **No**        | **IdlingLevel2**                             | Wisp snakes                                                    |
| **Idle2\_2**              | Yes, using Exit branches | No                | **No**        | **IdlingLevel2**                             | Reveals scroll and reads                                       |
| **Idle2\_3**              | Yes, using Exit branches | No                | **No**        | **IdlingLevel2**                             | Reveals scroll and writes                                      |
| **Idle3\_1**              | None                     | No                | **Yes**       | **IdlingLevel3**                             | Yawns                                                          |
| **Idle3\_2**              | Yes, using Exit branches | No                | **Yes**       | **IdlingLevel3**                             | Falls asleep (\*looping animation)                             |
| **LookDown**              | **LookDownReturn**       | No                | **No**        | None                                         | Looks down                                                     |
| **LookDownBlink**         | **LookDownReturn**       | No                | **No**        | None                                         | Blinks looking down                                            |
| **LookDownReturn**        | None                     | No                | **No**        | None                                         | Returns to neutral position                                    |
| **LookLeft**              | **LookLeftReturn**       | No                | **No**        | None                                         | Looks left                                                     |
| **LookLeftBlink**         | **LookLeftReturn**       | No                | **No**        | None                                         | Blinks looking left                                            |
| **LookLeftReturn**        | None                     | No                | **No**        | None                                         | Returns to neutral position                                    |
| **LookRight**             | **LookRightReturn**      | No                | **No**        | None                                         | Looks right                                                    |
| **LookRightBlink**        | **LookRightReturn**      | No                | **No**        | None                                         | Blinks looking right                                           |
| **LookRightReturn**       | None                     | No                | **No**        | None                                         | Returns to neutral position                                    |
| **LookUp**                | **LookUpReturn**         | No                | **No**        | None                                         | Looks up                                                       |
| **LookUpBlink**           | **LookUpReturn**         | No                | **No**        | None                                         | Blinks looking up                                              |
| **LookUpReturn**          | None                     | No                | **No**        | None                                         | Returns to neutral position                                    |
| **MoveDown**              | Yes, using Exit branches | No                | **Yes**       | **MovingDown**                               | Flies down                                                     |
| **MoveLeft**              | Yes, using Exit branches | No                | **Yes**       | **MovingLeft**                               | Flies left                                                     |
| **MoveRight**             | Yes, using Exit branches | No                | **Yes**       | **MovingRight**                              | Flies right                                                    |
| **MoveUp**                | Yes, using Exit branches | No                | **Yes**       | **MovingUp**                                 | Flies up                                                       |
| **Pleased**               | Yes, using Exit branches | Yes               | **No**        | None                                         | Smiles and holds hands together                                |
| **Process**               | No                       | No                | **No**        | None                                         | Spins into a cloud                                             |
| **Processing**            | Yes, using Exit branches | No                | **No**        | None                                         | Spins into a cloud (\*looping animation)                       |
| **Read**                  | **ReadReturn**           | Yes               | **Yes**       | None                                         | Reveals scroll, reads and looks up                             |
| **ReadContinued**         | **ReadReturn**           | Yes               | **No**        | None                                         | Reads and looks up                                             |
| **ReadReturn**            | None                     | No                | **No**        | None                                         | Returns to neutral position                                    |
| **Reading**               | Yes, using Exit branches | No                | **Yes**       | None                                         | Reveal scroll and reads (\*looping animation)                  |
| **RestPose**              | None                     | Yes               | **No**        | **Speaking**                                 | Neutral position                                               |
| **Sad**                   | Yes, using Exit branches | Yes               | **No**        | None                                         | Sad expression                                                 |
| **Search**                | No                       | No                | **No**        | None                                         | Reveals binoculars and turns                                   |
| **Searching**             | Yes, using Exit branches | No                | **No**        | None                                         | Reveals binoculars and turns (\*looping animation)             |
| **Show**                  | None                     | No                | **Yes**       | **Showing**                                  | Appears out of smoke                                           |
| **StartListening**        | Yes, using Exit branches | Yes               | **No**        | None                                         | Puts hand to ear                                               |
| **StopListening**         | Yes, using Exit branches | Yes               | **No**        | None                                         | Puts hands over ears                                           |
| **Suggest**               | Yes, using Exit branches | Yes               | **No**        | None                                         | Displays lightbulb                                             |
| **Surprised**             | Yes, using Exit branches | Yes               | **No**        | None                                         | Looks surprised                                                |
| **Think**                 | Yes, using Exit branches | Yes               | **No**        | None                                         | Looks up with hand on chin                                     |
| **Thinking**              | No                       | No                | **No**        | None                                         | Looks up with hand on chin (\*looping animation)               |
| **Uncertain**             | Yes, using Exit branches | Yes               | **No**        | None                                         | Moves one hand to chin, other to hip, and raises right eyebrow |
| **Wave**                  | Yes, using Exit branches | Yes               | **No**        | None                                         | Waves                                                          |
| **Write**                 | **WriteReturn**          | Yes               | **Yes**       | None                                         | Reveals scroll, writes and looks up                            |
| **WriteContinued**        | **WriteReturn**          | Yes               | **Yes**       | None                                         | Writes and looks up                                            |
| **WriteReturn**           | None                     | No                | **No**        | None                                         | Returns to neutral position                                    |
| **Writing**               | Yes, using Exit branches | No                | **Yes**       | None                                         | Reveals scroll, writes (\*looping animation)                   |



 

\* If you play a looping animation, you must use [**Stop**](stop-method.md) to clear it before other animations in the character's queue will play.

 

