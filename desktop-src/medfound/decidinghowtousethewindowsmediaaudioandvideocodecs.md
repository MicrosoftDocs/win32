---
description: Using the Codec and DSP Objects
ms.assetid: ec571d31-6542-421a-8027-d4c61ce00035
title: Using the Codec and DSP Objects
ms.topic: article
ms.date: 05/31/2018
---

# Using the Codec and DSP Objects

There are several ways to use the Windows Media Audio and Video codecs and DSPs to encode, decode, or transform your digital media content. The Windows Media Audio and Video Codec and DSP API is intended for those users who need to configure codec and DSP objects manually or use them outside of the context one of the Windows Media SDKs, such as the Windows Media Format SDK or Media Foundation SDK.

Content creators and end users can use a variety of tools and applications to encode content in Windows Media Audio or Windows Media Video streams. Windows Media Encoder, for example, is specifically designed to make the encoding process easy. Likewise, Windows Media Player is specially designed to work well with digital media data that is encoded in Windows Media formats. For many applications, using the Windows Media Encoder SDK or the Windows Media Player SDK is all that is needed. In particular, these two technologies are good for scenarios that resemble the functionality of the tools they automate.

If you need greater control over the encoding or decoding process, but you still intend to use the Advanced Systems Format (ASF) as a container for your media data, the Windows Media Format SDK might be a good choice. The objects of the Windows Media Format SDK provide a flexible framework for creating ASF files, and provide built-in support for the Windows Media Audio and Video codecs.

The Media Foundation SDK, which is new for Windows Vista, greatly simplifies encoding and decoding by providing a customizable media pipeline. You can set input and output media properties and the Media Foundation topology loader will configure the necessary codecs and DSPs for you.

The primary reason for using the codec objects directly is to use the Windows Media Audio and Video codecs outside of the ASF container. Using the codec and DSP objects also provides a level of control that is unavailable using any of the more abstracted technologies.

## Related topics

<dl> <dt>

[Windows Media Codecs](windows-media-codecs.md)
</dt> </dl>

 

 



