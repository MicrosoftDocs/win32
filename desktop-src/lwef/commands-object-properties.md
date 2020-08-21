---
title: Commands Object Properties
description: Commands Object Properties
ms.assetid: 889a56b2-0b6d-4df8-a313-7553371e4413
ms.topic: article
ms.date: 05/31/2018
---

# Commands Object Properties

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

The server supports the following properties for the [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection:

-   [**Caption**](caption-property-cmds.md)
-   [**Count**](count-property.md)
-   [**DefaultCommand**](defaultcommand-property.md)
-   [**FontName**](fontname-property.md)
-   [**FontSize**](fontsize-property.md)
-   [**GlobalVoiceCommandsEnabled**](globalvoicecommandsenabled-property.md)
-   [**HelpContextID**](helpcontextid-property.md)
-   [**Visible**](visible-property-cso.md)
-   [**Voice**](voice-property.md)
-   [**VoiceCaption**](voicecaption-property.md)

An entry for the [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection can appear in both the pop-up menu and the Voice Commands Window for a character. To make this entry appear in the pop-up menu, set its [**Caption**](caption-property-cmds.md) property. To include the entry in the Voice Commands Window, set its [**VoiceCaption**](voicecaption-property.md) property. (For backward compatibility, if there is no **VoiceCaption**, the **Caption** setting is used)

The following table summarizes how the properties of a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) object affect the entry's presentation:



| Caption Property                                                                                                                                                                                                                                            | Voice-Caption Property | Voice Property | Visible Property | Appears in Character's Pop-up Menu | Appears in Voice Commands Window |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|----------------|------------------|------------------------------------|----------------------------------|
| Yes                                                                                                                                                                                                                                                         | Yes                    | Yes            | True             | Yes, using Caption                 | Yes, using VoiceCaption          |
| Yes                                                                                                                                                                                                                                                         | Yes                    | No             | True             | Yes, using Caption                 | No                               |
| Yes                                                                                                                                                                                                                                                         | Yes                    | Yes            | False            | No                                 | Yes, using VoiceCaption          |
| Yes                                                                                                                                                                                                                                                         | Yes                    | No             | False            | No                                 | No                               |
| No                                                                                                                                                                                                                                                          | Yes                    | Yes            | True             | No                                 | Yes, using VoiceCaption          |
| No                                                                                                                                                                                                                                                          | Yes                    | Yes            | False            | No                                 | Yes, using VoiceCaption          |
| No                                                                                                                                                                                                                                                          | Yes                    | No             | True             | No                                 | No                               |
| No                                                                                                                                                                                                                                                          | Yes                    | No             | False            | No                                 | No                               |
| Yes                                                                                                                                                                                                                                                         | No1                    | Yes            | True             | Yes, using Caption                 | Yes, using Caption               |
| Yes                                                                                                                                                                                                                                                         | No                     | No             | True             | Yes                                | No                               |
| Yes                                                                                                                                                                                                                                                         | No                     | Yes            | False            | No                                 | Yes, using Caption               |
| Yes                                                                                                                                                                                                                                                         | No                     | No             | False            | No                                 | No                               |
| No                                                                                                                                                                                                                                                          | No                     | Yes            | True             | No                                 | No                               |
| No                                                                                                                                                                                                                                                          | No                     | Yes            | False            | No                                 | No                               |
| No                                                                                                                                                                                                                                                          | No                     | No             | True             | No                                 | No                               |
| No                                                                                                                                                                                                                                                          | No                     | No             | False            | No                                 | No                               |
|  If the property setting is null. In some programming languages, an empty string may not be interpreted as the same as a null string.  The command is still voice-accessible, and appears in the Voice Commands Window as "(command undefined)".<br/> |                        |                |                  |                                    |                                  |



 

 

