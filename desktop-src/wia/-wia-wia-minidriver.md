---
description: Applications see Windows Image Acquisition (WIA) devices as a hierarchical tree of IWiaItem or IWiaItem2 objects with the root item representing the device itself.
ms.assetid: ae4ded93-09be-4caa-ad6e-1a9071fdb4b6
title: WIA Minidriver
ms.topic: article
ms.date: 05/31/2018
---

# WIA Minidriver

Applications see Windows Image Acquisition (WIA) devices as a hierarchical tree of [**IWiaItem**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiaitem) or [**IWiaItem2**](-wia-iwiaitem2.md) objects with the root item representing the device itself. WIA devices may be used concurrently by more than one application. It is therefore necessary that each application's view of an **IWiaItem** or **IWiaItem2** object be independent of another application's views. This is accomplished by having two different item objects. The driver creates the driver item tree of [IWiaDrvItem Interface](https://msdn.microsoft.com/library/ms793976.aspx) objects, also called driver items, using the WIA driver services methods. These are global objects that the driver uses to represent each driver's internal items. When an application creates an **IWiaItem** or **IWiaItem2** object (also called an application item), this object is linked to the driver's corresponding [IWiaDrvItem Interface](https://msdn.microsoft.com/library/ms793976.aspx) in the driver item tree. A reference count is maintained on the [IWiaDrvItem Interface](https://msdn.microsoft.com/library/ms793976.aspx) object subject to the following rules:

-   When a driver adds an [IWiaDrvItem Interface](https://msdn.microsoft.com/library/ms793976.aspx) object to the driver item tree, the [IWiaDrvItem Interface](https://msdn.microsoft.com/library/ms793976.aspx) object's reference count is incremented. This typically takes place during [IWiaMiniDrv::drvInitializeWia](https://msdn.microsoft.com/library/ms794097.aspx) or when a WIA\_CMD\_SYNCHRONIZE command is processed.
-   When a driver removes an [IWiaDrvItem Interface](https://msdn.microsoft.com/library/ms793976.aspx) object from the driver item tree, the [IWiaDrvItem Interface](https://msdn.microsoft.com/library/ms793976.aspx) object's reference count is decremented and the [IWiaDrvItem Interface](https://msdn.microsoft.com/library/ms793976.aspx) object is marked so that it can't access the device again. This typically takes place when a device is disconnected or an item is deleted. Applications are still able to read properties from an [**IWiaItem**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiaitem) or [**IWiaItem2**](-wia-iwiaitem2.md) object even when the corresponding [IWiaDrvItem Interface](https://msdn.microsoft.com/library/ms793976.aspx) object has been removed from the driver item tree.
-   When an [**IWiaItem**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiaitem) or [**IWiaItem2**](-wia-iwiaitem2.md) object is created it is linked to a corresponding [IWiaDrvItem Interface](https://msdn.microsoft.com/library/ms793976.aspx) object. The reference count of the [IWiaDrvItem Interface](https://msdn.microsoft.com/library/ms793976.aspx) object is incremented.
-   When an [**IWiaItem**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiaitem) or [**IWiaItem2**](-wia-iwiaitem2.md) object is released, the link to its corresponding [IWiaDrvItem Interface](https://msdn.microsoft.com/library/ms793976.aspx) object is severed and the [IWiaDrvItem Interface](https://msdn.microsoft.com/library/ms793976.aspx) object's reference count is decremented.
-   If an [IWiaDrvItem Interface](https://msdn.microsoft.com/library/ms793976.aspx) object's reference count goes to zero, the [IWiaDrvItem Interface](https://msdn.microsoft.com/library/ms793976.aspx) object is deleted. This applies to all [IWiaDrvItem Interface](https://msdn.microsoft.com/library/ms793976.aspx) objects including the root item. An [IWiaDrvItem Interface](https://msdn.microsoft.com/library/ms793976.aspx) object's reference count only goes to zero when no application items reference it and it is no longer linked to the driver item tree.

Using this reference counting scheme, many [**IWiaItem**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiaitem) or [**IWiaItem2**](-wia-iwiaitem2.md) objects may link to one [IWiaDrvItem Interface](https://msdn.microsoft.com/library/ms793976.aspx) without interference. Because each **IWiaItem** or **IWiaItem2** contains its own property storage, an application can continue to read item properties even after an item has been deleted, but no operation that requires access to the device will succeed. Because item properties are stored in the **IWiaItem** or **IWiaItem2** object, the driver must set the **IWiaItem** or **IWiaItem2** object's properties to the device before a data transfer.

 

 



