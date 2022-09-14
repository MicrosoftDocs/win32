---
title: To Configure Constrained VBR
description: To Configure Constrained VBR
ms.assetid: a39e7628-0211-48ad-94e5-5003203f30be
keywords:
- streams,configuring VBR streams
- streams,variable bit rate (VBR)
- variable bit rate (VBR),streams
- VBR (variable bit rate),streams
- streams,configuring constrained VBR
- variable bit rate (VBR),configuring constrained
- VBR (variable bit rate),configuring constrained
- profiles,configuring constrained VBR
ms.topic: article
ms.date: 05/31/2018
---

# To Configure Constrained VBR

You can use constrained variable bit rate (VBR) encoding on a stream to specify an average bit rate that will be maintained in the encoded content. You also specify the maximum bit rate of the stream and the maximum required buffer window.

You cannot know what the average bit rate will be for a constrained VBR stream before encoding, but you can use a rough estimate. As a general rule, the maximum bit rate you specify will end up being two to three times the average bit rate.

Constrained VBR must be used in conjunction with two-pass encoding. Two-pass encoding is not set in the profile. You must configure the writer to perform a preprocessing pass before writing the stream. For more information about using two-pass encoding, see [Using Two-Pass Encoding](using-two-pass-encoding.md).

To configure a stream in a profile to use constrained VBR encoding, perform the following steps.

1.  Create a profile manager object by calling the [**WMCreateProfileManager**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-wmcreateprofilemanager) function.
2.  Open an existing profile to which you want to add VBR support. For more information about opening profiles, see [Working with Profiles](working-with-profiles.md).
3.  Get a stream configuration object for the stream you want to use by calling either [**IWMProfile::GetStream**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-getstream) or [**IWMProfile::GetStreamByNumber**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmprofile-getstreambynumber).
4.  Get a pointer to the [**IWMPropertyVault**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmpropertyvault) interface of the stream configuration object by calling **IWMStreamConfig::QueryInterface**.
5.  Enable VBR encoding for the stream by calling [**IWMPropertyVault::SetProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmpropertyvault-setproperty) for the **g\_wszVBREnabled** property.
6.  Use calls to **IWMPropertyVault::SetProperty** to set the desired maximum values for the **g\_wszVBRBitrateMax** and **g\_wszVBRBufferWindowMax** properties.
7.  Save the changes made to the stream by calling [**IWMProfile::ReconfigStream**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-reconfigstream).
8.  Save the profile, or pass it to the writer object.
9.  Configure the writer to perform a preprocessing pass.

## Related topics

<dl> <dt>

[**Configuring VBR Streams**](configuring-vbr-streams.md)
</dt> </dl>

 

 




