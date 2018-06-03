---
title: Service.AddChild method
description: The AddChild method adds a WPDObject obtained from the Service.CreateNewObject method, as a child of this Service object.
ms.assetid: fe8a0f15-cf1d-439f-a8a0-ec4c40df671f
keywords:
- AddChild method WPD Automation
- AddChild method WPD Automation , Service object
- Service object WPD Automation , AddChild method
topic_type:
- apiref
api_name:
- Service.AddChild
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Service.AddChild method

The **AddChild** method adds a **WPDObject** obtained from the [**Service.CreateNewObject**](service-createnewobject.md) method, as a child of this **Service** object.

## Syntax


```JScript
Service.AddChild(
  creationContainerObject
)
```



## Parameters

<dl> <dt>

*creationContainerObject* 
</dt> <dd>

A **creationContainer** that is used to set data in a [**WPDObject**](wpdobject.md) so that it can be added as a child of this **Service** object.

</dd> </dl>

## Return value

If called in synchronous mode, this method returns the newly created child object. If called in asynchronous mode, this method does not return a value. The newly created child object is provided as a parameter to the handler-function assigned to the [**onAddChildComplete**](service-onaddchildcomplete.md) event.

## Remarks

To enable asynchronous behavior, set the handler for the [**onAddChildComplete**](service-onaddchildcomplete.md) event before calling this method.

## Examples

The following JScript example uses the **AddChild** method to add a newly created service object (a WMA ringtone) as a child of another service object.


```JScript
// Get a WMA ringtone from a vendor.         
var request = new ActiveXObject("MSXML2.XMLHTTP.3.0");
request.open("GET", "https://vendor/site/ringtone.wma", false);
request.send();

// Create a new service object. Set its title, and set its data to
// the WMA ringtone.     
var ringtone = ringtoneService.CreateNewObject("Wma");
ringtone.MediaTitle = "blues";
ringtone.Data = request.responseStream;

// Add the new service object as a child of the ringtoneService object.
ringtoneService.AddChild(ringtone); 

// Also add the new object as a child of another object within the
// service. Doing both will result in two separate new service objects
// containing the same WMA ringtone.    
ringtoneFolder.AddChild(ringtone);
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Creation Container Object**](creation-container-object.md)
</dt> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> </dl>

 

 





