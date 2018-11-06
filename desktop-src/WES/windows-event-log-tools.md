---
title: Windows Event Log Tools
description: Windows Event Log provides the following tools that you use to build your provider.
ms.assetid: 20087fdf-3e9f-4090-8103-5864f1c9753c
ms.topic: article
ms.date: 05/31/2018
---

# Windows Event Log Tools

Windows Event Log provides the following tools that you use to build your provider.



| Tool                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Message Compiler (MC.exe)**](message-compiler--mc-exe-.md) | A command line utility used to compile instrumentation manifests and message text files.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                |
| WevtUtil.exe                                                   | A command line utility used primarily to register your provider on the computer. You can also use it to get metadata information about the provider, its events, and the channels to which it logs events, and to query events from a channel or log file. The WevtUtil.exe tool is included in %windir%\\System32. For usage information, enter "wevtutil /?" at a command prompt.<br/> This command is limited to members of the Administrators group and must be run with elevated privileges.<br/> |
| ECManGen.exe                                                   | A GUI that guides you through creating a manifest from scratch without ever having to use XML tags. Having knowledge of the information in the [Writing an Instrumentation Manifest](writing-an-instrumentation-manifest.md) and [EventManifest Schema](eventmanifestschema-schema.md) sections will help when using the tool. The tool is included in the \\Bin folder of the Windows SDK.<br/>                                                                                                           |



 

 

 





