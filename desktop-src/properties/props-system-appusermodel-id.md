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

To set this property on a window, use [**SHGetPropertyStoreForWindow**](/windows/desktop/api/Shellapi/nf-shellapi-shgetpropertystoreforwindow) to retrieve the window's property store, and use the methods of that retrieved [**IPropertyStore**](https://msdn.microsoft.com/library/Bb761474(v=VS.85).aspx) object to set the [System.AppUserModel.ID](https://msdn.microsoft.com/library/Dd391569(v=VS.85).aspx) property of that window.

For more information, see [Application User Model IDs (AppUserModelIDs)](https://msdn.microsoft.com/en-us/library/Dd378459(v=VS.85).aspx).

At the time the [System.AppUserModel.ID](https://msdn.microsoft.com/library/Dd391569(v=VS.85).aspx) property is set, the taskbar is notified to refresh its information on the window or shortcut given that AppUserModelID.

Other window and shortcut properties can be used in conjunction with an explicit AppUserModelID to further control the grouping and pinning associated with a window, the display name and icon used for it in the taskbar, and the command to launch either an application pinned to the taskbar or a new instance of the application through that application's Jump List. These properties should be set before setting the [System.AppUserModel.ID](https://msdn.microsoft.com/library/Dd391569(v=VS.85).aspx) property. For more information, see the following topics:

-   [System.AppUserModel.PreventPinning](https://msdn.microsoft.com/library/Dd561983(v=VS.85).aspx)
-   [System.AppUserModel.RelaunchCommand](https://msdn.microsoft.com/library/Dd391571(v=VS.85).aspx)
-   [System.AppUserModel.RelaunchDisplayNameResource](https://msdn.microsoft.com/library/Dd391572(v=VS.85).aspx)
-   [System.AppUserModel.RelaunchIconResource](https://msdn.microsoft.com/library/Dd391573(v=VS.85).aspx)

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

[Application User Model IDs (AppUserModelIDs)](https://msdn.microsoft.com/en-us/library/Dd378459(v=VS.85).aspx)
</dt> <dt>

[**SHGetPropertyStoreForWindow**](/windows/desktop/api/Shellapi/nf-shellapi-shgetpropertystoreforwindow)
</dt> <dt>

[propertyDescriptionList](https://msdn.microsoft.com/library/Bb773882(v=VS.85).aspx)
</dt> <dt>

[propertyDescription](https://msdn.microsoft.com/library/Bb773880(v=VS.85).aspx)
</dt> <dt>

[searchInfo](https://msdn.microsoft.com/library/Bb773885(v=VS.85).aspx)
</dt> <dt>

[labelInfo](https://msdn.microsoft.com/library/Bb773876(v=VS.85).aspx)
</dt> <dt>

[typeInfo](https://msdn.microsoft.com/library/Bb773889(v=VS.85).aspx)
</dt> <dt>

[displayInfo](https://msdn.microsoft.com/library/Bb773865(v=VS.85).aspx)
</dt> <dt>

[aliasInfo](https://msdn.microsoft.com/library/Bb773860(v=VS.85).aspx)
</dt> <dt>

[stringFormat](https://msdn.microsoft.com/library/Bb773886(v=VS.85).aspx)
</dt> <dt>

[booleanFormat](https://msdn.microsoft.com/library/Bb773862(v=VS.85).aspx)
</dt> <dt>

[numberFormat](https://msdn.microsoft.com/library/Bb773877(v=VS.85).aspx)
</dt> <dt>

[dateTimeFormat](https://msdn.microsoft.com/library/Bb773863(v=VS.85).aspx)
</dt> <dt>

[enumeratedList](https://msdn.microsoft.com/library/Bb773871(v=VS.85).aspx)
</dt> <dt>

[enum](https://msdn.microsoft.com/library/Bb773869(v=VS.85).aspx)
</dt> <dt>

[enumRange](https://msdn.microsoft.com/library/Bb773873(v=VS.85).aspx)
</dt> <dt>

[image](https://msdn.microsoft.com/library/Dd798383(v=VS.85).aspx)
</dt> <dt>

[drawControl](https://msdn.microsoft.com/library/Bb773866(v=VS.85).aspx)
</dt> <dt>

[editControl](https://msdn.microsoft.com/library/Bb773868(v=VS.85).aspx)
</dt> <dt>

[filterControl](https://msdn.microsoft.com/library/Bb773874(v=VS.85).aspx)
</dt> <dt>

[queryControl](https://msdn.microsoft.com/library/Bb773883(v=VS.85).aspx)
</dt> <dt>

[relatedPropertyInfo](https://msdn.microsoft.com/library/Dd798385(v=VS.85).aspx)
</dt> <dt>

[relatedProperty](https://msdn.microsoft.com/library/Dd798384(v=VS.85).aspx)
</dt> </dl>

 

 



