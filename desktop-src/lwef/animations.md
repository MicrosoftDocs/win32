---
title: Animations
description: Animations
ms.assetid: 8bd9ac94-3f86-4168-bf33-7a2c8d11907d
ms.topic: article
ms.date: 05/31/2018
---

# Animations

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

A character's animations reflect its gender, age, personality, and behavior. The number and types of animations you create for a character depend on what your character does and how it responds to different situations.

Like traditional animations, digital animations involve creating a series of slightly differing images that, when displayed sequentially, provide the illusion of action. Creating high-quality animation images may require a skilled animator, but the style and presentation of the character you create also affect quality. Two-dimensional characters with simple shapes and features can sometimes be as effective as (or more effective than) highly rendered characters. It is not necessary to create a realistic image to portray an effective character. Many popular cartoon characters are not realistic in their presentation, yet they are effective because the animator understands how to convey action and emotion. The Appendix provides general information about fundamental animation design principles.

### Frames

Each animation you create for a Microsoft Agent character is composed of a timed sequence of frames. Each frame in the animation is composed of one or more bitmap images. Images can be as small as you need them or as large as the frame itself.

Animation details such as eye blinking or finger movement can be included as additional images for the frame. You can overlay several images to create a composite, and vary their position in the layers. This technique enables you to reuse images in multiple frames and vary the details that change. For example, if you want to have a character wave its hand, for each frame you could use a base image with everything but the hand and overlay the base image with a different hand image. Similarly, if you want to make the character blink, you can overlay a different set of eyes over a base image for each frame. Images can also be offset from the base image. However, only the part of the image that exists within the frame's size will be displayed.

You can have as many frames in an animation as you wish; however, a typical animation averages about 14 frames so that it plays for no more than six seconds. This modest length of time ensures that your character appears responsive to user input. In addition, the greater the number of frames, the larger your animation file. For downloaded Web-based characters, keep the size of your animation file as small as possible while still providing a reasonably-sized set of frames, so that the character's animation does not appear jerky.

### Image Design

