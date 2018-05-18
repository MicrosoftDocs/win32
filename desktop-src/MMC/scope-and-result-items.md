---
title: Scope and Result Items
description: This content will use the term \ 0034;item \ 0034; to describe all objects directly inserted by snap-ins in either the scope pane or the result pane.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1bdd610f-e807-44be-8137-b6c6216b0645'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["scope and result items MMC"]
---

# Scope and Result Items

This content will use the term "item" to describe all objects directly inserted by snap-ins in either the scope pane or the result pane. Snap-ins insert scope items and result items using the MMC interface methods [**IConsoleNameSpace2::InsertItem**](iconsolenamespace2-insertitem.md) and [**IResultData::InsertItem**](iresultdata-insertitem.md), respectively. The term "item" is used instead of "node" in the MMC documentation because many interface methods in the MMC SDK use "item" to refer to either a scope item or a result item.

Be aware that snap-ins insert scope items in the scope pane, but the items can appear in either the scope pane or the result pane. Result items can only appear in the result pane. Finally, the term static node will continue to be used to refer to the stand-alone snap-in "root" scope item inserted by the console when the snap-in is loaded.

 

 




