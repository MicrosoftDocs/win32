---
title: Asynchronous Functions
description: For certain functions, asynchronous behavior can be enabled by setting an event handler for the completion events.
ms.assetid: 2d902b43-c1b7-470d-a75c-8aee93ccef87
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Asynchronous Functions

For certain functions, asynchronous behavior can be enabled by setting an event handler for the completion events.

> \[!Important\]  
> A function will behave asynchronously only if the event handler is set before the corresponding function for the completion event is called.

 

The following table shows the supported completion events and the corresponding functions.



| Completion event                                                               | Function                                                                 |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| [**onAddChildComplete**](service-onaddchildcomplete.md)                       | [**Service.AddChild**](service-addchild.md)                             |
| [**onGetChildrenByFormatComplete**](service-ongetchildrenbyformatcomplete.md) | [**Service.GetChildrenByFormat**](service-getchildrenbyformat.md)       |
| [**on*MethodName*Complete**](service-onmethodcomplete.md)                     | [**Service.*MethodName***](service-method.md) (service-defined methods) |
| [**onRemoveChildComplete**](service-onremovechildcomplete.md)                 | [**Service.RemoveChild**](service-removechild.md)                       |
| [**onAddChildComplete**](storage-onaddchildcomplete.md)                       | [**Storage.AddChild**](storage-addchild.md)                             |
| [**onGetChildrenByFormatComplete**](storage-ongetchildrenbyformatcomplete.md) | [**Storage.GetChildrenByFormat**](storage-getchildrenbyformat.md)       |
| [**onRemoveChildComplete**](storage-onremovechildcomplete.md)                 | [**Storage.RemoveChild**](storage-removechild.md)                       |



 

> [!Note]  
> For service-defined methods, the actual method name should be used in place of *MethodName*. For example, if a service supports the **AssociateContactWithRingtone** method, the completion event will be **onAssociateContactWithRingtoneComplete**.

 

The following sections illustrate reading resource data asynchronously by using a completion event, and writing resource data asynchronously by using an XMLHTTPRequest in asynchronous mode. To enable asynchronous behavior while writing data to a resource, an ActiveXObject such as MSXML2 can be used to open an XMLHTTPRequest in asynchronous mode, and a [**Resource.Stream**](resource-stream.md) can be sent using the XMLHTTPRequest.

## Asynchronously Reading Resource Data

The following JScript example modifies the synchronous example of retrieving ringtone data from a device and uploading it to a Web service. The modifications make the example asynchronous by opening an XMLHTTPRequest in asynchronous mode.

This example also uses an event handler for the [**Resource.onTransferProgress**](ontransferprogress.md) event to show the progress of the upload.


```JScript
// Retrieve the first instance of the Ringtones Service.
var ringtonesService = deviceObject.GetServicesByType("{D0EACE0E-707D-4106-8D38-4F560E6A9F8E}")[0];

// Event handler for showing upload progress.
function HandleUploadProgress(numBytes, totalBytes)
{
   var percentage = Math.round(numBytes/totalBytes * 100);

   // Display progress here.
}

function ReadRingtoneFromDeviceAsync()
{
   // Retrieve the first instance of the Ringtones Service.
   var ringtonesService = deviceObject.GetServicesByType("{D0EACE0E-707D-4106-8D38-4F560E6A9F8E}")[0];

   // Get the first available ringtone data.
   var ringtone = ringtonesService.GetChildrenByFormat("mp3")[0];
   var data = ringtone.Data;

   // Set the event handler for onTransferProgress to track 
   // the progress of the upload.
   data.onTransferProgress = HandleUploadProgress;     

   // Open an XMLHttpRequest to the Web service that will receive
   // the ringtone data.
   var request = new ActiveXObject("MSXML2.XMLHTTP.3.0");

   // Set this up as an asynchronous request by setting the
   // second parameter to true.
   request.open("PUT", "https://vendor/site/device/receiveRingtone.asp", true);
  
   // Send the ringtone to the Web service request asynchronously.
   request.send(data.Stream);
}
```



## Asynchronous Writing of Resource Data

The following JScript example modifies the synchronous example of a ringtone download/upload (see [Synchronous Reading and Writing](synchronous-reading-and-writing.md)) and makes it asynchronous by adding the HandleDownloadComplete event handler and setting it on the *ringtonesService*.onAddChildComplete event.

Two steps in the example remain the same: The new ringtone is downloaded from a Web service by using a resource stream. However, when the new ringtone is added as a child of the device service, the event handler is called asynchronously.

This example also uses an event handler for the [**Resource.onTransferProgress**](ontransferprogress.md) event to show the progress of the download.


```JScript
// Retrieve the first instance of the Ringtones Service.
var ringtonesService = deviceObject.GetServicesByType("{D0EACE0E-707D-4106-8D38-4F560E6A9F8E}")[0];

// Set the event handler for the onAddChildComplete method to 
// enable asynchronous mode and track completion. This handler
// must be set before AddChild is called to configure it to use
// asynchronous mode. Otherwise, AddChild will be synchronous.
ringtonesService.onAddChildComplete = HandleDownloadComplete;

// Event handler for showing download progress.
function HandleDownloadProgress(numBytes, totalBytes)
{
   var percentage = Math.round(numBytes/totalBytes * 100);

   // Display progress here.
}

// Event handler to show download completion. When this handler
// is set for the Service.onAddChildComplete method, it enables
// asynchronous mode.
function HandleDownloadComplete(hresult, newRingtone)
{
   alert(newRingtone.ObjectName + " uploaded successfully, hresult is: " + hresult);
}

function WriteRingtoneToDeviceAsync(title)
{
   // Open an XMLHttpRequest to the Web service that will send
   // the ringtone data.
   var request = new ActiveXObject("MSXML2.XMLHTTP.3.0");

   // Set this up as a synchronous request by setting the
   // second parameter to false.
   request.open("GET", "https://vendor/site/device/sendRingtone.asp", false);
   request.send();
   var stream = request.responseStream;

   // Create a new mp3 container object (a Creation Container Object)
   // and initialize it with data from the stream that contains the
   // new ringtone.
   var container = ringtonesService.CreateNewObject("mp3");

   container.ObjectName = title;
   container.Data = stream; 

   // Set the event handler for onTransferProgress to track 
   // the progress of the download.
   container.onTransferProgress = HandleDownloadProgress;

   // Add the new ringtone object to the device as a child of the
   // service object.
   ringtonesService.AddChild(container);

   // Add the new ringtone object to the device as a child of the
   // service object. 
   // Note: since we are using asynchronous mode, there is no 
   // return value. The new ringtone is returned as a parameter
   // of HandleDownloadComplete.
   ringtonesService.AddChild(container);

   ...
}
```



## Related topics

<dl> <dt>

[**Creation Container Object**](creation-container-object.md)
</dt> <dt>

[**Device Object**](device-object.md)
</dt> <dt>

[Reading and Writing Resource Data](reading-and-writing-resource-data.md)
</dt> <dt>

[**Resource Object**](resource-object.md)
</dt> <dt>

[**Service Object**](service-object.md)
</dt> </dl>

 

 




