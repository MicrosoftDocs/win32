---
description: This topic contains programming information. The following list identifies some programming tips to help you write a parser.
ms.assetid: 24d3e11f-8281-4464-a2d7-f4f2466e9d9e
title: Programming Considerations (Network Monitor)
ms.topic: article
ms.date: 05/31/2018
---

# Programming Considerations (Network Monitor)

This topic contains programming information. The following list identifies some programming tips to help you write a parser.



| Tip                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                          |
|-------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Auto-installing your parser                     | Implement the [**ParserAutoInstallInfo**](parserautoinstallinfo.md) function to automatically install your parser, and update the associated INI files. If you install your parser manually, you must update all associated INI files manually.                                                                                                                                                          |
| Parsing protocol properties                     | Implement the [**AttachProperties**](attachproperties.md) function to parse the protocol properties. Avoid using the [**AttachPropertyInstanceEx**](attachpropertyinstanceex.md) function when you attach a property instance, and use it for only non byte-aligned data, or data that must be decoded. Attaching properties refers to mapping a property instance to a specific location in a capture. |
| Parsing protocols that are split between frames | Assume that each piece of the protocol is complete within a frame, and assume that the user calls the Protocol Coalesce tool to combine the pieces into one protocol. Do not look back at a previous frame when parsing a protocol, and avoid trying to reconstruct a protocol that is split between frames.                                                                                              |
| Formatting displayed data                       | Call the [**FormatPropertyInstance**](formatpropertyinstance.md) function to use the generic formatter to format the data displayed in the details pane of the Network Monitor UI. Avoid writing a custom formatter for UI display data. However, you can call a custom formatter to create a [*summary property*](s.md) line for the protocol you are parsing.            |
| Using CCAlloc                                   | Use CCAlloc when you want Network Monitor to allocate data on a per-capture basis. Network Monitor does not specify the order that frames call the parser.                                                                                                                                                                                                                                                |
| Keeping a parser stateless                      | Keep parser operation stateless because when Network Monitor parses a capture, it does not pass the frames to the parser in a specific order. For this reason, it is recommended that you do not retain global data.                                                                                                                                                                                      |



 

 

 



