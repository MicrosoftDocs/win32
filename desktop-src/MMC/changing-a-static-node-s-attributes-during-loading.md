---
title: Changing a Static Node's Attributes during Loading
description: As is true of all other scope items, a stand-alone snap-in can programmatically change the display attributes of a static node (for example, its icon and display name) at any time by calling the IConsoleNameSpace2 SetItem method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e4a295bd-fb93-42e4-a4e1-2f94df7c1d2f'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["changing a static node's attributes during loading MMC", "display attributes MMC"]
---

# Changing a Static Node's Attributes during Loading

As is true of all other scope items, a stand-alone snap-in can programmatically change the display attributes of a static node (for example, its icon and display name) at any time by calling the [**IConsoleNameSpace2::SetItem**](iconsolenamespace2-setitem.md) method.

When the user saves the current console, MMC stores the icon and display name of each static node in the console tree in the .msc file that it creates. When the user loads the .msc file, MMC uses the stored icon and display name of the static node when that displays it.

Now, there are situations in which a snap-in may want to change the display attributes of its static node before it appears in a console tree. For example, the snap-in might collect information from the user that is used to construct the static node's display name.

To change a static node's attributes when loading a snap-in, the snap-in must support the [**CCF\_SNAPIN\_PRELOADS**](ccf-snapin-preloads.md) clipboard format and also handle the [**MMCN\_PRELOAD**](mmcn-preload.md) notification.

When saving a console file, MMC calls [**IDataObject::GetDataHere**](_ole_idataobject_getdatahere) on each loaded snap-in using the CCF\_SNAPIN\_PRELOADS clipboard format. If the snap-in handles the clipboard format and returns **TRUE**, MMC calls the [**IComponentData::Notify**](icomponentdata-notify.md) method of the snap-in with the [**MMCN\_PRELOAD**](mmcn-preload.md) notification the next time the snap-in is loaded from the saved console file. If the snap-in does not support CCF\_SNAPIN\_PRELOADS, MMC uses the static node's cached icon and display name instead.

## Related topics

<dl> <dt>

[Changing a Static Node's Attributes during Loading: Implementation Details](changing-a-static-node-s-attributes-during-loading-implementation-details.md)
</dt> <dt>

[Working with the Scope Pane: Interfaces](working-with-the-scope-pane-interfaces.md)
</dt> <dt>

[Working with the Scope Pane: Implementation Details](working-with-the-scope-pane-implementation-details.md)
</dt> </dl>

 

 




