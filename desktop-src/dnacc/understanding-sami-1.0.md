---
Description: Microsoft Corporation
ms.assetid: 1a94f822-30f1-4198-ac33-f63ed5026c9f
title: Understanding SAMI 1.0
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Understanding SAMI 1.0

Microsoft Corporation

Originally published October 2001; updated February 2003

**Summary:** This article describes how the Microsoft Synchronized Accessible Media Interchange (SAMI) technology expands the ability to provide closed captioning to a wide range of multimedia products. (17 printed pages)

Download [samioverview.exe](http://download.microsoft.com/download/f/d/f/fdf0ba36-42cf-487c-ba4c-eb6f5e6e3715/SAMIOverview.exe).

-   [Introduction](#introduction)
    -   [SAMI 1.0 Definition](#sami-10-definition)
    -   [Captioning Technologies for PC Multimedia](#captioning-technologies-for-pc-multimedia)
    -   [SMIL](#smil)
    -   [SAMI](#understanding-sami-10)
-   [Captioning](#captioning)
    -   [Uses](#uses)
-   [Audio Descriptions](#audio-descriptions)
    -   [Uses](#uses)
-   [SAMI Authoring](#sami-authoring)
    -   [Tools and Resources](#tools-and-resources)
-   [Writing for SAMI 1.0](#writing-for-sami-10)
    -   [File Name Extension](#file-name-extension)
    -   [SAMI Structure and Declaration](#sami-structure-and-declaration)
    -   [Header tag](#header-tag)
    -   [Title tag](#title-tag)
    -   [SAMI parameters](#sami-parameters)
    -   [Style parameters](#style-parameters)
    -   [Paragraph tag](#paragraph-tag)
    -   [Class and Localization](#class-and-localization)
    -   [ID Style](#id-style)
    -   [Source ID](#source-id)
-   [Synchronization](#synchronization)
-   [Overall Example](#overall-example)
-   [SAMI Clients](#sami-clients)
    -   [Windows Media Player](#windows-media-player)
    -   [Internet Explorer](#internet-explorer)
    -   [Examples](#examples)
    -   [Showcases and a SAMI document sample](#showcases-and-a-sami-document-sample)

## Introduction

### SAMI 1.0 Definition

Microsoft Synchronized Accessible Media Interchange (SAMI) simplifies captioning for developers, educators, and multimedia producers and designers who will now find it easier to make their work more universally accessible. The SAMI file format specification is available to the public as an open (no licensing fees) standard.

Captioning was initially developed by WGBH, the public television station in Boston, for an estimated 20 million Americans who were deaf or hard of hearing. SAMI technology expands the ability to provide closed captioning to a wide range of multimedia products. The sole purpose of this document is to cover captioning technology used in PC multimedia. Television captioning is not covered.

The CPB/WGBH National Center for Accessible Media (NCAM) was of great help in the development and update of this document. For more information, see the [NCAM](http://go.microsoft.com/fwlink/p/?linkid=208609) website.

### Captioning Technologies for PC Multimedia

SAMI is not the only captioning technology available for PC multimedia today. Multimedia producers and HTML authors can choose the technologies most suitable for them.

### SMIL

The Synchronized Multimedia Integration Language (SMIL) focuses on choreographing multimedia presentations of audio, video, text, and graphics in real-time. SMIL 1.0 is a World Wide Web Consortium (W3C) Recommendation (June 1998). W3C developed the succeeding version (SMIL 2.0). For more information about W3C and SMIL 2.0, see the website at [http://www.w3.org/AudioVideo/](http://go.microsoft.com/fwlink/p/?linkid=7974).

Internet Explorer 5.5 (or later) supports HTML+TIME based on the SMIL 2.0 specification. The technical detail of HTML+TIME is available in the MSDN article [available here](htime_node_entry).

### SAMI

SAMI 1.0 was designed and developed to caption the digital media widely available in PC systems. SAMI captions coexist with digital media as separate, simple text files. The captions can be easily modified, maintained, customized, and localized for different languages.

The SAMI specification is supported by Microsoft Encarta Encyclopedia, Windows Media Player, and some Microsoft multimedia titles. The technical detail is available in this documentation and in the [Windows Media Player 9 Series Software Development Kit (SDK)]( http://go.microsoft.com/fwlink/p/?linkid=208374).

A sample of SAMI closed-caption captioning is provided in this document.

For more information, see [Adding Closed Captions to Digital Media](wmp.adding_closed_captions_to_digital_media).

**Open Captions**

Open Captions are always visible on the screen and cannot be turned off. (The alternative, closed captions, can be turned on or off by the user.) Open Captions are useful but, when compared to other techniques, they can also be difficult to localize or edit in postproduction.

**Applying Captions**

A captioning author can choose from a variety of methods for adding closed or open captions to media. It is important for a captioning author to follow certain captioning styles for a better viewing experience.

For more information about captioning styles, techniques, tools, and services, see the section titled SAMI Authoring.

## Captioning

Captioning is a synchronized, alternative format used to deliver audio content. The goal for multimedia authors should be to provide captions for all audio content, including both video and animated content. Typically, captions are displayed through a client-side media player.

Because captions are used as an alternative method of delivering audio content, it is important that all aspects of audio content can be translated into a text equivalent. For example, captions should include the description of sounds (such as "... the dog barks...") as well as symbols and icons to represent the type of content (such as a musical note to represent music). SAMI also allows the user to select an authored Font style (for example, large print, high contrast) to customize the content to the user's needs.

### Uses

Although closed captioning was designed originally for people who are deaf or hard of hearing, captions can also be of great help to others. Captions are often used by people learning a second language, learning to read, using equipment with poor audio quality and by those in noisy environments.

## Audio Descriptions

Audio Descriptions (AD) are simply additional narrative tracks that describe the current scene or setting. Audio descriptions began in the early days of radio when all users relied on well-composed descriptions to visualize what they could not see. Today, most people watch television as a replacement for radio. Unfortunately, this development has created a large void for the visually impaired who must rely on audio to extract the entire meaning of an audio-visual presentation.

### Uses

To aid users who are blind or have limited vision, it is necessary to insert an audible description of the visual content into the quiet portions of a program's regular soundtrack. An audio description can be used to describe any important on-screen elements. For example, when viewing a media clip that contains a visible interruption of a dialog between two people, it would be necessary for the user who is blind to receive an audio description of what is occurring visually. This is explained further in the following example:

**James:** "How is your day so far?"

**Jennifer:** "My day is going quite well. . . ." Oh! Now it seems to be a little worse."

This dialog would make little sense to the user who cannot view the scene or was unable to experience both the visual and audio content of the media. However, with the use of an audio description, the content could be made clear. For example:

**James:** "How is your day so far?"

**Jennifer:** "My day is going quite well. . . ."

**Audio Description:** A passing waiter spills a pitcher of ice water down Jennifer's back.

**Jennifer:** "Oh! Now it seems to be a little worse."

## SAMI Authoring

Developing SAMI documents requires an understanding of the syntax used for SAMI. A basic understanding of HTML will help in understanding the fundamental design of this process. Knowledge of the client-side rendering tools is also necessary; this includes an understanding of development utilizing Windows Media Player or DHTML.

### Tools and Resources

For assistance in understanding the concepts behind SAMI captioning, developing accessibility solutions, and authoring tools, see:

-   [CPB/WGBH National Center for Accessible Media (NCAM)](http://go.microsoft.com/fwlink/p/?linkid=208609)
-   [Trace Research and Development Center](http://go.microsoft.com/fwlink/p/?linkid=208610)
-   [Captioning Key Guidelines and Preferred Techniques](http://go.microsoft.com/fwlink/p/?linkid=208611) by the [Described and Captioned Media Program](http://go.microsoft.com/fwlink/p/?linkid=208612)
-   [Hi-Caption](http://go.microsoft.com/fwlink/p/?linkid=208613), a captioning tool by HiSoftware
-   [Adding Captions for Producer 2003 Presentations](http://go.microsoft.com/fwlink/p/?linkid=208614)
-   [Adding Closed Captions to Digital Media](wmp.adding_closed_captions_to_digital_media)
-   [Captions and Audio Descriptions for PC Multimedia](captions-and-audio-descriptions-for-pc-multimedia.md)

## Writing for SAMI 1.0

### File Name Extension

SAMI documents must use the following extensions: .smi or .sami

**Example**

``` syntax
CC-SAMPLE.SMI 
CC-SAMPLE.SAMI
```

### SAMI Structure and Declaration

Because SAMI is based closely on HTML, it has a similar (but not identical) component construct that makes it an easy format to learn and edit. All SAMI documents must begin with a &lt;SAMI&gt; tag and end with a &lt;/SAMI&gt; tag.

### Header tag

The header section (between the &lt;Head&gt; and &lt;/Head&gt; tags) is required and contains the SAMIParam and Style sections. These sections contain the basic layout and format information.

### Title tag

The &lt;Title&gt; tag is used for informational purposes in SAMI and is optional.

### SAMI parameters

SAMI parameters are entered within the SAMIParam section, bounded by &lt;SAMIParam&gt; and &lt;/SAMIParam&gt;. SAMI parameters are of two types. Some parameters are strictly informational. A SAMI engine ignores these parameters. For example, copyright will not make or break a SAMI document; it is simply a designation of ownership. Other parameters are used to set the initial attributes of the displayed captions or the base values of encoder/decoder properties.

**Copyright**

The use of copyright is informational only and is not parsed by the SAMI rendering engine. Its use with the SAMIParam section implies that the copyright covers only the transcription, formatting, and time stamps. Copyright of the media must be specified elsewhere.

Use: Copyright {&lt;copyright string&gt;}

**Media**

The Media parameter is used both as a cross-reference for activation and as a record of the base media. A Primary URL and Secondary URL can be specified within the Media parameter. In most cases, only the Primary value will be used. The Secondary URL may be used in cases where users choose whether they want to play the video clip with sound or just the sound file. The Media parameter is not required (although it is a good practice and may be required in future versions).

Use: Media {&lt;primary URL&gt;}, {&lt;secondary URL&gt;}

> [!Note]  
> To date, Windows Media Player does not support the Media SAMI parameter.

 

**Metrics**

Metrics designate the time units for synchronization and duration. Microsoft DirectShow and Windows Media Player support only milliseconds (ms), but SAMI is suited for use with other systems that use different time increments.

Use: Metrics {time: &lt;time units&gt;; duration:&lt;media duration&gt;}

**Specification**

Specification designates the version of the SAMI document specification.

**Use:** Spec {MSFT:1.0;}

**Example**

``` syntax
   <SAMIParam>
      Copyright {(c)1998-2001, Microsoft Corporation}
      Media {SAMI.jpg}
      Metrics {time:ms; duration: 73000;}
      Spec {MSFT:1.0;}
   </SAMIParam>
```

### Style parameters

Style parameters are used to format textual display and to provide a method for multiple language support. SAMI style supports methods and attributes of [W3C CSS2](http://go.microsoft.com/fwlink/p/?linkid=161695) (Cascading Style Sheets, level 2). SAMI styles are based on CSS (W3C Cascading Style Sheet) methods and attributes. Style parameters are entered within the Style section, bounded by &lt;Style Type="text/css"&gt; and &lt;/Style&gt;.

**CSS use**

> [!Note]  
> It should be noted that while SAMI employs CSS methods and attributes, it does so in a restricted manner as specified in the following:

 

**Inline formatting use**

Authoring captions in SAMI provide a rich range of character formats. That is, SAMI supports the use of most standard HTML inline formatting (see following section) as well as ISO Latin-1 (ISO 8859) entities. The latter allows for easy localization of SAMI documents.

### Paragraph tag

A Caption block (one to four caption lines) is defined as a paragraph in SAMI. Basic formatting can be applied to all Caption blocks using a Paragraph style. Any CSS style will work.

**Example**

``` syntax
      p {
         margin-left: 8pt; 
         margin-right: 8pt;
         margin-bottom: 2pt; 
         margin-top:-10pt;
         text-align: left; 
         font-size: 12pt; 
         font-family: arial, sans-serif; 
         font-weight: bold;
         color: #fee8c6; }
```

### Class and Localization

Class is reserved for defining a language-specific caption or action. When a SAMI document is parsed, the rendering engine will match the user-selected Language value with the Name value within a Class definition. The SAMI rendering engine will render only those lines in which the Name value matches the user-selected (or author-selected) Language value. For an example, see **Language** on the **Play** menu of Windows Media Player. If the user (or author) has not explicitly selected a language, the first Class (language) definition will be used by default.

For consistency, the Language value should follow standard ISO639-ISO3166 naming conventions. For example, "en" is the ISO639 abbreviation for English, and "US" is the ISO3166 abbreviation for United States. Thus, "en-US" is how a type of English (for the United States) would be specified.

Class naming in SAMI is accomplished by creating a unique name preceded by a period. For example, **.ENCC** can be used for English captions and **.FRFRCC** can be used for French/France captions (as opposed to French/Canadian). A Class is referenced by placing the Class parameter within a paragraph tag. For example: &lt;P Class=ENCC&gt;.

In addition to language, Class can be used to modify the Caption block formatting. That is, any formatting parameters that are supported in the Paragraph style (as previously described) can be added to the Class style. This is helpful with multiple languages in which the font and margins are likely to be changed accordingly (for example, German takes 30 percent more line space than English). The use of formatting parameters within the Class style will supersede any Paragraph style parameters.

> [!Note]  
> Web authors can use the embedded Windows Media Player object model (properties) to switch languages in the scripting language. See samples attached to this document or Windows Media Player 9 Series Software Development Kit (SDK) for more details.

 

Additional resources about multiple language SAMI development can be found in the Other Reference Material section under the following topics:

Entities (ISO Latin-1 (ISO 8859))

Language Codes (ISO 639)

Country Codes (ISO 3166)

**Use**

``` syntax
<Class Name> {Name: <user selectable name>; Lang: <ISO639>-<ISO3166>; 
<character formatting parameters>}
```

**Example**

``` syntax
.ENCC {Name: English; lang: en-US; color: white; margin-left: 
            30pt; margin-right: 30pt;} 

.FRFRCC {Name: French; lang: fr-FR; color: yellow; margin-left: 
         12pt; margin-right: 12pt;} 

.DECCGer {Name: German; lang: de-DE; color: yellow; margin-left: 3pt; 
          margin-right: 3;}
```

### ID Style

Often, special formatting is helpful to meet the needs of a specific audience (for example, children or those who are visually impaired). In SAMI, this is accomplished with the ID property. For example, big print captions can be displayed in 18pt. This is done by creating a BigPrint ID style and applying it to the appropriate paragraph. ID styles are defined by appending a unique name to a pound sign (\#), followed by a list of supported formatting parameters.

In the HTML use of CSS styles, the author creates and applies the IDs. With SAMI, the author only creates the ID styles. The SAMI rendering engine applies the ID style at the time of synchronization, according to the user-selected style. That is, if the user selects the Big Print style, the SAMI engine applies the authored \#BigPrint style to each &lt;P Class=""&gt; tag that was rendered.

> [!Note]  
> Web authors can use the embedded Windows Media Player object model (properties) to switch styles in the scripting language. See samples attached to this document or Windows Media Player 9 Series Software Development Kit (SDK) for more details.

 

**Use**

``` syntax
#<unique name> {<formatting parameters>}
```

**Example**

Using the following Paragraph style:

``` syntax
p {font-size: 14pt; text-align: left; font-family: sans-serif; 
   color: white; background-color: black;}
```

The following Style IDs would result in:

``` syntax
#Standard {Name: Standard; margin-left: 30pt; margin-right: 30pt;}
```

![figure 1. example of 14pt font](images/atg-samiarticle01.png)

``` syntax
#Youth {Name: Youth; color: yellow; margin-left: 15pt; margin-right: 15pt;} 
```

![figure 2. example of increasing font size](images/atg-samiarticle02.png)

``` syntax
#BigPrint {Name: BigPrint; color: yellow; margin-left: 4pt; margin-right: 3pt;} 
```

![figure 3. example of big print captions](images/atg-samiarticle03.png)

### Source ID

The Source ID is always displayed as an additional line at the top of a Caption block (see the following). This is used to display the source of the voice or sound that is being captioned. It can contain a speaker's name or an object's name (for example, a radio). For the SAMI engine to support the Source ID feature, a \#Source must be defined in the Style block. The Source ID is then specified within a Sync block (see the following example and Synchronization section). The Source ID need only be updated when the source has changed.

> [!Note]  
> Windows Media Player 7.0 for Macintosh also supports SAMI closed captioning in the stand-alone player mode, although the Source ID needs to be updated in every synchronization &lt;Sync&gt; tag.

 

![figure 4. example of source id](images/atg-samiarticle04.png)

**Use**

``` syntax
#Source {<formatting parameters>}
```

**Example**

The following is an example of defining a Source ID in the Style block:

``` syntax
#Source {background-color: silver; color: black; font-size: 11pt; 
         font-family: sans-serif; font-weight: normal;} 
```

The following is an example of updating a Source ID within a Sync block:

``` syntax
<p Class=ENCC ID=Source> Pres. John F. Kennedy 
<p Class=ENCC> Let the word go forth, from this time and place...
```

## Synchronization

SAMI introduces the &lt;Sync Start=&gt; tag to support this functionality. The Start parameter is assigned the media's Elapsed Time value in milliseconds. When the elapsed play time of the media matches the Sync Start time, the SAMI rendering engine passes off the contents following the &lt;Sync Start=&gt; tag to the SAMI display engine. To blank a paragraph, a non-breaking space entity (&nbsp;) is used.

**Definition**

The SAMI engine parses all contents of a specific &lt;Sync&gt; block when the elapsed time for the media matches its Start=&lt;media elapsed time&gt; value. If a paragraph within the &lt;Sync&gt; block contains a Class property, it must match the user-selected language to be rendered. Each &lt;Sync&gt; block can contain only the following HTML markup tags for style, font, and format of the caption text. All markup tags are defined in W3C HTML 4.01.

**Table 1. HTML Markup Tags Supported in SAMI 1.0**



| Name       | Description                       |
|------------|-----------------------------------|
| b          | Bold text style                   |
| basefont   | Base font size                    |
| bdo        | I18N BiDi override                |
| big        | Large text style                  |
| blockquote | Long quotation                    |
| br         | Forced line break                 |
| caption    | Table caption                     |
| center     | Shorthand for DIV align=center    |
| col        | Table column                      |
| colgroup   | Table column group                |
| dd         | Definition description            |
| div        | Generic language/style container  |
| dl         | Definition list                   |
| dt         | Definition term                   |
| font       | Local change to font              |
| h1         | Heading                           |
| h2         | Heading                           |
| h3         | Heading                           |
| h4         | Heading                           |
| h5         | Heading                           |
| h6         | Heading                           |
| hr         | Horizontal rule                   |
| i          | Italic text style                 |
| img        | Embedded image                    |
| li         | List item                         |
| ol         | Ordered list                      |
| p          | Paragraph                         |
| pre        | Preformatted text                 |
| q          | Short inline quotation            |
| s          | Strike-through text style         |
| small      | Small text style                  |
| span       | Generic language/style container  |
| strike     | Strike-through text               |
| sub        | Subscript                         |
| sup        | Superscript                       |
| table      | N/A                               |
| tbody      | Table body                        |
| td         | Table data cell                   |
| tfoot      | Table footer                      |
| th         | Table header cell                 |
| thead      | Table header                      |
| tr         | Table row                         |
| tt         | Teletype or monospaced text style |
| u          | Underlined text style             |
| ul         | Unordered list                    |



 

**Example**

Following are four sequential Sync blocks that start at elapsed media times: 0, 1000, 2500, and 5000 milliseconds.

``` syntax
<sync start=0> 
    <p class=ENCC> Hello World! (The first caption) 

<sync start=1000> 
    <p class=ENCC id=Source> This is the Source ID line 
    <p class=ENCC> Hello my friend (The second caption) 

<sync start=2500> 
    <p class=ENC> If English (ENCC) is selected this line is displayed, 
    <p class=FRCC> but this line is not displayed. 

<sync start=5000> 
    <p class=ENCC ID=Source> This caption is blank, but not the Source ID 
    <p class=ENCC>
```

## Overall Example

The following is an example of a SAMI file being rendered within Windows Media Player embedded in an HTML page.

-   Area 1: This is the location in which the media file is being displayed.
-   Area 2: This is the Source ID line.
-   Area 3: This is the captions window that is synchronized with the subject speaking in the media.
-   Area 4: This is an example of how the SAMI file is read for the synchronization process of the media file.

Below is a screen capture from the SAMI demonstration series, provided only for the purpose of this explanation. Typically, the synchronization tags and caption text are not displayed with the media, although the synchronized DHTML with SAMI script can provide a very powerful representation, as shown in the demonstration series.

![figure 5. a screen capture from the sami demonstration series](images/atg-samiarticle05.png)

## SAMI Clients

### Windows Media Player

This section focuses on the rendering of SAMI captions by Microsoft Windows Media Player. Windows Media Player is a client-side player used to render audio and video files in multimedia presentations such as CD-ROM and web-based titles. With Windows Media Player, the SAMI document and media files are separate. Both the SAMI document and media files are fetched, parsed, synchronized, and rendered on the player. This allows for easy authoring, editing, and re-editing of the SAMI (captions) document.

Windows Media Player may require that all SAMI tags be presented in caps. Windows Media Player reads a separate .sami or .smi file and reads the &lt;Sync Start&gt; tag to identify when to display accompanying text or captions with the media file being played.

Windows Media Player has two user interface modes: full mode and skin mode. You can also embed the Windows Media Player ActiveX control in a webpage.

Properties exposed by the ClosedCaption object of the Windows Media Player control for SAMI captioning support include:

-   **ClosedCaption.captioningID**

    Specifies or retrieves the name of the frame or control displaying the captioning.

-   **ClosedCaption.SAMIFileName**

    Specifies or retrieves the name of the .smi file containing the closed-captioning text strings.

-   **ClosedCaption.SAMILang**

    Specifies or retrieves the closed-captioning language. If the **SAMILang** property is not set, the language associated with the first language tag in the .smi file is used as the default.

-   **ClosedCaption.SAMIStyle**

    Specifies or retrieves the font size and style used for the closed captioning.

Windows Media Player ClosedCaption object also supports some methods to get information about the currently loaded SAMI file. For more information about ClosedCaption object properties and methods, see the Windows Media Player 9 Series Software Development Kit (SDK) and MSDN article [Adding Closed Captions to Digital Media](wmp.adding_closed_captions_to_digital_media).

### Internet Explorer

Internet Explorer supports &lt;object&gt; tag to insert Microsoft ActiveX controls. As an ActiveX control, the Windows Media Player ActiveX control object model exposes methods, properties, and event supports to other Microsoft Windows applications. Windows Media Player supports an event for each &lt;Sync&gt; tag, and web authors can use the event for extensive effect by combining it with the DHTML support of Internet Explorer. DHTML technique examples are provided in the SAMI demonstration series.

You may also use &lt;embed&gt; tag to insert a media control into a webpage for compatibility purpose.

The following example shows how web authors can embed Windows Media Player objects with SAMI closed-captioning options. Web authors can access the embedded Windows Media Player object through scripting.

### Examples

``` syntax
<!-- An embedded Windows Media Player object with 
         SAMI closed captioning -->
<object   
   classid="CLSID:6BF52A52-394A-11d3-B153-00C04F79FAA6"
               id="WMP1" width=180 height=186
   Style="margin:6; border:3 inset white;">

   <param name="URL"
      value="http://foo/media/SAMI_Demo.wmv">
   <param name="SAMIFileName"
      value="http://foo/cc/SAMI_Demo.smi">
   <param name="captioningID"    value="cc">
   <param name="SAMIStyle"    value="Black Print">
   <param name="AutoStart"    value=false>
   <param name="AutoRewind"    value=true>
   <param name="EnableContextMenu"    value=false>
</object>

<!-- A <div> window for the SAMI captioning, 'id=cc' is specified 
      for 'captioningID' parameter -->
<div 
   id=cc 
   style="margin-top:3; width:290; height:90; background: 
         white; border:2 inset silver;">
</div>
```

### Showcases and a SAMI document sample

Windows Media Player can detect a SAMI caption file if it is named with the same file name as the .smi extension and is located in the same folder. However, Windows Media Player does not detect a .sami extension automatically. Windows Media Player lacks the user interface required to select a SAMI closed-caption file, although web authors can specify the file name of the SAMI caption file or the options for SAMI closed captioning. The SAMI demonstration series introduces the variety of SAMI usages and showcases.

**Sample SAMI document**

``` syntax
<SAMI>
<Head>
   <Title>President John F. Kennedy Speech</Title>
   <SAMIParam>
      Copyright {(C)Copyright 1997, Microsoft Corporation}
      Media {JF Kennedy.wav}
      Metrics {time:ms; duration: 73000;}
      Spec {MSFT:1.0;}
   </SAMIParam>

   <STYLE TYPE="text/css"><!--
      P {margin-left: 29pt; margin-right: 29pt; font-size: 12pt; 
      text-align: left; font-family: tahoma, arial, sans-serif; 
      font-weight: normal; color: white; background-color: black;}

      TABLE {Width: "248pt" ;}

      .ENUSCC {Name: "English Captions"; lang: en-US-CC;}

#Source {margin-bottom: -15pt; background-color: silver; 
         color: black; vertical-align: normal; font-size: 12pt; 
         font-family: tahoma, arial, sans-serif; 
         font-weight: normal;}

#Youth {color: greenyellow; font-size: 18pt;}

#BigPrint-1 {color: yellow; font-size: 24pt;}-->
   </Style>
</Head>

<Body>
   <SYNC Start=0>
      <P Class=ENUSCC ID=Source>Pres. John F. Kennedy   
   <SYNC Start=10>
      <P Class=ENUSCC>Let the word go forth, 
         from this time and place to friend and foe 
         alike that the torch
   <SYNC Start=8800>
      <P Class=ENUSCC>has been passed to a new generation of Americans, 
         born in this century, tempered by war,
   <SYNC Start=19500>
      <P Class=ENUSCC>disciplined by a hard and bitter peace, 
         proud of our ancient heritage, and unwilling to witness
   <SYNC Start=28000>
      <P Class=ENUSCC>or permit the slow undoing of those human rights
          to which this nation has always
   <SYNC Start=38000>
      <P Class=ENUSCC>been committed and to which we are 
         committed today at home and around the world.
   <SYNC Start=46000>
      <P Class=ENUSCC>Let every nation know, 
         whether it wishes us well or ill, 
         that we shall pay any price, bear any burden,
   <SYNC Start=61000>
      <P Class=ENUSCC>meet any hardship, support any friend, 
         oppose any foe, to ensure the survival and
         success of liberty.
   <SYNC Start=73000>
      <P Class=ENUSCC ID=Source>End of:
      <P Class=ENUSCC>President John F. Kennedy Speech
</Body>
</SAMI>
```

 

 



