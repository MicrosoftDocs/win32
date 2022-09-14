---
title: Agent States
description: Agent States
ms.assetid: 8c3c5b12-81af-4ba5-b834-9f0a7ff5d075
ms.topic: article
ms.date: 05/31/2018
---

# Agent States

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

The Microsoft Agent animation services automatically play certain animations for you. For example, when you use [**MoveTo**](moveto-method.md) or [**GestureAt**](gestureat-method.md) commands, the animation services play an appropriate animation. Similarly, after the idle time out, the services automatically play animations. To support these states, you can define appropriate animations and then assign them to the states. You can still play any animation you define directly using the [**Play**](play-method.md) method, even if you assign it to a state.

You can assign multiple animations to the same state, and the animation services will randomly choose one of your animations. This enables your character to exhibit a far more natural variety in its behavior.

Although animations that you assign to states can include branching frames, avoid looping animations (animations that branch forever). Otherwise, you will have to use the [**Stop**](play-method.md) method before you can play another animation.

It's important to define and assign at least one animation for each state that occurs for the character. If you do not supply these animations and state assignments, your character may not appear to behave appropriately to the user. However, if a state does not occur for a particular character, you need not assign an animation to that state. For example, if your host application never calls the [**MoveTo**](moveto-method.md) method, you can skip creating and assigning **Moving** state animations.



| State              | Example of Use                                                                         |
|--------------------|----------------------------------------------------------------------------------------|
| **GesturingDown**  | When the [**GestureAt**](gestureat-method.md) animation method is processed.          |
| **GesturingLeft**  | When the [**GestureAt**](gestureat-method.md) animation method is processed.          |
| **GesturingRight** | When the [**GestureAt**](gestureat-method.md) animation method is processed.          |
| **GesturingUp**    | When the [**GestureAt**](gestureat-method.md) animation method is processed.          |
| **Hearing**        | When the beginning of spoken input is detected.                                        |
| **Hiding**         | When the user or the application hides the character.                                  |
| **IdlingLevel1**   | When the character begins the **Idling** state.                                        |
| **IdlingLevel2**   | When the character begins the second **Idling** level state.                           |
| **IdlingLevel3**   | When the character begins the final **Idling** level state.                            |
| **Listening**      | When the character starts listening (the user first presses the speech input hot key). |
| **MovingDown**     | When the [**MoveTo**](moveto-method.md) animation method is processed.                |
| **MovingLeft**     | When the [**MoveTo**](moveto-method.md) animation method is processed.                |
| **MovingRight**    | When the [**MoveTo**](moveto-method.md) animation method is processed.                |
| **MovingUp**       | When the [**MoveTo**](moveto-method.md) animation method is processed.                |
| **Showing**        | When the user or the application shows the character.                                  |
| **Speaking**       | When the [**Speak**](speak-method.md) animation method is processed.                  |



 

### The Hearing and Listening States

The animation you assign to the **Listening** state plays when the user presses the push-to-talk hot key for speech input. Create and assign a short animation that makes the character look attentive. Similarly, define its **Return** animation to have a short duration so that the character plays its **Hearing** state animation when the user speaks. A **Hearing** state animation should also be brief, and designed to let the user know that the character is actively listening to what the user says. Head tilts or other slight gestures are appropriate. To provide natural variability, provide several **Hearing** state animations.

### The Gesturing States

You need to create and assign **Gesturing** state animations only if you plan to use the [**GestureAt**](gestureat-method.md) method. **Gesturing** state animations play when Microsoft Agent processes a call to the **GestureAt** method. If you define mouth overlays for your **Gesturing** state animations, the character can speak as it gestures.

The animation services determine the character's location and its relation to the location of the coordinates specified in the method, and play an appropriate animation. Gesturing direction is always with respect to the character; for example, **GestureRight** should be a gesture to the character's right.

### The Showing and Hiding States

The **Showing** and **Hiding** states play the assigned animations when the user or the host application requests to show or hide the character. These states also appropriately set the character frame's **Visible** state. When defining animations for these states, keep in mind that a character can appear or depart at any screen location. Because the user can show or hide any character, always support at least one animation for these states.

Animations that you assign to the **Showing** state typically end with a frame containing the character's neutral position image. Conversely, **Hiding** state animations typically begin with the neutral position. **Showing** and **Hiding** state animations can include an empty frame at the beginning or end, respectively, to provide a transition from the character's current state.

