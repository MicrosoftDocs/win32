---
title: Computer Management Extensible Node Types
description: The Computer Management snap-in allows extensions for the following node types.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f809ae71-c8c8-48bf-859f-45650999cecf'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
---

# Computer Management Extensible Node Types

The Computer Management snap-in allows extensions for the following node types.

Snap-in developers can write extensions for any of the node types listed in the following table.



| Node type                 | Node type GUID                         |
|---------------------------|----------------------------------------|
| Computer Management       | {476E6446-AAFF-11D0-B944-00C04FD8D5B0} |
| Services and Applications | {476E6449-AAFF-11D0-B944-00C04FD8D5B0} |
| Storage                   | {476E644A-AAFF-11D0-B944-00C04FD8D5B0} |
| System Tools              | {476E6448-AAFF-11D0-B944-00C04FD8D5B0} |



 

## Remarks

Snap-in developers can write extensions for any of the node types listed in the preceding table. However, namespace extensions to the Computer Management scope item are not recommended. The structure of namespace items in the Computer Management node type is designed to organize management functionality into three groups: System Tools, Storage, and Services and Applications. If an extension snap-in adds a new group to the namespace (by creating a namespace extension), then the user's interaction will not be consistent with the intended Computer Management snap-in experience.

An example of how the Computer Management snap-in can be extended is a dynamic namespace extension that provides control of a service running on a single computer; the dynamic namespace extension would extend the Services and Applications node type. Be aware that only dynamic extensions should extend the Services and Applications node type, and only in the manner described in the [Registering a Snap-in for an Optional Service](registering-a-snap-in-for-an-optional-service.md) topic.

## Related topics

<dl> <dt>

[Registering a Snap-in for an Optional Service](registering-a-snap-in-for-an-optional-service.md)
</dt> <dt>

[Retargeting the Computer Management Snap-in](retargeting-the-computer-management-snap-in.md)
</dt> </dl>

 

 




