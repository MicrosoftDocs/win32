---
title: HTML Clipboard Format
description: This section discusses the HTML Clipboard format.
ms.assetid: e891393f-234f-4c94-b581-c4e5f885d2ab
keywords:
- Windows User Interface,clipboard
- clipboard,cutting data
- clipboard,copying data
- clipboard,pasting data
- clipboard,formats
- clipboard,HTML format
- clipboard,cutting HTML text
- clipboard,pasting HTML text
- CF_HTML clipboard format
- clipboard,CF_HTML format
ms.topic: article
ms.date: 05/31/2018
---

# HTML Clipboard Format

The requirements for transferring HTML text by means of the clipboard differ depending on scenario. This article is concerned with cutting and pasting fragments of an HTML document. There may be requirements for transferring entire HTML documents through the clipboard; however, this article is driven by a requirement to transfer fragments of selected HTML text. As such, a method that required the entire HTML document to be copied to the clipboard is seen as too heavyweight.

The CF\_HTML clipboard format allows a fragment of raw HTML text and its context to be stored on the clipboard as ASCII. This allows the context of the HTML fragment, which consists of all preceding surrounding tags, to be examined by an application so that the surrounding tags of the HTML fragment can be noted with their attributes. Although it is up to applications to decide how to interpret such fragments, some basic guidelines are included here based on IE4/MSHTML implementations.

The official name of the clipboard (the string used by RegisterClipboardFormat) is HTML Format.

