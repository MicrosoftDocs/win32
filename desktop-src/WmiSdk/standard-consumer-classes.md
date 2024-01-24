---
description: The following table lists the classes for WMI preinstalled permanent consumers.
ms.assetid: 1239ea25-2835-4546-b66d-20a83704653e
ms.tgt_platform: multiple
title: Standard Consumer Classes
ms.topic: article
ms.date: 05/31/2018
---

# Standard Consumer Classes

The following table lists the classes for WMI preinstalled permanent consumers. You can create instances of these classes to provide the permanent consumer class to supply the logical consumer that responds when triggered by the events specified in the filter. For example, use the [**ActiveScriptEventConsumer**](activescripteventconsumer.md) class to define the script that executes when a specified event occurs.

For more information, see [Monitoring and Responding to Events with Standard Consumers](monitoring-and-responding-to-events-with-standard-consumers.md) and [Monitoring Events](monitoring-events.md).



| Class                                                                        | Description                                                                                                                                                                                                                                           |
|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ActiveScriptEventConsumer**](activescripteventconsumer.md)               | Executes a predefined script in an arbitrary scripting language when an event is delivered to it.<br/> Example: [Running a Script Based on an Event](running-a-script-based-on-an-event.md)<br/>                                         |
| [**CommandLineEventConsumer**](commandlineeventconsumer.md)                 | Launches an arbitrary process in the local system context when an event is delivered to it.<br/> Example: [Running a Program from the Command Line Based on an Event](running-a-program-from-the-command-line-based-on-an-event.md)<br/> |
| [**LogFileEventConsumer**](logfileeventconsumer.md)                         | Writes customized strings to a text log file when events are delivered to it.<br/> Example: [Writing to a Log File Based on an Event](writing-to-a-log-file-based-on-an-event.md)<br/>                                                   |
| [**NTEventLogEventConsumer**](nteventlogeventconsumer.md)                   | Logs a specific message to the Windows event log when an event is delivered to it.<br/> Example: [Logging to NT Event Log Based on an Event](logging-to-nt-event-log-based-on-an-event.md)<br/>                                          |
| [**ScriptingStandardConsumerSetting**](scriptingstandardconsumersetting.md) | Provides registration data common to all instances of the [**ActiveScriptEventConsumer**](activescripteventconsumer.md) class.<br/>                                                                                                            |
| [**SMTPEventConsumer**](smtpeventconsumer.md)                               | Sends an email message using SMTP each time an event is delivered to it.<br/> Example: [Sending Email Based on an Event](sending-e-mail-based-on-an-event.md)<br/>                                                                       |



 

## Related topics

<dl> <dt>

[Monitoring Events](monitoring-events.md)
</dt> <dt>

[Receiving Events At All Times](receiving-events-at-all-times.md)
</dt> <dt>

[Running a Script Based on an Event](running-a-script-based-on-an-event.md)
</dt> <dt>

[Sending Email Based on an Event](sending-e-mail-based-on-an-event.md)
</dt> </dl>

 

 




