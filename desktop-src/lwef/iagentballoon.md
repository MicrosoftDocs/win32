---
title: IAgentBalloon
description: IAgentBalloon
ms.assetid: 94a48cd9-bea5-4993-8991-50c6c86a646b
ms.topic: article
ms.date: 05/31/2018
---

# IAgentBalloon

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

**IAgentBalloon** defines an interface that allows applications to query properties for the Microsoft Agent word balloon. These functions are also available from [**IAgentBalloonEx**](https://www.bing.com/search?q=**IAgentBalloonEx**).

Initial defaults for a character's word balloon are set in the Microsoft Agent Character Editor, but once the application is running, the user may override the [**Enabled**](enabled-property.md) and [Font](fontname-property.md) properties. If a user changes the balloon's properties, the change affects all characters. The [**IAgentBalloon**](/windows/desktop/lwef/iagentballoon) object's properties also apply to text output through the [**Think**](think-method.md) method.

**Methods in Vtable Order**



| IAgentBalloon Methods                                       | Description                                                                           |
|-------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [GetEnabled](iagentballoon--getenabled.md)                 | Returns whether the word balloon is enabled.                                          |
| [GetNumLines](iagentballoon--getnumlines.md)               | Returns the number of lines displayed in the word balloon.                            |
| [GetNumCharsPerLine](iagentballoon--getnumcharsperline.md) | Returns the average number of characters per line displayed in the word balloon.      |
| [GetFontName](iagentballoon--getfontname.md)               | Returns the name of the font displayed in the word balloon.                           |
| [GetFontSize](iagentballoon--getfontsize.md)               | Returns the size of the font displayed in the word balloon.                           |
| [GetFontBold](iagentballoon--getfontbold.md)               | Returns whether the font displayed in the word balloon is bold.                       |
| [GetFontItalic](iagentballoon--getfontitalic.md)           | Returns whether the font displayed in the word balloon is italic.                     |
| [GetFontStrikethru](iagentballoon--getfontstrikethru.md)   | Returns whether the font displayed in the word balloon is displayed as strikethrough. |
| [GetFontUnderline](iagentballoon--getfontunderline.md)     | Returns whether the font displayed in the word balloon is underlined.                 |
| [GetForeColor](iagentballoon--getforecolor.md)             | Returns the foreground color displayed in the word balloon.                           |
| [GetBackColor](iagentballoon--getbackcolor.md)             | Returns the background color displayed in the word balloon.                           |
| [GetBorderColor](iagentballoon--getbordercolor.md)         | Returns the border color displayed in the word balloon.                               |
| [SetVisible](iagentballoon--setvisible.md)                 | Sets the word balloon to be visible.                                                  |
| [GetVisible](iagentballoon--getvisible.md)                 | Returns the visibility setting for the word balloon.                                  |
| [SetFontName](iagentballoon--setfontname.md)               | Sets the font used in the word balloon.                                               |
| [SetFontSize](iagentballoon--setfontsize.md)               | Sets the font size used in the word balloon.                                          |
| [SetFontCharSet](iagentballoon--setfontcharset.md)         | Sets the character set used in the word balloon.                                      |
| [GetFontCharSet](iagentballoon--getfontcharset.md)         | Returns the character set used in the word balloon.                                   |



 

 

 