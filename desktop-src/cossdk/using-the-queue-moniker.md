---
description: The queue moniker is used to activate a queued component programmatically.
ms.assetid: d3d22ae6-7d16-4f25-9f15-21b2163cb0f5
title: Using the Queue Moniker
ms.topic: article
ms.date: 05/31/2018
---

# Using the Queue Moniker

The queue moniker is used to activate a queued component programmatically. The queue moniker requires that it receive the class ID (CLSID) of the object to be invoked from the new moniker directly to the right of it. When left-prefixed, the new moniker passes the CLSID to the moniker to the left of it.

## Component Services Administrative Tool

Does not apply.

## Visual Basic

The GetObject display name parameter is "queue:/new:", followed by the program ID or string-form GUID, with or without braces, of the server object to be instantiated. The following examples show three valid activations of a component with the queue moniker:

1.  ``` syntax
    Set objMyQC = GetObject ("queue:/new:QCShip.Ship")
    ```

2.  ``` syntax
    Set objMyQC = GetObject ("queue:/new:{812DF40E-BD88-11D0-8A6D-00C04FC340EE}")
    ```

3.  ``` syntax
    Set objMyQC = GetObject ("queue:/new:812DF40E-BD88-11D0-8A6D-00C04FC340EE")
    ```

## C/C++

The [**CoGetObject**](/windows/win32/api/objbase/nf-objbase-cogetobject) display name parameter is "queue:/new:", followed by the program ID or string-form GUID, with or without braces, of the server object to be instantiated. The following examples show three valid activations of a component with the queue moniker:

1.  ``` syntax
    hr = CoGetObject (
      L"queue:/new:QCShip.Ship",
      NULL, IID_IShip, (void**)&pShip);
    ```

2.  ``` syntax
    hr = CoGetObject (
      L"queue:/new:{812DF40E-BD88-11D0-8A6D-00C04FC340EE}", 
      NULL, IID_IShip, (void**)&pShip);
    ```

3.  ``` syntax
    hr = CoGetObject (
      L"queue:/new:812DF40E-BD88-11D0-8A6D-00C04FC340EE",
      NULL, IID_IShip, (void**)&pShip);
    ```

## Remarks

The queue moniker accepts optional parameters that alter the properties of the message sent to Message Queuing. For example, to cause the Message Queuing message to be sent with a priority 6, the queued component would be activated as follows:

``` syntax
hr = CoGetObject (
  L"queue:Priority=6,ComputerName=MyComp/new:QCShip.Ship",
  NULL, IID_IShip, (void**)&pShip);
```

The following table lists the queue moniker parameters that affect the destination queue.




| Parameter | Description | 
|-----------|-------------|
| <em>ComputerName</em><br /> | Specifies the computer name portion of a Message Queuing queue path name. The Message Queuing queue path name is formatted as <em>ComputerName</em>\<em>QueueName</em>. If not specified, the computer name associated with the configured application is used.<br /> | 
| <em>QueueName</em><br /> | Specifies the Message Queuing queue name. The Message Queuing queue path name is formatted as <em>ComputerName</em>\<em>QueueName</em>. If not specified, the queue name associated with the configured application is used.<br /> To get a non-transactional queue, you can specify the queue name first and then create a COM+ application of the same name.<br /> | 
| <em>PathName</em><br /> | Specifies the complete Message Queuing queue path name. If not specified, the Message Queuing queue path name associated with the configured application is used. To override the destination name, the path can be specified in the following form for a Message Queuing workgroup installation:<br /> Queue:<em>PathName</em>=<em>ComputerName</em>\PRIVATE$\AppName/new:Myproject.CMyClass<br /><blockquote>[!Note]<br />Both the C and Microsoft Visual C++ programming languages require two backslashes to represent one backslash within string literals for example, chicago\\payroll.</blockquote><br /> | 
| <em>FormatName</em><br /> | When you mark a COM+ application as queued, COM+ creates a Message Queuing queue whose name is the same as the application. The Message Queuing format name of that queue is in the COM+ catalog, associated with the COM+ application. To override the destination name, the format name can be specified in the following form for a Message Queuing workgroup installation:<br /> Queue:<em>FormatName</em>=DIRECT=OS:<em>ComputerName</em>\PRIVATE$\AppName/new:ProgId<br /> In an Active Directory configuration, "PRIVATE$" is not specified as part of the queue name. <br /> | 




 

> [!Note]  
> Optional queue moniker parameters are processed left-to-right. Specify each keyword only one time. Specifying the *PathName* parameter replaces both the *ComputerName* and *QueueName*parameters. A specific *FormatName* parameter deletes prior knowledge of a *ComputerName*, *QueueName*, and *PathName* parameter.

 

## Associating the Queued Components Listener with a Specific Private Queue

