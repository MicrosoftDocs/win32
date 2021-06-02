---
description: "Learn more about: JET_BKLOGTIME Structure"
title: JET_BKLOGTIME Structure
TOCTitle: JET_BKLOGTIME Structure
ms:assetid: 31460079-7c5b-4145-837d-b112ba0117d6
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269219(v=EXCHG.10)
ms:contentKeyID: 32765522
ms.date: 04/11/2016
ms.topic: reference
api_name: 
topic_type: 
- apiref
- kbArticle
api_type: 
- COM
api_location: 
ROBOTS: INDEX,FOLLOW

---

# JET_BKLOGTIME Structure


_**Applies to:** Windows | Windows Server_

## JET_BKLOGTIME Structure

The **JET_BKLOGTIME** structure holds the date and time elements of an event. It is an extension of [JET_LOGTIME](./jet-logtime-structure.md).

**Windows Vista:  JET_BKLOGTIME** is introduced in Windows Vista.

```cpp
    typedef struct {
      char bSeconds;
      char bMinutes;
      char bHours;
      char bDay;
      char bMonth;
        char bYear;
        union {
        char bFiller1;
        struct {
          unsigned char fTimeIsUTC: 1;
          unsigned char fUnused: 7;
        };
      };
      union {
        char bFiller2;
        struct {
          unsigned char fOSSnapshot  :1;
          unsigned char fReserved  :7;
        };
      };
    } JET_BKLOGTIME;
```

### Members

**bSeconds**

The time of the event in seconds. This can be 0 (zero) to 60. 0 (zero) is used when the **JET_BKLOGTIME** structure is "null".

**bMinutes**

The time of the event in minutes. This can be 0 (zero) to 60. 0 (zero) is used when the **JET_BKLOGTIME** structure is "null".

**bHours**

The time of the event in hours. This can be 0 (zero) to 24. 0 (zero) is used when the **JET_BKLOGTIME** structure is "null".

**bDay**

The day of the month of the event. This can be 0 (zero) to 31. 0 (zero) is used when the **JET_BKLOGTIME** structure is "null".

**bMonth**

The month of the year of the event. This can be 0 (zero) to 12. 0 (zero) is used when the **JET_BKLOGTIME** structure is "null".

**bYear**

The year (offset by 1900) of the event. To achieve the actual year, add 1900 to this value. 0 (zero) is used when the **JET_BKLOGTIME** structure is "null".

**bFiller1**

This field should be ignored.

**fTimeIsUTC**

The time is in UTC format.

**fUnused**

This field should be ignored.

**bFiller2**

This field should be ignored.

**fOSSnapshot**

If this event is a backup, this flag contains one of the following possible values:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Name</p></th>
<th><p>Value</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>streaming backup</p></td>
<td><p>0 (zero)</p></td>
</tr>
<tr class="even">
<td><p>snapshot backup</p></td>
<td><p>1</p></td>
</tr>
</tbody>
</table>


**fReserved**

This field should be ignored.

### Remarks

This structure is used when debugging.

### Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Client</strong></p></td>
<td><p>Requires Windows Vista.</p></td>
</tr>
<tr class="even">
<td><p><strong>Server</strong></p></td>
<td><p>Requires Windows Server 2008.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Header</strong></p></td>
<td><p>Declared in Esent.h.</p></td>
</tr>
</tbody>
</table>


### See Also

[JET_LOGTIME](./jet-logtime-structure.md)  
[JET_DBINFOMISC](./jet-dbinfomisc-structure.md)
