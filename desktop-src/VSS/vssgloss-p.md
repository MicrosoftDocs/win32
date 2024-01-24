---
description: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 44279c0e-17f4-4109-bc12-af9064cd321e
title: P (Volume Shadow Copy Service)
ms.topic: article
ms.date: 05/31/2018
---

# P (Volume Shadow Copy Service)

[A](vssgloss-a.md) [B](vssgloss-b.md) [C](vssgloss-c.md) [D](vssgloss-d.md) [E](vssgloss-e.md) [F](vssgloss-f.md) [G](vssgloss-g.md) [H](vssgloss-h.md) [I](vssgloss-i.md) J K [L](vssgloss-l.md) M [N](vssgloss-n.md) [O](vssgloss-o.md) P Q [R](vssgloss-r.md) [S](vssgloss-s.md) [T](vssgloss-t.md) U [V](vssgloss-v.md) [W](vssgloss-w.md) X Y Z

<dl> <dt>

<span id="base.vssgloss_partial_file_support"></span><span id="BASE.VSSGLOSS_PARTIAL_FILE_SUPPORT"></span>**partial file support**
</dt> <dd>

The capacity to implement backup operations by modifying subsections of the files involved, rather than working with the entire files. See also [*directed targeting*](vssgloss-d.md).

</dd> <dt>

<span id="base.vssgloss_persistent_shadow_copy"></span><span id="BASE.VSSGLOSS_PERSISTENT_SHADOW_COPY"></span>**persistent shadow copy**
</dt> <dd>

A shadow copy that is not deleted automatically when the requester releases an [**IVssBackupComponents**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponents) object or when the computer is restarted. See also [*auto-release shadow copy*](vssgloss-a.md), [*shadow copy*](vssgloss-s.md).

</dd> <dt>

<span id="base.vssgloss_plex"></span><span id="BASE.VSSGLOSS_PLEX"></span>**Plex**
</dt> <dd>

A special type of shadow copy volume that fully and completely represents a shadow copy volume without the need for either original volume. This is also commonly known as a split-mirror, but this documentation uses the term Plex.

</dd> <dt>

<span id="base.vssgloss_postrestore_event"></span><span id="BASE.VSSGLOSS_POSTRESTORE_EVENT"></span>**PostRestore event**
</dt> <dd>

A VSS event indicating that a VSS restore has completed.

</dd> <dt>

<span id="base.vssgloss_postsnapshot_event"></span><span id="BASE.VSSGLOSS_POSTSNAPSHOT_EVENT"></span>**PostSnapshot event**
</dt> <dd>

A VSS event indicating that a shadow copy has been completed. See also [*shadow copy*](vssgloss-s.md).

</dd> <dt>

<span id="base.vssgloss_preparebackup_event"></span><span id="BASE.VSSGLOSS_PREPAREBACKUP_EVENT"></span>**PrepareForBackup event**
</dt> <dd>

A VSS event indicating that a backup operation is about to take place.

</dd> <dt>

<span id="base.vssgloss_preparesnapshot_event"></span><span id="BASE.VSSGLOSS_PREPARESNAPSHOT_EVENT"></span>**PrepareForSnapshot event**
</dt> <dd>

A VSS event indicating that writers should take steps to prepare for an upcoming shadow copy operation. See also [*shadow copy*](vssgloss-s.md).

</dd> <dt>

<span id="base.vssgloss_prerestore_event"></span><span id="BASE.VSSGLOSS_PRERESTORE_EVENT"></span>**PreRestore event**
</dt> <dd>

A VSS event indicating that a restore operation is about to take place.

</dd> <dt>

<span id="base.vssgloss_provider"></span><span id="BASE.VSSGLOSS_PROVIDER"></span>**provider**
</dt> <dd>

An operating system object that intercepts and manages I/O requests to create and represent volume shadow copies to the file system. See also [*hardware provider*](vssgloss-h.md), [*software provider*](vssgloss-s.md).

</dd> </dl>

 

 



