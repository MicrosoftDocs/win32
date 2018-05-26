---
title: System.Time.timeZones property
description: A collection of System.Time.timeZone objects.
ms.assetid: a763108e-11dd-4430-b743-e8aa87aedd1c
keywords:
- timeZones property Windows Sidebar
- timeZones property Windows Sidebar , System.Time object
- System.Time object Windows Sidebar , timeZones property
topic_type:
- apiref
api_name:
- System.Time.timeZones
api_location:
- Sidebar.Exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.Time.timeZones property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

A collection of [**System.Time.timeZone**](system-time-timezone.md) objects.

> [!Note]  
> Objects of type [**System.Time.timeZone**](system-time-timezone.md) can only be accessed through the **timeZones** collection. This collection is a member of [**System.Time**](system-time.md).

 

This property is read-only.

## Syntax


```JScript
objtimeZones = System.Time.timeZones
```



## Property value

A collection of [**System.Time.timeZone**](system-time-timezone.md) objects.

## Examples

The following example demonstrates how to create a **timeZones Collection**, select the [**System.Time.timeZone**](system-time-timezone.md) instance at index `1` from the **timeZones Collection**, and access the `name` property of that **System.Time.timeZone** instance.


```JScript
var collTimeZones = System.Time.timeZones; 
            
var oTimeZone = collTimeZones.item(1);  
            
var strName = oTimeZone.displayName;
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**count**](system-time-timezones-count.md)
</dt> <dt>

[**item**](system-time-timezones-item.md)
</dt> <dt>

[**System.Time.timeZone**](system-time-timezone.md)
</dt> <dt>

[**System.Time**](system-time.md)
</dt> </dl>

 

 





