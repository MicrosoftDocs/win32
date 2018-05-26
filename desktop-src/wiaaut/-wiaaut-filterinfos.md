---
title: FilterInfos object
description: Contains a collection of all the available FilterInfo objects. See the FilterInfos (ImageProcess) property on the ImageProcess object for detail on accessing the FilterInfos object.
ms.assetid: 4cef3c1d-f6e9-458c-b540-9233b6a46f7b
keywords:
- FilterInfos object WIA Automation
- FilterInfos object WIA Automation , described
topic_type:
- apiref
api_name:
- FilterInfos
api_location:
- Wiaaut.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FilterInfos object

Contains a collection of all the available [**FilterInfo**](-wiaaut-filterinfo.md) objects. See the [**FilterInfos (ImageProcess)**](-wiaaut-iimageprocess-filterinfos.md) property on the [**ImageProcess**](-wiaaut-imageprocess.md) object for detail on accessing the **FilterInfos** object.

## Members

The **FilterInfos** object has these types of members:

-   [Properties](#properties)

### Properties

The **FilterInfos** object has these properties.



| Property                                                             | Access type          | Description                                                                                           |
|:---------------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------------------------|
| [**Count (FilterInfos)**](-wiaaut-ifilterinfos-count.md)<br/> | Read-only<br/> | Retrieves the number of members in the **FilterInfos** collection.<br/>                         |
| [**Item (FilterInfos)**](-wiaaut-ifilterinfos-item.md)<br/>   | Read-only<br/> | Retrieves the specified item in the **FilterInfos** collection either by position or name.<br/> |



 

## Remarks

Note that the **FilterInfos** collection can be accessed by name, making it easy to add a filter to the filter chain.

For example code, see [Create an ImageProcess Object and Create one of Each Available Filter](-wiaaut-shared-samples.md#create-an-imageprocess-object-and-create-one-of-each-available-filter) in Shared Samples.

### Creation\\Access Functions

Use any of the following to retrieve a reference to the object:



[**FilterInfos (ImageProcess)**](-wiaaut-iimageprocess-filterinfos.md)



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**FilterInfos (ImageProcess)**](-wiaaut-iimageprocess-filterinfos.md)
</dt> </dl>

 

 





