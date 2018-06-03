---
title: Resource.onTransferProgress event
description: The onTransferProgress event indicates the progress of a resource-transfer operation.
ms.assetid: 35c2b56c-4e1e-4155-ae4b-efb9e9f95f68
keywords:
- onTransferProgress event WPD Automation
- onTransferProgress event WPD Automation , Resource object
- Resource object WPD Automation , onTransferProgress event
topic_type:
- apiref
api_name:
- Resource.onTransferProgress
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Resource.onTransferProgress event

The **onTransferProgress** event indicates the progress of a resource-transfer operation.

## Syntax


```JScript
Resource.onTransferProgress(
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

For an example of how to use the **onTransferProgress** event, see the examples in the topic [Asynchronous Functions](asynchronous-functions.md).

## Examples

The following code shows the handler-function syntax for the **onTransferProgress** event.


```JScript
function HandlerFunction(numBytesTransferred, numTotalBytes)
{

   // Code to handle an asynchronous transfer operation.              

}

// Set the event handler.
resource.onTransferProgress = HandlerFunction;
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Resource Object**](resource-object.md)
</dt> </dl>

 

 





