---
title: Synchronous Reading and Writing
description: This section demonstrates synchronously reading and writing resource data by downloading a ringtone to a device from a Web service, and uploading ringtone data from a device to a Web service.Note  In Windows 7, updating resource data directly is not supported. To update an existing object's data, a WPD Automation script should delete the existing object containing the old resource data, create a new object with the new resource data, and then add the new object. .
ms.assetid: '83f09399-4b5b-4baf-ace6-97d523e0f2a1'
---

# Synchronous Reading and Writing

This section demonstrates synchronously reading and writing resource data by downloading a ringtone to a device from a Web service, and uploading ringtone data from a device to a Web service.

> [!Note]  
> In Windows 7, updating resource data directly is not supported. To update an existing object's data, a WPD Automation script should delete the existing object containing the old resource data, create a new object with the new resource data, and then add the new object.

 

## Synchronous Reading of Resource Data

The following JScript example demonstrates reading a ringtone from the device and transferring it in a Web service request.


```JScript
function ReadRingtoneFromDevice()
{
   // Retrieve the first instance of the Ringtones Service.
   var ringtonesService = deviceObject.GetServicesByType("{D0EACE0E-707D-4106-8D38-4F560E6A9F8E}")[0];

   // Open an XMLHttpRequest to to the web service that will receive
   // the ringtone data.
   var request = new ActiveXObject("MSXML2.XMLHTTP.3.0");

   // Set this up as a synchronous request by setting the 
   // second parameter to false.
   request.open("PUT", "https://vendor/site/device/receiveRingtone.asp", false);
   
   // Get the first available ringtone data.
   var ringtone = ringtonesService.GetChildrenByFormat("mp3")[0];
   var stream = ringtone.Data.Stream;

   // Send the ringtone to the Web service request.
   request.send(stream);

   // Display the results of the data transfer.
   var result = request.responseText;

   ...   
} 
</script>
```



## Synchronous Writing of Resource Data

The following JScript example demonstrates writing a ringtone from a Web service request to the device.


```JScript
function WriteRingtoneToDevice(title)
{
   // Retrieve the first instance of the Ringtones Service.
   var ringtonesService = deviceObject.GetServicesByType("{D0EACE0E-707D-4106-8D38-4F560E6A9F8E}")[0];

   // Open an XMLHttpRequest to the Web service that will send the
   // ringtone data.
   var request = new ActiveXObject("MSXML2.XMLHTTP.3.0");

   // Set this up as a synchronous request by setting the
   // second parameter to false.
   request.open("GET", "https://vendor/site/device/sendRingtone.asp", false);
   request.send();
   var stream = request.responseStream;

   // Create a new mp3 container object (a Creation Container Object) and
   // initialize it with data from the stream that contains the new
   // ringtone.
   var container = ringtonesService.CreateNewObject("mp3");

   container.ObjectName = title;
   container.Data = stream; 

   // Add the new ringtone object to the device as a child of the
   // service object.
   var ringtone = ringtonesService.AddChild(container);

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

 

 




