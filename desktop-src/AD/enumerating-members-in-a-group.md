---
title: Enumerating Members in a Group
description: Learn about enumerating members in an Azure Active Directory group. The members of a group are stored in a multi-value attribute called member.
ms.assetid: 28cafdbe-e599-4b1d-a384-264f41d81c79
ms.tgt_platform: multiple
keywords:
- Enumerating Members in a Group
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Members in a Group

The members of a group are stored in a multi-value attribute called **member**. For groups with a small to medium-sized membership, use the [**IADsGroup.Members**](/windows/desktop/api/iads/nf-iads-iadsgroup-members) method to get a pointer to an [**IADsMembers**](/windows/desktop/api/iads/nn-iads-iadsmembers) object that contains the list of all members. Then use the [**IADsMembers::get\_\_NewEnum**](/windows/desktop/api/iads/nf-iads-iadsmembers-get__newenum) to get an enumerator object that you can use to enumerate the members.

If the anticipated group membership will be 1000 or more members, use ranging to retrieve users one range at a time. For more information about using ranging to enumerate members, see [Enumerating Groups That Contain Many Members](enumerating-groups-that-contain-many-members.md).

 

 