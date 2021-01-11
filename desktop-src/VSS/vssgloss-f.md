---
description: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 9d59b2f6-c3d9-40d4-be89-ae7283794eb3
title: F (Volume Shadow Copy Service)
ms.topic: article
ms.date: 05/31/2018
---

# F (Volume Shadow Copy Service)

[A](vssgloss-a.md) [B](vssgloss-b.md) [C](vssgloss-c.md) [D](vssgloss-d.md) [E](vssgloss-e.md) F [G](vssgloss-g.md) [H](vssgloss-h.md) [I](vssgloss-i.md) J K [L](vssgloss-l.md) M [N](vssgloss-n.md) [O](vssgloss-o.md) [P](vssgloss-p.md) Q [R](vssgloss-r.md) [S](vssgloss-s.md) [T](vssgloss-t.md) U [V](vssgloss-v.md) [W](vssgloss-w.md) X Y Z

<dl> <dt>

<span id="base.vssgloss_file_group_component"></span><span id="BASE.VSSGLOSS_FILE_GROUP_COMPONENT"></span>**file group component**
</dt> <dd>

A group of files other than those used as a database and defined by a writer as needing to be handled as a unit during backup and restore operations. See also [*component*](vssgloss-c.md), [*database component*](vssgloss-d.md).

</dd> <dt>

<span id="base.vssgloss_file_set"></span><span id="BASE.VSSGLOSS_FILE_SET"></span>**file set**
</dt> <dd>

The combination of a path, file specification, and recursive flag describing one of a file or group of files. For example, files are added to components in file sets.

Unless otherwise indicated, a file set's paths are standard Windows paths and can contain environment variables (for example, %SystemRoot%) but cannot contain wildcard characters. There is no requirement that the path end with a backslash ("\\"). It is up to applications that retrieve this information to check it.

The file specification contained in a file set indicates the name of the file or files it includes. This file specification cannot contain directory specifications (for example, no backslashes) but can contain the ? and \* wildcard characters.

The recursive tag is a Boolean specifying whether the file set's path should be treated as a only a single directory or if it indicates a hierarchy of directories to be traversed recursively. The Boolean is **true** if the path is treated as a hierarchy of directories to be traversed recursively, or **false** if not.

Information about a file set is returned through instances of the **IVssWMFiledesc** interface, and can contain additional information includes alternate paths, alternate location mappings, and file-level schema support settings.

See also [*alternate path*](vssgloss-a.md), [*alternate location mapping*](vssgloss-a.md), [*component*](vssgloss-c.md), *file specification*.

</dd> <dt>

<span id="base.vssgloss_file_specification"></span><span id="BASE.VSSGLOSS_FILE_SPECIFICATION"></span>**file specification**
</dt> <dd>

Used to match files within a directory and to define a file set. It cannot contain directory specifications (for example, no backslashes) but it can contain the ? and \* wildcard characters.

</dd> <dt>

<span id="base.vssgloss_file_system_replication"></span><span id="BASE.VSSGLOSS_FILE_SYSTEM_REPLICATION"></span>**File Replication Service**
</dt> <dd>

Used to replicate system files in a redundant system volume (SysVol) directory to support file system survivability, particularly for distributed file systems.

</dd> <dt>

<span id="base.vssgloss_freeze"></span><span id="BASE.VSSGLOSS_FREEZE"></span>**freeze**
</dt> <dd>

A period of time during the shadow copy creation process when all writers have flushed their writes to the volumes and are not initiating additional writes.

</dd> <dt>

<span id="base.vssgloss_freeze_event"></span><span id="BASE.VSSGLOSS_FREEZE_EVENT"></span>**Freeze event**
</dt> <dd>

A VSS event indicating that a shadow copy freeze is in progress. See also *freeze*, [*shadow copy*](vssgloss-s.md).

</dd> <dt>

<span id="base.vssgloss_front_end_level_applications"></span><span id="BASE.VSSGLOSS_FRONT_END_LEVEL_APPLICATIONS"></span>**front-end level applications**
</dt> <dd>

Indicates the point at which a writer is notified of a freeze by VSS. Writers that were initialized as front-end level applications are notified prior to writers initialized either as back-end level applications or as system-level applications. See also [*application level*](vssgloss-a.md), [*back-end level applications*](vssgloss-b.md), [*system-level applications*](vssgloss-s.md), [*writer*](vssgloss-w.md).

</dd> </dl>

 

 



