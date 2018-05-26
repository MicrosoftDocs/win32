---
title: WPDObject.WpdProperty property
description: The WpdProperty property gets or sets a predefined WPD property for this WPDObject.
ms.assetid: 4ecfc875-5d23-4417-b7f5-d36d6f60df6c
keywords:
- WpdProperty property WPD Automation
- WpdProperty property WPD Automation , WPDObject object
- WPDObject object WPD Automation , WpdProperty property
topic_type:
- apiref
api_name:
- WPDObject.WpdProperty
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WPDObject.WpdProperty property

The ***WpdProperty*** property gets or sets a predefined WPD property for this **WPDObject**.

This property is read/write.

## Syntax


```JScript
WpdProperty = WPDObject.WpdProperty
WPDObject.WpdProperty = WpdProperty
```



## Property value

This property has the same value as the predefined WPD property that it is reading from or writing to.

## Remarks

The following table contains the minimum required set of predefined WPD properties for a **WPDObject**. The properties are accessed by the WPD Automation name that corresponds to the WPD PROPERTYKEY.

For a complete list of WPD PROPERTYKEYs and their corresponding WPD Automation names, see [**Names for WPD PROPERTYKEYs**](names-for-wpd-propertykeys.md).



| WPD PROPERTYKEY                     | WPD Automation Name                           |
|-------------------------------------|-----------------------------------------------|
| WPD\_OBJECT\_ID                     | ObjectId                                      |
| WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID | ObjectPersistentUniqueId                      |
| WPD\_OBJECT\_FORMAT                 | ObjectFormat                                  |
| WPD\_OBJECT\_CONTENT\_TYPE          | ObjectContentType                             |
| WPD\_OBJECT\_SIZE                   | ObjectSize (for objects containing data only) |



 

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**WPDObject**](wpdobject.md)
</dt> </dl>

 

 





