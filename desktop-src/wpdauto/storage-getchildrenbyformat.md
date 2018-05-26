---
title: Storage.GetChildrenByFormat method
description: The GetChildrenByFormat method returns a collection of the immediate children of this Storage object filtered by one or more object formats.
ms.assetid: 7f9d88e7-802e-4015-b9db-f84bdbadeef3
keywords:
- GetChildrenByFormat method WPD Automation
- GetChildrenByFormat method WPD Automation , Storage object
- Storage object WPD Automation , GetChildrenByFormat method
topic_type:
- apiref
api_name:
- Storage.GetChildrenByFormat
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Storage.GetChildrenByFormat method

The **GetChildrenByFormat** method returns a collection of the immediate children of this **Storage** object filtered by one or more object formats.

## Syntax


```JScript
retVal = Storage.GetChildrenByFormat(
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

Returns a **childrenCollection** that contains all of the immediate children of this **Storage** object that have been formatted with one of the object formats in the specified format list.

## Remarks

This method may take a while to complete on slower devices, or devices with a lot of content.

To enable asynchronous behavior, set the handler for the [**onGetChildrenByFormatComplete**](storage-ongetchildrenbyformatcomplete.md) event before calling this method.

## Examples

The following JScript example uses the **GetChildrenByFormat** method to retrieve a childrenCollection of all the "WMA" and "MP3" formatted objects in the storage object.


```JScript
var storage = deviceObject.Storages[0];        
var childrenCollection = storage.GetChildrenByFormat(["Wma", "Mp3"]);
```



This JScript example demonstrates how the **VARIANT** parameter *FormatList* can be expressed. This parameter can contain one or more WPD-defined or service-defined format names.


```JScript
// A string.
var children = storage.GetChildrenByFormat("Wma");

// An array of strings.
var children = storage.GetChildrenByFormat(["Wma", "Mp3"]);

// An array of strings in a JScript Array object.
var formats = new Array("Wma", "Mp3"); 
var children = storage.GetChildrenByFormat(formats);

// A string representation of the format GUID. 
var children = storage.GetChildrenByFormat("{aaaaaaaa-bbbb-cccc-dddd-eeeeeeffffff}");
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**childrenCollection Object**](childrencollection-object.md)
</dt> <dt>

[**Storage Object**](storage-object.md)
</dt> </dl>

 

 





