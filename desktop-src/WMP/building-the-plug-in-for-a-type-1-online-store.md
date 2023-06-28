---
title: Building the Plug-in for a Type 1 Online Store
description: Building the Plug-in for a Type 1 Online Store
ms.assetid: 5d38a41f-9859-452b-953f-3449c2b0ce06
keywords:
- Windows Media Player online stores,plug-ins
- online stores,plug-ins
- type 1 online stores,plug-ins
- Windows Media Player online stores,building plug-ins
- online stores,building plug-ins
- type 1 online stores,building plug-ins
- Windows Media Player online stores,IWMPContentPartner interface
- online stores,IWMPContentPartner interface
- type 1 online stores,IWMPContentPartner interface
- plug-ins,Windows Media Player online stores
- plug-ins,online stores
- plug-ins,type 1 online stores
- plug-ins,IWMPContentPartner interface
- plug-ins,building
- Windows Media Player plug-ins,type 1 online stores
- Windows Media Player plug-ins,online stores
- Windows Media Player plug-ins,Windows Media Player online stores
- Windows Media Player plug-ins,IWMPContentPartner interface
- Windows Media Player plug-ins,building
- IWMPContentPartner
- building plug-ins,type 1 online stores
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Building the Plug-in for a Type 1 Online Store

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A type 1 online store must provide a plug-in that implements the [**IWMPContentPartner**](/previous-versions/windows/desktop/api/contentpartner/nn-contentpartner-iwmpcontentpartner) interface. The plug-in runs in a separate process from Windows Media Player.

The steps for creating a plug-in that runs out-of-process are as follows:

1.  Write your plug-in as if it were an in-process COM server.
2.  Create a **DllSurrogate** registry entry on the user's computer. The **DllSurrogate** entry informs the COM runtime that your plug-in should be created in an instance of the default DLL surrogate, dllhost.exe.

For detailed information about registering your plug-in, see [Registry Keys and Entries for a Type 1 Online Store](registry-keys-and-entries-for-a-type-1-online-store.md).

You do not need to create any proxy or stub code for your plug-in. All of the marshaling support is provided by Windows Media Player.

You can use the online store plug-in wizard to quickly create a plug-in that serves as a starting point. For more information, see [Installing the Online Store Plug-in Wizard](installing-the-online-store-plug-in-wizard.md).

## Related topics

<dl> <dt>

[**Programming Guide for Type 1 Online Stores**](programming-guide-for-type-1-online-stores.md)
</dt> </dl>

 

 




