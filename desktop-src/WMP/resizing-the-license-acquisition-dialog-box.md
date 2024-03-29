---
title: Resizing the License Acquisition Dialog Box
description: Resizing the License Acquisition Dialog Box
ms.assetid: e091d981-1574-4ffc-bdc4-b92f74396cb7
keywords:
- Windows Media Player,resizing License Acquisition dialog box
- Windows Media Player,License Acquisition dialog box
- Windows Media Player,DRM_LicenseAcqURL attribute
- resizing License Acquisition dialog box
- License Acquisition dialog box
- DRM_LicenseAcqURL
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Resizing the License Acquisition Dialog Box

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can append query string parameters to the URL you provide for the **DRM\_LicenseAcqURL** attribute to specify a size for the Windows Media Player 10 or later license acquisition dialog box. The following table lists the parameters.



| Parameter | Description                                        |
|-----------|----------------------------------------------------|
| *DlgX*    | Specifies the width of the dialog box, in pixels.  |
| *DlgY*    | Specifies the height of the dialog box, in pixels. |



 

For example, the following license acquisition URL would cause the license acquisition dialog box to open with a size of 800 by 600 pixels:


```C++
https://www.proseware.com/license/lic_acq.htm?DlgX=800&DlgY=600

```



The maximum size for the dialog box will never exceed the current screen dimensions minus 20 pixels. The minimum size is 333 x 210 pixels (the default size).

This feature requires Windows Media Player 10 or later.

## Related topics

<dl> <dt>

[**Windows Media Player**](windows-media-player.md)
</dt> </dl>

 

 




