---
title: Creation Container object
description: The Creation Container object is used to temporarily hold properties and data that must be set during the creation of a new object. It does not represent an actual object on the device.
ms.assetid: 6fe901a2-0702-4622-9350-d5bfd0dcc5cb
keywords:
- Creation Container object WPD Automation
- Creation Container object WPD Automation , described
topic_type:
- apiref
api_name:
- Creation Container
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# Creation Container object

The **Creation Container** object is used to temporarily hold properties and data that must be set during the creation of a new object. It does not represent an actual object on the device.

A **Creation Container** object is created when the [**Storage.CreateNewObject**](storage-createnewobject.md) method or the [**Service.CreateNewObject**](service-createnewobject.md) method is called. The properties of the **Creation Container** are used to set property values and data for the creation of a new **WPDObject**. However, a new object is not created, and the values and data set in the **Creation Container** are not persisted until the **Creation Container** is passed as a parameter to the **AddChild** method.

This JScript example demonstrates creating a **Creation Container**, setting the properties and data in the **Creation Container**, and persisting the properties and data by calling the **Service.AddChild** method.


```JScript
var createContainer = serviceObject.CreateNewObject("Mp3");

// Set the value of some service-defined properties.
createContainer.MusicAlbum = "Album Name";
createContainer.MusicArtist = "Artist Name";

// Receive object data from a completed XML HTTP Request and use the
// Data property to assign it to the createContainer.
var stream = xmlHttpRequest.getResponseStream();
createContainer.Data = stream;

// This method creates a new WPDObject (in this case, a Service object)
// using the properties and data in the createContainer, and adds it to
// the parent object.
serviceObject.AddChild(createContainer);
```



## Members

The **Creation Container** object has these types of members:

-   [Events](#events)
-   [Properties](#properties)

### Events

The **Creation Container** object has these events.



| Event                                                                      | Description                                                                          |
|:---------------------------------------------------------------------------|:-------------------------------------------------------------------------------------|
| [**onTransferProgress**](https://msdn.microsoft.com/library/windows/desktop/dd389201) | Indicates the progress of a data transfer operation from an **IStream**. <br/> |



 

### Properties

The **Creation Container** object has these properties.



| Property                                                                      | Access type           | Description                                                                                                                                                                           |
|:------------------------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Data**](createcontainerobject-data.md)<br/>                         | Write-only<br/> | Assigns an **IStream** returned by [IXMLHttpRequest.getResponseStream](http://go.microsoft.com/fwlink/p/?linkid=130621) to add data to this **Creation Container** object.<br/> |
| [***ServiceProperty***](createcontainerobject-serviceproperty.md)<br/> | Write-only<br/> | Sets the value of a service-defined property on this **Creation Container** object.<br/>                                                                                        |
| [***WpdProperty***](createcontainerobject-wpdproperty.md)<br/>         | Write-only<br/> | Sets the value of a predefined WPD property on this **Creation Container** object.<br/>                                                                                         |



 

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[About the Creation Container Object](about-the-creation-container-object.md)
</dt> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[**Storage Object**](storage-object.md)
</dt> <dt>

[WPD Automation Reference](wpd-automation-reference.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> </dl>

 

 





