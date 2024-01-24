---
description: Forced Key Frame Insertion
ms.assetid: 844e5a01-96db-4a69-9704-f0fdbfee3957
title: Forced Key Frame Insertion (Microsoft Media Foundation)
ms.topic: article
ms.date: 05/31/2018
---

# Forced Key Frame Insertion (Microsoft Media Foundation)

When you configure a video encoder object, you can set a maximum interval for key frames in the encoded content. However, the codec will place key frames within that interval as dictated by the content; the key frame interval is not constant. For some applications, the key frame distance is very important. For example, a video editing application needs key frames at locations that are logical to an editor, like at scene breaks and shot transitions.

Forced key frame insertion is a feature that enables you to request that an input frame be encoded as a key frame. The encoder will try to honor these requests, but the buffer settings (bit rate and buffer window) configured for the encoding session always take precedence.

The video encoder objects implement forced key frame insertion as a response to a data unit extension attached to the input sample. For more information about data unit extensions, see [Using Data Unit Extensions](usingdataunitextensions.md).

The extension data for forced key frame insertion is identified by the following GUID value: **F72A3C6F-6EB4-4EBC-B192-09AD9759E828**. The individual extensions are **BOOL** values. Set the value to **TRUE** to indicate a key frame request.

## Related topics

<dl> <dt>

[Using Data Unit Extensions](usingdataunitextensions.md)
</dt> <dt>

[Working with Video](workingwithvideo.md)
</dt> </dl>

 

 



