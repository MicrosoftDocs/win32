---
title: Refreshing Licenses for Stores That Have the PlaysForSure Logo
description: Refreshing Licenses for Stores That Have the PlaysForSure Logo
ms.assetid: d08d6b6e-937e-4dec-b7ca-376cdad069f9
keywords:
- Windows Media Player online stores,refreshing licenses
- online stores,license refreshing
- Windows Media Player online stores,license refreshing
- online stores,refreshing licenses
- Windows Media Player online stores,PlaysForSure logo
- online stores,PlaysForSure logo
- refreshing licenses
- licenses,refreshing
- PlaysForSure
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Refreshing Licenses for Stores That Have the PlaysForSure Logo

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Certain online music stores have the PlaysForSure logo but are not integrated with Windows Media Player 11. Those stores must provide a ServiceInfo document and a lightweight component so that Windows Media Player 11 can obtain and update licenses for their content.

The following example illustrates how the license updating process works.

1.  The user obtains 50 music tracks from the Proseware online store. Each track is a file with the .wma file name extension. Along with the tracks, the user obtains licenses to play the tracks.
2.  The user copies the 50 tracks to a new computer that has Windows Media Player 11 installed and adds the tracks to the Windows Media Player library.
3.  At some later time, the License Refresh Module (LRM), which is part of Windows Media Player 11, inspects the metadata in the fifty tracks and determines that Proseware is the content provider.
    > [!Note]  
    > Windows Media Player is able to identify the content provider by inspecting the **ContentDistributor** attribute in a media file. If an online store that has the PlaysForSure logo provides a media file that uses Windows Media Digital Rights Management (WMDRM), the online store must place the **ContentDistributor** attribute in the media file. For more information, see Adding the Content Distributor Attribute in the Windows Media Player SDK.

     

4.  The LRM looks up the URL of Proseware's ServiceInfo document, downloads the document, and inspects the document's **Install** element to obtain the URL of a package that the LRM can use to install Proseware's component. The LRM installs and loads the component.
5.  For each of the 50 tracks, the LRM calls the Proseware component's [IWMPSubscriptionService::allowPlay](/previous-versions/windows/desktop/api/subscriptionservices/nf-subscriptionservices-iwmpsubscriptionservice-allowplay) method. The **allowPlay** method places a license for the individual track on the new computer and returns **TRUE** in the *pfAllowPlay* parameter.
    > [!Note]  
    > The Proseware component must provide all licenses required to play the individual track. That is, the component must provide both a root license and a leaf license if needed.

     

    During the first call to the **allowPlay** method, the Proseware component must display a dialog box to verify that the current user has a Proseware account and has the right to play the track. During subsequent calls to **allowPlay**, the component can use the credentials that it obtained in the first call to verify that the user has the right to play the remaining tracks.

The component, which is written by the online store, must implement the **allowPlay** method of the **IWMPSubscriptionService** interface. The component must return E\_NOTIMPL from each of the other three methods: **allowCDBurn**, **allowPDATransfer**, and **startBackgroundProcessing**. Also, the component must set the value of the **Capabilities** registry entry to 1; that is, the SUBSCRIPTION\_CAP\_ALLOWPLAY capability flag must be set, and all other capability flags must be cleared. For more information about registering the component, see [Registry Keys and Entries for a Type 2 Online Store](registry-keys-and-entries-for-a-type-2-online-store.md).

For information about creating a component that implements the **IWMPSubscriptionService** interface, see [Building the Plug-in for a Type 2 Online Store](building-the-plug-in-for-a-type-2-online-store.md).

For information about providing Microsoft with a ServiceInfo document, send email to the Windows Media Player Virtual Services team. The team's email address is mpsvctm@microsoft.com.

For technical guidance on using a variety of Windows Media SDKs to create a service that offers licensed digital media content, go to the [Microsoft Windows Media Developer Center](https://msdn.microsoft.com/windowsmedia/default.aspx) and search for "Creating a Windows Media Player 10 Subscription Online Store".

## Related topics

<dl> <dt>

[**ServiceInfo Document**](serviceinfo-document.md)
</dt> <dt>

[**Windows Media Player Online Stores**](windows-media-player-online-stores.md)
</dt> </dl>

 

 




