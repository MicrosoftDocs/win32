---
title: UI_PKEY_FontProperties_ChangedProperties
description: Identifies the UI\_PKEY\_FontProperties\_ChangedProperties property.
ms.assetid: d96b89b5-af30-4e76-b6ec-03fbb8d28ab3
ms.topic: article
ms.date: 05/31/2018
---

# UI\_PKEY\_FontProperties\_ChangedProperties

Identifies the UI\_PKEY\_FontProperties\_ChangedProperties property.

```
propertyDescription
   name = UI_PKEY_FontProperties_ChangedProperties
   shellPKey = UI_PKEY_FontProperties_ChangedProperties
   formatID = 00000312-7363-696e-8441798acf5aebb7
   propID = 13
   typeInfo
      type = IUISimplePropertySet
```

## Remarks

UI\_PKEY\_FontProperties\_ChangedProperties is used by an application to query only changed properties from [UI\_PKEY\_FontProperties](windowsribbon-reference-properties-uipkey-fontproperties.md).

Calling the [**IUISimplePropertySet::GetValue**](https://msdn.microsoft.com/library/windows/desktop/dd371357) method on this [**IUISimplePropertySet**](https://msdn.microsoft.com/library/windows/desktop/dd371358) object returns an [IPropertyStore](https://go.microsoft.com/fwlink/p/?linkid=139562).

UI\_PKEY\_FontProperties\_ChangedProperties is passed as the last parameter of the [**IUICommandHandler::Execute**](https://msdn.microsoft.com/library/windows/desktop/dd371489) call to the Ribbon host application.

This property key is read-only.

## Related topics

<dl> <dt>

[Font Control Properties](windowsribbon-reference-properties-fontcontrol.md)
</dt> <dt>

[**IUISimplePropertySet**](https://msdn.microsoft.com/library/windows/desktop/dd371358)
</dt> <dt>

[Font Control](windowsribbon-controls-fontcontrol.md)
</dt> </dl>

 

 




