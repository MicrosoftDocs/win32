---
title: Installing from a CD While Online
description: Installing from a CD While Online
ms.assetid: 4cf34f0e-caa0-42d1-b99a-51bbb7f0a7df
keywords:
- Windows Media Player online stores,installing from CD while online
- online stores,installing from CD while online
- type 1 online stores,installing from CD while online
- type 2 online stores,installing from CD while online
- Windows Media Player online stores,online installs from CD
- online stores,online installs from CD
- type 1 online stores,online installs from CD
- type 2 online stores,online installs from CD
- Windows Media Player online stores,CD installs while online
- online stores,CD installs while online
- type 1 online stores,CD installs while online
- type 2 online stores,CD installs while online
- installing online stores from CD while online
- CD installs of online stores while online
- online installs of online stores
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Installing from a CD While Online

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Users can install Windows Media Player from a CD while connected to the Internet. When this happens, Windows Media Player setup locates the ServiceInfo document specified by the *ServiceInfo* command line parameter. If the **Key** attribute matches the *DefaultService* command line parameter, setup inspects the Install element to customize the setup process. Using the attribute values, setup displays your End User License Agreement (EULA) and your privacy statement, and also retrieves and installs your .cab file to the user's computer. For example, you can use this feature to install the latest version of a COM object that your online store requires.

After it is installed, Windows Media Player sets the initial online store using the key name you specified for the *DefaultService* command line parameter.

## Related topics

<dl> <dt>

[**Information Common to Type 1 and Type 2 Online Stores**](information-common-to-type-1-and-type-2-online-stores.md)
</dt> <dt>

[**Install Element**](install-element.md)
</dt> <dt>

[**ServiceInfo Document**](serviceinfo-document.md)
</dt> <dt>

[**Setting the Initial Online Store**](setting-the-initial-online-store.md)
</dt> <dt>

[**Setup Command-line Parameters for Online Stores**](setup-command-line-parameters-for-online-stores.md)
</dt> </dl>

 

 




