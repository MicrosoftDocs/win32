---
description: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: c4f826bc-ea80-4fd5-99da-630e7ae56dd7
title: S (Volume Shadow Copy Service)
ms.topic: article
ms.date: 05/31/2018
---

# S (Volume Shadow Copy Service)

[A](vssgloss-a.md) [B](vssgloss-b.md) [C](vssgloss-c.md) [D](vssgloss-d.md) [E](vssgloss-e.md) [F](vssgloss-f.md) [G](vssgloss-g.md) [H](vssgloss-h.md) [I](vssgloss-i.md) J K [L](vssgloss-l.md) M [N](vssgloss-n.md) [O](vssgloss-o.md) [P](vssgloss-p.md) Q [R](vssgloss-r.md) S [T](vssgloss-t.md) U [V](vssgloss-v.md) [W](vssgloss-w.md) X Y Z

<dl> <dt>

<span id="base.vssgloss_selectability_for_backup"></span><span id="BASE.VSSGLOSS_SELECTABILITY_FOR_BACKUP"></span>**selectability for backup**
</dt> <dd>

A component is said to be selectable for backup if its explicit inclusion in a backup operation is optional. Selectability for backup is enabled if the value of the **bSelectable** member of the [**VSS\_COMPONENTINFO**](/windows/desktop/api/VsBackup/ns-vsbackup-vss_componentinfo) structure is **true**. There is no default value for a component's selectability for backup; a writer must always set this value explicitly.

Writers also use selectability for restore to organize their component's participation in restore operations.

See also *selectable component*, *selectability for restore*, [*explicit component inclusion*](vssgloss-e.md), [*implicit component inclusion*](vssgloss-i.md).

</dd> <dt>

<span id="base.vssgloss_selectability_for_restore"></span><span id="BASE.VSSGLOSS_SELECTABILITY_FOR_RESTORE"></span>**selectability for restore**
</dt> <dd>

A component is said to be selectable for restore if it can be implicitly backed up as part of a component set, and then later individually restored without the rest of the component set. Selectability for restore is enabled if the value of the **bSelectableForRestore** member of the [**VSS\_COMPONENTINFO**](/windows/desktop/api/VsBackup/ns-vsbackup-vss_componentinfo) structure is **true**. By default, a component's selectability for restore is **false**. Selectability for restore has meaning only when a component has not been added to the backup document.

See also *selectable component*, *selectability for backup*, [*explicit component inclusion*](vssgloss-e.md), [*implicit component inclusion*](vssgloss-i.md).

</dd> <dt>

<span id="base.vssgloss_selectable_component"></span><span id="BASE.VSSGLOSS_SELECTABLE_COMPONENT"></span>**selectable component**
</dt> <dd>

A component is said to be selectable if its explicit inclusion in a backup or restore operation is optional.

Selectability for backup and selectability for restore are independent of each other—a component may be selectable for both operations, for restore and not backup, or for backup and not restore.

Writers also use selectability to organize their components into groups:

-   Nonselectable components with no selectable ancestors in their logical paths must always be explicitly included if a writer is to be backed up or restored.
-   Nonselectable components with selectable ancestors will only be included in a backup or restore if at least one selectable ancestor is included.
-   Selectable components without selectable ancestors can only be included in a backup or restore operation explicitly.
-   Selectable components with selectable ancestors can be explicitly included in a backup or restore operation, or can be implicitly included if one of their selectable ancestors is included.

See also [*components*](vssgloss-c.md), *selectability for backup*, *selectability for restore*, [*explicit component inclusion*](vssgloss-e.md), [*implicit component inclusion*](vssgloss-i.md).

</dd> <dt>

<span id="base.vssgloss_shadow_copy"></span><span id="BASE.VSSGLOSS_SHADOW_COPY"></span>**shadow copy**
</dt> <dd>

A read-only point-in-time replica of an original volume's contents. Each shadow copy is keyed by a persistent GUID. Also called a volume shadow copy. See also *shadow copy set*.

</dd> <dt>

