---
description: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: d7d9c8bf-993f-469c-aea1-5d86ca856690
title: B (Volume Shadow Copy Service)
ms.topic: article
ms.date: 05/31/2018
---

# B (Volume Shadow Copy Service)

[A](vssgloss-a.md) B [C](vssgloss-c.md) [D](vssgloss-d.md) [E](vssgloss-e.md) [F](vssgloss-f.md) [G](vssgloss-g.md) [H](vssgloss-h.md) [I](vssgloss-i.md) J K [L](vssgloss-l.md) M [N](vssgloss-n.md) [O](vssgloss-o.md) [P](vssgloss-p.md) Q [R](vssgloss-r.md) [S](vssgloss-s.md) [T](vssgloss-t.md) U [V](vssgloss-v.md) [W](vssgloss-w.md) X Y Z

<dl> <dt>

<span id="base.vssgloss_back_end_level_applications"></span><span id="BASE.VSSGLOSS_BACK_END_LEVEL_APPLICATIONS"></span>**back-end level applications**
</dt> <dd>

Indicates the point at which a writer is notified of a freeze by VSS. Writers that are initialized as back-end level applications are notified after writers initialized as front-end level applications and prior to those initialized as system-level applications. See also [*application level*](vssgloss-a.md), [*front-end level applications*](vssgloss-f.md), [*system-level applications*](vssgloss-s.md), [*writer*](vssgloss-w.md).

</dd> <dt>

<span id="base.vssgloss_backupcomplete_event"></span><span id="BASE.VSSGLOSS_BACKUPCOMPLETE_EVENT"></span>**BackupComplete event**
</dt> <dd>

A VSS event indicating that a VSS backup has completed. This event should be followed by a BackupShutdown event under normal operation. See also *BackupShutdown event*.

</dd> <dt>

<span id="base.vssgloss_backup_components_document"></span><span id="BASE.VSSGLOSS_BACKUP_COMPONENTS_DOCUMENT"></span>**Backup Components Document**
</dt> <dd>

An XML document created by a requester (using the **IVssBackupComponents** interface) in the course of setting up a restore or backup operation. The Backup Components Document contains a list of those explicitly included components, from one or more writers, participating in a backup or restore operation. It does not contain implicitly included component information. In contrast, a Writer Metadata Document contains only writer components that may participate in a backup.

A Backup Components Document can be saved to disk. See also [*explicit component inclusion*](vssgloss-e.md), [*implicit component inclusion*](vssgloss-i.md).

</dd> <dt>

<span id="base.vssgloss_backup_set"></span><span id="BASE.VSSGLOSS_BACKUP_SET"></span>**backup set**
</dt> <dd>

Those files to be backed up. It includes files selected by inclusion in a component, those indicated by writer-level include statements, less those files that have been explicitly included.

</dd> <dt>

<span id="base.vssgloss_backupshutdown_event"></span><span id="BASE.VSSGLOSS_BACKUPSHUTDOWN_EVENT"></span>**BackupShutdown event**
</dt> <dd>

A VSS event indicating that a compliant backup application has shut down. Normally, this is preceded by a BackupComplete event. However, if a backup terminates unexpectedly, this event can be generated without a preceding BackupComplete event. See also *BackupComplete event*.

</dd> <dt>

<span id="base.vssgloss_backup_stamp"></span><span id="BASE.VSSGLOSS_BACKUP_STAMP"></span>**backup stamp**
</dt> <dd>

A string containing information as to when a backup took place. VSS places no restriction on the format of this string, except that it be intelligible to all the writer instances of a given class. It may contain time and date information, logical sequence numbers, or any other information that will allow a writer of the same class to determine when the last backup has take place.

</dd> </dl>

 

 



