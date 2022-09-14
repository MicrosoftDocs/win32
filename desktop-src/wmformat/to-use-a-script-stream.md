---
title: To Use a Script Stream
description: To Use a Script Stream
ms.assetid: 502b1f66-213d-41d8-992a-9bef4f6209f9
keywords:
- Windows Media Format SDK,script streams
- Advanced Systems Format (ASF),script streams
- ASF (Advanced Systems Format),script streams
- script streams,about
ms.topic: article
ms.date: 05/31/2018
---

# To Use a Script Stream

This section describes how to send script data to the writer for inclusion in a file. For information about including script streams in profiles, see [Configuring Arbitrary Stream Types](configuring-arbitrary-stream-types.md).

Each script consists of two strings, a *type* string and an *argument* string.

The script data must be formatted before it is sent to the writer. The strings should be concatenated, separated by a **NULL** character, and terminated with a **NULL** character. The following example shows a legitimate script:



| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |   &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp;  | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp;  | &nbsp; |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| U   | R   | L   | &nbsp; | h   | t   | t   | p   | :   | /   | /   | w   | w   | w   | .   | a   | d   | a   | t   | u   | m   | .   | c   | o   | m   | &nbsp; |



 

Each pair of script commands should be written as a sample to the writer. For more information about writing samples, see [To Write Samples](to-write-samples.md).

When the ASF file is played, the script commands will be delivered by the reader (or synchronous reader) in presentation time order. It is the responsibility of the application to parse the two strings and respond to the script command.

> [!Note]  
> When using DRM to encrypt a file, no script command can have a presentation time of 0.

 

## Related topics

<dl> <dt>

[**Using Script Commands**](using-script-commands.md)
</dt> </dl>

 

 




