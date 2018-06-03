---
Description: Disables the ability of a shortcut or window to be pinned to the taskbar or the Start menu. This property also makes the item ineligible for inclusion in the Start menu's Most Frequently Used (MFU) list.
ms.assetid: 86239BF8-BCFC-4e76-BF94-5ABA4639562C
title: System.AppUserModel.PreventPinning
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.AppUserModel.PreventPinning

Disables the ability of a shortcut or window to be pinned to the taskbar or the **Start** menu. This property also makes the item ineligible for inclusion in the **Start** menu's Most Frequently Used (MFU) list.

This property must be set on a window before the [PKEY\_AppUserModel\_ID](https://www.bing.com/search?q=PKEY\_AppUserModel\_ID) property. After the PKEY\_AppUserModel\_ID property is set, changes to [PKEY\_AppUserModel\_PreventPinning](https://www.bing.com/search?q=PKEY\_AppUserModel\_PreventPinning) are ignored.

For more information about Application User Model IDs (AppUserModelIDs) and other methods of excluding an item from being pinned to the taskbar and from MFU inclusion, see [Application User Model IDs (AppUserModelIDs)](https://msdn.microsoft.com/windows/desktop/ebce2d99-6f20-4545-9f12-d79cd8d0828f).

To set this property on a window, use [**SHGetPropertyStoreForWindow**](/windows/desktop/api/Shellapi/nf-shellapi-shgetpropertystoreforwindow) to retrieve the window's property store, and use the methods of that retrieved [**IPropertyStore**](https://www.bing.com/search?q=**IPropertyStore**) object to set the [System.AppUserModel.PreventPinning](https://www.bing.com/search?q=System.AppUserModel.PreventPinning) property of that window.

Setting this property causes the following properties to be ignored:

-   [System.AppUserModel.RelaunchCommand](https://www.bing.com/search?q=System.AppUserModel.RelaunchCommand)
-   [System.AppUserModel.RelaunchDisplayNameResource](https://www.bing.com/search?q=System.AppUserModel.RelaunchDisplayNameResource)
-   [System.AppUserModel.RelaunchIconResource](https://www.bing.com/search?q=System.AppUserModel.RelaunchIconResource)

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.AppUserModel.PreventPinning
   shellPKey = PKEY_AppUserModel_PreventPinning
   formatID = 9F4C2855-9F79-4B39-A8D0-E1D42DE1D5F3
   propID = 9
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = Boolean
      IsInnate = false
```

## Remarks

PKEY values are defined in Propkey.h.

## Related topics

<dl> <dt>

[Application User Model IDs (AppUserModelIDs)](https://msdn.microsoft.com/windows/desktop/ebce2d99-6f20-4545-9f12-d79cd8d0828f)
</dt> <dt>

[System.AppUserModel.ID](https://www.bing.com/search?q=System.AppUserModel.ID)
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

 

 



