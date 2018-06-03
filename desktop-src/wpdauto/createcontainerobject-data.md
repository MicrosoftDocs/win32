---
title: createContainer.Data property
description: The Data property assigns an IStream returned by IXMLHttpRequest.getResponseStream to add data to this Creation Container Object.
ms.assetid: 10ae9243-8838-46f3-b7bc-b73f2742ae1b
keywords:
- Data property WPD Automation
- Data property WPD Automation , createContainer object
- createContainer object WPD Automation , Data property
topic_type:
- apiref
api_name:
- createContainer.Data
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# createContainer.Data property

The **Data** property assigns an **IStream** returned by [IXMLHttpRequest.getResponseStream](http://go.microsoft.com/fwlink/p/?linkid=130621) to add data to this **Creation Container Object**.

This property is write-only.

## Syntax


```JScript
createContainer.Data = Data
```



## Property value

Sets a [**Resource**](resource-object.md) object with a [**Stream**](resource-stream.md) property so that this object can receive data.

## Remarks

To create a properties-only object, for instance, a contact instead of a ringtone, the **Data** property must not be assigned.

## Examples

The following JScript example uses the **Data** property to assign a data stream that populates a **Creation Container** object (called *createContainer*) with Mp3 data. The new **Creation Container** object is then persisted by adding it to a parent service object. As soon as this new object is added, the **onAddChildComplete** event occurs, and a handler function is called to display the result of the **AddChild** method.


```JScript
// Create a handler function for the onAddChildComplete event.

function HandleAddComplete(hresult, newObject)
{
     alert(newObject.ObjectId +
           "created successfully (hresult: " + hresult + ")");
}

// When the CreateNewObject() method is called on a serviceObject or a 
// storageObject, a createContainer is created.

var createContainer = serviceObject.CreateNewObject("Mp3");

// Set the value of some service-defined properties. 

createContainer.MusicAlbum = "Album Name";
createContainer.MusicArtist = "Artist Name";

// Receive object data from a completed XML HTTP Request and use the
// Data property to assign it to the createContainer.

var stream = xmlHttpRequest.getResponseStream();
createContainer.Data = stream;

// Set the handler for the onAddChildComplete event.
// The AddChild method returns immediately, and the
// HandleAddComplete function is called with the object
// creation results. Note that the handler must be set before
// the AddChild method is called to enable an asynchronous
// transfer mode.

parentObject.onAddChildComplete = HandleAddComplete;

// Save the new object as a child of an existing parent object.
// The new object will not be persisted until the AddChild method
// is called. The parent object can also be a Storage Object if the
// new object is added as a child of a Storage.

serviceObject.AddChild(createContainer);
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

[**Resource Object**](resource-object.md)
</dt> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[**Storage Object**](storage-object.md)
</dt> <dt>

[WPD Automation Reference](wpd-automation-reference.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> </dl>

 

 





