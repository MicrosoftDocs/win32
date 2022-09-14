---
title: Customizing the Sample Project
description: Customizing the Sample Project
ms.assetid: 26031971-3d1b-4175-8fb3-f13b6c17dd01
keywords:
- Windows Media Player online stores,customizing sample projects
- online stores,customizing sample projects
- type 2 online stores,customizing sample projects
- Windows Media Player online stores,sample projects
- online stores,sample projects
- type 2 online stores,sample projects
- customizing sample projects
- samples,type 2 online stores
ms.topic: article
ms.date: 05/31/2018
---

# Customizing the Sample Project

When creating your own online store, you will want to change the implementations of the following methods in the file named YourProject.cpp:

-   **CYourProject::allowPlay**. Use this function to apply your business rules for permitting playback of protected content.
-   **CYourProject::allow CDBurn**. Use this function to apply your business rules for allowing users to copy protected content to a CD.
-   **CYourProject::allowPDATransfer**. Use this function to apply your business rules for allowing users to transfer protected content to a portable device.
-   **CYourProject::startBackgroundProcessing**. Use this function to initiate any background processing tasks you require. For example, you might use this as an opportunity to check for expired licenses.
-   **CYourProject::deviceAvailable**. Use this function to initiate any tasks related to a connected device.
-   **CYourProject::prepareForSync**. Use this function to perform necessary tasks just before synchronizing digital media to the device.
-   **CYourProject::serviceEvent**. Use this function to begin and end tasks that you want to run when your online store is the active one.
-   **CYourProject::stopBackgroundProcessing**. Use this function to stop any background processing tasks you started when Windows Media Player called **CYourProject::startBackgroundProcessing**.

## Working with Media and Playlist Objects

The **allowPlay** method provides a pointer to the **IWMPMedia** interface as a parameter. This interface is the Windows Media Player interface that represents media objects. By calling the methods on this interface, you can work with the attributes and properties of an individual media item.

The **allowCDBurn** and **allowPDATransfer** methods provide a pointer to the **IWMPPlaylist** interface as a parameter. This interface is the Windows Media Player interface that represents playlist objects. By calling the methods on this interface, you can work with the attributes and properties of a playlist, add items to a playlist, or remove items from a playlist.

To learn how to remove an item from a playlist programmatically, see the implementation of **CAllowBaseDialog&lt;T&gt;::OnRemoveMediaFromPlaylist**. To learn more about working with media and playlist objects, see [Player Object Model for Scripting Languages](player-object-model-for-scripting-languages.md).

## Code That Can Be Removed

You will probably want to remove the code that opens dialog boxes because it is unlikely that you will want users deciding which media items can be played or copied. From YourProject.h, remove the following code:

-   The declaration of **CAllowBaseDialog**.
-   The declaration of **CAllowBurnDialog**.
-   The declaration of **CAllowTransferDialog**.

From YourProject.cpp, remove the following code:

-   The implementation of **CAllowBaseDialog&lt;T&gt;::OnInitDialog**.
-   The implementation of **CAllowBaseDialog&lt;T&gt;::OnRemoveMediaFromPlaylist**.

## Related topics

<dl> <dt>

[**Building the Plug-in for a Type 2 Online Store**](building-the-plug-in-for-a-type-2-online-store.md)
</dt> </dl>

 

 




