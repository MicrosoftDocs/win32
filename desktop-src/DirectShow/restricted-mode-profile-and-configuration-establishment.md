---
description: Restricted Mode Profile and Configuration Establishment
ms.assetid: 550f5413-eaa4-4530-867e-fd9b1907cadf
title: Restricted Mode Profile and Configuration Establishment
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Restricted Mode Profile and Configuration Establishment

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Due to the variety of types of data that can be decoded by DirectX VA, and the multiple decoding configurations supported within DirectX VA for each of these types of data (for example, using bitstream buffers versus host residual difference decoding versus accelerator-based IDCT with and without encryption of each relevant type of buffer, and so on), we believe it would be somewhat ungainly to simply specify a unique GUID for every unique data type and decoding configuration. This would create a large number of GUIDs (for example, hypothetically if there were 16 profiles of DirectX VA and 16 configurations possible for each, there would need to be 256 defined GUIDs—requiring 4 kilobytes of memory just to hold them all. This issue is the most difficult part of determining how to map DirectX VA into **IAMVideoAccelerator**, with the remainder of the operational definition mostly being quite straightforward. As a result, we specify a unique GUID only for each type of data (for each restricted mode profile) and allow an additional GUID to be associated with each type of encryption. The decoding configuration is then established between the decoder and accelerator by a lower-level subordinate negotiation using probing and locking operations to establish configurations for each type of DirectX VA function.

 

 