### The Idling States

The **Idling** states are progressive. The animation services begin using the Level 1 assignments for the first idle period, and use the Level 2 animations for the second. After this, the idle cycle progresses to the Level 3 assigned animations and remains in this state until canceled, such as when a new animation request begins.

Design animations for the **Idling** states to communicate the state of the character, but not to distract the user. The animations should appropriately reflect the responsiveness of the character in subtle but clear ways. For example, glancing around or blinking are good animations to assign to the **IdlingLevel1** state. Reading animations work well for the **IdlingLevel2** state. Sleeping or listening to music with headphones are good examples of animations to assign to the **IdlingLevel3** state. Animations that include many or large movements are not well suited for idle animations because they draw the user's attention. Because **Idling** state animations are played frequently, provide several **Idling** state animations, especially for the **IdlingLevel1** and **IdlingLevel2** states.

Note that an application can turn off the automatic idle processing for a character and manage the character's **Idling** state itself. The Agent **Idling** states are designed to help you avoid any situation where the character has no animation to play. A character image that does not change after a brief period of time is like an application displaying a wait pointer for a long time, which detracts from the sense of believability and interactivity. Maintaining the illusion does not take much: sometimes just an animated blink, visible breath, or body shift.

### The Speaking State

The animation services use the **Speaking** state when a speaking animation cannot be found for the current animation. Assign a simple speaking animation to this state. For example, you can use a single frame consisting of the character's neutral position with mouth overlays.

### The Moving States

The **Moving** states play when an application calls the [**MoveTo**](moveto-method.md) method. The animation services determine which animation to play based on the character's current location and the specified coordinates. Movement direction is based on the character's position. Therefore, the animation you assign to the **MovingLeft** animation should be based on the character's left. If you don't use the **MoveTo** method, you can skip creating and assigning an animation.

**Moving** state animations should animate the character into its moving position. The last frame of this animation is displayed as the character's frame is moved on the screen. There is no support for animating the character while its frame moves.

### Standard Animation Set

While you can design a custom character to have the animations you want to use, Microsoft Agent defines a standard animation set. Characters that conform to this definition can be selected as a default character.

The following table lists the animations included in the standard animation set. Even if you are creating a custom character, you may want to use the list as a guide for designing your own characters. Characters that support the standard animation set must support at least the following animations.



