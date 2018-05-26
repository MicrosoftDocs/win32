---
title: To create a full-text search stop list
description: To create a full-text search stop list
ms.assetid: 660C38DF-384D-4b3a-8AB0-2534609BCE57
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# To create a full-text search stop list

1.  Open a text editor, such as Microsoft Notepad, and create a text file.
2.  Type in any words or numbers you want to exclude from a search, one word per line.
3.  Save the file, and then rename it with .stp as the file name extension.
4.  Add the .stp file to the same directory as your project (.hhp) file.
5.  [Add the stop list to your project file](to-add-a-full-text-search-stop-list-to-a-help-project.md).

## Sample stop list

Copy any words from the following sample that you want to include in your stop list:

-   a
-   about
-   after
-   against
-   all
-   also
-   among
-   an
-   and
-   are
-   as
-   at
-   be
-   became
-   because
-   been
-   between
-   but
-   by
-   can
-   come
-   do
-   during
-   each
-   early
-   for
-   form
-   found
-   from
-   had
-   has
-   have
-   he
-   her
-   his
-   however
-   in
-   include
-   into
-   is
-   it
-   its
-   late
-   later
-   me
-   med
-   made
-   many
-   may
-   more
-   most
-   near
-   no
-   non
-   not
-   of
-   on
-   only
-   or
-   other
-   over
-   several
-   she
-   some
-   such
-   than
-   that
-   the
-   their
-   then
-   there
-   these
-   they
-   this
-   through
-   to
-   under
-   until
-   use
-   was
-   we
-   were
-   when
-   where
-   which
-   who
-   with
-   you

## Notes

-   A stop list decreases the size of the full-text search index, which results in a smaller compiled help (.chm) file because fewer words are indexed. This is especially important if you have a large documentation set. All words in the stop list are omitted from the search. These are usually commonly occurring words, such as "the," "and," or "1" that a user is unlikely to search for.
-   Numbers can also be used in a stop list.
-   For the 1.3 release of HTML Help, the size of this file is limited to 512 bytes.
-   Do not set the stop list as read-only, it will not function if this property is set.

## Related topics

<dl> <dt>

[About Full-Text Search](adding-a-search-tab.md)
</dt> </dl>

 

 




