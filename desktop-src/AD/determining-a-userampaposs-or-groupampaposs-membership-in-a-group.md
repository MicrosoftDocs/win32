---
title: Determining a User's or Group's Membership in a Group
description: The IADsGroup.IsMember method can be used to determine if an object is a member of a group.
ms.assetid: c7168781-4ae4-4ce3-8d8a-2eefc7def62b
ms.tgt_platform: multiple
keywords:
- Determining a User's or Group's Membership in a Group AD
- groups AD , determining a user's or group's membership in a group
ms.topic: article
ms.date: 05/31/2018
---

# Determining a User's or Group's Membership in a Group

The [**IADsGroup.IsMember**](/windows/desktop/api/iads/nf-iads-iadsgroup-ismember) method can be used to determine if an object is a member of a group. This method returns **TRUE** if the specified object is a direct member of the group, that is, the group's member property contains the specified object.

A group can contain other groups. The [**IADsGroup.IsMember**](/windows/desktop/api/iads/nf-iads-iadsgroup-ismember) method does not recursively verify the members of groups in its member property, groups within those groups, and so on. To recursively verify that an object is a member of a group, enumerate the groups in the member property, verify the members of those groups to see if the object is a member, and if those groups contain other groups, check their members, and so on.

> [!Note]  
> Since groups can be nested, group membership may have loops. Any script that enumerates over many groups should keep an internal list of groups to end recursion if a group has already been visited.

 

 

 