---
title: Asynchronous Searching
description: The Device Finder object enables both synchronous and asynchronous searches. Asynchronous searches return control to the calling application immediately.
ms.assetid: 809cfb65-9d08-427b-90d9-b8a836176341
ms.topic: article
ms.date: 05/31/2018
---

# Asynchronous Searching

The Device Finder object enables both synchronous and asynchronous searches. Asynchronous searches return control to the calling application immediately. Then, the application is notified about each individual device as it is found, using a callback interface that the application has registered.

Asynchronous searching is best for graphical user interfaces, and applications that perform continuous monitoring.

The general structure of an asynchronous search is:

1.  Create a search object
2.  Start the search
3.  Receive callback notifications and take the appropriate processing steps.
4.  When the search is no longer needed, cancel the search and release the associated objects.

> [!Note]  
> In the callback code, an application cannot release the object it is receiving notification about, such as a new device, nor can the application cancel the search.

 

## C++ Example

C++ applications must implement a callback object to pass to the search. See [Searching Asynchronously in C++](searching-asynchronously-in-c-.md) for sample code that illustrates this action.

## VBScript Example

VBScript code must pass the address of the callback function.


```VB
Sub DeviceFinderCallback (device, UDN, calltype)

  select case calltype
    Case 0
      output = "Found: " & vbCrLf
      output = output & "DisplayName: " & device.FriendlyName & vbCrLf
      output = output & "Type: " & device.Type & vbCrLf
      output = output & "UDN: " & device.UniqueDeviceName & vbCrLf
      MsgBox output

    Case 1
      MsgBox "device removed: " & UDN

    Case 2
      MsgBox "search complete"

    end select
End Sub

Dim devicefinder
Dim findData

Set devicefinder = CreateObject("UPnP.UPnPDeviceFinder")

Sub StartFind()
  findData = devicefinder.CreateAsyncFind("upnp:rootdevice", 0, _
   GetRef("DeviceFinderCallback"))

  devicefinder.StartAsyncFind(findData)
End Sub

Sub StopFind()
  deviceFinder.CancelAsyncFind(findData)
End Sub
```



 

 




