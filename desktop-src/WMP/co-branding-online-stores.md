---
title: Co-Branding Online Stores
description: Co-Branding Online Stores
ms.assetid: b564845a-a4e0-4fe6-90cb-63ef320c7e52
keywords:
- Windows Media Player online stores,co-branding
- online stores,co-branding
- type 1 online stores,co-branding
- type 2 online stores,co-branding
- co-branding online stores
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Co-Branding Online Stores

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Personal computer OEMs who do not operate a music store can co-brand with online store providers. Windows Media Player setup supports the ServiceExtra command line parameter to enable hardware OEMs to set a custom attribute that the online store can use to identify which OEM installed the initial online store.

For example, if a computer maker named Fabrikam wants to set the initial online store to the Proseware music store, it might use the following command line to install Windows Media Player 10:


```C++
MP10Setup.exe /q:A /c:"setup_wm.exe /Q /R:N /DefaultService:Proseware /ServiceInfo:c:\Proseware\service_info_local.xml /ServiceExtra:OEM=Fabrikam"
```



When Windows Media Player is installed in this manner, the Player appends the ServiceExtra string each time it opens the Proseware service. The following example shows the URL that Windows Media Player would send to the Proseware service to retrieve the ServiceInfo document:


```C++
https://www.proseware.com/XML/serviceinfo.asp?OEM=Fabrikam
```



The Proseware online store can then use the query string to determine which OEM installed Windows Media Player and return a dynamically generated ServiceInfo document that points to the co-branded version of the online store.

## Related topics

<dl> <dt>

[**Information Common to Type 1 and Type 2 Online Stores**](information-common-to-type-1-and-type-2-online-stores.md)
</dt> <dt>

[**Setup Command-line Parameters for Online Stores**](setup-command-line-parameters-for-online-stores.md)
</dt> </dl>

 

 




