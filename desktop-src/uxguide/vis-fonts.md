---
title: Fonts
description: Users interact with text more than with any other element in Microsoft Windows. Segoe UI (pronounced \ 0034;SEE-go \ 0034;) is the Windows system font. The standard font size has been increased to 9 point.
ms.assetid: 6d4f669d-d28c-4585-9bc3-ecda44de6df5
ms.topic: article
ms.date: 10/20/2020
---

# Fonts

> [!NOTE]
> This design guide was created for Windows 7 and has not been updated for newer versions of Windows. Much of the guidance still applies in principle, but the presentation and examples do not reflect our [current design guidance](/windows/uwp/design/).

Users interact with text more than with any other element in Microsoft Windows. Segoe UI (pronounced "SEE-go") is the Windows system font. The standard font size has been increased to 9 point.

![illustration of alphabet in segoe ui font ](images/vis-fonts-image1.png)

The Segoe UI font.

Segoe UI and Segoe are not the same font. Segoe UI is the Windows font intended for user interface text strings. Segoe is a branding font used by Microsoft and partners to produce material for print and advertising.

Segoe UI is an approachable, open, and friendly typeface, and as a result has better readability than Tahoma, Microsoft Sans Serif, and Arial. It has the characteristics of a humanist sans serif: the varying widths of its capitals (narrow E and S, for instance, compared with Helvetica, where the widths are more alike, fairly wide); the stress and letterforms of its lowercase; and its true italic (rather than an "oblique" or slanted roman, like many industrial-looking sans serifs). The typeface is meant to give the same visual effect on screen and in print. It was designed to be a humanist sans serif with no strong character or distracting quirkiness.

Segoe UI is optimized for ClearType, which is on by default in Windows. With ClearType enabled, Segoe UI is an elegant, readable font. Without ClearType enabled, Segoe UI is only marginally acceptable. This factor determines when you should use Segoe UI.

Segoe UI includes Latin, Greek, Cyrillic, and Arabic characters. There are new fonts, also optimized for ClearType, created for other character sets and uses. These include Meiryo for Japanese, Malgun Gothic for Korean, Microsoft JhengHei for Chinese (Traditional), Microsoft YaHei for Chinese (Simplified), Gisha for Hebrew, and Leelawadee for Thai, and the ClearType Collection fonts designed for document use.

Meiryo includes Latin characters based on Verdana. Malgun Gothic, Microsoft JhengHei, and Microsoft YaHei use a customized Segoe UI. Use of italic versions of these fonts is not recommended. Malgun Gothic, Microsoft JhengHei, and Microsoft YaHei are supplied in regular and bold styles only, meaning italic characters are synthesized by slanting the upright styles. Although Meiryo includes true italic and bold italics, these styles only apply to the Latin characters the Japanese characters remain upright when italic styling is applied.

A variation of Meiryo, called Meiryo UI, is preferred in the [ribbons](cmd-ribbons.md) command user interface.

To support locales using these character sets, Segoe UI is replaced with the correct fonts depending on each locale during the [localization](glossary.md) process.

