---
title: Common On-Boarding Problems for Online Music Stores
description: Common On-Boarding Problems for Online Music Stores
ms.assetid: 4210aabb-d1ad-4f98-88e0-941933d77303
keywords:
- Windows Media Player Online Stores
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Common On-Boarding Problems for Online Music Stores

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Here is a list of common Windows Media Player on-boarding problems you should try to avoid. Any of these issues can cause your store to fail validation testing. Failing the RC2 pass will postpone your launch until the next available launch window.

1.  Failure to transition from test servers to production servers
    -   Missing pages
    -   IIS settings (Access, VRoots, https or other security settings)
    -   Test accounts don't work anymore.
    -   Test accounts don't have credits applied.
    -   Service hosted logos don't get moved.
    -   IP restrictions that have been previously worked around re-occur. In particular, e-commerce systems might have a different set of restrictions from the music site.
    -   The ServiceInfo document doesn't get updated to point to production.
2.  The Buy link (or Shop link) in the Now Playing area is invalid. This is a commonly overlooked issue, and it will cause your store to fail even when everything else is in working order.
3.  Microsoft's testers must have adequate purchasing power. Microsoft's validation team will run through several purchasing scenarios ranging from small purchases to very large purchases. You must provide a rechargeable way for them to act as consumers within your store. This can range from providing a variety of accounts through providing a dummy credit card. As an example, a store will fail in RC2 if a validation tester attempts to buy an album but has only enough credit to buy a single track.
4.  If you use ActiveX controls inside your service pages, ensure that they install and uninstall cleanly, both on all applicable versions of Windows. Failure to do so is a typical problem. Often the developers and testers at an online store have the ActiveX controls registered on their own computers but forget about installing the controls on the user's computer.

    If your store installs a plug-in or an ActiveX control, you must provide the user an easy way to uninstall it. For example, Microsoft recently found that some online stores installed ActiveX controls in Windows Media Player 11 for Windows Vista that could not be removed through the Add/Remove Programs menu. After some investigation, Microsoft found that the ActiveX controls could be removed through the Add-on manager in Internet Explorer. It's important that you communicate (through a Help file, at the least) the way to install and uninstall ActiveX controls and plug-ins.

    For more information on how to integrate your store with the security infrastructure in Windows Vista, see the article titled ["Developer Best Practices and Guidelines for Applications in a Least Privileged Environment"](/previous-versions/aa905330(v=msdn.10)).

 

 