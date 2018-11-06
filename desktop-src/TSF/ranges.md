---
title: Ranges
description: Ranges
ms.assetid: '7488e29e-3409-4db3-98b4-f3438ad7c94e'
keywords:
- Text Services Framework (TSF),ranges
- TSF (Text Services Framework),ranges
- text services,ranges
- TSF-enabled applications,ranges
- ranges
- Text Services Framework (TSF),anchors
- TSF (Text Services Framework),anchors
- text services,anchors
- TSF-enabled applications,anchors
- anchors
- Text Services Framework (TSF),clones
- TSF (Text Services Framework),clones
- text services,clones
- TSF-enabled applications,clones
- clones
- Text Services Framework (TSF),backups
- TSF (Text Services Framework),backups
- text services,backups
- TSF-enabled applications,backups
- backups
ms.topic: article
ms.date: 05/31/2018
---

# Ranges

## Anchors

A range is delimited by two *anchors*, a start anchor and an end anchor. An anchor exists in an imaginary slot between two characters. The start anchor relates to text that follows the anchor and the end anchor relates to text that precedes the anchor. Both the start and end anchors can exist in the same location. In this case, the range has zero length.

For example, start with the following text:


```C++
This is text.
```



Now apply a range to this text with both the start and end anchors at position 0. It is visually represented as:


```C++
<anchor></anchor>This is text.
```



The anchors do not take up any space within the text itself. This is a zero-length range and its text is empty.

Now shift the end anchor +3 positions. It is visually represented as:


```C++
<anchor>Thi</anchor>s is text.
```



The start anchor is positioned just before the character in position 0 and the end anchor is positioned just after the character in position 3 because the end anchor moved to the right 3 places. The range of text is now "Thi".

Additionally, the start anchor cannot be made to follow the end anchor and the end anchor cannot be made to precede the start anchor.

## Anchor Gravity

Each anchor has a *gravity* setting that determines how the anchor responds when text is inserted into the text stream at the anchor position. When an insertion is made at the position of an anchor, an adjustment must be made in the position of the anchor. The gravity determines how this anchor position adjustment is made.

For example:


```C++
It is <anchor></anchor>cold today.
```



If the word "very " is inserted at the range position, the start anchor can be positioned either before or after the inserted word:


```C++
It is <anchor>very </anchor>cold today.
```



\- Or -


```C++
It is very <anchor></anchor>cold today.
```



The anchor gravity specifies how the anchor is repositioned when an insertion is made at its position. The gravity can be either *backward* or *forward*.

If the anchor has backward gravity, the anchor moves backward, relative to the insertion point, on insertion so that the inserted text follows the anchor:


```C++
It is <anchor>very </anchor>cold today.
```



If the anchor has forward gravity, the anchor moves forward (relative to the insertion point) on insertion so that the inserted text precedes the anchor:


```C++
It is very <anchor></anchor>cold today.
```



## Clones and Backups

There are two ways to make a "copy" of a range object. The first is to make a *clone* of the range using [ITfRange::Clone](/windows/desktop/api/Msctf/nf-msctf-itfrange-clone). The second is to make a *backup* of the range using [ITfContext::CreateRangeBackup](/windows/desktop/api/Msctf/nf-msctf-itfcontext-createrangebackup).

A clone is a copy of a range that does not include static data. The anchors of the range are copied, but the clone still covers a range of text within the context. A clone is a range object in all respects. This means that the text and properties for a cloned range are dynamic and will change if the text and/or properties of the range covered by the clone changes.

A backup stores the text and properties of a range at the time the backup is made as static data. A backup also clones the original range so that changes to the size and position of the original range can be tracked. This means that the text and properties for a backed up range are static and do not change if the text and/or properties of the range covered by the backup changes.

For example, the following range (pRange) within the context:


```C++
"This is some <pRange>text</pRange>."
```



Now make a clone and a backup of this range:


```C++
ITfRange *pClone;
ITfRangeBackup *pBackup;

pRange->Clone(&pClone);
pContext->CreateRangeBackup(ec, pRange, &pBackup);
```



Now, the objects contain the following:


```C++
pRange  = "text"
pClone  = "text"
pBackup = "text"
```



Now change the text of pRange:


```C++
WCHAR wsz[] = L"other words";
pRange->SetText(ec, 0, wsz, lstrlenW(wsz));
```



Now, the objects contain the following:


```C++
Context = "This is some other words."
pRange  = "other words"
pClone  = "other words"
pBackup = "text"
```



Setting the text caused the text within the context to change. It also caused the end anchor of pRange and pClone to change. pClone now contains "other words" because the text changed within the range and these changes are tracked by all ranges. When the text covered by both pRange and pClone changed, the text of pClone changed as well.

The text in pBackup has not changed from the original pRange because the data (text and properties) in the backup is unrelated to the context and is stored separately. The clone contained within the backup does actually change, but the data is static.

When restoring a backup, the backup can be applied to the clone within the backup or to a different range entirely. To apply the backup to the clone within the backup, pass **NULL** to [ITfRangeBackup::Restore](/windows/desktop/api/Msctf/nf-msctf-itfrangebackup-restore) as shown in the following code example:


```C++
pBackup->Restore(ec, NULL);
```



Now, the objects contain the following:


```C++
Context = "This is some text."
pRange  = "text"
pClone  = "text"
pBackup = "text"
```



To restore the backup to a different range, pass a pointer to the range object when calling **ITfRangeBackup::Restore**. The backed up text and properties will be applied to the new range. For example, using the example above prior to the **Restore** call, pRange will be modified to demonstrate this:


```C++
LONG lShifted;
pRange->ShiftEnd(ec, -2, &lShifted, NULL);
```



Now, the objects contain the following:


```C++
Context = "This is some other words."
pRange  = "other wor"
pClone  = "other words"
pBackup = "text"
```



When the end anchor of pRange was shifted to the left two places, the end anchor of pClone did not change.

Now restore the backup using pRange with the following code example:


```C++
pBackup->Restore(ec, pRange);
```



Now, the objects contain the following:


```C++
Context = "This is some textds."
pRange  = "text"
pClone  = "textds"
pBackup = "text"
```



The text covered by pRange has been replaced with "text", a portion of the text covered by pClone has changed, and pBackup changes to match pRange.

 

 




