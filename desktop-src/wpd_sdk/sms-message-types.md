---
Description: The SMS\_MESSAGE\_TYPES enumeration type describes the content type of a short message service (SMS) message.
ms.assetid: 882886a6-ecce-443f-a7e9-2e4e367ad804
title: SMS\_MESSAGE\_TYPES enumeration
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# SMS\_MESSAGE\_TYPES enumeration

The **SMS\_MESSAGE\_TYPES** enumeration type describes the content type of a short message service (SMS) message.

## Syntax


```C++
typedef enum SMS_MESSAGE_TYPES { 
  SMS_TEXT_MESSAGE    = 0,
  SMS_BINARY_MESSAGE  = 1
} ;
```



## Constants

<dl> <dt>

<span id="SMS_TEXT_MESSAGE"></span><span id="sms_text_message"></span>**SMS\_TEXT\_MESSAGE**
</dt> <dd>

A text message.

</dd> <dt>

<span id="SMS_BINARY_MESSAGE"></span><span id="sms_binary_message"></span>**SMS\_BINARY\_MESSAGE**
</dt> <dd>

A binary message.

</dd> </dl>

## Remarks

This enumeration is used by the [**WPD\_COMMAND\_SMS\_SEND Command**](wpd-command-sms-send-command.md).

## Requirements



|                   |                                                                                             |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures and Enumeration Types**](structures-and-enumeration-types.md)
</dt> </dl>

 

 




