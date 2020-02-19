---
title: Working with Device Conformance Templates
description: Working with Device Conformance Templates
ms.assetid: 230744d2-7c0f-4a14-8018-da88b5285add
keywords:
- profiles,device conformance templates
- profiles,conformance templates
- codecs,device conformance templates
- codecs,conformance templates
- device conformance templates,about
- conformance templates
- templates,device conformance templates
- Advanced Systems Format (ASF),device conformance templates
- ASF (Advanced Systems Format),device conformance templates
ms.topic: article
ms.date: 05/31/2018
---

# Working with Device Conformance Templates

Because of the great flexibility of ASF files, it is often difficult to determine whether a file is appropriate for playback on a specific device. For example, files written for local playback on desktop computers are not optimal for use on handheld devices. Device conformance templates enable applications to quickly identify the type of playback device for which a file was intended. If the device conformance template does not match the device, the application can inform the user that the file is inappropriate for the device. In this way, the user can be assured of a better playback experience.

If you are writing files exclusively for use on personal computers, device conformance templates will not be as much of a factor in creating profiles. The main purpose of these templates is to ensure that files created for use with special hardware are compatible with a whole range of devices and not just a single device.

A device conformance template is an assertion that an ASF file contains data encoded within certain parameters. For more information about the settings appropriate to the individual templates, see [Device Conformance Template Parameters](device-conformance-template-parameters.md).

The following codecs support device conformance templates:

-   Windows Media Video 9
-   Windows Media Audio 9 and later
-   Windows Media Audio 9 Professional and later
-   Windows Media Audio 9 Voice

You do not need to take any special steps to use device conformance templates. The codec automatically writes a template string for each appropriate stream in the file. The codec will decide which template to use, based on the stream configuration settings in the profile. There is some overlap in device conformance template parameters, so you may want to request a specific template instead of letting the codec assign one for you. You can specify which template you want by setting the g\_wszDecoderComplexityRequested property with the methods of the [**IWMPropertyVault**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmpropertyvault) interface of the appropriate stream configuration object.

When an ASF file is written, the actual device conformance template for each stream is set to the value passed to the writer by the codec. When opening a file for reading, you can find out which template the streams of the file conform to by using the methods of the [**IWMHeaderInfo3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo3) interface to retrieve the g\_wszDeviceConformanceTemplate stream-level attribute. For more information about attributes, see [Working with Metadata](working-with-metadata.md).

## Related topics

<dl> <dt>

[**Designing Profiles**](designing-profiles.md)
</dt> <dt>

[**Device Conformance Template Parameters**](device-conformance-template-parameters.md)
</dt> </dl>

 

 




