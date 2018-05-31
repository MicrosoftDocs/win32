---
Description: Many fax service administration Component Object Model (COM) objects have Save or Refresh methods you can use to write their configuration to the fax server or to refresh their settings from values in the fax server.
ms.assetid: 9d5c9439-e3d1-4130-923a-60e4e8bf8e34
title: Saving and Refreshing Objects
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Saving and Refreshing Objects

Many fax service administration Component Object Model (COM) objects have **Save** or **Refresh** methods you can use to write their configuration to the fax server or to refresh their settings from values in the fax server. Objects that have read/write properties have a **Save** method, which saves the configuration of the object on the fax server. If an object is destroyed before its **Save** method is called, all data changes are lost without a warning.

Collection objects do not have **Save** or **Refresh** methods. When you add or remove an item from a collection, the operation takes effect immediately.

## Saving Objects

The **Save** method stores all settings of an object in persistent storage. It is important to note that in objects that have a **Save** method, changes to the object will not be saved unless you call the **Save** method.

In the following example, the change made to the device configuration will not be saved until the **Save** method is called in the last line of code.


```
Dim objFaxServer As New FAXCOMEXLib.FaxServer
Dim objFaxDevice As FaxDevice

'Connect to the fax server.
objFaxServer.Connect ""

'Get the device.
Set objFaxDevice = objFaxServer.GetDevices.ItemById(1)
objFaxDevice.Description = "Device Number 1"

'Set the device to answer automatically.
objFaxDevice.ReceiveMode = fdrmAUTO_ANSWER

'Set the number of rings before the device answers.
objFaxDevice.RingsBeforeAnswer = 5

'Enable Send.
objFaxDevice.SendEnabled = True

'Save the device configuration.
objFaxDevice.Save
```



## Refreshing Objects

The **Refresh** method retrieves and applies the most recent configuration for an object. The most recent configuration may be one that you saved using the **Save** method, a change saved by another fax service administrator, or may be a reflection of the status of the fax server. Use the **Refresh** method to be sure you have the current values for an object.

The **Refresh** method overwrites any changes made but not saved when it applies values from persistent storage. This can be useful when you want to cancel changes that have been made but not yet saved with the **Save** method.

> [!Note]  
> The **Refresh** method is optional. If you create an object which has readable properties and do not call its **Refresh** method, the first time your script or program reads any property in the object, a **Refresh** will be performed implicitly to initialize the object with its current state from the server.

 

In the following example the device configuration never changes because the **Save** method is not called before the **Refresh** method is called.


```
Dim objFaxServer As New FAXCOMEXLib.FaxServer
Dim objFaxDevice As FaxDevice

'Connect to the fax server.
objFaxServer.Connect ""

'Get the device.
Set objFaxDevice = objFaxServer.GetDevices.ItemById(1)
objFaxDevice.Description = "Device Number 1"

'Set the device to answer automatically.
objFaxDevice.ReceiveMode = fdrmAUTO_ANSWER

'Set the number of rings before the device answers.
objFaxDevice.RingsBeforeAnswer = 5

'Enable Send.
objFaxDevice.SendEnabled = True

'Abandon changes by calling Refresh.
objFaxDevice.Refresh
```



In the following example the **Refresh** method is called so that the most up-to date information about the **CurrentPage** property is provided to the administrator by the script.


```
Dim objFaxServer As New FAXCOMEXLib.FaxServer
Dim objFaxIncomingJob As FaxIncomingJob
Dim FaxCurrentPage As Long

'Connect to the fax server.
objFaxServer.Connect ""

'Get the job.
Set objFaxIncomingJob = objFaxServer.Folders.IncomingQueue.GetJobs.Item(1)

'Refresh so that you receive current information from the fax server.
objFaxIncomingJob.Refresh

'Get the current page information.
FaxCurrentPage = objFaxIncomingJob.CurrentPage
```



 

 



