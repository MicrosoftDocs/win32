---
title: Animation Design
description: Animation Design
ms.assetid: 8812e4cc-9062-4c65-81ef-229bd29534cd
ms.topic: article
ms.date: 05/31/2018
---

# Animation Design

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

### Image Design

Use the Microsoft Office Palette when designing your characters to minimize any potential palette realization issues. Avoid selecting a transparency color that is similar to the colors that you use in your document.

### Sounds

Microsoft Agent enables you to play sounds in your animations. We recommend you do not include sounds for your **Idle** animations. This is so there won't be a delay in the middle of the animation, if Agent has to load the system multimedia DLL.

### Frame Size

Typical Office Assistants are 123 x 93 pixels. While you can create characters of other sizes, they will be scaled to 123 x 93 in the Assistant Gallery.

### Frame Transition

All animations except for **Goodbye**, **Greeting**, **Show** and **Hide** should begin and end with the RestPose animation. Microsoft Office does not play explicit **Return** animations, so you should not define them. All animations should also have Exit Branching. Exit branching enables us to 'hurry up and finish' the current animation before we call the next animation. If you don't supply Exit Branching, the transition between animations may be jerky.

### Character Properties

Microsoft Agent enables you to set the character's [**Name**](name-property.md), [**Description**](description-property.md) and [**ExtraData**](extradata-property.md) properties. Microsoft Office uses the **ExtraData** field to hold to one or more Introduction Phrases and Reminder Phrases. Microsoft Office picks from the other Introduction Phrases to put in the speech balloon in the Assistant Gallery. We use the Reminder Phrases when you receive a reminder from Outlook.

The [**ExtraData**](extradata-property.md) field is formatted as follows:

IntroPhrase1~~IntroPhrase2~~IntroPhrase3^^ReminderPhrase1~~ReminderPhrase2~~ReminderPhrase3

Intro Phrases are separated by a pair of tilde characters (~), followed by Reminder Phrases. These Reminder Phrases are also separated by a pair of tilde characters. The two sets of phrases are separated by two caret characters (^^). There is no limit to the number of each kind of phrase, except that there must be at least one of each.

 

 




