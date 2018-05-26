---
title: To Configure Unconstrained VBR
description: To Configure Unconstrained VBR
ms.assetid: 69ef951f-d08b-401b-a285-2ffdf43ea35d
keywords:
- streams,configuring VBR streams
- streams,variable bit rate (VBR)
- variable bit rate (VBR),streams
- VBR (variable bit rate),streams
- streams,configuring unconstrained VBR
- variable bit rate (VBR),configuring unconstrained
- VBR (variable bit rate),configuring unconstrained
- profiles,configuring unconstrained VBR
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# To Configure Unconstrained VBR

You can use unconstrained variable bit rate (VBR) encoding on a stream to specify an average bit rate that will be maintained in the encoded content. Unconstrained VBR differs from normal CBR in that the variance in bit rate throughout the stream can be greater.

The bit rate of the stream, set with [**IWMStreamConfig::SetBitrate**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmstreamconfig-setbitrate?branch=master), is used as the desired average bit rate. When encoding of the stream is complete, you can use [**IWMPropertyVault::GetPropertyByName**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmpropertyvault-getpropertybyname?branch=master) to retrieve two additional properties: **g\_wszVBRPeak** and **g\_wszBufferAverage**. These properties describe the peak bit rate of the encoded content and the average buffer window of the content, respectively.

Unconstrained VBR must be used in conjunction with two-pass encoding. Two-pass encoding is not set in the profile. You must configure the writer to perform a preprocessing pass before writing the stream. For more information about using two-pass encoding, see [Using Two-Pass Encoding](using-two-pass-encoding.md).

To configure a stream in a profile to be encoded with unconstrained VBR, perform the following steps:

1.  Create a profile manager object by calling the [**WMCreateProfileManager**](/windows/win32/Wmsdkidl/nf-wmsdkidl-wmcreateprofilemanager?branch=master) function.
2.  Open an existing profile to which you want to add VBR support. For more information about opening profiles, see [Working with Profiles](working-with-profiles.md).
3.  Get a stream configuration object for the stream you want to use by calling either [**IWMProfile::GetStream**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-getstream?branch=master) or [**IWMProfile::GetStreamByNumber**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-getstreambynumber?branch=master).
4.  Get a pointer to the [**IWMPropertyVault**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmpropertyvault?branch=master) interface of the stream configuration object by calling **IWMStreamConfig::QueryInterface**.
5.  Enable VBR encoding for the stream by calling [**IWMPropertyVault::SetProperty**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmpropertyvault-setproperty?branch=master) for the **g\_wszVBREnabled** property.
6.  Set **g\_wszVBRBitrateMax** and **g\_wszVBRBufferWindowMax** both to zero with **IWMPropertyVault::SetProperty**.
7.  Save the changes made to the stream by calling [**IWMProfile::ReconfigStream**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmprofile-reconfigstream?branch=master).
8.  Save the profile, or pass it to the writer object.
9.  Configure the writer to perform a preprocessing pass.

## Related topics

<dl> <dt>

[**Configuring VBR Streams**](configuring-vbr-streams.md)
</dt> </dl>

 

 




