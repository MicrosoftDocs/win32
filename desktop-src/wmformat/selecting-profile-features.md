---
title: Selecting Profile Features
description: Selecting Profile Features
ms.assetid: 5e09000d-1417-43aa-9e9c-0aff536d52b7
keywords:
- profiles,feature selection
- profiles,selecting features
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Selecting Profile Features

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following table lists the profile features and describes when you would or would not want to use them.



| Feature                            | When to use                                                                                                                                                                                                                                                                                                                | When not to use                                                                                                                                                                                                                                                                    |
|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Mutual exclusion by bit rate (MBR) | The file will be streamed to an audience with connection speeds that vary from user to user (for example, files delivered over the Internet).                                                                                                                                                                              | The file will not be streamed over a network.The file will be streamed over a network with a consistently reliable available bandwidth (for example, files delivered over a corporate local area network).<br/>                                                              |
| Mutual exclusion by language       | The file contains streams that duplicate the same data in different languages. (For example, a movie dubbed in several languages would have the soundtrack encoded as mutually exclusive streams.)                                                                                                                         | The file contains only streams in a single language.If the file contains only streams that must be changed for individual languages, it may be simpler to create a new file for each language (for example, for a training film with lots of text in the video stream).<br/> |
| Mutual exclusion by presentation   | You want to provide video in more than one aspect ratio. For example, a file might contain the same video formatted for television and for the original theatrical wide-screen format.                                                                                                                                     | There is only one version of each video stream.                                                                                                                                                                                                                                    |
| Bandwidth sharing                  | The file will be streamed and has two or more streams that, when combined, use less available bandwidth than the bit rate values of both streams added together. Because the bit rate of a stream is essentially the maximum required bandwidth for the stream, some streams may have some periods of lower data transfer. | The file will not be streamed over a network.All streams have consistent bit rates.<br/>                                                                                                                                                                                     |
| Stream prioritization              | The file will be streamed and some streams are more important than others.                                                                                                                                                                                                                                                 | The file will not be streamed over a network.All streams are of equal importance.<br/>                                                                                                                                                                                       |
| Data Unit Extensions               | There is important information related to the samples in a stream that must be kept with the samples.                                                                                                                                                                                                                      | The file is intended for delivery through a restricted bandwidth. In this case, data unit extensions may use too much overhead.                                                                                                                                                    |



 

It is also important to consider the codec features that you want to use with your file when creating a profile. For more information see [Codec Features](codec-features.md).

## Related topics

<dl> <dt>

[**ASF File Features**](asf-file-features.md)
</dt> <dt>

[**Designing Profiles**](designing-profiles.md)
</dt> </dl>

 

 