<span id="base.vssgloss_shadow_copies_for_shared_folders"></span><span id="BASE.VSSGLOSS_SHADOW_COPIES_FOR_SHARED_FOLDERS"></span>**Shadow Copies for Shared Folders**
</dt> <dd>

A feature of Windows that creates lightweight, online backup copies of volumes using VSS. Clients can access these backups through the Windows shell to see old versions of files and undo mistakes without requiring a full restore. See also [*client accessible shadow copy*](vssgloss-c.md).

</dd> <dt>

<span id="base.vssgloss_shadow_copy_set"></span><span id="BASE.VSSGLOSS_SHADOW_COPY_SET"></span>**shadow copy set**
</dt> <dd>

A collection of volume shadow copies created at the same time and identified by a common shadow copy set ID (a persistent GUID) value. This is the mechanism used to allow a shadow copy operation to be managed across volumes. See also *shadow copy*.

</dd> <dt>

<span id="base.vssgloss_software_based_provider"></span><span id="BASE.VSSGLOSS_SOFTWARE_BASED_PROVIDER"></span>**software provider**
</dt> <dd>

A provider that intercepts I/O requests at the software level between the file system and the volume manager. See also [*hardware provider*](vssgloss-h.md), [*provider*](vssgloss-p.md).

</dd> <dt>

<span id="base.vssgloss_subcomponent"></span><span id="BASE.VSSGLOSS_SUBCOMPONENT"></span>**subcomponent**
</dt> <dd>

Any component that has a logical path containing a selectable (for either backup or restore) parent component. Subcomponents must have a logical path of the form {component\_name}\\{subcomponent\_name}. If a subcomponent's selectable (for either backup or restore) ancestor is explicitly included in a backup or restore, then the subcomponent is implicitly included in the operation. Implicitly included subcomponents do not have their data included in the Backup Components Document—regardless of whether they are selectable (for either restore or backup) or not. See also [*component*](vssgloss-c.md), [*logical path*](vssgloss-l.md).

</dd> <dt>

<span id="base.vssgloss_surfaced_shadow_copy"></span><span id="BASE.VSSGLOSS_SURFACED_SHADOW_COPY"></span>**surfaced shadow copy**
</dt> <dd>

A shadow copied volume visible to a system's Mount Manager namespace—meaning **FindFirstVolume** and **FindNextVolume** can find it and that volume arrival and departure notifications are generated. All exposed shadow copies are also surfaced shadow copies. However, a surfaced shadow copy need not be exposed. If a shadow copy is transportable, it cannot be surfaced. See also [*exposed shadow copy*](vssgloss-e.md), [*transportable shadow copy*](vssgloss-t.md).

</dd> <dt>

<span id="base.vssgloss_system_file_protection"></span><span id="BASE.VSSGLOSS_SYSTEM_FILE_PROTECTION"></span>**System File Protection**
</dt> <dd>

See [*Windows File Protection*](vssgloss-w.md).

</dd> <dt>

<span id="base.vssgloss_system_level_applications"></span><span id="BASE.VSSGLOSS_SYSTEM_LEVEL_APPLICATIONS"></span>**system-level applications**
</dt> <dd>

Indicates the point at which VSS notifies a writer of a freeze. Writers that are initialized as system-level applications are notified after writers initialized either as front-end level applications or as back-end level applications. See also [*application level*](vssgloss-a.md), [*back-end level applications*](vssgloss-b.md), [*front-end level applications*](vssgloss-f.md).

</dd> <dt>

<span id="base.vssgloss_system_provider"></span><span id="BASE.VSSGLOSS_SYSTEM_PROVIDER"></span>**system provider**
</dt> <dd>

The default preinstalled provider provided as part of Windows.

</dd> <dt>

<span id="base.vssgloss_system_volume_folder"></span><span id="BASE.VSSGLOSS_SYSTEM_VOLUME_FOLDER"></span>**System Volume Folder**
</dt> <dd>

A shared directory that stores the shared copies of a domain's public files—that is, those files that are replicated among all domain controllers in the domain.

</dd> </dl>

 

 



