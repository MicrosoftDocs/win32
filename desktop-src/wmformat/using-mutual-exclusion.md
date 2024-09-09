---
title: Using Mutual Exclusion
description: Using Mutual Exclusion
ms.assetid: 7bb161db-a525-4a5e-bf99-5ebdf91457c7
keywords:
- Windows Media Format SDK,mutual exclusion
- mutual exclusion,about
- profiles,mutual exclusion
- streams,mutual exclusion
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using Mutual Exclusion

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can use mutual exclusion objects to specify groups of streams, only one of which will be delivered at a time. Mutual exclusion can be used to handle a variety of scenarios, both native to the SDK and custom.

The following sections describe how to work with different types of mutual exclusion.



| Section                                                                                  | Description                                                                                                       |
|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| [Using Multiple Bit Rate Mutual Exclusion](using-multiple-bit-rate-mutual-exclusion.md) | Describes how to use mutual exclusion to encode one input into multiple streams with different bit rate settings. |
| [Using Custom Mutual Exclusion Types](using-custom-mutual-exclusion-types.md)           | Discusses custom mutual exclusion.                                                                                |



 

## Related topics

<dl> <dt>

[**Working with Profiles**](working-with-profiles.md)
</dt> </dl>

 

 




