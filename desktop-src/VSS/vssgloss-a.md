---
description: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 928341a3-ed3a-4db0-9648-1a5efaff5435
title: A (Volume Shadow Copy Service)
ms.topic: article
ms.date: 05/31/2018
---

# A (Volume Shadow Copy Service)

A [B](vssgloss-b.md) [C](vssgloss-c.md) [D](vssgloss-d.md) [E](vssgloss-e.md) [F](vssgloss-f.md) [G](vssgloss-g.md) [H](vssgloss-h.md) [I](vssgloss-i.md) J K [L](vssgloss-l.md) M [N](vssgloss-n.md) [O](vssgloss-o.md) [P](vssgloss-p.md) Q [R](vssgloss-r.md) [S](vssgloss-s.md) [T](vssgloss-t.md) U [V](vssgloss-v.md) [W](vssgloss-w.md) X Y Z

<dl> <dt>

<span id="base.vssgloss_abort_event"></span><span id="BASE.VSSGLOSS_ABORT_EVENT"></span>**Abort event**
</dt> <dd>

A VSS event issued by the Volume Shadow Copy Service indicating that a compliant backup or restore operation has been aborted. The event handler is **CVssWriter::OnAbort**.

</dd> <dt>

<span id="base.vssgloss_active_directory"></span><span id="BASE.VSSGLOSS_ACTIVE_DIRECTORY"></span>**Active Directory**
</dt> <dd>

Active Directory Service (ADSI) is a COM-based service providing a mechanism for locating, identifying, and accessing the users and resources available in a distributed computing environment system. In particular, the Active Directory service is used to manage enterprise directory information for distribution by a Windows domain server.

</dd> <dt>

<span id="base.vssgloss_alternate_location_mapping"></span><span id="BASE.VSSGLOSS_ALTERNATE_LOCATION_MAPPING"></span>**alternate location mapping**
</dt> <dd>

A path, other than a file's original path, to which the file may be restored under certain conditions. Typically, alternate location mappings are not defined for a single well-defined file, but for a path/file specification pair, and may be recursive.

An alternate location mapping is used only during a restore operation and should not be confused with an alternate path, which is used only during a backup operation. See also *alternate path*.

</dd> <dt>

<span id="base.vssgloss_alternate_path"></span><span id="BASE.VSSGLOSS_ALTERNATE_PATH"></span>**alternate path**
</dt> <dd>

During backup operations, a path/file specification pair (handled by an instance of the **IVssWMFiledesc** interface) is said to have an alternate path if its file descriptor (as returned by **IVssWMFiledesc::GetAlternateLocation**) is non-NULL. It is from this path, rather than the default specified path, that files are to be copied when a volume is backed up.

An alternate path is used only during a backup operation and should not be confused with an alternate location mapping. An alternate location mapping is used only during restore operations. See also *alternate location mapping*.

</dd> <dt>

<span id="base.vssgloss_application_level"></span><span id="BASE.VSSGLOSS_APPLICATION_LEVEL"></span>**application level**
</dt> <dd>

Used by VSS to indicate the point in the course of the creation of a shadow copy that a writer is notified of a freeze. See also [*back-end level applications*](vssgloss-b.md), [*freeze*](vssgloss-f.md), [*front-end level applications*](vssgloss-f.md), [*shadow copy*](vssgloss-s.md), [*system-level applications*](vssgloss-s.md), [*writer*](vssgloss-w.md).

</dd> <dt>

<span id="base.vssgloss_auto_recoved_shadow_copy"></span><span id="BASE.VSSGLOSS_AUTO_RECOVED_SHADOW_COPY"></span>**auto-recovered shadow copy**
</dt> <dd>

A shadow copy that has had additional processing by a writer to be in a completely consistent state for backup or data mining actions (for example, rolling back all transactions that did not yet complete at the point that the shadow copy was created.) This can be initiated by a writer by specifying an appropriate flag from the **VSS\_COMPONENT\_FLAGS** enumeration in the **dwComponentFlags** member of the **VSS\_COMPONENTINFO** structure or by a requester by adding the **VSS\_VOLSNAP\_ATTR\_ROLLBACK\_RECOVERY** flag to the context for the shadow copy. Auto-recovery allows the shadow copied data to be used on a read-only volume, for data mining, partial restores (for example selected items in a database), or other purposes.

See also [*transportable shadow copy*](vssgloss-t.md).

</dd> <dt>

<span id="base.vssgloss_auto_release_shadow_copy"></span><span id="BASE.VSSGLOSS_AUTO_RELEASE_SHADOW_COPY"></span>**auto-release shadow copy**
</dt> <dd>

A shadow copy that will be deleted upon the termination of a backup operation. Programmatically, this means the shadow copy will be deleted when the **IVssBackupComponents** interface is released. An auto-release shadow copy cannot be persistent.

By default, all shadow copies are auto-release. See also [*persistent shadow copy*](vssgloss-p.md), [*transportable shadow copy*](vssgloss-t.md).

</dd> </dl>

 

 



