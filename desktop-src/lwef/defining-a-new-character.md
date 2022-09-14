---
title: Defining a New Character
description: Defining a New Character
ms.assetid: 4102cb7d-2fec-45d2-882a-04704c7f5a48
ms.topic: article
ms.date: 05/31/2018
---

# Defining a New Character

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

To define a new character, run the Agent Character Editor. If you have an existing character file loaded, choose the **New** command from the **File** menu. This displays a submenu of choices. If you creating a character for your own use, choose **Custom Character**. If you want to create a character that can be used as an Agent default character, choose **Default Character**. This will pre-configure the editor with all the required animation names and animation state assignments as well as set the **Supports Standard Animation Set** option. Similarly, if you choose Office Assistant Character, the editor is pre-configured with the animation names and animation state assignment required for an Office Assistant character. This action selects the **Character** icon in the tree and displays its property pages on the right side of the window. The following sections describe how to set your character's properties and how to create animations for the character.

### Setting Your Character's General Information

To begin defining a character, enter the character's name in the **Name** text box (32 characters maximum). Because Microsoft Agent uses the name to allow users to access the character, specify a user-friendly name. Supply a name that can be pronounced using conventional spelling, or you may disable speech input for the character. You can also specify a short optional description (256 characters) for your character in the Description text box. The server exposes what you enter in the Description text box to client applications.

You can also store your own data as part of your character using the ExtraData field. You can use this capability to include special information about your character or other data. Once compiled with the Character Editor, this information can be accessed using the ExtraData property at run time when the character is loaded.

You can set the character's name, description, and extra data information based on the character's language ID setting. To set this data for another language, select Language and enter the text. You also must have the language codepages installed on the system you build the character file. If you don't the appropriate language settings will not be included in the compiled character file. You do not have to provide information in other languages. If these properties are queried at runtime using the Agent API and there are no specific settings for that language, the English (Default) settings are returned.

### Setting Your Character's Output Options

If you set the Supports Standard Animation Set option, the Character Editor will check to make certain that you have included all the required animations and animation state assignments for a default character when you attempt to build the character. If something is missing, a message box will list the missing elements. For details on the standard animation set, see [**Designing Characters for Microsoft Agent**](designing-characters-for-microsoft-agent.md).

For your character's spoken output, Microsoft Agent provides the choice of a synthesized, text-to-speech (TTS) voice or a voice that uses recorded sound files. If you want to use a synthesized voice, check the Use Synthesized Speech For Voice Output option. This will add a Voice page for selecting the characteristics of the voice. Choose the Voice page and use the controls on it page to select a voice, speed, and pitch of any compatible TTS engines you have installed. The range of the voice parameters you can select depends on TTS engines. If you have not yet installed a TTS engine, the Voice ID list will be empty. You must have a TTS engine installed before you define your character's voice settings in the Agent Character Editor.

If you plan to use a TTS engine for your character's output you must also install that engine on the user's system. If you select a voice based on a particular TTS engine, but the user has a different TTS engine installed, the server attempts to match the voice based on the characteristics you defined in the Agent Character Editor.

If you plan to use recorded sound files (.WAV files) for your character's spoken output, you do not need to check the Use Synthesized Speech For Voice Output option. Instead, you will need to record the spoken output audio files separately and load them from your application code.

The Use **Word Balloon** option enables you to determine whether you want to support a word balloon for your character. This feature can also be set at run time.

When the **Use Word Balloon** option is checked, you can access the **Word Balloon** page. The options on the **Word Balloon** page enable you to change the default characteristics of your word balloon. The **Characters Per Line** setting enables you to define the width of the balloon based on the average number of characters per line. You can set the default height based on either a fixed number of lines you want to display at once or automatically sized to the text you supply in the [**Speak**](speak-method.md) method. You can also set whether the balloon automatically hides after a **Speak** method is completed and whether the balloon automatically displays or "paces" words to the character's speech output speed setting.

The **Word Balloon** page also enables you to set the default font for the character's word balloon and the balloon's display colors. However, be aware that users can override your word balloon font settings using the Microsoft Agent property sheet.

### Setting Your Character's Identifier

Each character requires a unique identifier (GUID). The server uses the identifier to differentiate characters. When you create a new character, the Editor automatically creates a new identifier for your character. You need to change a character's identifier only if you copied the character definition file of another character or if you intentionally want to differentiate a character from a former version. To change a character's identifier, click the New GUID button and the Editor will generate a new identifier.

 

 




