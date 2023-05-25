---
description: Enforcing Parental Management Levels
ms.assetid: ad996a03-e94e-4743-90a2-aa390984a231
title: Enforcing Parental Management Levels
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Enforcing Parental Management Levels

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Any title or portion of a title on a DVD-Video disc can be assigned a generic parental management level (PML) from 1 through 8. When the DVD Navigator is reading content that has a PML, it is said to be in a *parental block*. A parental block may consist of part of a chapter, multiple chapters, or multiple titles. A DVD application intended for an international market should not hard code a particular rating system into its parental management logic.

The DVD Navigator itself does not enforce the PMLs; it merely informs your application when it encounters PML information on the disc. By default, it ignores this information on the disc and plays the highest level content. To enforce the PMLs, your application must implement some form of password control logic that associates users with levels, instruct the DVD Navigator to send it PML event notifications (by calling the [**IDvdControl2::SetOption**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-setoption) method on startup, with the parameters DVD\_NotifyParentalLevelChange and **TRUE**), and respond to those events to allow or disallow access as appropriate.

A DVD title can have one overall PML, but disc authors can give certain sections of that title higher or more restrictive PMLs. These are called temporary PML commands; these commands always contain two branching instructions: one to follow if the temporary PML command is accepted by the player application, and the other to follow if the command is rejected. The sequence of events is as follows. The DVD Navigator is reading video content (DVD Title Domain) when it encounters a temporary PML command on the disc. It checks its internal flag to see whether the application has requested to be notified of this event. If the flag is not set, the DVD continues playing, following the "parental level change rejected" branch specified on the disc. If the flag is set, the DVD sends an EC\_DVD\_PARENTAL\_LEVEL\_CHANGE event to the application and waits in a paused state until it gets a response. When your application receives the event, it uses its own logic to determine whether to accept the command. It then calls [**IDvdControl2::AcceptParentalLevelChange**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-acceptparentallevelchange) with an argument of **TRUE** or **FALSE**. If **TRUE**, the DVD Navigator resumes playing, following the "parental level change accepted" branch specified on the disc. Otherwise it resumes playing and follow the "parental level change rejected" branch.

## Related topics

<dl> <dt>

[DVD Applications](dvd-applications.md)
</dt> </dl>

 

 



