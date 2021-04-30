---
description: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 3e8b9c48-9d2d-4055-b78d-c4a22d780764
title: L (Volume Shadow Copy Service)
ms.topic: article
ms.date: 05/31/2018
---

# L (Volume Shadow Copy Service)

[A](vssgloss-a.md) [B](vssgloss-b.md) [C](vssgloss-c.md) [D](vssgloss-d.md) [E](vssgloss-e.md) [F](vssgloss-f.md) [G](vssgloss-g.md) [H](vssgloss-h.md) [I](vssgloss-i.md) J K L M [N](vssgloss-n.md) [O](vssgloss-o.md) [P](vssgloss-p.md) Q [R](vssgloss-r.md) [S](vssgloss-s.md) [T](vssgloss-t.md) U [V](vssgloss-v.md) [W](vssgloss-w.md) X Y Z

<dl> <dt>

<span id="base.vssgloss_logical_path"></span><span id="BASE.VSSGLOSS_LOGICAL_PATH"></span>**logical path**
</dt> <dd>

A mechanism for describing a writer's components. It is used to express relationships between components, in particularly their hierarchy. For instance, if a writer managed several electronic books, it might assign logical paths of "\\ebook\\book1" and "\\ebook\\book2" to file group components containing each book. Logical paths are required when specifying subcomponents.

By convention the backslash "\\" is used to separate elements of a logical path. Beyond that, there are no restrictions on the characters that can appear in a non-**NULL** logical path.

A logical path can be **NULL**. By convention, components with **NULL** logical paths are said to be at the top level of a writer's logical path hierarchy.

See also [*component*](vssgloss-c.md), [*subcomponent*](vssgloss-s.md).

</dd> </dl>

 

 



