---
title: Windows Media Player Online Stores
description: Windows Media Player Online Stores
ms.assetid: 81009d7b-5c2a-4447-a85e-138ab7834b7a
keywords:
- Windows Media Player online stores,about
- online stores,about
ms.topic: article
ms.date: 05/31/2018
---

# Windows Media Player Online Stores

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

Windows Media Player provides functionality that allows digital media content providers to integrate their services with Windows Media Player. Integration between the Player and an online digital media store provides an enjoyable, comprehensive experience for the user, including the ability to locate content, download and manage files, play content, and copy content to CDs or devices.

## Contacting Microsoft

If you would like your online digital media store to be integrated with Windows Media Player, but you have not yet made contact with Microsoft, you can get started by sending email to the Windows Media Player Services Virtual Team. The team's email address is mpsvctm@microsoft.com.

## For More Information

For technical guidance on using a variety of Windows Media SDKs to create a service that offers licensed digital media content, go to the [Microsoft Windows Media Developer Center](https://msdn.microsoft.com/windowsmedia/default.aspx) and search for "Creating a Windows Media Player 10 Subscription Online Store".

## Online Stores in Windows Media Player 9 Series

Windows Media Player 9 Series introduced the concept of online stores. In Windows Media Player 9 Series, online store providers could integrate their services into the **Premium Services** feature of Windows Media Player.

## Online Stores in Windows Media Player 10

In Windows Media Player 10, premium services were renamed online stores, and the following new features were added:

-   Windows Media Player provides up to three task panes for use by the online store.
-   When a user chooses, in the Player's user interface, to view more information about digital media content, Windows Media Player calls on the online store to provide the information.
-   When the user chooses, in the Player's user interface, to buy a media item, Windows Media Player call on the online store to handle the purchase.
-   The online store can provide a plug-in that Windows Media Player calls for assistance with digital rights management and the timing of background processing.
-   Online stores can be integrated with Windows Media Player setup.

## Online Stores in Windows Media Player 11

Windows Media Player 11 introduces a new type of online music store, one that is more deeply integrated into the Player's user interface. In Windows Media Player 11, the following new features have been added to support this new type of online store.

-   Windows Media Player downloads the online store's media catalog, so the user can browse the online store's content quickly.
-   Windows Media Player displays the online store's music content in the library tree view control.
-   As the user navigates in the Player's user interface, the Player calls on the online store to provide webpages that enhance the user's experience.
-   The online store provides a plug-in that handles all aspects of the communication between Windows Media Player and the online store. For example, the plug-in handles login, license renewal, catalog upgrade, downloading of content, and purchasing of content.
-   Windows Media Player provides enhanced communication between the Player and webpages that are provided by the online store and hosted in the Player.

## Types of Online Stores

There are two types of online stores: type 1 and type 2.

A type 1 store provides the most advanced level of integration with Windows Media Player. It provides a downloadable music catalog and is deeply integrated into the Player's user interface. Type 1 stores are supported by Windows Media Player 11 and later.

Type 2 stores, which are supported by Windows Media Player 9 Series and later, have two subcategories: commerce stores and music stores.

A commerce store provides the most basic experience by providing up to three service task panes that display the store's webpages.

A music store provides a more integrated experience for the user than a commerce store. In a music store, users can click buttons and links in Windows Media Player (outside of the webpages provided by the store) to perform actions like buying a CD or DVD, getting more information about a particular media item, or displaying the Info Center View pane. In each case, Windows Media Player calls the current music store to handle these requests.

> [!Note]  
> Some documents refer to commerce stores as basic commercial services and refer to music stores as integrated music services.

 

The following table shows the features available to the different types of online stores.




| Feature | Type 2 commerce store | Type 2 music store | Type 1 store | 
|---------|-----------------------|--------------------|--------------|
| Create service task panes<blockquote>[!Note]<br />Windows Media Player 10 has up to three service task panes. Windows Media Player 11 has only one.</blockquote><br /> | Yes | Yes | Yes | 
| Change the appearance of the store by changing attributes like button color, taskbar color, and button text. | Yes | Yes | Yes | 
| Add logo images to the Windows Media Player online store menu and taskbar. | Yes | Yes | Yes | 
| Navigate from HTMLView to the online store. | Yes | Yes | Yes | 
| Handle Windows Media Player requests to purchase a CD or DVD. | No | Yes | Yes | 
| Handle Windows Media Player requests to provide rich album information. | No | Yes | Yes | 
| Provide the Info Center View webpage. | No | Yes | Yes | 
| Customize Windows Media Player setup to specify an initial online store. | No | Yes | Yes | 
| Provide a plug-in that implements <a href="/previous-versions/windows/desktop/api/subscriptionservices/nn-subscriptionservices-iwmpsubscriptionservice"><strong>IWMPSubscriptionService</strong></a>.<blockquote>[!Note]<br />In Windows Media Player 10 and later, this plug-in can also implement <a href="/previous-versions/windows/desktop/api/subscriptionservices/nn-subscriptionservices-iwmpsubscriptionservice2"><strong>IWMPSubscriptionService2</strong></a>.</blockquote><br /> | No | Yes | No | 
| Provide a music catalog that is downloaded by Windows Media Player | No | No | Yes | 
| Provide customized webpages and context menus based on the user's navigation throughout the Player's user interface. | No | No | Yes | 
| Provide a plug-in that implements <a href="/previous-versions/windows/desktop/api/contentpartner/nn-contentpartner-iwmpcontentpartner"><strong>IWMPContentPartner</strong></a>. | No | No | Yes | 




 

The remainder of the documentation about online stores is divided into the following sections.



| Section                                                                                                                              | Description                                                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [Online Stores Welcome Kit](online-stores-welcome-kit.md)                                                                           | Contains information about how to bring an online digital media store on board in Windows Media Player.             |
| [Type 1 Online Stores](type-1-online-stores.md)                                                                                     | Contains About, Guide, and Reference sections for Type 1 online stores.                                             |
| [Type 2 Online Stores](type-2-online-stores.md)                                                                                     | Contains About, Guide, and Reference sections for Type 2 online stores.                                             |
| [Information Common to Type 1 and Type 2 Online Stores](information-common-to-type-1-and-type-2-online-stores.md)                   | Contains information that applies to both Type 1 and Type 2 online stores.                                          |
| [Refreshing Licenses for Stores That Have the PlaysForSure Logo](refreshing-licenses-for-stores-that-have-the-playsforsure-logo.md) | Contains information about how online stores that are not integrated with Windows Media Player can update licenses. |



 

## Related topics

<dl> <dt>

[**Windows Media Player SDK**](windows-media-player-sdk.md)
</dt> </dl>

 

 





