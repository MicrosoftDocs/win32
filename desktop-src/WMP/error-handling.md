---
title: Error Handling (Windows Media Player SDK)
description: Error Handling
ms.assetid: f0567c77-a855-4b93-9fb7-a36cde63859f
keywords:
- Windows Media Player,error handling
- Windows Media Player object model,error handling
- object model,error handling
- Windows Media Player ActiveX control,error handling
- ActiveX control,error handling
- Windows Media Player Mobile ActiveX control,error handling
- Windows Media Player Mobile,error handling
- migration guide,error handling
- error handling in object model
ms.topic: article
ms.date: 05/31/2018
---

# Error Handling (Windows Media Player SDK)

The Windows Media Player 6.4 ActiveX control provides default error handling by displaying error messages in dialog boxes and on the status bar. You can also provide custom error handling by processing errors in your script. Error handling is event driven, which means you receive a notification for each error, and must decide how to deal with each error event when it occurs. For more information about handling errors using the version 6.4 object model, see the Error Handling section of the Version 6.4 Player Object Model Guide, which is part of the Windows Media Player SDK.

The Windows Media Player 7 or later object model provides the **Error** object and the **ErrorItem** object to handle errors. These two objects work together to provide you with an error handling mechanism that gives you complete and flexible control of the error handling process. The **Error** object provides access to a collection of **ErrorItem** objects; each **ErrorItem** object provides details about an individual error message.

When an error occurs, the error information is posted to an error queue. The queue is a collection of **ErrorItem** objects. As each error is added to the queue, it is associated with an index number (beginning with zero) that can be used to identify the particular **ErrorItem** object. The *Error*.**errorCount** property retrieves the number of errors in the error queue. Since the index numbers are zero-based, the most recent error posted to the queue will always have an index value equal to *Error*.**errorCount** minus one.

You can create an error event handler for Windows Media Player using script. The following JScript example shows how to retrieve the most recent error item from the error queue and display the error code and error description using the Windows Media Player 7 or later object model. The **Player** object was created with ID = "WMP9".


```C++
<!-- Create an error event handler for Windows Media Player 7 or later errors. -->
<SCRIPT  LANGUAGE = "JScript"  FOR = WMP9  EVENT = error()>

// Store the number of errors in the error queue.
var max = WMP9.error.errorCount;

// Retrieve most recent ErrorItem object.
var err = WMP9.error.item(max-1)

// Store the error code number.
var errNum = err.errorCode;

// Store the error description string.
var errDesc = err.errorDescription;

// Build a message string to notify the user.
var msg = "Error number: " + errNum + "\n";
msg += "Error description: " + errDesc;

// Display the message box.
alert(msg);

</SCRIPT>

```



The **Error** object has two additional methods that you can use. The *Error*.**clearErrorQueue** method allows you to remove all the errors from the error queue and reset the index number to zero. You have complete control over this process; you can keep errors in the queue for as long as you need them to be available, and then empty the queue when you're finished handling the errors.

The *Error*.**webHelp** method provides a way to display the most current error information to the user by using the Internet. When called, this method transfers all relevant information about the first error in the queue (the one with index zero) to Microsoft Windows Media Player Web Help, which displays further information about the error in the current browser window.

## Related topics

<dl> <dt>

[**Error Object**](error-object.md)
</dt> <dt>

[**ErrorItem Object**](erroritem-object.md)
</dt> <dt>

[**Object Model Migration Guide**](object-model-migration-guide.md)
</dt> </dl>

 

 




