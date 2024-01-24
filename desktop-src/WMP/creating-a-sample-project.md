---
title: Creating a Sample Project
description: Creating a Sample Project
ms.assetid: 9cbbd1a7-88e7-4947-8dca-e06e364102f7
keywords:
- Windows Media Player online stores,creating sample projects
- online stores,creating sample projects
- type 2 online stores,creating sample projects
- Windows Media Player online stores,sample projects
- online stores,sample projects
- type 2 online stores,sample projects
- Windows Media Player online stores,project wizard
- online stores,project wizard
- type 2 online stores,project wizard
- plug-ins,project wizard
- Windows Media Player plug-ins,project wizard
- creating sample projects
- samples,type 2 online stores
- project wizard
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Creating a Sample Project

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

To create a new project using the project wizard, follow these steps:

1.  Open Microsoft Visual Studio.
2.  From the **File** menu, point to **New**, and then click **Project**.
3.  In the **Project Types** list box, choose **Visual C++ Projects**.
4.  In the **Templates** list box, choose **Windows Media Player Online Stores Wizard**.
5.  Type a name and location for your project.
6.  Click **OK** to start the project wizard.
7.  Select **Type 2 (Basic integration)**, and click **Next**.
8.  Type the friendly name and content distributor ID for your service. Type the URL for the webpage that removes the service from the user's computer.
    > [!Note]  
    > The value you provide for the content distributor ID must not contain spaces. The wizard removes any spaces from the string you provide.

     

9.  Click **Finish** to create the project.

The wizard automatically generates a new C++ project that creates a type 2 online store plug-in that implements the **IWMPSubscriptionService** and **IWMPSubscriptionService2** interfaces. Each time you run the wizard it creates the same project, but the component that is created when you compile the project has a unique class ID. The project name, the friendly name, and content distributor ID may also be different depending on the values you provided when you ran the wizard. The sample project registers the component by using a key name that matches the value you supplied for the friendly name.

The sample uses Active Template Library (ATL) code to provide COM implementations.

The wizard creates the following files for you:

-   *ProjectName*dll.cpp. Implements the Dynamic Link Library (DLL) exports such as the main DLL entry point function. Also contains the ATL object map and module declaration.
-   *ProjectName*.cpp. Contains default implementations for the methods of the IWMPSubscriptionService and IWMPSubscriptionService2 interfaces. Also contains code to define the dialog boxes that the sample opens when methods are called by Windows Media Player.
-   *ProjectName*.def. Declares the DLL exports.
-   StdAfx.cpp. Includes standard headers.
-   wmp.h. The Windows Media Player header file.
-   wmpplug.h. The Windows Media Player plug-in header file.
-   subscriptionservices.h. The Windows Media Player online stores header file.
-   resource.h. Contains resource definitions.
-   **ProjectName**.h. Contains class definitions for the online store object and the dialog boxes. Defines the object's class ID and the content distributor ID constant.
-   StdAfx.h. Contains standard system includes.
-   *ProjectName*.rc. The resource script file. This contains definitions for the dialog box resources and controls. This is also where the string table is stored. The string table contains your project name and friendly name string constants. Usually you work with this file in the Visual Studio resource editor, not as plain text.
-   *ProjectName*.rgs. The registry script file. This file contains the information used to add your component class to the registry so Windows Media Player can locate it. You can change the key name for your service in this file.

> [!Note]  
> You should set the base address for your DLL to 0x0F100000 to avoid conflicts with Windows Media Player.

 

## Related topics

<dl> <dt>

[**Building the Plug-in for a Type 2 Online Store**](building-the-plug-in-for-a-type-2-online-store.md)
</dt> <dt>

[**IWMPSubscriptionService Interface**](/previous-versions/windows/desktop/api/subscriptionservices/nn-subscriptionservices-iwmpsubscriptionservice)
</dt> <dt>

[**IWMPSubscriptionService2 Interface**](/previous-versions/windows/desktop/api/subscriptionservices/nn-subscriptionservices-iwmpsubscriptionservice2)
</dt> </dl>

 

 