To license Segoe UI and other Microsoft fonts for distribution with a Windows-based program, contact [Monotype](https://www.monotype.com/).

**Note:** Guidelines related to [style and tone](text-style-tone.md) and [user interface text](text-ui.md) are presented in separate articles.

## Design concepts

### Fonts, typefaces, point sizes, and attributes

In traditional typography, a font describes a combination of a typeface, a point size, and attributes. A typeface is the look of the font. Segoe UI, Tahoma, Verdana, and Arial are all typefaces. Point size refers to the size of the font, measured from the top of the ascenders to the bottom of the descenders, minus the internal spacing (called leading). A point is roughly 1/72 inch. Finally, a font can have attributes of bold or italic.

Informally, people often use font in place of typeface as done in this article but technically, Segoe UI is a typeface, not a font. Each combination of attributes is a unique font (for example, 9 point Segoe UI regular, 10 point Segoe UI bold, and so on).

### Serif and sans serif

Typefaces are either serif or sans serif. Serif refers to small turns that often finish the strokes of letters in a font. A sans serif typeface doesn't have serifs.

Readers generally prefer serif fonts used as body text within a document. The serifs provide a feeling of formality and elegance to a document. For UI text, the need for a clean appearance and the lower resolution of computer monitors makes sans serif typefaces the better choice.

### Contrast

Text is easiest to read when there is a large difference between the luminance of the text and the background. Black text on a white background gives the highest contrast dark text on a very light background can provide high contrast as well. This combination is best for primary UI surfaces.

Light text on a dark background offers good contrast, but not as good as dark text on a light background. This combination works well for secondary UI surfaces, such as Explorer task panes, that you want to de-emphasize relative to the primary UI surfaces.

**If you want to make sure users read your text, use dark text on a light background.**

### Affordances

Text can use the following [affordances](glossary.md) to indicate how it is used:

-   **Pointer.** The I-bar ("text select") pointer indicates that the text is selectable, whereas the left-pointing arrow ("normal select") pointer indicates that text isn't.
-   **Caret.** When text has input focus, the caret is the flashing vertical bar that indicates the insertion/selection point in selectable or editable text.
-   **Box.** A box around text that indicates that it's editable. To reduce the weight of the presentation, the box may be displayed dynamically only when the editable text is selected.
-   **Foreground color.** Light gray indicates that text is disabled. Non-gray colors, especially blue and purple, indicate that text is a link.
-   **Background color.** A light gray background weakly suggests that text is read-only, but in practice read-only text can have any color background.

These affordances are combined for the following meanings:

-   **Editable.** Text displayed in a box, with a text select pointer, a caret (on input focus), and usually on a white background.
-   **Read-only, selectable.** Text with a select pointer and a caret (on input focus).
-   **Read-only, non-selectable.** Text with an arrow pointer.
-   **Disabled.** Light gray text with an arrow pointer, sometimes on a gray background.

Read-only text traditionally has a gray background, but a gray background isn't necessary. In fact, a gray background can be undesirable, especially for large blocks of text, because it suggests that the text is disabled and discourages reading.

### Accessibility and the system font, sizes, and colors

The guidelines for making text accessible to users with disabilities or impairments can be boiled down to one simple rule: Respect the user's settings by always using the system font, sizes, and colors.

**If you do only one thing...**

Respect the user's settings by always using the system font, sizes, and colors.

**Developers:** From code, you can determine the system font properties (including its size) using the GetThemeFont API function. You can determine the system colors using the GetThemeSysColor API function.

Because you can't make any assumptions about users' system theme settings, you should:

-   Always base your font colors and backgrounds off system theme colors. Never make your own colors based on fixed RGB (red, green, blue) values.
-   Always match system text colors with their corresponding background colors. For example, if you choose COLOR\_STATICTEXT for the text color, you must also choose COLOR\_STATIC for the background color.
-   Always create new fonts based on proportional-sized variations of the system font. Given the system font metrics, you can create bold, italic, larger, and smaller variations.

**A simple way to ensure that your program respects users' settings is to test using a different font size and a high contrast color scheme.** All text should resize and display correctly in the chosen color scheme.

## Usage patterns

Text has several usage patterns:



|    Usage                                         |    Description                            |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Title bar text**<br/> Text on the title bar that identifies the window.<br/>                                                                                                                                                                | ![example of title-bar text font ](images/vis-fonts-image2.png)<br/>                                                                            |
| **Main instructions**<br/> Text that explains what to do on a page, window, or dialog box. <br/>                                                                                                                                              | ![example of main-instructions text font ](images/vis-fonts-image3.png)<br/>                                                                    |
| **Secondary instructions**<br/> Supplemental text that explains what to do on a page, window, or dialog box. <br/>                                                                                                                            | ![example of secondary-instructions text font ](images/vis-fonts-image4.png)<br/>                                                               |
| **Normal text**<br/> Ordinary (read-only) text displayed in a user interface. <br/>                                                                                                                                                           | ![example of normal text font ](images/vis-fonts-image5.png)<br/>                                                                               |
| **Emphasized text**<br/> Bold text is used to make the text easier to parse and to draw attention to text users must read. italic text is used to refer to text literally (instead of quotation marks) and to emphasize specific words. <br/> | ![example of emphasized text font ](images/vis-fonts-image6.png)<br/>                                                                           |
| **Editable text**<br/> Text that users can edit is shown in a box. to reduce the weight of the presentation, the box may be displayed only when the editable text is selected. <br/>                                                          | ![example of editable text font ](images/vis-fonts-image7.png)<br/>                                                                             |
| **Disabled text**<br/> Text that doesn't apply to the current context, such as labels for disabled controls. disabled text indicates that users (normally) shouldn't bother reading the text. <br/>                                           | ![example of disabled text font ](images/vis-fonts-image8.png)<br/>                                                                             |
| **Links**<br/> Text used to navigate to another page, window, or help topic, or initiate a command. <br/>                                                                                                                                     | ![example of link text font ](images/vis-fonts-image9.png)<br/> ![example of links (hover) text font ](images/vis-fonts-image10.png)<br/> |
| **Group header**<br/> Text used to group items in a list view. <br/>                                                                                                                                                                          | ![example of group-header text font ](images/vis-fonts-image11.png)<br/>                                                                        |
| **File name**<br/> File name text (in content view only). <br/>                                                                                                                                                                               | ![example of file name (in content view) text font ](images/vis-fonts-image12.png)<br/>                                                         |
| **Document text**<br/> Text used in documents (as opposed to ui text). <br/>                                                                                                                                                                  | ![example of document text font ](images/vis-fonts-image13.png)<br/>                                                                            |
| **Document headings**<br/> Text used as a heading within a document. <br/>                                                                                                                                                                    | ![example of document headings text font ](images/vis-fonts-image14.png)<br/>                                                                   |



 

## Guidelines

### Fonts and colors

-   **The following fonts and colors are defaults for Windows Vista and Windows 7.**



| Pattern | Theme symbol | Font, Color |
|-----------------------------------------------------------------------------------------------|-----------------------------|------------------------------------------------------------|
| ![example of title-bar text font ](images/vis-fonts-image2.png)<br/>                    | CaptionFont<br/>      | 9 pt. black (\#000000) Segoe UI<br/>                 |
| ![example of main-instructions text font ](images/vis-fonts-image3.png)<br/>            | MainInstruction<br/>  | 12 pt. blue (\#003399) Segoe UI<br/>                 |
| ![example of secondary-instructions text font ](images/vis-fonts-image4.png)<br/>       | Instruction<br/>      | 9 pt. black (\#000000) Segoe UI<br/>                 |
| ![example of normal text font ](images/vis-fonts-image5.png)<br/>                       | BodyText<br/>         | 9 pt. black (\#000000) Segoe UI<br/>                 |
| ![example of emphasized text font ](images/vis-fonts-image6.png)<br/>                   | BodyText<br/>         | 9 pt. black (\#000000) Segoe UI, bold or italic<br/> |
| ![example of editable text font ](images/vis-fonts-image7.png)<br/>                     | BodyText<br/>         | 9 pt. black (\#000000) Segoe UI, in a box<br/>       |
| ![example of disabled text font ](images/vis-fonts-image8.png)<br/>                     | Disabled<br/>         | 9 pt. dark gray (\#323232) Segoe UI<br/>             |
| ![example of link text font ](images/vis-fonts-image9.png)<br/>                         | HyperLinkText<br/>    | 9 pt. blue (\#0066CC) Segoe UI<br/>                  |
| ![example of links (hover) text font ](images/vis-fonts-image10.png)<br/>               | Hot<br/>              | 9 pt. light blue (\#3399FF) Segoe UI<br/>            |
| ![example of group-header text font ](images/vis-fonts-image11.png)<br/>                |                             | 11 pt. blue (\#003399) Segoe UI<br/>                 |
| ![example of file name (in content view) text font ](images/vis-fonts-image12.png)<br/> |                             | 11 pt. black (\#000000) Segoe UI<br/>                |
| ![example of document text font ](images/vis-fonts-image13.png)<br/>                    | (none)<br/>           | 9 pt. black (\#000000) Calibri<br/>                  |
| ![example of document headings text font ](images/vis-fonts-image14.png)<br/>           | (none)<br/>           | 17 pt. black (\#000000) Calibri<br/>                 |



 

-   **Choose fonts and optimize window layouts based on the UI technology and the target version of Windows:**



| UI technology | Target Windows version | Fonts to use and optimize for |
|--------------------------------------------|-------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows Presentation Foundation<br/> | All<br/>                                        | Use WPF theme parts.<br/>                                                                                                                                                                                                                                                                                                                                  |
| Win32 or WinForms<br/>               | Windows Vista or later<br/>                     | Use the appropriate Segoe UI font.<br/>                                                                                                                                                                                                                                                                                                                    |
|                                            | Extensible components or pre-Windows Vista<br/> | To target Windows XP and Windows 2000, use the 8 point MS Shell Dlg 2 pseudo font, which maps to Tahoma.<br/> To target earlier versions of Windows, use 8 point MS Shell Dlg pseudo font, which maps to Tahoma on Windows 2000 and Windows XP, and to MS Sans Serif on Windows 95, Windows 98, Windows Millennium Edition, and Windows NT 4.0.<br/> |



 

-   **Developers:**
    -   For elements that use fixed layout (such as Windows dialog templates and WinForms), hard code the appropriate font from the preceding table.
    -   For elements that use dynamic layout (such as Windows Presentation Foundation), use the theme fonts. Use theme APIs like DrawThemeText to draw text based on the theme symbol. Be sure to have an alternative based on system metrics in case the theme service isn't running.
-   **For Segoe UI, use a 9 point font size or larger.** The Segoe UI font is optimized for these sizes, so avoid using smaller sizes.
-   **Always match system text colors with their corresponding background colors.** For example, if you choose COLOR\_STATICTEXT for the text color, you must also choose COLOR\_STATIC for the background color.
-   **Always create new fonts based on proportional-sized variations of the system font.** Given the system font metrics, you can create bold, italic, larger, and smaller variations.
-   Display large blocks of read-only text (such as license terms) against a light background instead of a gray background. Gray backgrounds suggest that the text is disabled and discourages reading.
-   **Consider a maximum line length of 65 characters** to make the text easy to read. (Characters include letters, punctuation, and spaces.)

### Attributes

-   Most UI text should be plain without any attributes. Attributes may be used as follows:
    -   **Bold.** Use in control labels to make the text easier to parse. Use sparingly to draw attention to text users must read. Using too much bold lessens its impact.
    -   **Italic.** Use to refer to text literally instead of quotation marks. Use sparingly to emphasize specific words. Use for [prompts](glossary.md) in [text boxes](ctrl-text-boxes.md) and [editable drop-down lists](/windows/desktop/uxguide/ctrl-drop).
    -   **Bold italic.** Don't use.
    -   **Underline.** Don't use except for links. Use italic instead for emphasis.
-   Not all fonts support bold and italic, so they should never be crucial to understanding the text.

