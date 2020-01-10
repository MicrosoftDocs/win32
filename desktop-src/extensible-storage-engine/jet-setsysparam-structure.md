---
title: JET_SETSYSPARAM Structure
TOCTitle: JET_SETSYSPARAM Structure
ms:assetid: 3c0fdd28-99bd-4026-b64b-6859ef9dc91b
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg269230(v=EXCHG.10)
ms:contentKeyID: 32765532
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

# JET_SETSYSPARAM Structure


_**Applies to:** Windows | Windows Server_

## JET_SETSYSPARAM Structure

An array of **JET_SETSYSPARAM** structures indicate a specific set of global system parameters that are set as an argument when using the [JetEnableMultiInstance](gg294107\(v=exchg.10\).md) function.

**Windows XP:** This structure is introduced in Windows XP.

```cpp
    typedef struct {
      unsigned long paramid;
      JET_API_PTR lParam;
      const tchar* sz;
      JET_ERR err;
    } JET_SETSYSPARAM;
```

### Members

**paramid**

The ID of the system parameter that will be set.

See [Extensible Storage Engine System Parameters](gg294139\(v=exchg.10\).md) for a complete list of system parameters and their properties.

**lParam**

The optional value to be set for the selected system parameter if that system parameter is of an integer type.

**sz**

The optional value to be set for the selected system parameter if that system parameter is of a string type.

**err**

The error resulting from the call to [JetSetSystemParameter](gg294044\(v=exchg.10\).md) with the previously specified parameters.

### Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Client</strong></p></td>
<td><p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p></td>
</tr>
<tr class="even">
<td><p><strong>Server</strong></p></td>
<td><p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Header</strong></p></td>
<td><p>Declared in Esent.h.</p></td>
</tr>
<tr class="even">
<td><p><strong>Unicode</strong></p></td>
<td><p>Implemented as <strong>JET_ SETSYSPARAM_W</strong> (Unicode) and <strong>JET_ SETSYSPARAM_A</strong> (ANSI).</p></td>
</tr>
</tbody>
</table>


### See Also

[Extensible Storage Engine System Parameters](gg294139\(v=exchg.10\).md)  
[JET_API_PTR](gg269209\(v=exchg.10\).md)  
[JET_ERR](gg294092\(v=exchg.10\).md)  
[JetEnableMultiInstance](gg294107\(v=exchg.10\).md)  
[JetSetSystemParameter](gg294044\(v=exchg.10\).md)

