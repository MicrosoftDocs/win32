---
title: Service.GetChildrenByFormat method
description: The GetChildrenByFormat method returns a collection of the immediate children of this Service object filtered by one or more object formats.
ms.assetid: 1533aa9c-e730-4034-a504-30ed5c32e8f5
keywords:
- GetChildrenByFormat method WPD Automation
- GetChildrenByFormat method WPD Automation , Service object
- Service object WPD Automation , GetChildrenByFormat method
topic_type:
- apiref
api_name:
- Service.GetChildrenByFormat
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Service.GetChildrenByFormat method

The **GetChildrenByFormat** method returns a collection of the immediate children of this **Service** object filtered by one or more object formats.

## Syntax


```JScript
retVal = Service.GetChildrenByFormat(
  FormatList
)
```



## Parameters

<dl> <dt>

*FormatList* 
</dt> <dd>

**VARIANT** that can be a string containing the name of one format, or an array of strings containing several formats. An individual format name can be a WPD-defined format, a service-defined format, or a string representation of a format GUID, for example "{aaaaaaaa-bbbb-cccc-dddd-eeeeeeffffff}".

</dd> </dl>

## Return value

Returns a **childrenCollection** that contains all of the immediate children of this **Service** object that have been formatted with one of the object formats in the specified format list.

## Remarks

This method might take a while to complete on slower devices, or devices with a lot of content.

To enable asynchronous behavior, set the handler for the [**onGetChildrenByFormatComplete**](service-ongetchildrenbyformatcomplete.md) event before calling this method.

## Examples

The following JScript example uses the **GetChildrenByFormat** method to retrieve a **childrenCollection** of all the Windows Media Audio (WMA) and MP3 formatted ringtones in the ringtoneService object.


```JScript
var children = ringtonesService.GetChildrenByFormat(["Wma", "Mp3"]);
```



The following JScript example demonstrates the different ways in which the **VARIANT** parameter *FormatList* can be expressed. This parameter can contain one or more WPD-defined or service format names.


```JScript
// A string.
var children = service.GetChildrenByFormat("AbstractContact");

// An array of strings.
var children = service.GetChildrenByFormat(["AbstractContact", "Vcard2"]);

// An array of strings in a JScript Array object.
var formats = new Array("AbstractContact", "Vcard2"); 
var children = service.GetChildrenByFormat(formats);

// A string representation of the format GUID. 
var children = service.GetChildrenByFormat("{aaaaaaaa-bbbb-cccc-dddd-eeeeeeffffff}");
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

[**Service Object**](service-object.md)
</dt> </dl>

 

 





