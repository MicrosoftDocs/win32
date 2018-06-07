---
Description: Audio Processing Objects Utility Functions
ms.assetid: 68e6b7ac-ac5c-428f-8ecd-e7fd1cd8c987
title: Audio Processing Objects Utility Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Audio Processing Objects Utility Functions

Audio processing objects must have real-time compatibility. This means that all buffers set aside for use by the audio processing interfaces and methods must be nonpageable. The real-time compatibility requirement also means that all code and data in the process path must also be nonpageable.

The following utility functions allocate or release locked memory for use by the interfaces and methods that perform audio processing.

<dl>

[**AERT\_Allocate**](/windows/desktop/api/baseaudioprocessingobject/nf-baseaudioprocessingobject-aert_allocate)  
[**AERT\_Free**](/windows/desktop/api/baseaudioprocessingobject/nf-baseaudioprocessingobject-aert_free)  
</dl>

The following utility functions are used to create media types for audio data processing.

<dl>

[**CreateAudioMediaType**](/windows/desktop/api/audiomediatype/nf-audiomediatype-createaudiomediatype)  
[**CreateAudioMediaTypeFromUncompressedAudioFormat**](/windows/desktop/api/audiomediatype/nf-audiomediatype-createaudiomediatypefromuncompressedaudioformat)  
</dl>

For more information about the general requirements to help you develop audio processing objects, see [Design Considerations for sAPO Development](https://www.bing.com/search?q=Design+Considerations+for+sAPO+Development).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Baudio\audio%5D:%20Audio%20Processing%20Objects%20Utility%20Functions%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



