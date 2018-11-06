---
Description: Prevents a Start menu entry for a newly installed application shortcut from receiving a highlight.
ms.assetid: ff85da6f-a506-4225-8ac9-4a8a7be8d599
title: System.AppUserModel.ExcludeFromShowInNewInstall
ms.topic: article
ms.date: 05/31/2018
---

# System.AppUserModel.ExcludeFromShowInNewInstall

Prevents a **Start** menu entry for a newly installed application shortcut from receiving a highlight. This is equivalent to clearing the **Highlight newly installed programs** option in the **Customize Start Menu** window on an individual item. This property should be set on shortcuts for tools and secondary applications.

> [!Note]  
> This property is property is only used by the Start menu on Windows Vista and Windows 7. The property is not used by the Start screen or Start menu on Windows 8 and later

 

.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.AppUserModel.ExcludeFromShowInNewInstall
   shellPKey = PKEY_AppUserModel_ExcludeFromShowInNewInstall
   formatID = 9F4C2855-9F79-4B39-A8D0-E1D42DE1D5F3
   propID = 8
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

[Application User Model IDs (AppUserModelIDs)](https://msdn.microsoft.com/en-us/library/Dd378459(v=VS.85).aspx)
</dt> <dt>

[System.AppUserModel.ID](https://msdn.microsoft.com/library/Dd391569(v=VS.85).aspx)
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
</dt> <dt>

[startPinOption](https://msdn.microsoft.com/library/JJ553605(v=VS.85).aspx)
</dt> </dl>

 

 



