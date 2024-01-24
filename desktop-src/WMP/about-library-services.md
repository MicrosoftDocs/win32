---
title: About Library Services
description: About Library Services
ms.assetid: 2334aa4a-7988-481d-9b21-9f7b432fbd05
keywords:
- Windows Media Player,library
- Windows Media Player object model,library
- object model,library
- Windows Media Player ActiveX control,library for object model
- ActiveX control,library for object model
- Windows Media Player Mobile ActiveX control,library for object model
- Windows Media Player Mobile,library for object model
- Windows Media Player library,about
- Windows Media Player library,services
- library,services
- library,about
- versions of Windows Media Player,library services
- enumerations,library services
- events,library services
- samples,library services
- interfaces,library services
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About Library Services

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

In earlier versions of Windows Media Player, the software used a single library database for each user. This database was stored on the user's computer and was conceptually tied to the user and a particular instance of the Player.

Windows Media Player 11 introduces the concepts of multiple and remote libraries. Now, in addition to its default, or *local*, library, Windows Media Player can display content retrieved from libraries on other computers connected to a network, which might include other users logged on to the same computer. The Player can also display library views from other sources, such as MTP-enabled devices or data CDs. From the end user's perspective, this means that digital media content located in many different places can be managed from multiple locations by using the same, familiar Windows Media Player user interface. From the developer's perspective, this means that you can use the Windows Media Player SDK COM interfaces to enumerate the available libraries and then use them like you have used the local library in earlier versions.

To enumerate the available libraries, use the **IWMPLibraryServices** interface. This interface exposes the [IWMPLibraryServices::getCountByType](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmplibraryservices-getcountbytype) method, which retrieves the count of libraries of a given type. Library types are defined by the [WMPLibraryType](/previous-versions/windows/desktop/api/wmp/ne-wmp-wmplibrarytype) enumeration. This enumeration includes a value for the local library, wmpltLocal. This is because the library services feature always enables you work with the local library by using **IWMPLibraryServices** and the related interfaces.

> [!Note]  
> The **WMPLibraryType** enumeration includes the value wmpltRemote, which represents media libraries shared by the network. To access those shared libraries, the Player control must be running in remote mode. For information about running the Player control in remote mode, see [Remoting the Windows Media Player Control](remoting-the-windows-media-player-control.md).

 

After you retrieve the library count, you can iterate the collection of available libraries by repeatedly calling [IWMPLibraryServices::getLibraryByType](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmplibraryservices-getlibrarybytype) in a loop, passing a new index value with each iteration. This method retrieves a pointer to an [IWMPLibrary](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmplibrary) interface, which represents the individual library.

After you retrieve a pointer to **IWMPLibrary**, you can call [IWMPLibrary::get\_mediaCollection](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmplibrary-get_mediacollection) to retrieve a pointer to an **IWMPMediaCollection** interface. With this interface pointer, you can work with an individual library much like you would use the local library. You can also retrieve a string containing the name of the library by calling [IWMPLibrary::get\_name](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmplibrary-get_name), which is useful if you need to display the library name to the user. You can call [IWMPLibrary::get\_type](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmplibrary-get_type) to get the **WMPLibraryType** of a particular library.

You can handle the [IWMPEvents3::LibraryConnect](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpevents3-libraryconnect) event to know when a library becomes available and the [IWMPEvents3::LibraryDisconnect](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpevents3-librarydisconnect) event to know when a library disconnects. Each of these events provides an **IWMPLibrary** pointer that represents the library that connected or disconnected. You can call [IWMPLibrary::isIdentical](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmplibrary-isidentical) to determine whether the library that connected or disconnected is a library that you are currently using.

There are some important differences when you work with a library retrieved through the **IWMPLibraryServices** interface compared to working with a library retrieved by using [IWMPCore::get\_mediaCollection](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpcore-get_mediacollection). The following differences apply:

-   You can usually retrieve query results much faster from libraries retrieved through **IWMPLibraryServices**. (This assumes that other factors such as network and hard disk access times are equal.)
-   The list of media item metadata attributes available from libraries retrieved through **IWMPLibraryServices** is usually a subset of those available from the local library retrieved through [IWMPCore](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpcore).
-   If you retrieve the local library through **IWMPLibraryServices**, all of the same attributes are available for your use as those available when you retrieve the local library through **IWMPCore**. However, you will be able to retrieve query results much faster for the most commonly-used attributes.
-   You should use string collections to create user interface elements when you work with libraries retrieved through **IWMPLibraryServices**. For example, [IWMPMediaCollection2::getStringCollectionByQuery](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpmediacollection2-getstringcollectionbyquery) enables you to use a custom query (represented by the **IWMPQuery** interface) to retrieve a string collection.
-   Remote libraries retrieved through the **IWMPLibraryServices** interface might not always be connected to the current Player instance. This means that it is important to handle the **LibraryConnect** and **LibraryDisconnect** events to know when library availability changes, and to handle the [IWMPEvents3::StringCollectionChange](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpevents3-stringcollectionchange) event to know when strings are added to or removed from the string collections you use to display user interface elements. You should also handle **StringCollectionChange** events for the local library for similar reasons.

It is important to understand that string collections for a particular library can change at any time. A string collection could be empty when you first retrieve it, as in the case of a library that has recently connected but the Player has not yet enumerated its contents. Conversely, a string collection might already contain all the information you need. In this case, you might never receive a **StringCollectionChange** event because the library's contents had been completely enumerated before you created your query and nothing else is changing.

Therefore, to keep your user interface current, you must both enumerate the string collection contents when you retrieve the **IWMPStringCollection** interface and handle the **StringCollectionChange** event to know about updates when they happen.

## Sample

The sample named WMPML demonstrates how to work with library services. For more information about Windows Media Player SDK samples, see [Samples](samples.md).

## Related topics

<dl> <dt>

[**About the Library**](about-the-library.md)
</dt> <dt>

[**About the Query Object**](about-the-query-object.md)
</dt> <dt>

[**IWMPEvents3 Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpevents3)
</dt> <dt>

[**IWMPLibrary Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmplibrary)
</dt> <dt>

[**IWMPLibrary Interface (VB and C#)**](iwmplibrary--vb-and-c.md)
</dt> <dt>

[**IWMPLibraryServices Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmplibraryservices)
</dt> <dt>

[**IWMPLibraryServices Interface (VB and C#)**](iwmplibraryservices--vb-and-c.md)
</dt> <dt>

[**IWMPMediaCollection Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpmediacollection)
</dt> <dt>

[**IWMPMediaCollection Interface (VB and C#)**](iwmpmediacollection--vb-and-c.md)
</dt> <dt>

[**IWMPStringCollection Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpstringcollection)
</dt> <dt>

[**IWMPStringCollection Interface (VB and C#)**](iwmpstringcollection--vb-and-c.md)
</dt> <dt>

[**IWMPQuery Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpquery)
</dt> <dt>

[**IWMPQuery Interface (VB and C#)**](iwmpquery--vb-and-c.md)
</dt> <dt>

[**Working with the Library**](working-with-the-library.md)
</dt> </dl>

 

 




