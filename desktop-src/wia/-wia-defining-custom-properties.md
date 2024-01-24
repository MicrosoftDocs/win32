---
description: Defining Custom Properties.
ms.assetid: 6adcf414-2c5a-451c-b30a-d1c161886c9a
title: Defining Custom Properties
ms.topic: article
ms.date: 05/31/2018
---

# Defining Custom Properties

**Defining Custom Properties**.

If it is necessary for the Windows Image Acquisition (WIA) minidriver to define custom properties, the WIA\_PRIVATE\_DEVPROP property should be used for custom root item properties, and the WIA\_PRIVATE\_ITEMPROP" property should be used for other item properties. These constants are defined in *wiadef.h*.

The following example code shows definitions for three root item properties. The property ID for the first custom root item property, CUSTOM\_ROOT\_PROP\_1, is defined in terms of WIA\_PRIVATE\_DEVPROP. Property IDs for additional root item properties are defined in terms of WIA\_PRIVATE\_DEVPROP + 1, WIA\_PRIVATE\_DEVPROP + 2, and so on. The pattern can be continued if additional custom root item properties are needed.


```
#define CUSTOM_ROOT_PROP_1 WIA_PRIVATE_DEVPROP
#define CUSTOM_ROOT_PROP_2 (WIA_PRIVATE_DEVPROP + 1) 
#define CUSTOM_ROOT_PROP_3 (WIA_PRIVATE_DEVPROP + 2)
```



The next example shows definitions for three custom child item properties and property IDs. The property ID for the first custom child item property, CUSTOM\_CHILD\_PROP\_1, is defined in terms of WIA\_PRIVATE\_ITEMPROP. Property IDs for additional child item properties are defined in terms of WIA\_PRIVATE\_ITEMPROP + 1, and so on. As before, the pattern can be continued if more of these custom child item properties are needed.


```
#define CUSTOM_CHILD_PROP_1 WIA_PRIVATE_ITEMPROP
#define CUSTOM_CHILD_PROP_2 (WIA_PRIVATE_ITEMPROP + 1)
#define CUSTOM_CHILD_PROP_3 (WIA_PRIVATE_ITEMPROP + 2)
```



Custom WIA properties must have custom property names that are associated with the custom property IDs. The following example code shows definitions for three custom root item property names. (These property names are used with the custom property IDs that were created in a previous example, where the custom property name contained in CUSTOM\_ROOT\_PROP\_1\_STR is associated with the custom root item property ID CUSTOM\_ROOT\_PROP\_1.)


```
#define CUSTOM_ROOT_PROP_1_STR L"My First Custom Root Item Property"
#define CUSTOM_ROOT_PROP_2_STR L"My Second Custom Root Item Property"
#define CUSTOM_ROOT_PROP_3_STR L"My Third Custom Root Item Property"
```



> [!Note]  
> WIA property names are *not* localized in multiple languages. This is because WIA properties can be read by applications using the property ID or the property name. If the name is used, it must be a constant, just as the property ID is.

 

 

 



