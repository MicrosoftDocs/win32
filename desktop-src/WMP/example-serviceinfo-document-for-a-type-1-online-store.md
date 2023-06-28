---
title: Example ServiceInfo Document for a Type 1 Online Store
description: Example ServiceInfo Document for a Type 1 Online Store
ms.assetid: 7d997773-1c11-44d5-ae67-05ba3909c481
keywords:
- Windows Media Player online stores,example ServiceInfo document
- online stores,example ServiceInfo document
- type 1 online stores,example ServiceInfo document
- Windows Media Player online stores,ServiceInfo document
- online stores,ServiceInfo document
- type 1 online stores,ServiceInfo document
- Windows Media Player online stores,code example
- online stores,code example
- type 1 online stores,code example
- example ServiceInfo document
- ServiceInfo document
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Example ServiceInfo Document for a Type 1 Online Store

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following code example shows a complete ServiceInfo.xml document. You can use this XML as a starting point for your own ServiceInfo document.


```C++
<?xml version="1.0" encoding="utf-8" ?>
<ServiceInfo Version="1.00" Key="Proseware" ContentPartner="true">

    <FriendlyName>Proseware Service</FriendlyName>

    <Description>
        Proseware Music has all your favorite songs.
    </Description>

    <Image 
        EulaURL = "https://www.proseware.com/service/images/eula.png"
        MenuURL = "https://www.proseware.com/service/images/menuicon.jpg"
        ServiceLargeURL = "https://www.proseware.com/service/images/45x13Large.png"
        ServiceSmallURL = "https://www.proseware.com/service/images/45x13Small.png" />

    <Color
        MediaPlayer = "#FF8040"
        MediaPlayerText = "#FFFFFF"/>

    <ServiceTask1
        URL = "https://www.proseware.com/service/html/Music.asp">
        <ButtonText>Proseware\nMusic</ButtonText>
        <ButtonTip>Proseware Music Store</ButtonTip>
    </ServiceTask1>

    <Navigate
        BaseURL = "https://www.proseware.com/service/html/navigate.asp">
    </Navigate>

    <InfoCenter
        URL = "https://www.proseware.com/service/html/InfoCenter.asp"/>

    <AlbumInfo
        URL = "https://www.proseware.com/service/html/AlbumInfo.asp"/>

    <BuyCD
        MediaPlayerURL = "https://www.proseware.com/service/html/BuyCDMediaPlayer.asp"
        MediaCenterURL = "https://www.proseware.com/service/html/BuyCDMediaCenter.asp"
        BrowserURL = "https://www.proseware.com/service/html/BuyCDBrowser.asp"/>

    <DownloadStatus
        URL = "https://www.proseware.com/service/html/Music_Download.htm"/>

    <HTMLView
        BaseURL = "https://www.proseware.com/"/>

    <Install
        EULAURL="https://www.proseware.com/service/html/eula.txt"
        CodeURL="https://www.proseware.com/service/html/ProsewareInstall.cab"
        PrivacyInfoURL="https://www.proseware.com/service/html/PrivacyPolicy.htm"
        InstallApp="ProsewareSetup.exe"  
        CatalogURL="https://www.proseware.com/service/html/Catalog.asp"/>

</ServiceInfo>
```



## Related topics

<dl> <dt>

[**Programming Guide for Type 1 Online Stores**](programming-guide-for-type-1-online-stores.md)
</dt> <dt>

[**ServiceInfo Document for a Type 1 Online Store**](serviceinfo-document-for-a-type-1-online-store.md)
</dt> <dt>

[**ServiceInfo Document**](serviceinfo-document.md)
</dt> </dl>

 

 




