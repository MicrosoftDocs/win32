---
title: Windows 8.1 allows only https URIs, not http URIs
description: Windows 8.1 allows only https URIs, not http URIs
ms.assetid: 06BDD3A3-67B7-4085-83DA-F322F718C876
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Windows 8.1 allows only https URIs, not http URIs

## Platforms

<dl> Clients - Windows 8.1  
Servers - Windows Server 2012 R2  
</dl>

## Description

While apps built for Windows 8 can include http and https URIs in their application content URIs, apps built for Windows 8.1 may include only https URIs.

The only exception is for dynamic ContentUriRules that are specified in the app’s AppxManifest.xml file. With dynamic ContentUriRules, apps can access additional domains or network resources that are provided by the admin, such as Group Policy URIs. However, dynamic ContentUriRules are only available to Windows Store apps if they meet these conditions:

-   The Group Policy is enabled
-   The package has specified the enterpriseAuthentication capability
-   The package’s OSMaxVersionTested is Windows 8.1 or greater

The new restrictions in Windows 8.1 are part of enhanced security restrictions to further protect the platform.

## Manifestations

When running an app built for Windows 8 on Windows 8.1, the use of http URIs in the [ApplicationContentUriRules](http://go.microsoft.com/fwlink/p/?LinkId=325296) is allowed.

## Mitigations

We recommend that WWA developers switch from [<iframe>](http://go.microsoft.com/fwlink/p/?LinkId=325297) to the [WebView](http://go.microsoft.com/fwlink/p/?LinkId=325298) control (<x-ms-webview>). However, if you need support for AppCache, IndexedDB, geolocation, or programmatic clipboard access, you will need to continue using <iframe> for Windows 8.1.

Continued usage of <iframe> for remote content will require a new entry in the ApplicationContentUriRules for the app. Apps with WebView require new entries in the ApplicationContentUriRules if the web content needs to invoke window.external.notify for generating a [ScriptNotify](http://go.microsoft.com/fwlink/p/?LinkId=325299) event. If you do not have Visual Studio, you can update the app manifest by adding the following XML, including wildcards for subdomains (e.g. https://\*.microsoft.com):


```
<Package>
    …
    <Applications>
        <Application>
            …
            <ApplicationContentUriRules>
                <Rule Match="https://www.example.com" Type="include"/>
            </ApplicationContentUriRules>
        </Application>
    </Applications>
</Package>
```



## Resources

-   [ApplicationContentUriRules](http://go.microsoft.com/fwlink/p/?LinkId=325296)
-   [<iframe> element \| <iframe> object](http://go.microsoft.com/fwlink/p/?LinkId=325297)
-   [Webview class](http://go.microsoft.com/fwlink/p/?LinkId=325298)
-   [WebView.ScriptNotify event](http://go.microsoft.com/fwlink/p/?LinkId=325299)

 

 




