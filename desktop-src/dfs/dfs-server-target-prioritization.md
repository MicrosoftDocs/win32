---
title: DFS Server Target Prioritization
description: DFS Server Target Prioritization is a feature available in Microsoft Windows Server 2003 with Service Pack 1 (SP1) and later operating systems.
ms.assetid: 0aacebf7-49cc-4287-a5c4-0d25a416d227
ms.topic: article
ms.date: 05/31/2018
---

# DFS Server Target Prioritization

DFS Server Target Prioritization is a feature available in Microsoft Windows Server 2003 with Service Pack 1 (SP1) and later operating systems. This feature enables DFS servers to take advantage of available Active Directory site-cost information to prioritize the targets in client referrals.

Before Windows Server 2003 with SP1, targets were grouped into two sets: one group for containing all targets in the same site as the client; and another group for all other targets. Those targets sharing the same site as the client are called "in-site", and if site-costing is enabled, they are assigned a specific cost value relative to the site overall, with lower site costs preferred over higher ones.

With the availability of this site-costing data, server targets can be prioritized for more effective DFS server failover strategies. In the past, this granular level of detail was not available, and administrators had to resort to artificial means (such as dummy sites in AD) to support even simple requirements like the designation of specific servers as a "backup" or "secondary" server in the case where a "primary" DFS server fails. Now, with the additional detail provided by site-costing, multi-level failover strategies are possible.

The following discussion assumes that site-costing is enabled.

## Target Prioritization

Target priority is a specific ordering from an administrative perspective, classifying and ranking in-site servers in terms of explicit preference based on their site cost from a DFS client. Global priority is independent of the site-cost. Note that global priority classes do not necessarily indicate the most optimal targets from a DFS client's perspective, but instead reflect the importance, or lack of importance, of specific targets from a site administrator's perspective.

Server target priority is divided into two value categories: priority class and priority rank. Priority classes are divided into two levels: local and global. Within these classes there is a rough ordering of targets based on site cost, grouped as high, normal, and low priority. The result is five priority classes, in order from highest to lowest priority as follows:

- Global high priority
- Site-cost high priority
- Site-cost normal priority
- Site-cost low priority
- Global low priority

The site-cost classes can be considered as subdivisions of "global normal priority". Priority rank is a simple integer ranking based on ordinal values: 0, 1, 2, and onward, with 0 being the highest value and all subsequent values indicating decreasing rank.

The global high and low priorities do not consider site-cost values. Targets with a global high priority receive preference over all other targets, and targets with a global low priority receive the least preference.

In ordering a referral, the complete process has the following steps:

1. The sets of global high and low targets are identified, along with the remaining "global normal" targets.
2. If the "INSITE" option is set, all targets outside of the client's site are removed. The "INSITE" option is not applied to the global high and low priority sets.
3. Within each of these three sets, the targets are ordered using the AD site-cost mechanism, using either local or full site costing. The result is sets of targets of equal site cost.
4. Within the sets of "global normal" targets of equal site cost, targets are assigned a priority class from the site-cost high, normal, and low priority rankings.
5. Within the sets of targets of equal site cost and priority class, targets are now ordered by priority rank, with 0 being the highest rank.
6. Within the sets of targets of equal site cost, priority class, and priority rank, targets are randomly shuffled for load balancing.

Graphically, a set of targets are ordered as seen below:

- global high priority class targets 
- site-cost high priority class targets with site cost = 0
- normal with site cost = 0
- low with site cost = 0
- site-cost high priority class targets with site cost = 1
- normal with site cost = 1
- low with site cost = 1
- and so on
- global low priority class targets

Within each of these sets, targets are sorted according to priority rank. The highest rank is zero, with each subsequent integer value (1, 2, and so on) indicating an increasingly lower rank.

Target priority is set on a specific target of a link (or root) in a DFS namespace. A target's priority for one link does not influence the ordering of other links if that same target path is used multiple times. For example, if two links have \\\\server\\share1 as a target, the priority of \\\\server\\share1 is set separately for both links.

The default priority for all links is the site-cost normal priority with a rank of 0. Target priority does not affect the ordering of referrals unless it is used, and all existing links are ordered as they are received.

The referral response from a DFS server consists of target sets ordered as indicated above, with each non-global target set containing targets of the same site cost, priority class, and priority rank. Targets within each set are ordered randomly. DFS clients that receive the referral start with the first target of the first set, and continue through the list until an available target for a given DFS root or link is found.

For the specific API implementation of this feature, please see the following reference topics:

[**DFS_INFO_6**](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_info_6)
[**DFS_INFO_104**](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_info_104)
[**DFS_INFO_106**](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_info_106)
[**DFS_TARGET_PRIORITY**](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_target_priority)
[**DFS_TARGET_PRIORITY_CLASS**](/windows/win32/api/lmdfs/ne-lmdfs-dfs_target_priority_class~r1)
