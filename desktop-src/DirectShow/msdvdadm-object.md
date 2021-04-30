---
description: MSDVDAdm Object
ms.assetid: 753d2820-4d47-4e07-9f54-9b996e55f0b6
title: MSDVDAdm Object
ms.topic: article
ms.date: 05/31/2018
---

# MSDVDAdm Object

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

> [!Note]  
> This API is deprecated. For information about DVD playback and navigation in DirectShow, see [DVD Applications](dvd-applications.md).

 

The methods and properties of the `MSDVDAdm` "administration" object enable a scripting application to modify its default settings in the Microsoft® Windows® registry. The registry is a database on all Windows systems where applications can store information about themselves to be used on initialization or during run time.

Most of these methods and properties do not set or retrieve the current values in the [MSWebDVD](mswebdvd-object.md) object itself. This means, for example, that when you call **GetParentalLevel** the returned value is not the current parental level stored in the object. Rather, it is the default parental level stored in the registry. To get the current parental level, call the **MSWebDVD** method [**GetPlayerParentalLevel**](getplayerparentallevel-method.md). Calling [**SaveParentalLevel**](saveparentallevel-method.md) simply writes a new default parental access level to the registry; you still need to call the **MSWebDVD** method [**SelectParentalLevel**](selectparentallevel-method.md) to make the change take effect immediately in the **MSWebDVD** object. The default locale identifier (LCID) methods work in a similar way.

On the other hand, the [**BookmarkOnStop**](bookmarkonstop-property.md) and [**BookmarkOnClose**](bookmarkonclose-property.md) methods take effect immediately because the **MSWebDVD** object checks these settings just before the user stops playback or closes the application, rather than during initialization.

You access the `MSDVDAdm` object through the **DVDAdm** property of **MSWebDVD**. So, for example, if the **MSWebDVD** object is named "DVD," call **ChangePassword** as shown in the following code example.


```C++
DVD.DVDAdm.ChangePassword(sUserName, sOld, sNew)
```



**Methods and Properties**

The following table lists the methods and properties exposed by the MSDVDAdm object methods and properties.



| Method                                                          | Description                                                                                                                                                                      |
|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ChangePassword**](changepassword-method.md)                 | Saves a new application password in the registry.                                                                                                                                |
| [**SaveParentalLevel**](saveparentallevel-method.md)           | Saves a new default parental level to the registry.                                                                                                                              |
| [**SaveParentalCountry**](saveparentalcountry-method.md)       | Saves the application's new parental country/region to the registry.                                                                                                             |
| [**ConfirmPassword**](confirmpassword-method.md)               | Tests whether the specified password matches the previously saved password.                                                                                                      |
| [**GetParentalLevel**](getparentallevel-method.md)             | Retrieves the parental level that was last saved to the registry.                                                                                                                |
| [**GetParentalCountry**](getparentalcountry-method.md)         | Retrieves the parental country/region that was last saved to the registry.                                                                                                       |
| [**RestoreScreenSaver**](restorescreensaver-method.md)         | Restores the system screen saver settings.                                                                                                                                       |
| Property                                                        | Description                                                                                                                                                                      |
| [**DisableScreenSaver**](disablescreensaver-property.md)       | Turns the system screen saver on or off.                                                                                                                                         |
| [**DefaultAudioLCID**](defaultaudiolcid-property.md)           | Sets or retrieves the registry setting for the user-specified default LCID for the audio stream.                                                                                 |
| [**DefaultSubpictureLCID**](defaultsubpicturelcid-property.md) | Sets or retrieves the registry setting for the user-specified default LCID for the subpicture stream.                                                                            |
| [**DefaultMenuLCID**](defaultmenulcid-property.md)             | Sets or retrieves the registry setting for the user-specified default LCID for menus.                                                                                            |
| [**BookmarkOnStop**](bookmarkonstop-property.md)               | Sets or retrieves a value that tells the MSDVDAdm object whether to automatically save a bookmark of the current location and settings when the user clicks the **Stop** button. |
| [**BookmarkOnClose**](bookmarkonclose-property.md)             | Sets or retrieves a value that tells the MSDVDAdm object whether to automatically save a bookmark of the current location and settings when the user closes the application.     |



 

 

 