You can use any graphics or animation tool to create images for animation frames, provided that you store the final images in the Windows bitmap (.BMP) format. When the images are created, use the Microsoft Agent Character Editor (available in the [downloadable](https://www.microsoft.com/download/en/details.aspx?id=14765)) to assemble, sequence, and time the images, supply other character information, and compile all the information into a final character file.

Character images must be designed to a 256-color palette, preserving the 20 standard Windows system colors in their standard position in the palette (the first 10 and last 10 positions). That means your character's color palette can use the standard system colors and up to 236 other colors. When defining your palette, include any props your character uses in the animation. If your character's palette places colors in the system color positions, those character colors will be overwritten with the system colors when Microsoft Agent creates the palette.

The larger the number of colors you use in a character's color palette, the greater the possibility that part of your character's colors may get remapped for systems configured to an 8-bit (256) color setting. Consider also the palette usage of the application in which the character will be used. It's best to avoid having the character remap the colors of its host application and vice-versa. Similarly, if you plan to support multiple characters displayed at the same time, you'll probably want to maintain a consistent palette for those characters. You might consider using only the standard system colors in your character if you target users with an 8-bit color configuration. However, this still may not prevent remapping of your character's color if another application extensively redefines the color palette. On systems set to higher color resolutions, color palette remapping should not be a problem because the system manages the color palettes automatically.

Using a larger number of colors in an image can also increase the overall size of your animation file. The number of colors and frequency of variation may determine how well your character file compresses. For example, a two-dimensional character that uses only a few colors will compress better than a three-dimensional, shaded character.

You must use the same color palette for your entire character file. You cannot change the palette for different animations. If you attempt to support 8-bit color configurations, consider using the same palette for your application and any other characters you plan to support.

The 11<sup>th</sup> position in the palette is defined by default as the transparency (or alpha) color, although you can also set the color using the Microsoft Agent Character Editor. The Microsoft Agent animation services render transparent any pixels in this color, so use the color in your images only where you want transparency.

Carefully consider the shape of your character, because it can affect animation performance. To display the character, the animation services create a region window based on the overall image. Small irregular areas often require more region data and may reduce the animation performance of your character. Therefore, when possible, avoid gaps or single-pixel elements and details.

Avoid anti-aliasing the outside edge of your character. Although anti-aliasing is a good technique to reduce jagged edges, it is based on adjacent colors. Because your character may appear on top of a variety of colors, anti-aliasing the outside edge may make your character appear poorly against other backgrounds. However, you can use anti-aliasing on the inside details of your character without encountering this problem.

### Frame Size

Frame size should typically be no larger than 128 x 128 pixels. Although characters can be larger or smaller in either dimension, the Microsoft Agent Character Editor uses this as its display size, and scales character images if you define a larger frame size. The 128 x 128 frame size makes reasonable tradeoffs with the space the character will occupy on the screen. Your application can scale a character at run time.

### Frame Duration

You can use the Microsoft Agent Character Editor to set how long each frame of animation will display before moving to the next frame. Set the duration of each frame to at least 10 hundredths of a second (10 frames per second) -- anything less might not be perceptible on some systems. You can also set the duration longer, but avoid unnatural pauses in the action.

The Microsoft Agent Character Editor also supports branching from one frame in an animation to another, based on probability percentages that you supply. For any given frame, you can define up to three different branches. Branching enables you to create animations that vary when they are played and animations that loop. However, be careful when using branching as it may create problems when trying to play one animation after another. For example, if you play a looping or branching animation, it could continue indefinitely unless you use a [**Stop**](stop-method.md) method. If you are uncertain, avoid branching.

Frames that don't have images and are set to zero duration do not appear when included in an animation. You can use this feature to create frames that support branching without being visible. However, a frame that does not have images yet has a duration greater than zero will be displayed. Therefore, avoid including empty frames in your animation, because the user may not be able to distinguish an empty frame from when the character is hidden.

### Frame Transition

When designing an animation, consider how to smoothly transition from and to the animation. For example, if you create an animation in which the character gestures right, and another in which the character gestures left, you want the character to animate smoothly from one position to the other. Although you could build this into either animation, a better solution is to define a neutral or transitional position from which the character starts and returns. Animating to the neutral position can be incorporated as part of each animation or as a separate animation. In the Microsoft Agent Character Editor, you can specify a complementary **Return** animation for each animation for your character. The **Return** animation should typically be no more than 2-4 frames so the character can quickly transition to the neutral position.

For example, using the "gesturing right, then gesturing left" scenario, you can create a **GestureRight** animation, starting with a frame where the character appears in a neutral position, and add frames with images that extend the character's hand to the right. Then create its **Return** animation: a complementary animation with images that return the character to its neutral position. You can assign this as the Return animation for the **GestureRight** animation. Next, create the **GestureLeft** animation that starts from the neutral position and extends the character's arm to the left. Finally, create a complementary **Return** animation for this animation as well. A **Return** animation typically begins with an image that follows the last image of the preceding animation.

Starting and returning to the same neutral position, either within an animation or by using a Return animation, enables you to play any animation in any order. The Microsoft Agent animation services automatically play your designated Return animation in many situations. For example, the services play the designated **Return** animation before playing your character's Idling state animations. It is a good idea to define and assign **Return** animations if your animations do not already end in the neutral position.

If you want to provide your own transitions between specific animations; for example, because you always play them in a well-defined order, you can avoid defining **Return** animations. However, it is still a good idea to begin and end the sequence of animations from the neutral position.

### Speaking Animation

Supply mouth images for each animation during which you want the character to be able to speak, unless your character's design has no animated mouth or indication of spoken output. In general, mouth movement is very important. A character may appear less intelligent, likable, or honest if its mouth movement is not reasonably synced with its speech. Mouth images allow your character to lip-sync to spoken output. You define mouth images separately and as Windows bitmap files. They must match the same color palette as the other images in your animation.

The Microsoft Agent animation services display mouth animation frames on top of the last frame of an animation, also called the *speaking frame* of the animation. For example, when the character speaks in the **GestureRight** animation, the animation services overlay the mouth animation frames on the last frame of **GestureRight**. A character cannot speak while animating, so you only supply mouth images for only the last frame of an animation. In addition, the speaking frame must be the end frame of an animation, so a character cannot speak in a looping animation.

Typically, you would supply the mouth images in the same size as the frame (and base image), but include only the area that animates as part of the mouth movement, and render the rest of the image in the transparent color. Design the image so that it matches the image in the speaking frame when overlaid on top of it. To have it match correctly, it is likely you'll need to create a separate set of mouth images for every animation in which the character speaks.

A mouth image can include more than the mouth itself, such as the chin or other parts of the character's body while it speaks. However, if you move a hand or leg, note that it may appear to move randomly because the mouth overlay displayed will be based on the current phoneme of a spoken phrase. In addition, the server clips the mouth image to the speaking frame image's outline. Design your mouth overlay image to remain within the outline of its base speaking frame image, because the server uses the base image to create the window boundary for the character.

The Microsoft Agent Character Editor enables you to define seven basic mouth positions that correspond to common phoneme mouth shapes shown in the following table:

**Mouth Animation Images**



| Mouth Position | Sample Image                       | Representation                                                                                                                     |
|----------------|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Closed         | :::image type="icon" source="images/g07ci01.gif":::<br/> | Normal mouth closed shape. Also used for phonemes such as "m" as in "mom," "b" as in "bob," "f" as in "fife."<br/>           |
| Open-wide 1    | :::image type="icon" source="images/g07ci02.gif":::<br/> | Mouth is slightly open, at full width. Used for phonemes such as "g" as in "gag," "l" as in "lull," "ear" as in "hear."<br/> |
| Open-wide 2    | :::image type="icon" source="images/g07ci03.gif":::<br/> | Mouth is partially open, at full width. Used for phonemes such as "n" as in "nun," "d" as in "dad," "t" as in "tot."<br/>    |
| Open-wide 3    | :::image type="icon" source="images/g07ci04.gif":::<br/> | Mouth is open, at full width. Used for phonemes such as "u" as in "hut," "ea" as in "head," "ur" as in "hurt."<br/>          |
| Open-wide 4    | :::image type="icon" source="images/g07ci05.gif":::<br/> | Mouth is completely open, at full width. Used for phonemes such as "a" as in "hat," "ow" as in "how."<br/>                   |
| Open-medium    | :::image type="icon" source="images/g07ci06.gif":::<br/> | Mouth is open at half width. Used for phonemes such as "oy" as in "ahoy," "o" as in "hot."<br/>                              |
| Open-narrow    | :::image type="icon" source="images/g07ci07.gif":::<br/> | Mouth is open at narrow width. Used for phonemes such as "o" as in "hoop", "o" as in "hope," "w" as in "wet."<br/>           |



 

 

 





