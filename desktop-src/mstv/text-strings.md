---
title: Text Strings
description: Text Strings
ms.assetid: fe5e972b-7a82-4131-ab22-840272be1dba
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Text Strings

This topic applies to Windows XP Service Pack 1 or later.

DVD discs, especially karaoke discs, may contain a database of text information to supplement the video or audio content. Such text on karaoke discs might include song titles, artist names, record labels, and so on. Versions of this text can be present in more than one language. These strings are optional; discs are not required to have them. If present they are organized in a way that closely mirrors the logical hierarchy of the DVD volume. Each string is preceded by a number that identifies what part of the disc structure it belongs to or gives some clue as to the content of the string. Text strings do not contain the on-screen lyrics for karaoke discs, nor do they currently contain chapter or title names or information for movie DVDs.

There are two basic types of text strings: structure identifiers and content strings. Types with a value of 0x01 through 0x20 are structure identifiers. They are empty strings; the numerical code is used to identify the logical structure to which any following content strings belong. This structure corresponds very closely to the logical structure of DVD disc contents: volume, title, chapter, and so on. The remaining types identify content strings that hold information that may be displayed to the viewer in a user interface. The exact way in which content strings are used is not closely defined, so DVD authors might use them in various ways.

DVD text strings are currently used almost exclusively on karaoke discs, and these discs mostly use the 0x01 and 0x02 structure identifiers and the 0x30 type content string. But it is reasonable to assume that as time goes by, (1) more types of DVD-Video discs will contain text strings and (2) these strings will be organized in more complex ways in order to provide fuller descriptions of disc contents.

