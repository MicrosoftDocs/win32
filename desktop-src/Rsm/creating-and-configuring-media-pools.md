---
Description: Applications use media pools to hold media that share common attributes.
ms.assetid: 1eefa52b-f490-487b-b010-263fa96d762a
title: Creating and Configuring Media Pools
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating and Configuring Media Pools

\[[Removable Storage Manager](removable-storage-manager.md) is no longer available as of Windows 7 and Windows Server 2008 R2.\]

Applications use media pools to hold media that share common attributes. These attributes are: media type, relationship to the free pool and security. These properties are set on a pool and all media in that pool are then governed by these properties. All media in a pool are of the same type. Accessibility to each cartridge in the pool is governed by the ACL placed on the pool. The media pool used by the application determines what happens when an application requires a new cartridge or is done with a cartridge.

Your application might use two media pools, for example, if it needs to use cartridges of two different types. Similarly, your application might need to use two media pools if it has some cartridges that must only be accessible to certain users and other cartridges that are available to every one.

The following points should be considered when you set the parameters for this function and configure the media pool:

-   Available media types

    You can enumerate the media pools in the free media pool folder to generate a list of the media types in an RSM system. You can enumerate the media type object to list all the media types supported by RSM. You can also enumerate the media type object of each library in the system.

-   Automatic media draw

    Decide whether RSM will automatically draw media from the free pool when there are no media set to the Available state in the media pool.

-   Automatic media return

    Decide whether RSM will automatically return media to the free pool when the media are no longer needed.

-   Media pool security

    Decide what level of security you want to assign to the media pool.

The first task your application should perform, usually when installed, is to create and configure media pools. You can use the [**CreateNtmsMediaPool**](/windows/desktop/api/Ntmsapi/nf-ntmsapi-createntmsmediapool) function to create media pools.

 

 



