---
Description: An explicit Application User Model ID (AppUserModelID) used to associate processes, files, and windows with a particular application.
ms.assetid: 07858b3c-e601-40ec-a87a-d66612d5473a
title: System.AppUserModel.ID
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.AppUserModel.ID

An explicit Application User Model ID (AppUserModelID) used to associate processes, files, and windows with a particular application. In some cases, it is sufficient to rely on the internal AppUserModelID assigned to a process by the system. However, an application that owns multiple processes or an application that is running in a host process might need to explicitly identify itself through this property so that it can group its otherwise disparate windows under a single taskbar button and control the contents of that application's Jump List.

To set this property on a window, use [**SHGetPropertyStoreForWindow**](/windows/desktop/api/Shellapi/nf-shellapi-shgetpropertystoreforwindow) to retrieve the window's property store, and use the methods of that retrieved [**IPropertyStore**](https://www.bing.com/search?q=**IPropertyStore**) object to set the [System.AppUserModel.ID](https://www.bing.com/search?q=System.AppUserModel.ID) property of that window.

For more information, see [Application User Model IDs (AppUserModelIDs)](https://msdn.microsoft.com/windows/desktop/ebce2d99-6f20-4545-9f12-d79cd8d0828f).

At the time the [System.AppUserModel.ID](https://www.bing.com/search?q=System.AppUserModel.ID) property is set, the taskbar is notified to refresh its information on the window or shortcut given that AppUserModelID.

Other window and shortcut properties can be used in conjunction with an explicit AppUserModelID to further control the grouping and pinning associated with a window, the display name and icon used for it in the taskbar, and the command to launch either an application pinned to the taskbar or a new instance of the application through that application's Jump List. These properties should be set before setting the [System.AppUserModel.ID](https://www.bing.com/search?q=System.AppUserModel.ID) property. For more information, see the following topics:

-   [System.AppUserModel.PreventPinning](https://www.bing.com/search?q=System.AppUserModel.PreventPinning)
-   [System.AppUserModel.RelaunchCommand](https://www.bing.com/search?q=System.AppUserModel.RelaunchCommand)
-   [System.AppUserModel.RelaunchDisplayNameResource](https://www.bing.com/search?q=System.AppUserModel.RelaunchDisplayNameResource)
-   [System.AppUserModel.RelaunchIconResource](https://www.bing.com/search?q=System.AppUserModel.RelaunchIconResource)

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.AppUserModel.ID
   shellPKey = PKEY_AppUserModel_ID
   formatID = 9F4C2855-9F79-4B39-A8D0-E1D42DE1D5F3
   propID = 5
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = String
      IsInnate = false
```

## Remarks

PKEY values are defined in Propkey.h.

## Related topics

<dl> <dt>

[Application User Model IDs (AppUserModelIDs)](https://msdn.microsoft.com/windows/desktop/ebce2d99-6f20-4545-9f12-d79cd8d0828f)
</dt> <dt>

[**SHGetPropertyStoreForWindow**](/windows/desktop/api/Shellapi/nf-shellapi-shgetpropertystoreforwindow)
</dt> <dt>

[propertyDescriptionList](https://www.bing.com/search?q=propertyDescriptionList)
</dt> <dt>

[propertyDescription](https://www.bing.com/search?q=propertyDescription)
</dt> <dt>

[searchInfo](https://www.bing.com/search?q=searchInfo)
</dt> <dt>

[labelInfo](https://www.bing.com/search?q=labelInfo)
</dt> <dt>

[typeInfo](https://www.bing.com/search?q=typeInfo)
</dt> <dt>

[displayInfo](https://www.bing.com/search?q=displayInfo)
</dt> <dt>

[aliasInfo](https://www.bing.com/search?q=aliasInfo)
</dt> <dt>

[stringFormat](https://www.bing.com/search?q=stringFormat)
</dt> <dt>

[booleanFormat](https://www.bing.com/search?q=booleanFormat)
</dt> <dt>

[numberFormat](https://www.bing.com/search?q=numberFormat)
</dt> <dt>

[dateTimeFormat](https://www.bing.com/search?q=dateTimeFormat)
</dt> <dt>

[enumeratedList](https://www.bing.com/search?q=enumeratedList)
</dt> <dt>

[enum](https://www.bing.com/search?q=enum)
</dt> <dt>

[enumRange](https://www.bing.com/search?q=enumRange)
</dt> <dt>

[image](https://www.bing.com/search?q=image)
</dt> <dt>

[drawControl](https://www.bing.com/search?q=drawControl)
</dt> <dt>

[editControl](https://www.bing.com/search?q=editControl)
</dt> <dt>

[filterControl](https://www.bing.com/search?q=filterControl)
</dt> <dt>

[queryControl](https://www.bing.com/search?q=queryControl)
</dt> <dt>

[relatedPropertyInfo](https://www.bing.com/search?q=relatedPropertyInfo)
</dt> <dt>

[relatedProperty](https://www.bing.com/search?q=relatedProperty)
</dt> </dl>

 

 



