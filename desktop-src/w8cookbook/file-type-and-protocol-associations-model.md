---
title: File type and URI associations model
description: File type and URI associations model
ms.assetid: 4DE7DD08-088A-4E09-B1C7-AE9033EA533D
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# File type and URI associations model

## Platforms

<dl> **Clients** - Windows 8  
**Servers** - Windows Server 2012  
</dl>

## Description

The file type and URI association model has changed in Windows 8. Apps are no longer able to programmatically set themselves as the default handler for a file type or URI. Instead, now the user always controls what the default handler is for a file type or URI scheme.

## Manifestation

How this change presents to the user depends upon how the app is designed, for example:

-   Many apps check to see if they are the default every time they run and, if they are not, they prompt the user to set them as default. However, because apps can no longer accurately query to determine which app is the default handler for a file type or URI scheme, neither of these operations works.
-   Many apps have a dialog box or menu built in or in their installer that specifies the file types for which the app should serve as the default. However, because apps can no longer programmatically set themselves as the default handler for a file type or URI scheme, this no longer works.

## Mitigation

There are several things users can do to accommodate these changes:

-   Users are prompted contextually to choose a default app to handle file types, URI schemes, or both when one has not been specified
-   Users are offered the option to change their default handler after installing new apps that can handle a file type or URI scheme
-   The default programs control panel allows users to set defaults for an app, or for a file type, URI scheme, or both; apps can link to the control panel
-   Defaults can be changed from Windows Explorer

## Solution

As a result of these changes, this API guidance is provided:

-   The functionality of some method calls within the [IApplicationAssociationRegistration](http://go.microsoft.com/fwlink/p/?LinkId=325451) API has changed, and should no longer be used.

    -   **Do not** call [QueryAppIsDefault](http://go.microsoft.com/fwlink/p/?LinkId=325452)/[QueryAppIsDefaultAll](http://go.microsoft.com/fwlink/p/?LinkId=325453) to determine if an app is the default
    -   **Do not** call [QueryCurrentDefault](http://go.microsoft.com/fwlink/p/?LinkId=325454) to determine which app (if any) is the current default
    -   **Do not** call [SetAppIsDefault](http://go.microsoft.com/fwlink/p/?LinkId=325455)/[SetAppIsDefaultAll](http://go.microsoft.com/fwlink/p/?LinkId=325456) to set the default app

-   The guidance going forward is:

    -   **Do not** query to see which app is the default handler for file types or URI schemes

    -   **Do not** attempt to monitor changes in the default handler for file types or URI schemes

    -   **Do not** attempt to set an app as the default handler for file types or URI schemes

    -   **Do not** attempt to manage defaults for file types or URI schemes from within an app

    -   **Do** integrate with the [Set Default Programs](http://go.microsoft.com/fwlink/p/?LinkId=325457) control panel if you want to allow users of your app to access the default management UI (the management UI within the app is no longer supported)

        -   Calling [IApplicationAssociationRegistrationUI::LaunchAdvancedAssociationUI](http://go.microsoft.com/fwlink/p/?LinkId=325458) allows the user to access the ‘[Set Default Programs](http://go.microsoft.com/fwlink/p/?LinkId=325457)’ control panel page for the specified app

## Tests

-   Test to verify that apps register properly in Set Default Programs control panel
-   Test to verify that apps register properly to appear in the OpenWith list for the file types, URI schemes, or both, that they register to handle
-   Test to verify that new app notifications appear after your app is installed and the user invokes a file type, URI scheme, or both, that your app has registered to handle

## Resources

-   [Best Practices for File Type and URI Associations in Windows 8 Desktop Apps](http://go.microsoft.com/fwlink/p/?linkid=228165)
-   [File Type Associations and AutoPlay Build Conference Presentation](http://go.microsoft.com/fwlink/p/?LinkId=325427)

 

 




