---
title: Storage.onObjectAdded event
description: The onObjectAdded event occurs after an object has been added to this Storage object.
ms.assetid: 43aaef2f-9e1f-4aab-9df1-3bc05750dbb7
keywords:
- onObjectAdded event WPD Automation
- onObjectAdded event WPD Automation , Storage object
- Storage object WPD Automation , onObjectAdded event
topic_type:
- apiref
api_name:
- Storage.onObjectAdded
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Storage.onObjectAdded event

The **onObjectAdded** event occurs after an object has been added to this **Storage** object.

## Syntax


```JScript
Storage.onObjectAdded(
  wpdObject
)
```



## Parameters

<dl> <dt>

*wpdObject* 
</dt> <dd>

The **WPDObject** that was added.

</dd> </dl>

## Return value

This event does not return a value.

## Examples

The following code shows the handler-function syntax for the **onObjectAdded** event.


```JScript
function HandlerFunction(wpdObject)
{

   // Code to handle a newly added object.               

}

// Set the event handler.
Storage.onObjectAdded = HandlerFunction;
```



> [!Note]  
> We recommended that you clear the event handler of a **Storage** object variable by setting it to **null**, before reusing that variable to represent a new object. This will keep an event handler object from persisting as a property of the old **Storage** object.

 

The following example demonstrates this with the **Storage** object variable "currentStorage". The variable is used to represent one **Storage** object, and a handler-function is set for that object. The handler-function is then cleared before currentStorage is used to represent a new **Storage** object.


```JScript
// Set this variable to represent a Storage object.
currentStorage = deviceObject.Storages[0];

// Set the event handler for the Storage object.
currentStorage.onObjectAdded = HandlerFunction;

// Do something with the storage object.
...

// Clear the event handler when done with the storage object.
currentStorage.onObjectAdded = null;

// Set the variable to represent a new Storage object.
currentStorage = deviceObject.Storages[1];
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Storage Object**](storage-object.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> </dl>

 

 





