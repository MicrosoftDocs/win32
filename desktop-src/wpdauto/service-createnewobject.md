---
title: Service.CreateNewObject method
description: The CreateNewObject method creates and initializes a WPDObject to the specified data format.
ms.assetid: cd1a3595-02f7-4282-a5af-c558110c9dbb
keywords:
- CreateNewObject method WPD Automation
- CreateNewObject method WPD Automation , Service object
- Service object WPD Automation , CreateNewObject method
topic_type:
- apiref
api_name:
- Service.CreateNewObject
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Service.CreateNewObject method

The **CreateNewObject** method creates and initializes a [**WPDObject**](wpdobject.md) to the specified data format.

## Syntax


```JScript
retVal = Service.CreateNewObject(
  Format
)
```



## Parameters

<dl> <dt>

*Format* 
</dt> <dd>

String that is the data format of the new **WPDObject**.

</dd> </dl>

## Return value

Returns a [**Creation Container**](creation-container-object.md) object that is used to set properties and data. When the [**Creation Container**](creation-container-object.md) is passed to the [**Service.AddChild**](service-addchild.md) method, a new **WPDObject** containing the properties and data of the specified data format will be added as the child of a **Service** object.

## Examples

The following JScript example uses the **CreateNewObject** method to add a newly created **Service** object (a WMA ringtone) as a child of another **Service** object. In this example, *ringtone* is the [**Creation Container**](creation-container-object.md) that is used to set the property *MediaTitle*, and the ringtone data. When *ringtone* is added as a child of the *ringtoneService* object, it becomes a new **WPDObject** object that represents a ringtone on the device, and the property value and data are persisted.


```JScript
// Get a WMA ringtone from a vendor.         
var request = new ActiveXObject("MSXML2.XMLHTTP.3.0");
request.open("GET", "https://vendor/site/ringtone.wma", false);
request.send();

// Create a new service object of the "Wma" format. Set its title,
// and set its data to the WMA ringtone obtained from the vendor.    
var ringtone = ringtonesService.CreateNewObject("Wma");  
ringtone.MediaTitle = "blues";
ringtone.Data = request.responseStream;

// Add the new service object as a child of the ringtoneService object.
// Note that the new object will not be persisted until it is added by
// using this method.    
ringtoneService.AddChild(ringtone);
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> </dl>

 

 





