---
description: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 7eb1d433-21db-45cc-a141-13a89993e30c
title: E (Volume Shadow Copy Service)
ms.topic: article
ms.date: 05/31/2018
---

# E (Volume Shadow Copy Service)

[A](vssgloss-a.md) [B](vssgloss-b.md) [C](vssgloss-c.md) [D](vssgloss-d.md) E [F](vssgloss-f.md) [G](vssgloss-g.md) [H](vssgloss-h.md) [I](vssgloss-i.md) J K [L](vssgloss-l.md) M [N](vssgloss-n.md) [O](vssgloss-o.md) [P](vssgloss-p.md) Q [R](vssgloss-r.md) [S](vssgloss-s.md) [T](vssgloss-t.md) U [V](vssgloss-v.md) [W](vssgloss-w.md) X Y Z

<dl> <dt>

<span id="base.vssgloss_explicit_component_inclusion"></span><span id="BASE.VSSGLOSS_EXPLICIT_COMPONENT_INCLUSION"></span>**explicit component inclusion**
</dt> <dd>

Adding of a component's information to a requester's Backup Components Document when it participates in a backup or restore operation. Requesters use [**IVssBackupComponents::AddComponent**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addcomponent) to explicitly include a component in a backup operation, and [**IVssBackupComponents::SetSelectedForRestore**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-setselectedforrestore) or [**IVssBackupComponents::AddRestoreSubcomponent**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addrestoresubcomponent) to explicitly include a component in a restore operation.

If any component of a writer is backed up or restored, all nonselectable components without any selectable ancestors must be explicitly included in a backup or restore operation.

Selectable components without selectable ancestors chosen by a requester for participation in a backup or restore must be explicitly included in the operation.

Nonselectable components with a selectable ancestor are never explicitly included.

Selectable components with a selectable ancestor may be included explicitly, or may be included implicitly if the ancestor is included explicitly.

</dd> <dt>

<span id="base.vssgloss_exposed_shadow_copy"></span><span id="BASE.VSSGLOSS_EXPOSED_SHADOW_COPY"></span>**exposed shadow copy**
</dt> <dd>

A volume shadow copy that is mounted on a system and available to processes other than the one that manages it. A shadow copy volume mounted under a drive letter or a directory location is referred to as "locally exposed." A shadow copy volume accessible through a share (except for client-accessible shadow copies) is referred to as "remotely exposed." All exposed shadow copies are also surfaced shadow copies. See also [*client accessible shadow copy*](vssgloss-c.md), [*shadow copy*](vssgloss-s.md).

</dd> </dl>

 

 



