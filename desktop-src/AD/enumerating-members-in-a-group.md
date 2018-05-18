---
title: Enumerating Members in a Group
description: The members of a group are stored in a multi-value attribute called member.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '28cafdbe-e599-4b1d-a384-264f41d81c79'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["Enumerating Members in a Group"]
---

# Enumerating Members in a Group

The members of a group are stored in a multi-value attribute called **member**. For groups with a small to medium-sized membership, use the [**IADsGroup.Members**](https://msdn.microsoft.com/library/aa706032) method to get a pointer to an [**IADsMembers**](https://msdn.microsoft.com/library/aa706041) object that contains the list of all members. Then use the [**IADsMembers::get\_\_NewEnum**](https://msdn.microsoft.com/library/aa706042) to get an enumerator object that you can use to enumerate the members.

If the anticipated group membership will be 1000 or more members, use ranging to retrieve users one range at a time. For more information about using ranging to enumerate members, see [Enumerating Groups That Contain Many Members](enumerating-groups-that-contain-many-members.md).

 

 




