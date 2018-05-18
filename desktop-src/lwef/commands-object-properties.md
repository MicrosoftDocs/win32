---
title: Commands Object Properties
description: Commands Object Properties
ms.assetid: '889a56b2-0b6d-4df8-a313-7553371e4413'
---

# Commands Object Properties

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

The server supports the following properties for the [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms695971) collection:

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

An entry for the [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms695971) collection can appear in both the pop-up menu and the Voice Commands Window for a character. To make this entry appear in the pop-up menu, set its [**Caption**](caption-property-cmds.md) property. To include the entry in the Voice Commands Window, set its [**VoiceCaption**](voicecaption-property.md) property. (For backward compatibility, if there is no **VoiceCaption**, the **Caption** setting is used)

The following table summarizes how the properties of a [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms695971) object affect the entry's presentation:



| Caption Property                                                                                                                                                                                                                                            | Voice-Caption Property | Voice Property | Visible Property | Appears in Character's Pop-up Menu | Appears in Voice Commands Window |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|----------------|------------------|------------------------------------|----------------------------------|
| Yes                                                                                                                                                                                                                                                         | Yes                    | Yes            | True             | Yes, using Caption                 | Yes, using VoiceCaption          |
| Yes                                                                                                                                                                                                                                                         | Yes                    | No¹            | True             | Yes, using Caption                 | No                               |
| Yes                                                                                                                                                                                                                                                         | Yes                    | Yes            | False            | No                                 | Yes, using VoiceCaption          |
| Yes                                                                                                                                                                                                                                                         | Yes                    | No¹            | False            | No                                 | No                               |
| No¹                                                                                                                                                                                                                                                         | Yes                    | Yes            | True             | No                                 | Yes, using VoiceCaption          |
| No¹                                                                                                                                                                                                                                                         | Yes                    | Yes            | False            | No                                 | Yes, using VoiceCaption          |
| No¹                                                                                                                                                                                                                                                         | Yes                    | No¹            | True             | No                                 | No                               |
| No¹                                                                                                                                                                                                                                                         | Yes                    | No¹            | False            | No                                 | No                               |
| Yes                                                                                                                                                                                                                                                         | No1                    | Yes            | True             | Yes, using Caption                 | Yes, using Caption               |
| Yes                                                                                                                                                                                                                                                         | No¹                    | No¹            | True             | Yes                                | No                               |
| Yes                                                                                                                                                                                                                                                         | No¹                    | Yes            | False            | No                                 | Yes, using Caption               |
| Yes                                                                                                                                                                                                                                                         | No¹                    | No¹            | False            | No                                 | No                               |
| No¹                                                                                                                                                                                                                                                         | No¹                    | Yes            | True             | No                                 | No²                              |
| No¹                                                                                                                                                                                                                                                         | No¹                    | Yes            | False            | No                                 | No²                              |
| No¹                                                                                                                                                                                                                                                         | No¹                    | No¹            | True             | No                                 | No                               |
| No¹                                                                                                                                                                                                                                                         | No¹                    | No¹            | False            | No                                 | No                               |
| ¹If the property setting is null. In some programming languages, an empty string may not be interpreted as the same as a null string. ²The command is still voice-accessible, and appears in the Voice Commands Window as "(command undefined)".<br/> |                        |                |                  |                                    |                                  |



 

 

 





