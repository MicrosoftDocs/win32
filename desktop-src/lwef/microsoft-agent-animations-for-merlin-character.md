---
title: Microsoft Agent Animations for Merlin Character
description: Microsoft Agent Animations for Merlin Character
ms.assetid: 4563a464-2c1a-4928-a471-e3f0fdfe85c0
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft Agent Animations for Merlin Character

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

The [Microsoft Agent Merlin Character](https://www.microsoft.com/downloads/details.aspx?FamilyID=fee1dadd-2f23-41d0-8a81-2affd74c0aa5) is a copyrighted work of Microsoft Corporation.

Merlin supports the animations listed in the table below. Refer to [Programming the Microsoft Agent Server Interface](/windows/desktop/lwef/programming-the-microsoft-agent-server-interface) and [Programming the Microsoft Agent Control](programming-the-microsoft-agent-control.md) for information on how to call the character's animations.

If accessing these character animations using the HTTP protocol and the control's [**Get**](get-method.md) or server's [**Prepare**](/windows/desktop/lwef/iagentcharacter--prepare) method, consider how you will download them. Instead of downloading all the animations at once, you may want to retrieve the **Showing** and **Speaking** state animations first. This will enable you to display the character quickly and have it speak while bringing down other animations asynchronously. In addition, to ensure that character and animation data load successfully, use the [**RequestComplete**](requestcomplete-event.md) event. If a load request fails, you can retry loading the data or display an appropriate message.

If an animation's **Return** animation is defined using Exit branches, you do not need to call it explicitly; Agent automatically plays the **Return** animation before the next animation. However, if a **Return** animation is listed, you must call the animation using the [**Play**](play-method.md) method before another animation to provide a smooth transition. If no **Return** animation is listed, the animation typically ends without needing a transitional animation.

The character file includes sound effects for some animations as noted in the following table. Sound effects play only if this option is enabled in the Microsoft Agent property sheet. You can also disable sound effects in your application.



| Animation                 | Return Animation         | Supports Speaking | Sound Effects | Assigned to State                            | Description                                      |
|---------------------------|--------------------------|-------------------|---------------|----------------------------------------------|--------------------------------------------------|
| **Acknowledge**           | None                     | No                | **No**        | None                                         | Nods head                                        |
| **Alert**                 | Yes, using Exit branches | Yes               | **No**        | **Listening**                                | Straightens and raises eyebrows                  |
| **Announce**              | Yes, using Exit branches | Yes               | **Yes**       | None                                         | Raises trumpet and plays                         |
| **Blink**                 | None                     | No                | **No**        | **IdlingLevel1** **IdlingLevel2**<br/> | Blinks eyes                                      |
| **Confused**              | Yes, using Exit branches | Yes               | **Yes**       | None                                         | Scratches head                                   |
| **Congratulate**          | Yes, using Exit branches | Yes               | **Yes**       | None                                         | Displays trophy                                  |
| **Congratulate\_2**       | Yes, using Exit branches | Yes               | **Yes**       | None                                         | Applauds                                         |
| **Decline**               | Yes, using Exit branches | Yes               | **No**        | None                                         | Raises hands and shakes head                     |
| **DoMagic1**              | None                     | Yes               | **No**        | None                                         | Raises magic wand                                |
| **DoMagic2**              | Yes, using Exit branches | No                | **Yes**       | None                                         | Lowers wand, clouds appear                       |
| **DontRecognize**         | Yes, using Exit branches | Yes               | **No**        | None                                         | Holds hand to ear                                |
| **Explain**               | Yes, using Exit branches | Yes               | **No**        | None                                         | Extends arms to side                             |
| **GestureDown**           | Yes, using Exit branches | Yes               | **No**        | **GesturingDown**                            | Gestures down                                    |
| **GestureLeft**           | Yes, using Exit branches | Yes               | **No**        | **GesturingLeft**                            | Gestures left                                    |
| **GestureRight**          | Yes, using Exit branches | Yes               | **No**        | **GesturingRight**                           | Gestures right                                   |
| **GestureUp**             | Yes, using Exit branches | Yes               | **No**        | **GesturingUp**                              | Gestures up                                      |
| **GetAttention**          | **GetAttentionReturn**   | Yes               | **Yes**       | None                                         | Leans forward and knocks                         |
| **GetAttentionContinued** | **GetAttentionReturn**   | Yes               | **Yes**       | None                                         | Leaning forward, knocks again                    |
| **GetAttentionReturn**    | None                     | No                | **No**        | None                                         | Returns to neutral position                      |
| **Greet**                 | Yes, using Exit branches | Yes               | **Yes**       | None                                         | Bows                                             |
| **Hearing\_1**            | None                     | No                | **No**        | **Hearing**                                  | Ears extend (\*looping animation)                |
| **Hearing\_2**            | None                     | No                | **No**        | **Hearing**                                  | Tilts head left (\*looping animation)            |
| **Hearing\_3**            | None                     | No                | **No**        | **Hearing**                                  | Turns head left (\*looping animation)            |
| **Hearing\_4**            | None                     | No                | **No**        | **Hearing**                                  | Turns head right (\*looping animation)           |
| **Hide**                  | None                     | No                | **Yes**       | **Hiding**                                   | Disappears under cap                             |
| **Idle1\_1**              | Yes, using Exit branches | No                | **No**        | **IdlingLevel1** **IdlingLevel2**<br/> | Takes breath                                     |
| **Idle1\_2**              | Yes, using Exit branches | No                | **No**        | **IdlingLevel1** **IdlingLevel2**<br/> | Glances left and blinks                          |
| **Idle1\_3**              | Yes, using Exit branches | No                | **No**        | **IdlingLevel1** **IdlingLevel2**<br/> | Glances right                                    |
| **Idle1\_4**              | Yes, using Exit branches | No                | **No**        | **IdlingLevel1** **IdlingLevel2**<br/> | Glances up to the right and blinks               |
| **Idle2\_1**              | None                     | No                | **No**        | **IdlingLevel2**                             | Looks at wand and blinks                         |
| **Idle2\_2**              | None                     | No                | **No**        | **IdlingLevel2**                             | Holds hands and blinks                           |
| **Idle3\_1**              | None                     | No                | **Yes**       | **IdlingLevel3**                             | Yawns                                            |
| **Idle3\_2**              | Yes, using Exit branches | No                | **Yes**       | **IdlingLevel3**                             | Falls asleep (\*looping animation)               |
| **LookDown**              | **LookDownReturn**       | No                | **No**        | None                                         | Looks down                                       |
| **LookDownBlink**         | **LookDownReturn**       | No                | **No**        | None                                         | Blinks looking down                              |
| **LookDownReturn**        | None                     | No                | **No**        | None                                         | Returns to neutral position                      |
| **LookLeft**              | **LookLeftReturn**       | No                | **No**        | None                                         | Looks left                                       |
| **LookLeftBlink**         | **LookLeftReturn**       | No                | **No**        | None                                         | Blinks looking left                              |
| **LookLeftReturn**        | None                     | No                | **No**        | None                                         | Returns to neutral position                      |
| **LookRight**             | **LookRightReturn**      | No                | **No**        | None                                         | Looks right                                      |
| **LookRightBlink**        | **LookRightReturn**      | No                | **No**        | None                                         | Blinks looking right                             |
| **LookRightReturn**       | None                     | No                | **No**        | None                                         | Returns to neutral position                      |
| **LookUp**                | **LookUpReturn**         | No                | **No**        | None                                         | Looks up                                         |
| **LookUpBlink**           | **LookUpReturn**         | No                | **No**        | None                                         | Blinks looking up                                |
| **LookUpReturn**          | None                     | No                | **No**        | None                                         | Returns to neutral position                      |
| **MoveDown**              | Yes, using Exit branches | No                | **Yes**       | **MovingDown**                               | Flies down                                       |
| **MoveLeft**              | Yes, using Exit branches | No                | **Yes**       | **MovingLeft**                               | Flies left                                       |
| **MoveRight**             | Yes, using Exit branches | No                | **Yes**       | **MovingRight**                              | Flies right                                      |
| **MoveUp**                | Yes, using Exit branches | No                | **Yes**       | **MovingUp**                                 | Flies up                                         |
| **Pleased**               | Yes, using Exit branches | Yes               | **No**        | None                                         | Smiles and holds hands together                  |
| **Process**               | No                       | No                | **Yes**       | None                                         | Stirs caldron                                    |
| **Processing**            | Yes, using Exit branches | No                | **Yes**       | None                                         | Stirs caldron (\*looping animation)              |
| **Read**                  | **ReadReturn**           | Yes               | **Yes**       | None                                         | Opens book, reads and looks up                   |
| **ReadContinued**         | **ReadReturn**           | Yes               | **Yes**       | None                                         | Reads and looks up                               |
| **ReadReturn**            | None                     | No                | **Yes**       | None                                         | Returns to neutral position                      |
| **Reading**               | Yes, using Exit branches | No                | **Yes**       | None                                         | Reads (\*looping animation)                      |
| **RestPose**              | None                     | Yes               | **No**        | **Speaking**                                 | Neutral position                                 |
| **Sad**                   | Yes, using Exit branches | Yes               | **No**        | None                                         | Sad expression                                   |
| **Search**                | No                       | No                | **Yes**       | None                                         | Looks into crystal ball                          |
| **Searching**             | Yes, using Exit branches | No                | **Yes**       | None                                         | Looks into crystal ball (\*looping animation)    |
| **Show**                  | None                     | No                | **Yes**       | **Showing**                                  | Appears out of cap                               |
| **StartListening**        | Yes, using Exit branches | Yes               | **No**        | None                                         | Puts hand to ear                                 |
| **StopListening**         | Yes, using Exit branches | Yes               | **No**        | None                                         | Puts hands over ears                             |
| **Suggest**               | Yes, using Exit branches | Yes               | **Yes**       | None                                         | Displays lightbulb                               |
| **Surprised**             | Yes, using Exit branches | Yes               | **Yes**       | None                                         | Looks surprised                                  |
| **Think**                 | Yes, using Exit branches | Yes               | **No**        | None                                         | Looks up with hand on chin                       |
| **Thinking**              | No                       | No                | **No**        | None                                         | Looks up with hand on chin (\*looping animation) |
| **Uncertain**             | Yes, using Exit branches | Yes               | **No**        | None                                         | Leans forward and raises eyebrow                 |
| **Wave**                  | Yes, using Exit branches | Yes               | **No**        | None                                         | Waves                                            |
| **Write**                 | **WriteReturn**          | Yes               | **Yes**       | None                                         | Opens book, writes and looks up                  |
| **WriteContinued**        | **WriteReturn**          | Yes               | **Yes**       | None                                         | Writes and looks up                              |
| **WriteReturn**           | None                     | No                | **Yes**       | None                                         | Returns to neutral position                      |
| **Writing**               | Yes, using Exit branches | No                | **Yes**       | None                                         | Writes (\*looping animation)                     |



 

\* If you play a looping animation, you must use [**Stop**](stop-method.md) to clear it before other animations in the character's queue will play.

 

