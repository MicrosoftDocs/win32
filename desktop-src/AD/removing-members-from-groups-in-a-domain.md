---
title: Removing Members from Groups in a Domain
description: You can remove users, groups, or contacts from groups.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 036f2882-7da9-4293-87a0-a087235b212f
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- groups AD ,removing members from groups in a domain
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Removing Members from Groups in a Domain

You can remove users, groups, or contacts from groups. The **member** attribute of the **group** object contains all direct members of the group.

The simplest way to remove a member from a group is to call the [**IADsGroup.Remove**](https://msdn.microsoft.com/library/aa706034) method on the [**IADsGroup**](https://msdn.microsoft.com/library/aa706021) interface of the group object you want to remove members from.

 

 




