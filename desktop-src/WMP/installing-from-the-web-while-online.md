---
title: Installing from the Web While Online
description: Installing from the Web While Online
ms.assetid: 891483b0-6ba4-4ed4-b043-c6c109dc696b
keywords:
- Windows Media Player online stores,installing from Web while online
- online stores,installing from Web while online
- type 1 online stores,installing from Web while online
- type 2 online stores,installing from Web while online
- Windows Media Player online stores,online installs from Web
- online stores,online installs from Web
- type 1 online stores,online installs from Web
- type 2 online stores,online installs from Web
- installing online stores from Web while online
- online installs of online stores
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Installing from the Web While Online

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Users can install Windows Media Player as a Web download while connected to the Internet. In this case, Microsoft can configure the initial online store that you specify.

To redistribute Windows Media Player in this manner, use the following URL:

https://go.microsoft.com/fwlink/p/?linkid=32981&SV=*version*&UserLocale=*localID*&Service=*key*

In the preceding URL, set *key* to the key name for your online store, and set *localeID* to the identifier of the locale where your store provides service. Set *version* to 2 for Windows Media Player 11 on Windows XP or 1 for Windows Media Player 10. The URL installs Windows Media Player and sets the initial active store to the one specified by *key*.

The following example shows a URL that installs Windows Media Player 11 and sets Proseware as the initial active store. The value of 409 for *localeID* indicates that Proseware provides service in the United States.

https://go.microsoft.com/fwlink/p/?linkid=32981&SV=2&UserLocale=409&Service=Proseware

If the ServiceInfo document for the online store includes an Install element, Windows Media Player setup will customize the setup process. Using the attribute values, setup displays your End User License Agreement (EULA) and your privacy statement, and also retrieves and installs your .cab file to the user's computer. For example, you can use this feature to install the latest version of a COM object that your online store requires.

## Related topics

<dl> <dt>

[**Information Common to Type 1 and Type 2 Online Stores**](information-common-to-type-1-and-type-2-online-stores.md)
</dt> <dt>

[**Install Element**](install-element.md)
</dt> <dt>

[**ServiceInfo Document**](serviceinfo-document.md)
</dt> <dt>

[**Setting the Initial Online Store**](setting-the-initial-online-store.md)
</dt> </dl>

 

 




