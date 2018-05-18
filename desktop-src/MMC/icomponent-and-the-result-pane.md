---
title: IComponent and the Result Pane
description: An instance of the IComponent interface is associated with each MDI child window of a snap-in. Several instances of IComponent are possible for each instance of IComponentData (one per view, plus others used by MMC).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '09e06eef-6e24-42ea-a5cc-73ea386f49c0'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["IComponent and the result pane MMC"]
---

# IComponent and the Result Pane

An instance of the [**IComponent**](icomponent.md) interface is associated with each MDI child window of a snap-in. Several instances of **IComponent** are possible for each instance of [**IComponentData**](icomponentdata.md) (one per view, plus others used by MMC).

Every snap-in that inserts items in the result pane must implement the [**IComponent**](icomponent.md) interface. Similar to the [**IComponentData**](icomponentdata.md) interface, it is one of the console's interfaces to the snap-in and is closely associated with the functionality of the items displayed in the result pane.

However, this does not imply that [**IComponent**](icomponent.md) is the "result pane" interface and that [**IComponentData**](icomponentdata.md) is the "scope pane" interface. Many actions performed on nodes in the scope pane are handled by **IComponent**. For example, when the user selects a node in the scope pane of a view, MMC sends the [**MMCN\_SELECT**](mmcn-select.md) notification to the snap-in's **IComponent** implementation associated with that view.

All [**IComponent**](icomponent.md) instances of a snap-in are created through [**IComponentData::CreateComponent**](icomponentdata-createcomponent.md), and *not* through [**CoCreateInstance**](_com_cocreateinstance). Thus, it is possible for [**IComponentData**](icomponentdata.md) to be aware of all **IComponent** instances that it creates by holding pointers to them and deleting the pointers when [**IComponent::Destroy**](icomponent-destroy.md) is called. In addition, an **IComponent** instance can hold a pointer to the **IComponentData** instance that created it. This makes it easy, for example, for a snap-in to pass information from the document side to all views without having to call [**IConsole2::UpdateAllViews**](iconsole2-updateallviews.md).

 

 




