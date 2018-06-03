---
title: WPDObject.GetChildrenByFormat method
description: The GetChildrenByFormat method returns a collection of the immediate children of this WPDObject filtered by one or more object formats.
ms.assetid: 51d383a4-ac01-4f42-a39c-9d4d59705a4a
keywords:
- GetChildrenByFormat method WPD Automation
- GetChildrenByFormat method WPD Automation , WPDObject object
- WPDObject object WPD Automation , GetChildrenByFormat method
topic_type:
- apiref
api_name:
- WPDObject.GetChildrenByFormat
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WPDObject.GetChildrenByFormat method

The **GetChildrenByFormat** method returns a collection of the immediate children of this **WPDObject** filtered by one or more object formats.

## Syntax


```JScript
retVal = WPDObject.GetChildrenByFormat(
  FormatList
)
```



## Parameters

<dl> <dt>

*FormatList* 
</dt> <dd>

A **VARIANT** that can be a string containing the name of one format, or an array of strings containing several formats. An individual format name can be a WPD-defined format, a service-defined format, or a string representation of a format GUID, such as "{aaaaaaaa-bbbb-cccc-dddd-eeeeeeffffff}".

</dd> </dl>

## Return value

Returns a [**childrenCollection**](childrencollection-object.md) that contains all of the immediate children of this **WPDObject** that have been formatted with one of the object formats in the format list.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**childrenCollection Object**](childrencollection-object.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> </dl>

 

 





