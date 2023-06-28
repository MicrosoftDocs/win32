---
title: Providing a User Interface
description: Providing a User Interface
ms.assetid: 43a0cfea-4f35-4c4a-97f5-a3787b597dc5
keywords:
- Windows Media Player plug-ins,property pages
- plug-ins,property pages
- digital signal processing plug-ins,property pages
- DSP plug-ins,property pages
- digital signal processing plug-ins,user interface
- DSP plug-ins,user interface
- property pages
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Providing a User Interface

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

DSP plug-ins can provide a property page to create a user interface. To do this, the plug-in must include a property page object that provides an implementation of an **IPropertyPage** interface. The DSP plug-in object must implement **ISpecifyPropertyPages::GetPages**, which allows Windows Media Player to locate and identify the correct property page for the plug-in.

**Displaying a Status Graphic**

DSP plug-ins can display a small graphic, or series of graphics, in the Windows Media Player status area to notify the user that a plug-in is active. To support this feature, the plug-in must implement the **IPropertyBag** interface. Windows Media Player calls **IPropertyBag::Read**, providing a pointer to the requested property name "IconStreams", which is case-sensitive, and a pointer to a **VARIANT** structure that receives the data for the graphic. The plug-in creates an **IStream** object (or a SAFEARRAY of **IStream** objects if there are multiple graphics), then loads the graphic data, including header information, into the stream, and then returns a pointer to the **IStream** object using the **punkVal** member of the **VARIANT** structure. If the plug-in supplies only one graphic, it specifies the **vt** member of the **VARIANT** structure as VT\_UNKNOWN. If the plug-in supplies multiple graphic **IStream** objects using a SAFEARRAY, it specifies the **vt** member of the **VARIANT** structure as VT\_ARRAY.

Graphics can be stored in a variety of file formats, including:

**BMP**

Microsoft Windows Bitmap images are uncompressed.

**JPEG**

Compressed image format commonly used for webpages. JPEG format files usually have .jpg file name extensions.

**GIF**

Compressed image format commonly used for webpages.

**PNG**

Compressed image format commonly used for webpages.

The maximum dimensions for DSP plug-in graphics are 38 pixels wide and 14 pixels high.

The **IStream** byte stream containing the status graphic must include header information. Without header information, Windows Media Player cannot properly identify the type of graphic and therefore will not load the image.

## Related topics

<dl> <dt>

[**DSP Plug-in Developer Overview**](dsp-plug-in-developer-overview.md)
</dt> </dl>

 

 