| Animation                        | Example of Use                                                                                           | Example Animation                                                                                                                                                                                                      |
|----------------------------------|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Acknowledge**                  | When the character acknowledges the user's request.                                                      | Character nods or flashes "OK" hand gesture. Note that this animation should return the character to its neutral position.<br/>                                                                                  |
| **Alert**<sup>1,2</sup>          | When the character is waiting for instructions, typically played after the user turns on listening mode. | Character faces front, breathing, blinking occasionally, but clearly awaiting instruction.                                                                                                                             |
| **Announce**<sup>1,2</sup>       | When the character has found information for the user.                                                   | Character gestures by raising eyebrows and hand or opens an envelope.                                                                                                                                                  |
| **Blink**                        | When the character finishes speaking or idle.                                                            | Character naturally blinks eyes.                                                                                                                                                                                       |
| **Confused**<sup>1,2</sup>       | When the character doesn't understand what to do.                                                        | Character scratches head.                                                                                                                                                                                              |
| **Congratulate**<sup>1,2</sup>   | When the character or user completes a task (a stronger form of the **Acknowledge** animation.)          | Character performs congratulatory gesture, conveys "Yes!"                                                                                                                                                              |
| **Decline**<sup>1,2</sup>        | When the character cannot do or declines the user's request.                                             | Character shakes head, conveys "no can do."                                                                                                                                                                            |
| **DoMagic1**                     | Character prepares to display something.                                                                 | Character waves hands or wand.                                                                                                                                                                                         |
| **DoMagic2**                     | Character completes display of something.                                                                | Character completes magic gesture.                                                                                                                                                                                     |
| **DontRecognize**<sup>1,2</sup>  | When the character didn't recognize the user's request.                                                  | Character holds hand to ear.                                                                                                                                                                                           |
| **Explain**<sup>1,2</sup>        | When the character explains something to the user.                                                       | Character gestures as if explaining something.                                                                                                                                                                         |
| **GestureDown**<sup>1,2</sup>    | When the character needs to point to something below it.                                                 | Character points down.                                                                                                                                                                                                 |
| **GestureLeft**<sup>1,2</sup>    | When the character needs to point to something at its left.                                              | Character points with left hand or morphs into an arrow pointing left.                                                                                                                                                 |
| **GestureRight**<sup>1,2</sup>   | When the character needs to point to something at its right.                                             | Character points with right hand or morphs into an arrow pointing right.                                                                                                                                               |
| **GestureUp**<sup>1,2</sup>      | When the character needs to point to something above it.                                                 | Character points up.                                                                                                                                                                                                   |
| **GetAttention**                 | When the character needs to notify the user about something important.                                   | Character waves hands or jumps up and down.                                                                                                                                                                            |
| **GetAttentionContinued**        | To emphasize the importance of the notification.                                                         | A continuation or repeat of the initial gesture.                                                                                                                                                                       |
| **GetAttentionReturn**           | When the character completes the **GetAttention** or **GetAttentionContinued** animation.                | Character returns to its neutral position.                                                                                                                                                                             |
| **Greet**<sup>1,2</sup>          | When the user starts up the system.                                                                      | Character smiles and waves.                                                                                                                                                                                            |
| **Hearing1**                     | When the character hears the start of a spoken utterance (actively listening).                           | Character leans forward and nods, or turns head showing response to speech input. Note: This animation loops to some intermediate frame that occurs after the character moves to an appropriate position.<br/>   |
| **Hearing2**                     | When the character hears the start of a spoken utterance (actively listening).                           | Another variation of the type of animation used in **Hearing1**Note: This animation loops to some intermediate frame that occurs after the character moves to an appropriate position.<br/>                      |
| **Hide**                         | When the user dismisses the character.                                                                   | Character removes self from screen.                                                                                                                                                                                    |
| **Idle1\_1**                     | When the character has no task and the user is not interacting with the character.                       | Character blinks or looks around, remaining in or returning to the neutral position.                                                                                                                                   |
| **Idle1\_2**                     | When the character has no task and the user is not interacting with the character.                       | Another variation of the type of animation used in **Idle1\_1**.                                                                                                                                                       |
| **Idle2\_1**                     | When the character has been idle for some time.                                                          | Character yawns or reads magazine remaining in or returning to the neutral position.                                                                                                                                   |
| **Idle2\_2**                     | When the character has been idle for some time.                                                          | Another variation of the type of animation used in **Idle2\_1**.                                                                                                                                                       |
| **Idle3\_1**                     | When the character has been idle for a long time.                                                        | Character yawns.                                                                                                                                                                                                       |
| **Idle3\_2**                     | When the character has been idle for a long time.                                                        | Character sleeps or puts on headphones to listen to music. Note: This animation loops to some intermediate frame that occurs after the character moves to an appropriate position.<br/>                          |
| **LookDown**                     | When the character needs to look down.                                                                   | Character looks down.                                                                                                                                                                                                  |
| **LookLeft**                     | When the character needs to look left.                                                                   | Character looks to the left.                                                                                                                                                                                           |
| **LookRight**                    | When the character needs to look right.                                                                  | Character looks to the right.                                                                                                                                                                                          |
| **LookUp**                       | When the character needs to look up.                                                                     | Character looks up.                                                                                                                                                                                                    |
| **MoveDown**                     | When the character prepares to move down.                                                                | Character transitions to a walking/flying down position.                                                                                                                                                               |
| **MoveLeft**                     | When the character prepares to move left.                                                                | Character transitions to a walking/flying left position.                                                                                                                                                               |
| **MoveRight**                    | When the character prepares to move right.                                                               | Character transitions to a walking/flying right position.                                                                                                                                                              |
| **MoveUp**                       | When the character prepares to move up.                                                                  | Character transitions to a walking/flying up position.                                                                                                                                                                 |
| **Pleased**<sup>1,2</sup>        | When the character is pleased with the user's request or choice.                                         | Character smiles.                                                                                                                                                                                                      |
| **Process**                      | When the character performs some type of generic task.                                                   | Character presses buttons or uses some type of tool.                                                                                                                                                                   |
| **Processing**                   | When the character is busy working on a generic task.                                                    | Character scribbles on pad of paper or uses some type of tool. Note: This animation loops to some intermediate frame that occurs after the character moves to an appropriate position.<br/>                      |
| **Read**                         | When the character reads something to the user.                                                          | Character displays book or paper, reads, and looks back at user.                                                                                                                                                       |
| **ReadContinued**                | When the character reads further to the user.                                                            | Character reads again, then looks back at user.                                                                                                                                                                        |
| **ReadReturn**                   | When the character completes the **Read** or **ReadContinued** animation.                                | Character returns to its neutral position.                                                                                                                                                                             |
| **Reading**                      | When the character reads something but cannot accept input.                                              | Character reads from a piece of paper. Note: This animation loops to some intermediate frame(s) that occurs after the character moves to an appropriate position.<br/>                                           |
| **RestPose**                     | When the character speaks from its neutral position.                                                     | Character stands with relaxed but attentive posture.                                                                                                                                                                   |
| **Sad**<sup>1,2</sup>            | When the character is disappointed with the user's choice.                                               | Character frowns or looks disappointed.                                                                                                                                                                                |
| **Search**                       | When character searches for something.                                                                   | Character shuffles through file drawer or other container looking for something.                                                                                                                                       |
| **Searching**                    | When character is searching for user-specified information.                                              | Character shuffles through file drawer or other container looking for something. Note: This animation loops to some intermediate frame(s) that occurs after the character moves to an appropriate position.<br/> |
| **Show**                         | When the character starts up or returns after being summoned.                                            | Character pops up in a puff of smoke, beams in, or walks on-screen.                                                                                                                                                    |
| **StartListening**<sup>1,2</sup> | When the character is listening.                                                                         | Character puts hand to ear.                                                                                                                                                                                            |
| **StopListening**<sup>1,2</sup>  | When the character stops listening.                                                                      | Character puts hands over ears.                                                                                                                                                                                        |
| **Suggest**<sup>1,2</sup>        | When the character has a tip or suggestion for the user.                                                 | Light bulb appears next to character.                                                                                                                                                                                  |
| **Surprised**<sup>1,2</sup>      | When the character is surprised by the user's action or choice.                                          | Character widens eyes, opens mouth.                                                                                                                                                                                    |
| **Think**<sup>1,2</sup>          | When the character is thinking about something.                                                          | Character looks up and holds hand on head.                                                                                                                                                                             |
| **Uncertain**<sup>1,2</sup>      | When the character needs the user to confirm a request.                                                  | Character looks quizzical, conveys ("Are you sure?")                                                                                                                                                                   |
| **Wave**<sup>1,2</sup>           | When the user chooses to shut down the server or system.                                                 | Character waves good-bye or hello.                                                                                                                                                                                     |
| **Write**                        | When the character is listening for instructions from the user.                                          | Character displays paper, writes, and looks back at user.                                                                                                                                                              |
| **WriteContinued**               | When the character continues listening for instructions from the user.                                   | Character writes on a piece of paper and looks back at user.                                                                                                                                                           |
| **WriteReturn**                  | When the character completes the **Write** or **WriteContinued** animation.                              | Character returns to its neutral position.                                                                                                                                                                             |
| **Writing**                      | When the character writes out information for the user.                                                  | Character writes on piece of paper. Note: This animation loops.<br/>                                                                                                                                             |



 

  Animation requires mouth overlays and a defined speaking frame.

  Animation requires an assigned Return animation either based on its exit branching or an explicit Return animation.

In addition, a character must have the following state assignments.



| State          | Required Animations                           |
|----------------|-----------------------------------------------|
| GesturingDown  | GestureDown                                   |
| GesturingLeft  | GestureLeft                                   |
| GesturingRight | GestureRight                                  |
| GesturingUp    | GestureUp                                     |
| Hearing        | Hearing1, Hearing2                            |
| Hiding         | Hide                                          |
| IdlingLevel1   | Blink, Idle1\_1, Idle1\_2                     |
| IdlingLevel2   | Blink, Idle1\_1, Idle1\_2, Idle2\_1, Idle2\_2 |
| IdlingLevel3   | Idle3\_1, Idle3\_2                            |
| Listening      | Alert                                         |
| MovingDown     | MoveDown                                      |
| MovingLeft     | MoveLeft                                      |
| MovingRight    | MoveRight                                     |
| MovingUp       | MoveUp                                        |
| Showing        | Show                                          |
| Speaking       | RestPose                                      |



 

 

 





