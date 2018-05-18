---
title: Extending the WAB Property Sheets
description: The WAB has an extensibility mechanism by which a client application can add its own property sheets to the WAB's predefined set of property sheets. This document describes how to extend the WAB Property Sheets for WAB contacts and groups.
ms.assetid: '5770cd32-3d44-4b36-8d55-3251a994a7c7'
keywords: ["address books", "Windows Address Book (WAB),property sheets", "WAB (Windows Address Book),property sheets", "Windows Address Book (WAB),registering property sheet extensions", "WAB (Windows Address Book),registering property sheet extensions", "registering WAB property sheet extensions"]
---

# Extending the WAB Property Sheets

New applications should not use this set of interfaces. These interfaces exist for backward compatibility with legacy applications. These interfaces will be unavailable in the future.

> [!Note]  
> In Windows Vista, Windows Contacts replaces Windows Address Book (WAB). For more information about this new mechanism for storing and retrieving contact information, see [Windows Contacts](_wincontacts_entry_point).

 

WAB clients are able to extend the WAB schema easily by using named properties for storing private client-specific data. Although clients can provide their own user interface (UI) for modifying the private data, clients might want the user to access private data through the user interface that is consistent and unified with the WAB's native details UI for contacts and groups. The WAB has an extensibility mechanism by which a client application can add its own property sheets to the WAB's predefined set of property sheets. This document describes how to extend the WAB Property Sheets for WAB contacts and groups.

## Overview

A client can add a property sheet to the WAB by:

1.  Implementing the property sheet UI and UI handler in a separate module (DLL).
2.  Implementing [IShellPropSheetExt](_win32_IShellPropSheetExt) and [**IWABExtInit**](-wab-iwabextinit.md) to expose its property sheets.
3.  Registering its property sheet extension DLL in the registry under HKCR\\CLSID.
4.  Registering its CLSID under the WAB's registry key.

Because multiple clients can register their own property sheets with the WAB, the WAB might load and invoke modules from several different clients every time the user opens properties on a contact. For performance reasons, it is highly recommended that the client implement the property sheet extension module as a small separate DLL whose functionality is limited to data display and data validation only.

An extension property sheet must only allow modification of the client's private named properties. This ensures that two or more extension property sheets are not providing duplicate user interfaces to modify the same standard property. In the event that two or more property sheets provide user interfaces to modify the same property, it is undefined which property sheet gets preference when saving data to the WAB's store.

The process of creating property sheet extensions for groups is similar to that for creating extensions for contacts. The two processes differ only in where the extension is registered.

