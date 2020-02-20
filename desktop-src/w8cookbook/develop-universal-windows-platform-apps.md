---
title: Develop Universal Windows Platform (UWP) apps
description: Develop Universal Windows Platform (UWP) apps
ms.assetid: 215256D7-CBBA-43B0-A99C-490A25D1F82C
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Develop Universal Windows Platform (UWP) apps

We encourage all desktop (Win32) app ISVs to bring your desktop apps to the [Universal Windows Platform (UWP)](https://developer.microsoft.com/windows/bridges/desktop/) via the Desktop Bridge. UWP apps are also supported in the [Windows Store](https://blogs.windows.com/buildingapps/2016/02/04/windows-store-trends-february-2016/), so it’s easier for you to update your users to a consistent version automatically, lowering your support costs.

If your desktop apps cannot be converted using the Desktop Bridge, we highly recommend that you use an installer that follows best practices, and ensure this is fully tested. An installer is your user or customer's first experience with your app. All too often, this doesn’t work well or it hasn’t been fully tested for all scenarios. The [Windows App Certification Kit](https://dev.windows.com/develop/app-certification-kit) can help you test install and uninstall of your Win32 app and help you identify use of undocumented APIs, as well as other basic performance-related best-practice issues before your users do.

## Best practices:

-   Use installers that work for both 32-bit and 64-bit versions of Windows.
-   Design your installers to run on multiple scenarios (user or machine level).
-   Keep all Windows redistributables in the original packaging – if you repackage these, it’s possible that this will break the installer.
-   Schedule development time for your installers—these are often overlooked as a deliverable during the software development lifecycle.

 

 




