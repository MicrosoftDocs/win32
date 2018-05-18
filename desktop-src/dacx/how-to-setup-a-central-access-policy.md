---
title: How to setup a central access policy
description: This topic describes a Central Access Policy (CAP).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '353BA03E-CB6B-4E5F-83D4-ED1A3C5DF34F'
ms.prod: 'windows-server-dev'
ms.technology: 'dynamic-access-control'
ms.tgt_platform: multiple
---

# How to setup a central access policy

This topic describes a Central Access Policy (CAP).

## Instructions

### Step 1: Central Access Policy (msAuthz-CentralAccessPolicy)

A central access policy consists of a unique GUID (msAuthz-CentralAccessPolicyID) and multiple central access rules (msAuthz-MemberRulesInCentralAccessPolicy). They can be published through group policy to target file servers. Once published, they can be selected by file administrators on file servers they manage. At any time, only one policy can be assigned to one resource explicitly or inherited from parent.

## Related topics

<dl> <dt>

[How to use central access policies for dynamic access control](how-to-use-central-access-policies-for-dynamic-access-control.md)
</dt> </dl>

 

 




