---
description: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: ebf8d0a7-e465-4f9f-9e3d-b97dbcf321b8
title: I (Volume Shadow Copy Service)
ms.topic: article
ms.date: 05/31/2018
---

# I (Volume Shadow Copy Service)

[A](vssgloss-a.md) [B](vssgloss-b.md) [C](vssgloss-c.md) [D](vssgloss-d.md) [E](vssgloss-e.md) [F](vssgloss-f.md) [G](vssgloss-g.md) [H](vssgloss-h.md) I J K [L](vssgloss-l.md) M [N](vssgloss-n.md) [O](vssgloss-o.md) [P](vssgloss-p.md) Q [R](vssgloss-r.md) [S](vssgloss-s.md) [T](vssgloss-t.md) U [V](vssgloss-v.md) [W](vssgloss-w.md) X Y Z

<dl> <dt>

<span id="base.vssgloss_identify_event"></span><span id="BASE.VSSGLOSS_IDENTIFY_EVENT"></span>**Identify event**
</dt> <dd>

A VSS event indicating that a writer or a requester needs to query the current writer. It is used to construct the current writer's metadata information. See also [*requester*](vssgloss-r.md), [*writer*](vssgloss-w.md).

</dd> <dt>

<span id="base.vssgloss_implicit_component_inclusion"></span><span id="BASE.VSSGLOSS_IMPLICIT_COMPONENT_INCLUSION"></span>**implicit component inclusion**
</dt> <dd>

Not adding a component's information to a requester's Backup Components Document when it participates in a backup or restore operation.

Nonselectable components with a selectable ancestor are only implicitly included if their ancestor is included.

Selectable components with a selectable ancestor may be included implicitly, if the ancestor is included, or may be included explicitly.

Nonselectable components without any selectable ancestors are never implicitly included in a backup or restore operation—all such components must be explicitly added to the Backup Components Document if any of the writer's components participate.

Selectable components without selectable ancestors chosen by a requester for participation in a backup or restore cannot be implicitly included in the operation, but must be explicitly added to the Backup Components Document.

</dd> <dt>

<span id="base.vssgloss_incremental_backup_operations"></span><span id="BASE.VSSGLOSS_INCREMENTAL_BACKUP_OPERATIONS"></span>**incremental backup operations**
</dt> <dd>

A backup or restore operation is performed only on files created or changed since the last full, incremental, or differential backup was saved. See also [*differential backup operations*](vssgloss-d.md).

</dd> </dl>

 

 



