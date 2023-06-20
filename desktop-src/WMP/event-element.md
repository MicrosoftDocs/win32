---
title: EVENT Element (WMP SDK)
description: The EVENT element defines a behavior or action taken by Windows Media Player when it receives a script command labeled as an event.
ms.assetid: d12af3bd-a63e-4022-aa84-0386eeef1390
keywords:
- EVENT Element Windows Media Player
topic_type:
- apiref
api_name:
- EVENT Element
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# EVENT Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **EVENT** element defines a behavior or action taken by Windows Media Player when it receives a script command labeled as an event.

``` syntax
<EVENT   
   NAME = "text string"
   WHENDONE = "RESUME" | "NEXT" | "BREAK"
>
</EVENT>
```

## Attributes

**NAME** (required)

The name of the event.

**WHENDONE** (required)

A value that defines what Windows Media Player does after playing the referenced content.

The following values are possible.



| Value  | Description                                                                                                                                                                                                                     |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RESUME | The current entry (the clip interrupted by the event) resumes playing. If the content is stored content, it resumes at the same point where it stopped; if the content is broadcast, it resumes at the current position.        |
| NEXT   | The next **ENTRY** element plays as if the event had not occurred and Windows Media Player had reached the end of the current clip.                                                                                             |
| BREAK  | If the current entry is within a **REPEAT** loop, the loop terminates as if the repeat count had been completed. Otherwise, Windows Media Player jumps to the end of the playlist as if the final entry had completed as usual. |



 

## Parent/Child Elements



| Hierarchy       | Elements                |
|-----------------|-------------------------|
| Parent elements | **ASX**                 |
| Child elements  | **ENTRY**, **ENTRYREF** |



 

## Remarks

This element defines a behavior or action taken by Windows Media Player when it receives a script command labeled as an event. An event is a particular type of script command embedded in a stream sent to Windows Media Player that consists of a double string. The first string is the word "event", and the second string is the event name. The event name in the second string must match the event name defined in the metafile. (The match is not case-sensitive.) Events can be sent to Windows Media Player receiving a real-time stream, or can be saved in an .asf, .wma, or .wmv file that gets delivered as an on-demand unicast stream. When Windows Media Player receives the script command, it processes the event as defined by the **EVENT** element.

This element defines a scope of **ENTRY** or **ENTRYREF** elements that are processed whenever Windows Media Player receives the script command with the named event. The **ENTRYREF** can be a URL that points to an ASP page. With this element, you can specify a behavior for stream switching in near real time, as opposed to pre-authored stream changes using references to other pieces of content or Windows Media metafiles.

When you use ASP pages to generate playlists, you must specify a value for the *Response*.**ContentType** property and the *Response*.**expires** property in the ASP page because of latency issues with Windows Media Player. The *Response*.**ContentType** must be a valid file name extension for Windows Media metafiles. Valid types include .asf, .asx, .wma, .wax, .wmv, and .wvx.

See the Platform SDK for details about using the **Response** object in ASP.

This element can appear anywhere within the **ASX** element. If multiple **EVENT** elements within an **ASX** element have identical values for their **NAME** attributes, Windows Media Player uses the first occurrence within the **ASX** element, and ignores all others. When **EVENT** elements have distinct **NAME** attributes, their order within the **ASX** element does not matter.

Windows Media Player discards events it receives while processing another event. Nesting of events is not supported. When Windows Media Player is in preview mode, event content is not constrained by the **PREVIEWDURATION** element; the full length of event content can play even if the preview duration for the active **ENTRY** element expires prior to the end of the event.

## Examples

In this example, when Windows Media Player receives the script command EVENT and command string "Adlink" in the streaming media it is rendering, it searches the playlist for an **EVENTNAME** "Adlink". Windows Media Player switches from the stream it is rendering and plays the content referenced in the **EVENT**, "https://example.microsoft.com/adlink.htm".

**ENTRY** attribute **CLIENTSKIP** is set to NO to prevent the **EVENT** clip from being skipped. It must be played.

The script `WHENDONE="RESUME"` instructs Windows Media Player to resume playing the previous media it switched from as soon as Adlink.asf is finished.


```XML
<ASX VERSION="3.0">
<ENTRY CLIENTSKIP="NO">
   <REF HREF="https://example.microsoft.com/clip1.asf" />
</ENTRY>
<EVENT NAME="Adlink" WHENDONE="RESUME">
   <ENTRYREF HREF="https://example.microsoft.com/adlink.htm" 
       CLIENTSKIP="NO" />
</EVENT>
</ASX>
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Windows Media Metafile Elements Reference**](windows-media-metafile-elements-reference.md)
</dt> <dt>

[**Windows Media Metafile Reference**](windows-media-metafile-reference.md)
</dt> <dt>

[**Windows Media Player Object Model**](windows-media-player-object-model.md)
</dt> </dl>

 

 