The following code shows how to determine the number of text string language blocks on the disc, and display the languages available in a list box *lboTextLanguages*. For more information on LCIDs and primary language IDs, see [**LanguageFromLCID**](https://www.bing.com/search?q=**LanguageFromLCID**)


```C++
Function GetTextLanguages()
   Dim numLangs As Long, lPrimaryLang As Long
   Dim j As Long, lLCID As Long
   Dim strLanguage As String
   
   ' Get the number of text blocks.
   numLangs = oVidWeboVidWebDVD.DVDTextNumberOfLanguages()
   For j = 0 To numLangs - 1
      'get the locale identifier for the language block
      lLCID = oVidWebDVD.DVDTextLanguageLCID(j)
    
      ' Get the primary language ID from the LCID.
      lPrimaryLang = lLCID And &amp;H3FF
    
      ' Get the human-readable string from the primary language ID.
      strLanguage = oVidWebDVD.LanguageFromLCID(lPrimaryLang)
    
      ' Add it to the list box.
      lboTextStrings.AddItem strLanguage
   Next j
End Sub
```



The following test code demonstrates how to enumerate the strings and examine the text string type. It enters the results into the list box *lboStringTypes* so you can see how the numeric string types are used to organize the content strings. A real application would probably create its own data structure to hold the strings, or else would display them in a more useful way for the viewer.


```C++
Function GetTextStrings(lLanguage)
' lLanguage is the 0-based index for the language block.

Dim numStrings As Long
Dim stringType As DVDTextStringType
Dim j As Integer

numStrings = oVidWebDVD.DVDTextNumberOfStrings(lLanguage)

For j = 0 To numStrings - 1
   stringType = oVidWebDVD.DVDTextStringType(lLanguage, j)

  If (stringType > &amp;H20) Then 'There is actually some text to read here
     lboTextStringTypes.AddItem stringType & ": "
       & oVidWebDVD.DVDTextString(lLanguage, j)
  Else ' It's a node indicating what level of the volume structure.
       '   the following strings will apply to
     lboTextStringTypes.AddItem stringType
  End If
Next j

End Function
```



**DVD Text String Types**

The following tables list a subset of the DVD text string types. All types with a value 0x20 and below are empty strings that merely indicate the node level in the disc's content data structure. The other strings are content strings. Most title and song names are type 0x30. The types in the Title, SubTitle and Original categories help to further identify the particular genre. The exact meaning and intended use of these categories is defined in a public document that can be downloaded from the DVD Forum's Web site.

**Structure Identifiers**



|            |      |                                                                                                            |
|------------|------|------------------------------------------------------------------------------------------------------------|
| Volume     | 0x01 | Indicates that the strings that follow pertain to the DVD volume.                                          |
| Title      | 0x02 | Indicates that the strings that follow pertain to a title.                                                 |
| ParentalID | 0x03 | Indicates that the strings that follow pertain to a particular parental ID.                                |
| Chapter    | 0x04 | Indicates that the strings that follow pertain to a chapter.                                               |
| Cell       | 0x05 | Indicates that the strings that follow pertain to a cell (typically consisting of one scene from a movie). |



 

**Stream Identifiers**



|            |      |                                                                        |
|------------|------|------------------------------------------------------------------------|
| Audio      | 0x10 | Indicates that the strings that follow pertain to an audio stream.     |
| Subpicture | 0x11 | Indicates that the strings that follow pertain to a subpicture stream. |
| Angle      | 0x12 | Indicates that the strings that follow pertain to an angle block.      |



 

**Audio Channel Identifiers**



|         |      |                                                                                   |
|---------|------|-----------------------------------------------------------------------------------|
| Channel | 0x20 | Indicates that the strings that follow pertain to one channel in an audio stream. |



 

**General Content Strings**



|          |      |                                                                                  |
|----------|------|----------------------------------------------------------------------------------|
| Name     | 0x30 | The most common identifer for title names, chapter names, song names, and so on. |
| Comments | 0x31 | General comments about the title, chapter, song, and so on.                      |



 

**Title Content Strings**



|        |      |                                                                                                    |
|--------|------|----------------------------------------------------------------------------------------------------|
| Series | 0x38 | Additional information about the title, chapter, song, and so on.                                  |
| Movie  | 0x39 | Additional information about the title or chapter if this is a movie.                              |
| Video  | 0x3a | Additional information about the title or chapter if this is a video.                              |
| Album  | 0x3b | Additional information about the title or chapter if this is an album.                             |
| Song   | 0x3c | Additional information about the title or chapter if this is a song.                               |
| Other  | 0x3f | Additional information about the title or chapter if this belongs to some other genre or category. |



 

**Secondary Title Content Strings**



|        |      |                                                                                                    |
|--------|------|----------------------------------------------------------------------------------------------------|
| Series | 0x40 | Additional information about the title, chapter, song, and so on.                                  |
| Movie  | 0x41 | Additional information about the title or chapter if this is a movie.                              |
| Video  | 0x42 | Additional information about the title or chapter if this is a video.                              |
| Album  | 0x43 | Additional information about the title or chapter if this is an album.                             |
| Song   | 0x44 | Additional information about the title or chapter if this is a song.                               |
| Other  | 0x45 | Additional information about the title or chapter if this belongs to some other genre or category. |



 

**Original Content Strings**



|        |      |                                                                                                    |
|--------|------|----------------------------------------------------------------------------------------------------|
| Series | 0x48 | Additional information about the title, chapter, song, and so on.                                  |
| Movie  | 0x49 | Additional information about the title or chapter if this is a movie.                              |
| Video  | 0x4a | Additional information about the title or chapter if this is a video.                              |
| Album  | 0x4b | Additional information about the title or chapter if this is an album.                             |
| Song   | 0x4c | Additional information about the title or chapter if this is a song.                               |
| Other  | 0x4f | Additional information about the title or chapter if this belongs to some other genre or category. |



 

**Other Info Content Strings**



|             |      |                                                                              |
|-------------|------|------------------------------------------------------------------------------|
| Other Scene | 0x50 | Additional information about an alternate scene in a movie title or chapter. |
| Other Cut   | 0x51 | Additional information about an alternate cut in a movie title or chapter.   |
| Other Take  | 0x52 | Additional information about an alternate take in a movie title or chapter.  |



 

## Related topics

<dl> <dt>

[DVD Applications in Visual Basic (Video Control)](dvd-applications-in-visual-basic--video-control.md)
</dt> </dl>

 

 




