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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# To Use a Script Stream

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




