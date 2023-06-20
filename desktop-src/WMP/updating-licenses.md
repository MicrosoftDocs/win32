---
title: Updating Licenses
description: Updating Licenses
ms.assetid: b298badf-efcf-423c-8cc7-c3f50ab288a0
keywords:
- Windows Media Player online stores,updating licenses
- online stores,updating licenses
- type 1 online stores,updating licenses
- Windows Media Player online stores,license updating
- online stores,license updating
- type 1 online stores,license updating
- updating licenses
- licenses,updating
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Updating Licenses

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Online stores can deliver content that is licensed for a specific period of time or until a certain date. This would be normal for music content delivered as part of a subscription service agreement. In this case, the online store needs an opportunity to update these licenses before they expire, assuming, of course, that the user has paid to renew his or her subscription. (If the user has not renewed the subscription, the licenses can simply be left to expire.)

Windows Media Player queries the content partner plug-in about how much advance warning the Player should provide about a license that is about to expire. It does this by calling [IWMPContentPartner::GetContentPartnerInfo](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-getcontentpartnerinfo), passing the constant g\_szContentPartnerInfo\_LicenseRefreshAdvanceWarning through the *bstrInfoName* parameter. To alert the plug-in about licenses that are about to expire, Windows Media Player calls [IWMPContentPartner::RefreshLicense](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-refreshlicense). This call takes parameters that provide details about the file being refreshed, such as whether the file is on the user's computer, and the path to the file. If the license is being refreshed as part of a device synchronization operation, the *pReasonContext* parameter supplies the cannonical name of the device

When Windows Media Player calls **RefreshLicence**, it passes a cookie that identifies the update request. When the plug-in has finished processing the update request, it notifies Windows Media Player by calling [IWMPContentPartnerCallback::RefreshLicenseComplete](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartnercallback-refreshlicensecomplete), passing the cookie, the ID of the media item, and an **HRESULT** that indicates whether the update was successful.

Online store plug-ins can also do license inspection and updates as a background process. Windows Media Player notifies the plug-in about times when it is permissible to perform background processing tasks by calling [IWMPContentPartner::Notify](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-notify). To signal the plug-in to start background processing, the Player passes the [WMPPartnerNotification](/previous-versions/windows/desktop/api/contentpartner/ne-contentpartner-wmppartnernotification) enumeration value wmpsnBackgroundProcessingBegin; to signal the plug-in to stop background processing, the Player passes the value wmpsnBackgroundProcessingEnd.

## Related topics

<dl> <dt>

[**Programming Guide for Type 1 Online Stores**](programming-guide-for-type-1-online-stores.md)
</dt> </dl>

 

 




