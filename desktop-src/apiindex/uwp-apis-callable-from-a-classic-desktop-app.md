---
Description: With some notable exceptions, the general rule is that a Universal Windows Platform (UWP)&\#160;API can be called from a classic desktop app.
ms.assetid: F3808C28-72DE-49B5-A389-EB085EFC02CC
title: UWP APIs callable from a classic desktop app
ms.topic: article
ms.date: 05/31/2018
---

# UWP APIs callable from a classic desktop app

With some notable exceptions, the general rule is that a Universal Windows Platform (UWP) API can be called from a classic desktop app. The two main areas of APIs that are an exception to this general rule are XAML UI APIs, and APIs that require the calling app to have a package identity. UWP apps have a well-defined app model, and they have a package identity. Classic desktop apps do not have a well-defined app model, and they do not have a package identity. A [classic desktop app that has been converted to a UWP app](https://go.microsoft.com/fwlink/p/?LinkId=761468) does have a package identity.

## The DualApiPartition attribute

This is the process to follow whenever there's a particular UWP API that you'd like to call from your classic desktop app. This process will answer the question of whether the API is allowed to be called from a classic desktop app. First, visit the [Windows API reference for Windows Runtime apps](https://www.bing.com/search?q=Windows+API+reference+for+Windows+Runtime+apps), find the reference topic for the class or member API you're interested in, scroll right to the bottom of the topic to the Attributes section, and check whether the [**DualApiPartition**](https://msdn.microsoft.com/en-us/library/Hh700630(v=WIN.10).aspx) attribute is listed.

## If the DualApiPartition attribute is listed

If the API does not need the calling app to have a package identity then the API is allowed to be called from a classic desktop app. [**Windows.Devices.Geolocation.Geolocator**](https://msdn.microsoft.com/en-us/library/BR225534(v=Win.10).aspx) is an example; an app does not need to be uniquely identified in order to perform location tasks.

If the API does need the calling app to have a package identity then the API is not allowed to be called from a classic desktop app. But the API can be called from a classic desktop app that has been converted to a UWP app. [**Windows.Storage.ApplicationData**](https://msdn.microsoft.com/en-us/library/BR241587(v=Win.10).aspx) is an example; an app needs to be uniquely identified in order for the system to access the app's particular data store.

## If the DualApiPartition attribute is not listed

In this case, the API is not allowed to be called from a classic desktop app. [**Windows.UI.Xaml.Controls.Button**](https://msdn.microsoft.com/en-us/library/BR209265(v=Win.10).aspx) is an example.

 

 



