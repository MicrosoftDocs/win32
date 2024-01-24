---
description: MTP Extension Properties
ms.assetid: 58fc8741-261a-4e63-9fd3-8f0ca05866ad
title: MTP Extension Properties
ms.topic: article
ms.date: 05/31/2018
---

# MTP Extension Properties

Properties describe objects, properties, resources, and devices.

## Vendor-Extended Object Properties

When a device manufacturer creates a vendor-extended property for a device object, they combine the **WPD\_PROPERTIES\_MTP\_VENDOR\_EXTENDED\_OBJECT\_PROPS** GUID with the object's property code to construct a **PROPERTYKEY** structure.

For example, if the object's property code is 0xD801, the resulting **PROPERTYKEY** would be as shown in the following example:


```C++
{4D545058-4FCE-4578-95C8-8698A9BC0F49}\D801
```



## Vendor-Extended Device Properties

When a device manufacturer creates a vendor-extended property for a device, they combine the **WPD\_PROPERTIES\_MTP\_VENDOR\_EXTENDED\_DEVICE\_PROPS** GUID with the object's property code to construct a **PROPERTYKEY** structure.

For example, if the object's property code is 0xD001, the resulting **PROPERTYKEY** would be as shown in the following example:


```C++
{4D545058-8900-40b3-8F1D-DC246E1E8370}\D001
```



## Related topics

<dl> <dt>

[Supporting MTP Extensions](supporting-mtp-extensions.md)
</dt> </dl>

 

 



