---
title: Encrypting and Importing Media Samples
description: Encrypting and Importing Media Samples
ms.assetid: f9784c9a-c672-432d-a3ad-eb2ed73ac523
keywords:
- Windows Media Format SDK,DRM import
- Windows Media Format SDK,import
- Windows Media Format SDK,encrypting media samples
- digital rights management (DRM),import
- DRM (digital rights management),import
- digital rights management (DRM),encrypting media samples
- DRM (digital rights management),encrypting media samples
- DRM Client Extended APIs,import
- Client Extended APIs,import
- DRM Client Extended APIs,encrypting media samples
- Client Extended APIs,encrypting media samples
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Encrypting and Importing Media Samples

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

For each media sample that you encrypt using Windows Media DRM, you must generate a salt value that is strictly bigger than the previous one (monotonically increasing). Use the new salt value to create a transitory encryption key by applying the SHA-1 encryption algorithm to the initialization vector concatenated with the salt value.

Next, encrypt the sample according to the RC4 algorithm using the generated transitory key. Before the sample is passed to the SDK, your application must associate the salt value with the sample by setting an extension attribute.

Here are the steps for encrypting media samples:

1.  Call the **QueryInterface** method of the sample object to get the [**INSSBuffer3**](/previous-versions/windows/desktop/api/wmsbuffer/nn-wmsbuffer-inssbuffer3) interface.
2.  Increment the salt value.
3.  Encrypt the sample using an RC1 encryption algorithm. For the encryption you create a key by concatenating the initialization vector and the salt value.
4.  Provide the salt value to the SDK by calling [**INSSBuffer::SetProperty**](/previous-versions/windows/desktop/api/Wmsbuffer/nf-wmsbuffer-inssbuffer3-setproperty).

## Related topics

<dl> <dt>

[**DRM Import**](drm-import.md)
</dt> <dt>

[**Media Sample Encryption Example**](media-sample-encryption-example.md)
</dt> </dl>

 

 