The COM+ Queued Components listener receives only from queues associated with the COM+ application marked queued. When you mark a COM+ application as queued, COM+ creates a Message Queuing queue whose name is the same as the application. The Message Queuing format name of that queue is in the COM+ catalog, associated with the COM+ application. When the COM+ application is started and marked as listen, a listener in the COM+ application process is started and the queue is opened. The following table lists the queue moniker parameters that affect the Message Queuing message.




| Parameter | Description | 
|-----------|-------------|
| <em>AppSpecific</em><br /> | Specifies an unsigned integer for example, AppSpecific=12345.<br /> | 
| <em>AuthLevel</em><br /> | Specifies the message authentication level. An authenticated message is digitally signed and requires a certificate for the user sending the message. Acceptable values:<br /><ul><li>MQMSG_AUTH_LEVEL_NONE,0</li><li>MQMSG_AUTH_LEVEL_ALWAYS,1</li></ul> | 
| <em>Delivery</em><br /> | Specifies the message delivery option. This value is ignored for transactional queues. Acceptable values:<br /><ul><li>MQMSG_DELIVERY_EXPRESS,0</li><li>MQMSG_DELIVERY_RECOVERABLE,1</li></ul> | 
| <em>EncryptAlgorithm</em><br /> | Specifies the encryption algorithm to be used by Message Queuing to encrypt and decrypt the message. Acceptable values:<br /><ul><li>CALG_RC2, CALG_RC4</li><li>Any integer value that is acceptable to Message Queuing for an <em>EncryptAlgorithm</em>.</li></ul> | 
| <em>HashAlgorithm</em><br /> | Specifies a cryptographic hash function. Acceptable values:<br /><ul><li>CALG_MD2, CALG_MD4, CALG_MD5, CALG_SHA, CALG_SHA1, CALG_MAC, CALG_SSL3_SHAMD5, CALG_HMAC, CALG_TLS1PRF</li><li>Any integer value that is acceptable to Message Queuing for a <em>HashAlgorithm</em>.</li></ul> | 
| Journal<br /> | Specifies the Message Queuing message journal option. Acceptable values:<br /><ul><li>MQMSG_JOURNAL_NONE,0</li><li>MQMSG_DEADLETTER,1</li><li>MQMSG_JOURNAL,2</li></ul> | 
| <em>Label</em><br /> | Specifies a message label string up to MQ_MAX_MSG_LABEL_LEN characters. <br /> | 
| <em>MaxTimeToReachQueue</em><br /> | Specifies a maximum time, in seconds, for the message to reach the queue. <br /> Acceptable values:<br /><ul><li>INFINITE</li><li>LONG_LIVED</li><li>Number of seconds</li></ul> | 
| <em>MaxTimeToReceive</em><br /> | Specifies a maximum time, in seconds, for the message to be received by the target application. Acceptable values:<br /><ul><li>INFINITE</li><li>LONG_LIVED</li><li>Number of seconds</li></ul> | 
| <em>Priority</em><br /> | Specifies a message priority level, within the Message Queuing values permitted.<br /> Acceptable values:<br /><ul><li>MQ_MIN_PRIORITY,0</li><li>MQ_MAX_PRIORITY,7</li><li>MQ_DEFAULT_PRIORITY,3</li><li>Number between 0 and 7</li></ul> | 
| <em>PrivLevel</em><br /> | Specifies a privacy level, used to encrypt messages.<br /> Acceptable values:<br /><ul><li>MQMSG_PRIV_LEVEL_NONE, NONE, 0</li><li>MQMSG_PRIV_LEVEL_BODY, BODY,</li><li>MQMSG_PRIV_LEVEL_BODY_BASE, BODY_BASE, 1</li><li>MQMSG_PRIV_LEVEL_BODY_ENHANCED, BODY_ENHANCED, 3</li></ul> | 
| <em>Trace</em><br /> | Specifies trace options, used in tracing Message Queuing routing.<br /> Acceptable values:<br /><ul><li>MQMSG_TRACE_NONE,0</li><li>MQMSG_SEND_ROUTE_TO_REPORT_QUEUE,1</li></ul> | 




 

The complete set of COM+ Administrative SDK functions is available by using COM objects. This allows any program to start and stop COM+ applications as required.

> [!Note]  
> When a COM+ application is started, it is the application that is running, not the individual components within the application. If an application calls a non-queued component, the COM+ application that contains the component is started. If the listener check box is enabled, the listener also starts and begins processing for messages for queued components. While the queued components service can be started in this way, if you package queued and non-queued components into a single COM+ application, be sure that you really want queued components to start if a non-queued component is executed. If this is not the case, package the queued components into a COM+ application that is separate from the other components.

 

## Related topics

<dl> <dt>

[Activating Component Queues](activating-component-queues.md)
</dt> </dl>
