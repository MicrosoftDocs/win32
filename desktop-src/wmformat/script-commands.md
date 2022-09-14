---
title: Script Commands
description: Script Commands
ms.assetid: b8d7d4d3-c0d3-4b09-b5dd-1c6bbc3f2020
keywords:
- Windows Media Format SDK,script commands
- Advanced Systems Format (ASF),script commands
- ASF (Advanced Systems Format),script commands
- Windows Media Format SDK,script streams
- Advanced Systems Format (ASF),script streams
- ASF (Advanced Systems Format),script streams
- Windows Media Format SDK,streams
- Advanced Systems Format (ASF),streams
- ASF (Advanced Systems Format),streams
- scripts,commands
- scripts,streams
ms.topic: article
ms.date: 05/31/2018
---

# Script Commands

The script commands supported by the Windows Media Format SDK are simple name and value string pairs. For example, a common script command is "URL", which is used by Windows Media Player and other playing applications to open Web pages. The other half of the script pair for "URL" command contains a valid uniform resource locator (URL), such as `https://www.adatum.com`. No support is provided by the objects of this SDK for any specific commands; your application must include logic to handle whatever commands you use. You can use the commands supported by Windows Media Player to maintain compatibility with most players.

Script commands can be delivered in one of two ways: in a script stream or in the file header.

## Script Streams

You can deliver script commands in their own stream in an ASF file. Each sample in a script stream contains the two strings of the name/value pair. The advantage of using a script stream is that the commands will be delivered at the correct presentation time.

## Script Commands in the File Header

Script commands can be included in the file header for retrieval at the time of playback. The playing application is responsible for executing the script commands at the proper time. The advantage of using script commands in the file header is that all of the script commands are available before beginning to receive samples.

## Related topics

<dl> <dt>

[**ASF File Features**](asf-file-features.md)
</dt> <dt>

[**Using Script Commands**](using-script-commands.md)
</dt> </dl>

 

 




