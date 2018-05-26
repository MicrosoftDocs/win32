---
title: createContainer.onTransferProgress event
description: The onTransferProgress event indicates the progress of a data transfer operation from an IStream.
ms.assetid: 35c2b56c-4e1e-4155-ae4b-efb9e9f95f68
keywords:
- onTransferProgress event WPD Automation
- onTransferProgress event WPD Automation , createContainer object
- createContainer object WPD Automation , onTransferProgress event
topic_type:
- apiref
api_name:
- createContainer.onTransferProgress
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# createContainer.onTransferProgress event

The **onTransferProgress** event indicates the progress of a data transfer operation from an **IStream**.

## Syntax


```JScript
createContainer.onTransferProgress(
  numBytesTransferred,
  numTotalBytes
)
```



## Parameters

<dl> <dt>

*numBytesTransferred* 
</dt> <dd>

The number of bytes that have been transferred so far.

</dd> <dt>

*numTotalBytes* 
</dt> <dd>

The total number of bytes that will be transferred.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event will occur only if the **Data** property is set to a valid **IStream**, and the **AddChild** method is called to assign this container object to a parent object and to persist the data. If the **Data** property is not assigned, this event will not be triggered.

For an example of how to use the **onTransferProgress** event, see the examples in the topic [Asynchronous Functions](asynchronous-functions.md).

## Examples

The following code shows the handler-function syntax for the **onTransferProgress** event.


```JScript
function HandlerFunction(numBytesTransferred, numTotalBytes)
{

   // Code to handle an asynchronous transfer operation.              

}

// Set the event handler.
createContainerObject.onTransferProgress = HandlerFunction;
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

[**Storage Object**](storage-object.md)
</dt> </dl>

 

 





