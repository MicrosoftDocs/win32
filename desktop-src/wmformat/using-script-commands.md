---
title: Using Script Commands
description: Using Script Commands
ms.assetid: be8a2d22-35cb-4b8d-ad00-e8a45bb85b39
keywords:
- Windows Media Format SDK,script commands
- Advanced Systems Format (ASF),script commands
- ASF (Advanced Systems Format),script commands
- scripts,commands
ms.topic: article
ms.date: 05/31/2018
---

# Using Script Commands

The Windows Media Format SDK supports the use of script commands to communicate application actions in ASF files. Each script command is made up of two strings, the first string is the type of command, the second is the command data. For example, you can use the script type "URL" and pass a valid Internet URL as the command data. When a reading application that supports script commands of type "URL" receives this command, it will open the specified address in a browser window.

The Windows Media Format SDK provides two options for delivering script in ASF files. You can create a script stream or you can include script commands in the header of the file. Script streams are useful because the script commands are delivered in presentation time order. If you use script commands in the file header, your application will need to retrieve all of the script commands before starting playback. You must keep track of the presentation times of script commands and respond to them at the right time.

The following sections describe how to include script commands in an ASF file.



| Section                                                                                                                | Description                                                  |
|------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| [To Use a Script Stream](to-use-a-script-stream.md)                                                                   | Describes how to include script commands in a script stream. |
| [To Add Script Data to the Header](to-add-script-data-to-the-header.md)                                               | Describes how to include script commands in the file header. |
| [Using Script Commands Supported by Windows Media Player](using-script-commands-supported-by-windows-media-player.md) | Describes the script commands used by Windows Media Player.  |



 

> [!Note]  
> In previous versions of the Windows Media Format SDK, script streams were used to open Web addresses corresponding to the content of an ASF file. You can now use Web streams to work with synchronized Web pages. For more information. see [Web Streams](web-streams.md).

 

## Related topics

<dl> <dt>

[**Script Commands**](script-commands.md)
</dt> <dt>

[**Programming Guide**](programming-guide.md)
</dt> </dl>

 

 




