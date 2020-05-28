---
title: Type 2 Online Store Plug-in
description: Type 2 Online Store Plug-in
ms.assetid: 16e90a01-20be-49a6-96df-de81a7283f42
keywords:
- Windows Media Player online stores,plug-ins
- online stores,plug-ins
- type 2 online stores,plug-ins
- Windows Media Player online stores,IWMPSubscriptionService interface
- online stores,IWMPSubscriptionService interface
- type 2 online stores,IWMPSubscriptionService interface
- plug-ins,Windows Media Player online stores
- plug-ins,online stores
- plug-ins,type 2 online stores
- plug-ins,IWMPSubscriptionService interface
- Windows Media Player plug-ins,type 2 online stores
- Windows Media Player plug-ins,online stores
- Windows Media Player plug-ins,Windows Media Player online stores
- Windows Media Player plug-ins,IWMPSubscriptionService interface
- IWMPSubscriptionService
ms.topic: article
ms.date: 05/31/2018
---

# Type 2 Online Store Plug-in

A type 2 online store plug-in is a COM component that implements the [IWMPSubscriptionService](/previous-versions/windows/desktop/api/subscriptionservices/nn-subscriptionservices-iwmpsubscriptionservice) interface and optionally the [IWMPSubscriptionService2](/previous-versions/windows/desktop/api/subscriptionservices/nn-subscriptionservices-iwmpsubscriptionservice2) interface. Windows Media Player 9 calls the methods of the **IWMPSubscriptionService** interface. Windows Media Player 10 or later calls the methods of both the **IWMPSubscriptionService** and **IWMPSubscriptionService2** interfaces.

A type 2 online store plug-in is packaged as an in-process COM server. That is, the plug-in is implemented in a .dll file that is mapped into the Windows Media Player process.

Windows Media Player activates type 2 online store plug-ins as needed. For example, suppose the user attempts to play a protected song, and there is no current license to play it. In that case, Windows Media Player inspects the **ContentDistributor** attribute in either the file header or the DRM header. If a value exists that matches the key name of an online store, Windows Media Player checks the registry to see whether that online store has provided a type 2 plug-in. If the plug-in exists, Windows Media Player loads the plug-in and calls its methods to determine whether the user is has the rights to play the song.

The following list describes some of the scenarios in which Windows Media Player calls a type 2 online store plug-in.

-   **The user attempts to play online store content.** When this happens, Windows Media Player calls the plug-in's [IWMPSubscriptionService::allowPlay](/previous-versions/windows/desktop/api/subscriptionservices/nf-subscriptionservices-iwmpsubscriptionservice-allowplay) method, passing a pointer to the digital media item that the user is attempting to play. The online store can use this as an opportunity to update the user's license to play the content or to disallow playback. If the plug-in returns **TRUE** in the *pfAllowPlay* parameter, Windows Media Player attempts to play the content. Playback will still fail if a valid license does not exist; this process does not circumvent digital rights management (DRM).
-   **The user requests permission to burn content to a CD or DVD.** When this happens, Windows Media Player calls the plug-in's [IWMPSubscriptionService::allowCDBurn](/previous-versions/windows/desktop/api/subscriptionservices/nf-subscriptionservices-iwmpsubscriptionservice-allowcdburn) method.
-   **The user attempts to synchronize online store content with a device, or Windows Media Player is ready to automatically synchronize online store content with a device.** When this happens, Windows Media Player calls the plug-in's [IWMPSubscriptionService2::prepareForSync](/previous-versions/windows/desktop/api/subscriptionservices/nf-subscriptionservices-iwmpsubscriptionservice2-prepareforsync) method to alert the online store that a media item is about to be synchronized with a particular device, which is identified by its canonical name. This is an opportunity for the online store to determine whether the user is allowed to synchronize the media item with the device. It is also an opportunity for the online store to prepare the device for synchronization and to update records, such as synchronization counts, associated with the device or the media item. The plug-in should pass the permission, preparation, and record-keeping tasks to a separate thread and return immediately from **prepareForSync**. When the separate thread has finished its work, it must notify Windows Media Player by calling [IWMPSubscriptionServiceCallback::onComplete](/previous-versions/windows/desktop/api/subscriptionservices/nf-subscriptionservices-iwmpsubscriptionservicecallback-oncomplete).
-   **A device becomes available for background processing.** When a device is connected, Windows Media Player alerts the online store that the device is available and idle by calling [IWMPSubscriptionService2::deviceAvailable](/previous-versions/windows/desktop/api/subscriptionservices/nf-subscriptionservices-iwmpsubscriptionservice2-deviceavailable).
-   **The user clicks a button to activate an online store in Windows Media Player.** When this occurs, Windows Media Player calls the plug-in's [IWMPSubscriptionService2::serviceEvent](/previous-versions/windows/desktop/api/subscriptionservices/nf-subscriptionservices-iwmpsubscriptionservice2-serviceevent) method. Windows Media Player also calls this method when the user switches to another service.
-   **Windows Media Player enters a state of low activity.** When this happens, the Player calls the plug-in's [IWMPSubscriptionService::startBackgroundProcessing](/previous-versions/windows/desktop/api/subscriptionservices/nf-subscriptionservices-iwmpsubscriptionservice-startbackgroundprocessing) method. The online store can use this opportunity to start or wake up any threads that perform background tasks, such as renewing expired licenses or compiling play-count data.
-   **Windows Media Player enters a state of high activity.** When this happens, Windows Media Player calls the plug-in's [IWMPSubscriptionService2::stopBackgroundProcessing](/previous-versions/windows/desktop/api/subscriptionservices/nf-subscriptionservices-iwmpsubscriptionservice2-stopbackgroundprocessing) method. This informs the plug-in that it must suspend any threads that are performing background tasks.

Windows Media Player releases the online store component when the Player session ends. Upon release, the component must interrupt any background processing in progress and then shut down.

## Related topics

<dl> <dt>

[**IWMPSubscriptionService Interface**](/previous-versions/windows/desktop/api/subscriptionservices/nn-subscriptionservices-iwmpsubscriptionservice)
</dt> <dt>

[**IWMPSubscriptionService2 Interface**](/previous-versions/windows/desktop/api/subscriptionservices/nn-subscriptionservices-iwmpsubscriptionservice2)
</dt> <dt>

[**IWMPSubscriptionServiceCallback Interface**](/previous-versions/windows/desktop/api/subscriptionservices/nn-subscriptionservices-iwmpsubscriptionservicecallback)
</dt> <dt>

[**Type 2 Online Store Samples**](type-2-online-store-samples.md)
</dt> </dl>

 

 




