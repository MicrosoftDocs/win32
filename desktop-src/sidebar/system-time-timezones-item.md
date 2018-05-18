---
title: timeZones.item property
description: Gets a System.Time.timeZone object from the timeZones collection.
ms.assetid: 'be5fd778-e568-4e3a-b479-94e4c350c9b2'
keywords: ["item property Windows Sidebar", "item property Windows Sidebar , timeZones collection", "timeZones collection Windows Sidebar , item property"]
topic_type:
- apiref
api_name:
- timeZones.item
api_location:
- Sidebar.Exe
api_type:
- COM
---

# timeZones.item property

\[ The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets a [**System.Time.timeZone**](system-time-timezone.md) object from the [**timeZones**](system-time-timezones.md) collection.

This property is read-only.

## Syntax


```JScript
objitem = timeZones.item
```



## Property value

An **Object** that receives a [**System.Time.timeZone**](system-time-timezone.md) object from the specified index.

## Examples

The following example demonstrates how to iterate through the [**timeZones**](system-time-timezones.md) collection.


```JScript
// Set the time zone selection list.
var sTimeZoneSelect = function() 
{ 
    var sSelect = "<select name='TimeZones' id='selTimeZones' title='Time zones' onChange='DisplayTimeZoneContent()'>";
    for (var loop = 0; loop < collTimeZones.count; loop++)
    {
        oTimeZone = collTimeZones.item(loop);
        sSelect += "<option value='" + oTimeZone.name + "'";
        if (oTimeZone.standardDisplayName == oSelectedTimeZone.standardDisplayName)
        {
            sSelect += " selected";
        }
        sSelect += ">" + oTimeZone.name + "</option>";
    }
    sSelect += "</select>";
    return sSelect;
}
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**timeZones**](system-time-timezones.md)
</dt> <dt>

[**count**](system-time-timezones-count.md)
</dt> </dl>

 

 





