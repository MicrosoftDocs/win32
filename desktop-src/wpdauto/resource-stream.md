---
title: Resource.Stream property
description: The Stream property gets or sets an IStream containing resource data.
ms.assetid: 'cdd3e719-de9c-4b23-a863-a879e4056a4c'
keywords: ["Stream property WPD Automation", "Stream property WPD Automation , Resource object", "Resource object WPD Automation , Stream property"]
topic_type:
- apiref
api_name:
- Resource.Stream
api_type:
- COM
---

# Resource.Stream property

The **Stream** property gets or sets an **IStream** containing resource data.

This property is read-only.

## Syntax


```JScript
Stream = Resource.Stream
```



## Property value

An **IStream** containing **Resource** data.

## Remarks

The **IStream** in this property can be used in conjunction with the **IXMLHttpRequest.send** method to transmit and receive data via XML HTTP Requests. The example code on this page shows how this is done.

## Examples

The following JScript example uses **Resource.Stream** in a function that retrieves a stream of diagnostic data from a device, transfers the data to a web service, and displays the upload result in an HTML Div called UploadResultDiv.


```JScript
// This function reads diagnostics data from a device and displays 
// the data in UploadResultDiv.

function UploadDiagnostics()
{
   // Invoke a service-defined method to retrieve the diagnostics
   // resource from the device.
   var diagnostics = acmeSupportService.Diagnostics();
    
   // Use the Stream property of the resource to access its IStream.
   var stream = diagnostics.Data.Stream;

   // Create a new XML HTTP object for sending and receiving requests.
   var request = new ActiveXObject("MSXML2.XMLHTTP.3.0");
   request.open("PUT", "https://vendor/site/device/uploadSettings.asp", false);
   
   // Establish a connection with the resource stream so that
   // data can be sent. 
   request.send(stream);  
   
   // Display the results of the data transfer from the resource stream. 
   UploadResultDiv.childNodes[0].nodeValue = request.responseText;
}
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Resource Object**](resource-object.md)
</dt> </dl>

 

 





