---
title: Removing Members from Groups in a Domain
description: You can remove users, groups, or contacts from groups.
ms.assetid: 036f2882-7da9-4293-87a0-a087235b212f
ms.tgt_platform: multiple
keywords:
- groups AD ,removing members from groups in a domain
ms.topic: article
ms.date: 05/31/2018
---

# Removing Members from Groups in a Domain

You can remove users, groups, or contacts from groups. The **member** attribute of the **group** object contains all direct members of the group.

The simplest way to remove a member from a group is to call the [**IADsGroup.Remove**](/windows/desktop/api/iads/nf-iads-iadsgroup-remove) method on the [**IADsGroup**](/windows/desktop/api/iads/nn-iads-iadsgroup) interface of the group object you want to remove members from.

 

 