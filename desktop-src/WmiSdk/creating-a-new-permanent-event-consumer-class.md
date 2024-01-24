---
description: One of the first steps in creating a permanent event consumer is to create the WMI class that describes the event consumer. Specifically, the permanent event consumer class defines the parameters of the action implemented by the physical consumer.
ms.assetid: a5b6d0b9-8df1-47e3-bb3b-cc69db6d9c0e
ms.tgt_platform: multiple
title: Creating a New Permanent Event Consumer Class
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Creating a New Permanent Event Consumer Class

One of the first steps in creating a permanent event consumer is to create the WMI class that describes the event consumer. Specifically, the permanent event consumer class defines the parameters of the action implemented by the physical consumer.

The following procedure describes how to create a permanent event consumer class.

**To create a permanent event consumer class**

1.  Derive a class from the [**\_\_EventConsumer**](--eventconsumer.md) system class.
2.  Implement any parameters necessary to process an event notification.

The following example shows the syntax used to create the SMTPConsumerEvent class. You can use this as an example for creating your new class. The [**SMTPEventConsumer**](smtpeventconsumer.md) class sends an email message by using Simple Mail Transfer Protocol (SMTP) each time an event is delivered to it. This class is defined in smtpcons.mof.

``` syntax
class SMTPEventConsumer : __EventConsumer
{
  [key] string Name;
  [not_null] string SMTPServer;
  [Template] string Subject;
  [Template] string FromLine;
  [Template] string ReplyToLine;
  [Template] string Message;
  [Template] string ToLine;
  [Template] string CcLine;
  [Template] string BccLine;
  string HeaderFields[];
};
```

You should be able to create instances of your permanent event consumer class to describe one or more ways to send events to your physical consumer. For more information, see [Creating a Logical Consumer](creating-a-logical-consumer.md).

 

 



