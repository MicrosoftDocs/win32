---
title: Microsoft Agent Animations for Peedy Character
description: Microsoft Agent Animations for Peedy Character
ms.assetid: 335d915c-9cae-4850-a6bf-66ad78d533ff
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft Agent Animations for Peedy Character

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

The [Microsoft Agent Peedy Character](https://www.microsoft.com/downloads/details.aspx?FamilyID=bd3c4655-79e4-4791-ab9d-abc7bbd133ef) is a copyrighted work of Microsoft Corporation.

Peedy supports the animations listed in the table below. Refer to [Programming the Microsoft Agent Server Interface](/windows/desktop/lwef/programming-the-microsoft-agent-server-interface) and [Programming the Microsoft Agent Control](programming-the-microsoft-agent-control.md) for information on how to call the character's animations.

If accessing these character animations using the HTTP protocol and the control's [**Get**](get-method.md) or server's [**Prepare**](/windows/desktop/lwef/iagentcharacter--prepare) method, consider how you will download them. Instead of downloading all the animations at once, you may want to retrieve the **Showing** and **Speaking** state animations first. This will enable you to display the character quickly and have it speak while bringing down other animations asynchronously. In addition, to ensure that character and animation data load successfully, use the [**RequestComplete**](requestcomplete-event.md) event. If a load request fails, you can retry loading the data or display an appropriate message.

If an animation's **Return** animation is defined using Exit branches, you do not need to call it explicitly; Agent automatically plays the **Return** animation before the next animation. However, if a **Return** animation is listed, you must call the animation using the [**Play**](play-method.md) method before another animation to provide a smooth transition. If no **Return** animation is listed, the animation typically ends without needing a transitional animation.

If accessing these character animations using the HTTP protocol and the control's [**Get**](get-method.md) or server's [**Prepare**](/windows/desktop/lwef/iagentcharacter--prepare) method, consider how you will download them. Instead of downloading all the animations at once, you may want to retrieve the **Showing** and **Speaking** state animations first. This will enable you to display the character quickly and have it speak while bringing down other animations asynchronously. In addition, to ensure that character and animation data load successfully, use the [**RequestComplete**](requestcomplete-event.md) event. If a load request fails, you can retry loading the data or display an appropriate message.

The character file includes sound effects for some animations as noted in the following table. Sound effects play only if this option is enabled in the Microsoft Agent property sheet. You can also disable sound effects in your application.



| Animation                  | Return Animation         | Supports Speaking | Sound Effects | Assigned to State                            | Description                                            |
|----------------------------|--------------------------|-------------------|---------------|----------------------------------------------|--------------------------------------------------------|
| **Acknowledge**            | None                     | No                | **No**        | None                                         | Nods head                                              |
| **Alert**                  | Yes, using exit branches | Yes               | **No**        | **Listening**                                | Straightens and raises eyebrows                        |
| **Announce**               | Yes, using exit branches | Yes               | **Yes**       | None                                         | Paper airplane flies in and unfolds                    |
| **Blink**                  | None                     | No                | **No**        | **IdlingLevel1** **IdlingLevel2**<br/> | Blinks eyes                                            |
| **Confused**               | Yes, using exit branches | Yes               | **Yes**       | None                                         | Eyes spin around                                       |
| **Congratulate**           | Yes, using exit branches | Yes               | **Yes**       | None                                         | Displays blue ribbon                                   |
| **Decline**                | Yes, using exit branches | Yes               | **No**        | None                                         | Shakes head                                            |
| **DoMagic1**               | None                     | Yes               | **Yes**       | None                                         | Raises magic wand                                      |
| **DoMagic2**               | Yes, using exit branches | No                | **Yes**       | None                                         | Lowers wand, clouds appear                             |
| **DontRecognize**          | Yes, using exit branches | Yes               | **No**        | None                                         | Shakes head and holds wing to ear                      |
| **Explain**                | Yes, using exit branches | Yes               | **No**        | None                                         | Extends arms to side                                   |
| **GestureDown**            | Yes, using exit branches | Yes               | **No**        | **GesturingDown**                            | Gestures down                                          |
| **GestureLeft**            | Yes, using exit branches | Yes               | **No**        | **GesturingLeft**                            | Gestures left                                          |
| **GestureRight**           | Yes, using exit branches | Yes               | **No**        | **GesturingRight**                           | Gestures right                                         |
| **GestureUp**              | Yes, using exit branches | Yes               | **No**        | **GesturingUp**                              | Gestures up                                            |
| **GetAttention**           | **GetAttentionReturn**   | Yes               | **Yes**       | None                                         | Jumps up with wings outstretched                       |
| **GetAttentionContinued**  | **GetAttentionReturn**   | Yes               | **Yes**       | None                                         | Jumps up with wings outstretched again                 |
| **GetAttentionReturn**     | None                     | No                | **No**        | None                                         | Returns to neutral position                            |
| **Greet**                  | Yes, using exit branches | Yes               | **Yes**       | None                                         | Bows                                                   |
| **Hearing\_1**             | None                     | No                | **No**        | **Hearing**                                  | Tilts head right (\*looping animation)                 |
| **Hearing\_2**             | None                     | No                | **No**        | **Hearing**                                  | Tilts head left (\*looping animation)                  |
| **Hearing\_3**             | None                     | No                | **No**        | **Hearing**                                  | Turns head right then left (\*looping animation)       |
| **Hide**                   | None                     | No                | **Yes**       | **Hiding**                                   | Flies away                                             |
| **Idle1\_1**               | None                     | No                | **No**        | **IdlingLevel1** **IdlingLevel2**<br/> | Takes breath                                           |
| **Idle1\_2**               | None                     | No                | **No**        | **IdlingLevel1** **IdlingLevel2**<br/> | Glances right and blinks                               |
| **Idle1\_3**               | None                     | No                | **No**        | **IdlingLevel1** **IdlingLevel2**<br/> | Glances left and blinks                                |
| **Idle1\_4**               | None                     | No                | **No**        | **IdlingLevel1** **IdlingLevel2**<br/> | Glances up and blinks                                  |
| **Idle1\_5**               | None                     | No                | **No**        | **IdlingLevel1** **IdlingLevel2**<br/> | Glances down and blinks                                |
| **Idle2\_1**               | Yes, using exit branches | No                | **No**        | **IdlingLevel2**                             | Puts on sunglasses                                     |
| **Idle2\_2**               | None                     | No                | **Yes**       | **IdlingLevel2**                             | Eats a cracker                                         |
| **Idle3\_1**               | None                     | No                | **Yes**       | **IdlingLevel3**                             | Yawns                                                  |
| **Idle3\_2**               | Yes, using exit branches | No                | **Yes**       | **IdlingLevel3**                             | Falls asleep (\*looping animation)                     |
| **Idle3\_3**               | Yes, using exit branches | No                | **No**        | **IdlingLevel3**                             | Listens to music (\*looping animation)                 |
| **LookDownLookDownReturn** |                          | No                | **No**        | None                                         | Looks down                                             |
| **LookDownBlink**          | **LookDownReturn**       | No                | **Yes**       | None                                         | Blinks looking down                                    |
| **LookDownReturn**         | None                     | No                | **No**        | None                                         | Returns to neutral position                            |
| **LookDownLeft**           | **LookDownLeftReturn**   | No                | **No**        | None                                         | Looks down left                                        |
| **LookDownLeftBlink**      | **LookDownLeftReturn**   | No                | **Yes**       | None                                         | Blinks looking down left                               |
| **LookDownLeftReturn**     | None                     | No                | **No**        | None                                         | Returns to neutral position                            |
| **LookDownRight**          | **LookDownRightReturn**  | No                | **No**        | None                                         | Looks down right                                       |
| **LookDownRightBlink**     | **LookDownRightReturn**  | No                | **Yes**       | None                                         | Blinks looking down right                              |
| **LookDownRightReturn**    | None                     | No                | **No**        | None                                         | Returns to neutral position                            |
| **LookLeft**               | **LookLeftReturn**       | Yes               | **No**        | None                                         | Looks left                                             |
| **LookLeftBlink**          | **LookLeftReturn**       | Yes               | **Yes**       | None                                         | Blinks looking left                                    |
| **LookLeftReturn**         | None                     | No                | **No**        | None                                         | Returns to neutral position                            |
| **LookRight**              | **LookRightReturn**      | Yes               | **No**        | None                                         | Looks right                                            |
| **LookRightBlink**         | **LookRightReturn**      | Yes               | **Yes**       | None                                         | Blinks looking right                                   |
| **LookRightReturn**        | None                     | No                | **No**        | None                                         | Returns to neutral position                            |
| **LookUp**                 | **LookUpReturn**         | No                | **No**        | None                                         | Looks up                                               |
| **LookUpBlink**            | **LookUpReturn**         | No                | **Yes**       | None                                         | Blinks looking up                                      |
| **LookUpReturn**           | None                     | No                | **No**        | None                                         | Returns to neutral position                            |
| **LookUpLeft**             | **LookUpLeftReturn**     | No                | **No**        | None                                         | Looks up left                                          |
| **LookUpLeftBlink**        | **LookUpLeftReturn**     | No                | **Yes**       | None                                         | Blinks looking up left                                 |
| **LookUpLeftReturn**       | None                     | No                | **No**        | None                                         | Returns to neutral position                            |
| **LookUpRight**            | **LookUpRightReturn**    | No                | **No**        | None                                         | Looks up right                                         |
| **LookUpRightBlink**       | **LookUpRightReturn**    | No                | **Yes**       | None                                         | Blinks looking up right                                |
| **LookUpRightReturn**      | None                     | No                | **No**        | None                                         | Returns to neutral position                            |
| **MoveDown**               | Yes, using exit branches | No                | **Yes**       | **MovingDown**                               | Flies down                                             |
| **MoveLeft**               | Yes, using exit branches | No                | **Yes**       | **MovingLeft**                               | Flies left                                             |
| **MoveRight**              | Yes, using exit branches | No                | **Yes**       | **MovingRight**                              | Flies right                                            |
| **MoveUp**                 | Yes, using exit branches | No                | **Yes**       | **MovingUp**                                 | Flies up                                               |
| **Pleased**                | Yes, using exit branches | Yes               | **No**        | None                                         | Smiles                                                 |
| **Process**                | None                     | No                | **Yes**       | None                                         | Uses calculator                                        |
| **Processing**             | Yes, using exit branches | No                | **Yes**       | None                                         | Uses calculator (\*looping animation)                  |
| **Read**                   | **ReadReturn**           | Yes               | **Yes**       | None                                         | Opens magazine, reads and looks up                     |
| **ReadContinued**          | **ReadReturn**           | Yes               | **Yes**       | None                                         | Reads and looks up                                     |
| **ReadReturn**             | None                     | No                | **Yes**       | None                                         | Returns to neutral position                            |
| **Reading**                | Yes, using Exit branches | No                | **Yes**       | None                                         | Reads (\*looping animation)                            |
| **RestPose**               | None                     | Yes               | **No**        | **Speaking**                                 | Neutral position                                       |
| **Sad**                    | Yes, using exit branches | Yes               | **No**        | None                                         | Sad expression                                         |
| **Search**                 | None                     | No                | **Yes**       | None                                         | Reveals telescope and rotates                          |
| **Searching**              | Yes, using exit branches | No                | **Yes**       | None                                         | Reveals telescope and rotates (\*looping animation)    |
| **Show**                   | None                     | No                | **Yes**       | **Showing**                                  | Flies in                                               |
| **StartListening**         | Yes, using exit branches | Yes               | **No**        | None                                         | Puts hand to ear                                       |
| **StopListening**          | Yes, using exit branches | Yes               | **No**        | None                                         | Puts hands to ears                                     |
| **Suggest**                | Yes, using exit branches | Yes               | **Yes**       | None                                         | Displays light bulb                                    |
| **Surprised**              | Yes, using exit branches | Yes               | **Yes**       | None                                         | Looks surprised                                        |
| **Think**                  | Yes, using exit branches | Yes               | **No**        | None                                         | Looks up with wing on face                             |
| **Thinking**               | None                     | No                | **No**        | None                                         | Looks up with wing on face (\*looping animation)       |
| **Uncertain**              | Yes, using exit branches | Yes               | **No**        | None                                         | Leans to right and shrugs                              |
| **Wave**                   | Yes, using exit branches | Yes               | **No**        | None                                         | Waves                                                  |
| **Write**                  | **WriteReturn**          | Yes               | **Yes**       | None                                         | Takes out pencil and pad, writes and looks up          |
| **WriteContinued**         | **WriteReturn**          | Yes               | **Yes**       | None                                         | Writes and looks up                                    |
| **WriteReturn**            | None                     | No                | **No**        | None                                         | Returns to neutral position                            |
| **Writing**                | Yes, using Exit branches | No                | **Yes**       | None                                         | Takes out pencil and pad, writes (\*looping animation) |



 

\* If you play a looping animation, you must use [**Stop**](stop-method.md) to clear it before other animations in the character's queue will play.

 

