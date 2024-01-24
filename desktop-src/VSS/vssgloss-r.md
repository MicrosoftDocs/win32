---
description: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 2442a788-2e70-44c1-9c38-901c1c18a742
title: R (Volume Shadow Copy Service)
ms.topic: article
ms.date: 05/31/2018
---

# R (Volume Shadow Copy Service)

[A](vssgloss-a.md) [B](vssgloss-b.md) [C](vssgloss-c.md) [D](vssgloss-d.md) [E](vssgloss-e.md) [F](vssgloss-f.md) [G](vssgloss-g.md) [H](vssgloss-h.md) [I](vssgloss-i.md) J K [L](vssgloss-l.md) M [N](vssgloss-n.md) [O](vssgloss-o.md) [P](vssgloss-p.md) Q R [S](vssgloss-s.md) [T](vssgloss-t.md) U [V](vssgloss-v.md) [W](vssgloss-w.md) X Y Z

<dl> <dt>

<span id="base.vssgloss_requester"></span><span id="BASE.VSSGLOSS_REQUESTER"></span>**requester**
</dt> <dd>

Minimally, any process that interacts with VSS to create and manage shadow copies and shadow copy sets of one or more volumes.

Typically, a requester manages shadow copies to support some other functionality, such as backup and restore operations and disk mirroring. See also [*shadow copy*](vssgloss-s.md), [*shadow copy set*](vssgloss-s.md).

</dd> <dt>

<span id="base.vssgloss_restore_method"></span><span id="BASE.VSSGLOSS_RESTORE_METHOD"></span>**restore method**
</dt> <dd>

A specification of the restore process method. It controls such issues as whether files are overwritten on restore. If a restore method setting is in conflict with those of the restore target, then the restore target takes precedence. See also *restore target*.

</dd> <dt>

<span id="base.vssgloss_restore_target"></span><span id="BASE.VSSGLOSS_RESTORE_TARGET"></span>**restore target**
</dt> <dd>

Under VSS, a restore target is a specification of how a requester should restore a file, for example, if it should overwrite existing files.

</dd> </dl>

 

 



