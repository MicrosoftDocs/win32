---
title: Working with Output Protection Levels
description: Working with Output Protection Levels
ms.assetid: ec5982cd-0b87-4081-98e2-ab2d102a36d8
keywords:
- Windows Media Format SDK,output protection levels (OPL)
- Windows Media Format SDK,protection levels
- Advanced Systems Format (ASF),output protection levels (OPL)
- ASF (Advanced Systems Format),output protection levels (OPL)
- Advanced Systems Format (ASF),protection levels
- ASF (Advanced Systems Format),protection levels
- Advanced Systems Format (ASF),multiple licenses
- ASF (Advanced Systems Format),multiple licenses
- digital rights management (DRM),output protection levels (OPL)
- DRM (digital rights management),output protection levels (OPL)
- digital rights management (DRM),protection levels
- DRM (digital rights management),protection levels
- digital rights management (DRM),evaluating output protection levels (OPL)
- DRM (digital rights management),evaluating output protection levels (OPL)
- digital rights management (DRM),multiple licenses
- DRM (digital rights management),multiple licenses
- output protection levels (OPL)
- OPL (output protection levels)
ms.topic: article
ms.date: 05/31/2018
---

# Working with Output Protection Levels

Licenses created by using the Windows Media Rights Manager 10 SDK can specify action restrictions using output protection levels (OPLs). OPLs enable a license creator to allow some actions only on devices with specific technologies. The benefits of using OPLs is that you get more flexibility in creating license restrictions than previous versions. In addition, OPLs are expandable to accommodate future technologies. You can support such licenses in your applications by using the methods of the [**IWMDRMReader2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdrmreader2) interface.

To read files that are protected by a license that specifies OPLs, you must check the OPL for the desired action. The output technology your application is using must be allowed by the OPL in the license. For example, some licenses for protected audio may require that you use secure audio path to play it.

## Configuring the Reader to Evaluate Output Protection Levels

Before you can check OPLs for files loaded in the reader, you must call the [**IWMDRMReader2::SetEvaluateOutputLevelLicenses**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader2-setevaluateoutputlevellicenses) method, passing **TRUE** for the *fEvaluate* parameter. If you do not call this method, licenses that require OPLs are not visible to your application.

## Evaluating Copy Output Protection Levels

To get output protection levels for the copy action, call the [**IWMDRMReader2::GetCopyOutputLevels**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader2-getcopyoutputlevels) method. The data you receive from the call is stored in a [**DRM\_COPY\_OPL**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-drm_copy_opl) structure. The structure contains a base output protection level, which specifies the minimum output level for the copy action in the license. However, the DRM\_COPY\_OPL structure also contains two lists of technology identifiers: one for allowed technologies that are rated at a lower OPL than the base, and one for technologies that are rated equal to or higher than the base OPL but that are restricted by the license. You must check the inclusions and exclusions to ensure that the technology your application is using is allowed by the license.

## Evaluating Play Output Protection Levels

To get output protection levels for the play action, call the [**IWMDRMReader2::GetPlayOutputLevels**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader2-getplayoutputlevels) method. The data you receive from the call is stored in a [**DRM\_PLAY\_OPL**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-drm_play_opl) structure. The structure contains several other structures. The base output protection levels for the play action are stored in a [**DRM\_MINIMUM\_OUTPUT\_PROTECTION\_LEVELS**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-drm_minimum_output_protection_levels) structure (the **minOPL** member of **DRM\_PLAY\_OPL**), which defines the minimum OPL required to play content in a variety of formats. You must check the member for the type of output formats that your application delivers.

The **DRM\_PLAY\_OPL** structure defines two kinds of restrictions: required down-sampling and allowed video output protection identifiers.

Required down-sampling is defined as a list of output technology identifiers (the **oplIdDownsample** member of **DRM\_PLAY\_OPL**) that, if used, can receive the content for playback only if the content is first down-sampled to a lower bit rate.

Allowed video output protection identifiers are defined as a list of video output technologies with configuration information for each.

## Handling Multiple Licenses

Some files may have multiple licenses associated with them in the local license store. When you evaluate OPLs for a file that you are reading, you can check for additional licenses by calling the [**IWMDRMReader2::TryNextLicense**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader2-trynextlicense) method. You should continue trying licenses until you find one that allows the action you want to perform or until TryNextLicense returns DRM\_S\_FALSE, which indicates that there are no more licenses.

In some cases, a file might have an associated license that requires an OPL that your application cannot support. In such a case it is important to check for additional licenses because a license may exist that does not specify OPLs.

**Note** DRM is not supported by the x64-based version of this SDK.

## Related topics

<dl> <dt>

[**Enabling DRM Support**](enabling-drm-support.md)
</dt> <dt>

[**IWMDRMReader2 Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdrmreader2)
</dt> </dl>

 

 