-   [Description](#description)
-   [Scenarios](#scenarios)

## Description

CF\_HTML is entirely text format (to be, among other things, in the HTML spirit, and uses UTF-8) and includes a `description`, an optional `context`, and, within the context, the `fragment`.

The following is an example of a clipboard:


```
Version:0.9
    StartHTML:71
    EndHTML:170
    StartFragment:140
    EndFragment:160
    StartSelection:140
    EndSelection:160
    <!DOCTYPE>
    <HTML>
    <HEAD>
    <TITLE> The HTML Clipboard</TITLE>
    <BASE HREF="https://sample/specs">
    </HEAD>
    <BODY>
    <UL>
    <!--StartFragment -->
    <LI> The Fragment </LI>
    <!--EndFragment -->
    </UL>
    </BODY>
    </HTML>
```



The description includes the clipboard version number and offsets, indicating where the context and the fragment start and end. The description is a list of ASCII text keywords (min/maj is not meaningful) followed by a string and separated by a colon (:).

**Version**: vv version number of the clipboard. Starting version is 0.9.

**StartHTML**: bytecount from the beginning of the clipboard to the start of the context, or -1 if no context.

**EndHTML**: bytecount from the beginning of the clipboard to the end of the context, or -1 if no context.

**StartFragment**: bytecount from the beginning of the clipboard to the start of the fragment.

**EndFragment**: bytecount from the beginning of the clipboard to the end of the fragment.

**StartSelection**: bytecount from the beginning of the clipboard to the start of the selection.

**EndSelection**: bytecount from the beginning of the clipboard to the end of the selection.

The StartSelection and EndSelection keywords are optional and must both be omitted if you do not want the application to generate this information.

Other information of this kind could be added here later, since the HTML starts at the StartHTMLoffset. For example, multiple pairs of StartFragment / EndFragment could be added later to support noncontiguous selection of fragments.

For the convenience of the programs generating the bytecounts, bytecounts could be left padded by zeros. For example, programs generating the bytecounts could arbitrarily affect ten (10) zeros to each keyword (StartHTML: 0000000000) and then, when the exact StartHTML bytecount is known (say, 71), the program can replace the appropriate number of zeros by the bytecount (StartHTML: 0000000071).

The only character set supported by the clipboard is Unicode in its UTF-8 encoding. Because the first characters of UTF-8 and ASCII match, the description is always ASCII, but the bytes of the context (starting at StartHTML) could be using any other characters coded in UTF-8.

End of lines in the clipboard format header could be CR or CR/LF or LF.

The fragment contains pure, valid HTML representing the area the user has selected (to Copy, for example). This contains the selected text plus the opening tags and attributes of any element that has an end tag within the selected text, and end tags at the end of the fragment for any start tag included. This is all information required for basic pasting of an HTML fragment.

The fragment should be preceded and followed by the HTML comments <!--StartFragment--> and <!--EndFragment--> (no space allowed between the !-- and the text) to conveniently indicate where the fragment starts and ends. Thus the start and end of the fragment are indicated by the presence of these comments and by StartFragment and EndFragment byte counts in the description. Tools are expected to produce this information. This redundancy has been introduced to be able to rapidly find the start of the fragment (from the byte count) and mark the position of the fragment directly in the HTML tree.

The selection indicates inside the fragment the exact HTML area the user has selected (to Copy, for example). This adds more information to the fragment by indicating the exact selected text, without the opening tags and end tags that have been added to ensure the fragment is well-formed HTML.

The selection is optional, as sufficient information is included in the fragment for basic pasting. If the selection is not stored, both StartSelection and EndSelection are not stored in the header.

The context is a valid, complete HTML document. This article contains the fragment and all preceding surrounding tags (start and end tags; these preceding surrounding tags represent all the parent nodes of the fragment, until the HTML node). The article also contains the complete HEAD, and allows the BASE and TITLE elements, for example, to be included so this additional information can be obtained. An application copying a fragment of HTML to the clipboard can choose to create a BASE element to include in the context if such an element is not already present so that partial URLs in the fragment can be resolved.

The context is optional, as sufficient information is included in the fragment for basic pasting of an HTML fragment to take place. If the context is not stored, the fragment only is stored and the StartHTML=EndHTML=-1.

## Scenarios

The following scenarios describe how the IE4/MSHTML HTML editor handles HTML cut and paste; other applications may or may not follow these scenarios. The clipboard format described here is intended to allow flexibility for how an application chooses to function. (These scenarios show only good HTML, that is, no overlapping tags.)

1.  Simple Fragment of HTML.
    -   -   HTML text:

            &lt;BODY&gt;This is normal <B>This is bold </B><I><B>This is bold italic </B>This is italic </I>&lt;/BODY&gt;

        -   Appears as:

            This is normal **This is bold**  ***This is bold italic**  This is italic*

        -   The text between the \*\* is selected and copied to the clipboard:

            This is normal **This is** \*\* **bold**   ***This is bold italic**  This*\*\* *is italic*

        -   This is what will be on the clipboard (note this is IE4/MSHTML's interpretation):

            Version:0.9

            StartHTML:71

            EndHTML:160

            StartFragment:130

            EndFragment:150

            **StartSelection:130**

            **EndSelection:150**

            <!DOCTYPE ...>

            &lt;BODY&gt;

            <!-- StartFragment -->>

            **<B>bold</B><I><B>This is bold italic</B>This</I>**

            <!-- EndFragment -->

            &lt;/BODY&gt;

            &lt;/HTML&gt;

        -   In this scenario only the BODY tag and the HTML tag appear in the context as it precedes the selected fragment. Note that start tags and end tags are included in the context. The selection, as delimited by StartSelection and EndSelection, is shown in bold.

2.  Fragment of a table in HTML.
    -   -   HTML text:

            &lt;BODY&gt;<TABLE BORDER><TR><TH ROWSPAN=2>Head1</TH><TD>Item 1</TD><TD>Item 2</TD><TD>Item 3</TD><TD>Item 4</TD></TR><TR><TD>Item 5</TD><TD>Item 6</TD><TD>Item 7</TD><TD>Item 8</TD></TR><TR><TH>Head2</TH><TD>Item 9</TD><TD>Item 10</TD><TD>Item 11</TD><TD>Item 12</TD></TR></TABLE>&lt;/BODY&gt;

        -   Appears as: ><TABLE BORDER><TR><TH ROWSPAN=2>Head1</TH><TD>Item 1</TD><TD>Item 2</TD><TD>Item 3</TD><TD>Item 4</TD></TR><TR><TD>Item 5</TD><TD>Item 6</TD><TD>Item 7</TD><TD>Item 8</TD></TR><TR><TH>Head2</TH><TD>Item 9</TD><TD>Item 10</TD><TD>Item 11</TD><TD>Item 12</TD></TR></TABLE><!\[CDATA\[\]\]>
        -   The Item 6, Item7, Item 10, and Item 11 elements of the table are selected as a block and copied to the clipboard.
        -   This is what will be on the clipboard (note this is IE4/MSHTML's interpretation):

            <!DOCTYPE ...>

            &lt;HTML&gt;&lt;BODY&gt;<TABLE BORDER>

            <!--StartFragment-->

            **<TR><TD>Item 6</TD><TD>Item 7</TD></TR><TR><TD>Item 10</TD><TD>Item 11</TD></TR>**

            <!--EndFragment-->

            </TABLE>

            &lt;/BODY&gt;&lt;/HTML&gt;The selection, as delimited by StartSelection and EndSelection, is shown in bold.

3.  Pasting a fragment of an ordered list into plain text.
    -   -   HTML text:

            &lt;BODY&gt;<OL TYPE = a><LI>Item 1<LI>Item 2<LI>Item 3<LI>Item 4<LI>Item 5<LI>Item 6</OL>&lt;/BODY&gt;

        -   Appears as:
            1.  Item 1
            2.  Item 2
            3.  Item 3
            4.  Item 4
            5.  Item 5
            6.  Item 6
        -   The user selects and copies items 3 through 5 to the clipboard. The following HTML is in the clipboard:

            <DOCTYPE...>&lt;HTML&gt;&lt;BODY&gt;<OL TYPE = a>

            <!-- StartFragment-->

            **<LI>Item 3<LI>Item 4<LI>Item 5**

            <!-- EndFragment-->

            </OL>&lt;/BODY&gt;&lt;/HTML&gt;

            The selection, as delimited by StartSelection and EndSelection, is show in bold.

        -   If this fragment is now pasted into an empty document, the following HTML will be created:

            &lt;BODY&gt;<OL TYPE = a><LI>Item 3<LI>Item 4<LI>Item 5</OL>&lt;/BODY&gt;

        -   Appearing as:
            1.  Item 3
            2.  Item 4
            3.  Item 5

4.  Pasting a partially selected region.
    -   -   HTML text:

            <P> IE4/MSHTML is a WYSIWYG Editor that supports :<UL><LI>Cut<LI>Copy<LI>Paste</UL><P>This is a Great Tool !

        -   Appears as:IE4/MSHTML is a WYSIWYG Editor that supports :
            -   -   Cut
                -   Copy
                -   Paste

        -   The user selects from "WYSIWYG" until "Cop".The following HTML is in the clipboard:

            <DOCTYPE...>&lt;HTML&gt;&lt;BODY&gt;

            <!-- StartFragment-->

            <P>

            **WYSIWYG Editor, which supports**

            **<UL><LI>Cut<LI>Cop**

            </UL>

            <!-- EndFragment-->

            &lt;/BODY&gt;&lt;/HTML&gt;The selection, as delimited by StartSelection and EndSelection, is shown in bold.

     
    -   -   The user selects from "opy" until "Great".

            The following HTML is in the clipboard:

            <DOCTYPE...>&lt;HTML&gt;&lt;BODY&gt;

            <!-- StartFragment-->

            <UL><LI>

            **opy<LI>Paste</UL><P> This is a Great**

            </P>

            <!-- EndFragment-->

            &lt;/BODY&gt;&lt;/HTML&gt;

            The selection, as delimited by StartSelection and EndSelection, is shown in bold.

 

 




