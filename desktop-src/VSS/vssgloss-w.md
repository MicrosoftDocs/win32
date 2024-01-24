---
description: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: daa383ba-994e-4986-9979-119576cecd1c
title: W (Volume Shadow Copy Service)
ms.topic: article
ms.date: 05/31/2018
---

# W (Volume Shadow Copy Service)

[A](vssgloss-a.md) [B](vssgloss-b.md) [C](vssgloss-c.md) [D](vssgloss-d.md) [E](vssgloss-e.md) [F](vssgloss-f.md) [G](vssgloss-g.md) [H](vssgloss-h.md) [I](vssgloss-i.md) J K [L](vssgloss-l.md) M [N](vssgloss-n.md) [O](vssgloss-o.md) [P](vssgloss-p.md) Q [R](vssgloss-r.md) [S](vssgloss-s.md) [T](vssgloss-t.md) U [V](vssgloss-v.md) W X Y Z

<dl> <dt>

<span id="base.vssgloss_windows_file_protection"></span><span id="BASE.VSSGLOSS_WINDOWS_FILE_PROTECTION"></span>**Windows File Protection**
</dt> <dd>

A system service that protects special operating system files. If one of these files is deleted or overwritten, Windows File Protection replaces the file with the original from its cache.

</dd> <dt>

<span id="base.vssgloss_writer"></span><span id="BASE.VSSGLOSS_WRITER"></span>**writer**
</dt> <dd>

An application that coordinates its I/O operations with VSS shadow copy and shadow copy related operations (such as backups and restores) so that their data contained on the shadow copied volume is in a consistent state.

To support this coordination, a writer must implement an instance of a class derived from the abstract base class **CVssWriter** to communicate with the VSS infrastructure. See also [*shadow copy*](vssgloss-s.md).

</dd> <dt>

<span id="base.vssgloss_writer_class"></span><span id="BASE.VSSGLOSS_WRITER_CLASS"></span>**writer class**
</dt> <dd>

A globally unique identifier (GUID) supplied by a writer during initialization to indicate that it belongs to a given type of writers. For instance, multiple implementations of a writer could share the same writer class ID.

Writers of the same class may be distinguished by their writer instances. It is up to an application developer to specify writer classes. See also *writer instance*.

</dd> <dt>

<span id="base.vssgloss_writer_instance"></span><span id="BASE.VSSGLOSS_WRITER_INSTANCE"></span>**writer instance**
</dt> <dd>

A globally unique identifier (GUID) supplied by VSS for each writer process running on a system. A unique value for the writer instance is generated each time the writer starts.

</dd> <dt>

<span id="base.vssgloss_writer_metadata_document"></span><span id="BASE.VSSGLOSS_WRITER_METADATA_DOCUMENT"></span>**Writer Metadata Document**
</dt> <dd>

An XML document created by a writer (using the **IVssCreateWriterMetadata** interface) containing information about the writer's state and components. A requester can query Writer Metadata Documents (using the **IVssExamineWriterMetadata** interface) when performing a restore or backup operation.

A Writer Metadata Document contains the list of all of a writer's components, any one of which might participate in a backup. This differs from the requester's Backup Components Document, which contains only those components explicitly included for a backup or restore operation.

Once constructed, the Writer Metadata Document should be viewed as a read-only object. It can be saved to disk. See also [*Backup Components Document*](vssgloss-b.md), [*explicit component inclusion*](vssgloss-e.md), [*implicit component inclusion*](vssgloss-i.md).

</dd> </dl>

 

 