You can choose at all times whether to display your property sheet from any WAB-related process or choose to show the property sheet extension only within your own process. See [Registering Your Property Sheet Extension](#registering-your-property-sheet-extension).

## Creating the Property Sheet Extension DLL

Create your property sheet UI and a function handler for the property sheet in your module. Your property sheet can have a maximum size of 318 x 203 dialog units (dlus). Property sheets that are larger than this are not recommended, because they disrupt the consistent look of the other WAB property pages.

To expose your property sheet, you must implement the [IShellPropSheetExt](_win32_IShellPropSheetExt) interface. You must also implement the [**IWABExtInt**](-wab-iwabextinit.md) interface defined in Wabapi.h. This interface has the standard [IUnknown](33f1d79a-33fc-4ce5-a372-e08bda378332) methods, as well as [**IWABExtInit::Initialize**](-wab-iwabextinit-initialize.md).

When the WAB is ready to create your property sheet, it retrieves your module's CLSID and calls [CoCreateInstance](7295a55b-12c7-4ed0-a7a4-9ecee16afdec) on the CLSID specifying IID\_IShellPropSheetExt to request a [IShellPropSheetExt Interface](_win32_IShellPropSheetExt) object.

The WAB calls [IUnknown::QueryInterface](54d5ff80-18db-43f2-b636-f93ac053146d) on the returned object, requesting an [**IWABExtInit**](-wab-iwabextinit.md) object. The WAB then calls [**Initialize**](-wab-iwabextinit-initialize.md) to provide your module with information about the object that is being displayed.

To add your page, the WAB calls [IShellPropSheetExt::AddPages Method](_win32_IShellPropSheetExt_AddPages). In this call, you can create as many property sheets as you want by calling [CreatePropertySheetPage](_win32_CreatePropertySheetPage) and passing the resulting **HPROPSHEETPAGE** handle and *lParam* to the WAB through the *lpfnAddPage* function.

The [IShellPropSheetExt::ReplacePage Method](_win32_IShellPropSheetExt_ReplacePage) method is not supported at present and will not be invoked by the WAB.

The WAB uses your **HPROPSHEETPAGE** handle to add your property sheet to its set of preexisting property sheets. When the user switches to or from your property sheet, and makes modifications on your property sheets, your property sheet handler function will automatically be invoked.

When the WAB invokes [**Initialize**](-wab-iwabextinit-initialize.md), it will pass a pointer to a [**WABEXTDISPLAY**](-wab-wabextdisplay.md) structure. The object being displayed is available to user's property sheet through the **lpPropObj** member of the **WABEXTDISPLAY** structure.

When your property sheet has been activated by the user, it receives a [PSN\_ACTIVE](_win32_PSN_SETACTIVE) notification. The property sheet must then retrieve its relevant properties from the object by calling [IMAPIProp::GetProps](68b1621a-ba95-44a6-9433-56e59fafbcfe) and use these properties to populate the UI.

When your page receives a [PSN\_KILLACTIVE](_win32_PSN_KILLACTIVE) notification and loses focus, you must update the relevant properties on the object. This is done by calling [IMAPIProp::DeleteProps](7825c1aa-c5a8-4211-b782-a82846cbb7c6) to clear any properties that have been deleted by you and calling [IMAPIProp::SetProps](2d255c31-b855-4bf0-9e64-5a1401b7d992) to set any new data added. You thereby ensure that the data is accessible to all other property sheets at all times. At no point should your property page call [IMAPIProp::SaveChanges](CD0D7010-EA53-4053-87C7-92E4EA6454C3) on the object, as this might cause unintended data loss. The WAB determines if and when to persist any changes made to the object.

## Registering Your Property Sheet Extension

After you have created your property sheet extension module, you need to register it with both the system and the WAB.

Register your property sheet extension module with the system just as you would register a [Shell Property Sheet Extension module](_win32_propsheet_handlers).

With the WAB, you can create property sheet extensions for Contacts ([**IMailUser**](-wab-imailuser.md) objects), Distribution Lists ([**IDistList**](-wab-idistlist.md) objects), or both.

### Registering for Contacts

To register property sheet extension under the WAB for extending the UI on Contacts ([**IMailUser**](-wab-imailuser.md) objects), place this information in the registry:


```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         WAB
            WAB4
               ExtDisplay
                  MailUser
```



Create a new string value whose name is the full CLSID identifying your extension module, as it is registered with the system. The value data can be set to the string "0" or to the string "1". The string "0" signifies that your property sheet should be shown at all times, whenever the WAB is asked to display its property sheets. The string "1" means that your property sheet will only be shown as part of your own process.

If you want to add a property sheet that will only be shown within your own process, identify your process to the WAB. To do this, pass the GUID used for registering the property sheet extension into the **guidPSExt** member of the [**WAB\_PARAM**](-wab-wab-param.md) structure passed into [**WABOpen**](-wab-wabopen.md). When the WAB needs to load property sheets, it will load your extension only if the GUID matches and the Value-data is "1". The WAB will automatically load all extensions with value data "0".

### Registering for Distribution Lists

To register your property sheet extension for extending the UI on Groups ([**IDistList**](-wab-idistlist.md) objects), register the same information as for the property sheet extension under the following key.


```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         WAB
            WAB4
               ExtDisplay
                  DistList
```



> [!Note]
>
> The Wab32.dll that ships with Microsoft Internet Explorer 4.01  Service Pack 1 (SP1) (Windows 98 version) may prevent the WAB from loading the property sheets unless two keys exist. One key is HKLM\\Software\\Microsoft\\WAB\\WAB4\\ExtDisplay\\MailUser. The other is HKLM\\Software\\Microsoft\\WAB\\WAB4\\ExtDisplay\\DistList. Neither key needs to contain any values, but both keys must exist for any extension property sheets to be loaded. Even if the application is providing extensions for only one type of object (MailUser or DistList), make sure that the application creates both the keys, not just one, for this feature to work correctly under Internet Explorer 4.01.

 

## Related topics

<dl> <dt>

[Extending the WAB Toolbar and Context Menu Actions](-wab-extending-context-menus.md)
</dt> </dl>

 

 




