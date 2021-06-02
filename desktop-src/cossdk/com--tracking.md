---
description: COM+ Tracking
ms.assetid: ad3bdeb5-f303-411a-abfb-ccde3f9a86b9
title: COM+ Tracking
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Tracking

The COM+ tracking service enables you to build your own administrative and diagnostic programs that track the status and performance of running COM+ applications. COM+ tracking provides statistical information about the use of COM+ applications as well as status information, such as whether a COM+ server application instance is paused or has been recycled. Tools can use tracking information in diagnostic monitoring or for display purposes. For example, the Component Services administrative tool uses COM+ tracking to display the status of COM+ application instances in the COM+ Applications and Running Processes folders.

COM+ tracking calculates and periodically updates a set of commonly-used metrics, making this information available to programs that need it. It is similar to COM+ Instrumentation in that both services automatically collect data from COM+ application instances and make this data available to consumers. However, there are some important differences between these services, both in the functionality provided and typical usage. The following table summarizes these differences.



| COM+ Instrumentation                                                                                                                                                                                                   | COM+ Tracking                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Fine-grained data. The COM+ instrumentation service notifies registered subscribers of individual discrete events (for example, method called, object destroyed) that occur in a COM+ application instance.<br/> | Aggregated data. COM+ tracking calculates and periodically updates commonly-used metrics for the status and performance of COM+ application instances.<br/> |
| Event subscribers typically calculate metrics on their own, using ad-hoc algorithms and policies.<br/>                                                                                                           | Metrics are calculated automatically by the COM+ tracking service. All consumers get the same data, with no support for custom metrics.<br/>                |
| After registering a subscription, the consumer does not receive any information about a COM+ application instance until an event occurs.<br/>                                                                    | Tracking data for all COM+ application instances may be retrieved at any time.<br/>                                                                         |
| Supports only a COM+ events-based subscription mechanism for consumers.<br/>                                                                                                                                     | Supports both a COM+ events-based subscription mechanism and polling on a COM local server interface.<br/>                                                  |
| Examples                                                                                                                                                                                                               |                                                                                                                                                                   |
| Notifications when a method is called or returns.<br/>                                                                                                                                                           | Average call response time, number of method calls that succeeded or failed in a recent time period, number of objects currently in a method call.<br/>     |
| Notifications when an object is added to or obtained from the object pool.<br/>                                                                                                                                  | Number of objects in the pool, total number of objects.<br/>                                                                                                |
| Notifications when a COM+ server application is started, paused, or recycled.<br/>                                                                                                                               | Status of the COM+ server application process (for example, whether it is paused or recycled).<br/>                                                         |
| Notifications of transaction start, prepare, abort, and commit events.<br/>                                                                                                                                      | No equivalent.<br/>                                                                                                                                         |
| Notifications of successful and failed method call level authentication attempts.<br/>                                                                                                                           | No equivalent.<br/>                                                                                                                                         |



 

Although COM+ tracking is more limited in terms of data scope and flexibility for calculating metrics, the metrics it provides should be sufficient for a wide variety of administrative and diagnostic programs. Using COM+ tracking, when possible, can simplify the design of these programs. Additionally, using COM+ tracking in production systems can have a significantly lower performance impact, making it more appropriate for real-time monitoring tools.

## How COM+ Tracking Collects Data

When a COM+ server application process is started, COM+ registers the process with the *tracker server*, a component of the system application. Components in COM+ library applications and services without components (SWC) contexts also support tracking. When a library component or SWC context is created in a process, COM+ registers the process with the tracker server if it has not been registered already.

COM+ updates statistics for a tracked process when certain events occur in the process, such as the creation of an object or the completion of a method call. Updated data is periodically submitted to the tracker server, at which point it becomes available to consumers. The tracker server is also responsible for calculating some of the metrics used by the COM+ application recycling and hang monitoring features. This data is also available to consumers.

Tracking data is organized according to the process that generated the data. Data at the level of individual COM+ applications or components in the process is also available for consumers that need this information.

## Events versus Polling

COM+ tracking supports two mechanisms for a consumer to obtain tracking data from the tracker server, a COM+ events-based subscription mechanism and a COM local server interface.

Programs that need to be notified periodically with updated tracking data can register a subscription for the [**IComTrackingInfoEvents**](/windows/desktop/api/ComSvcs/nn-comsvcs-icomtrackinginfoevents) event interface. Roughly every three seconds, the tracker server calls each subscriber's [**IComTrackingInfoEvents::OnNewTrackingInfo**](/windows/desktop/api/ComSvcs/nf-comsvcs-icomtrackinginfoevents-onnewtrackinginfo) method, sending the most recent tracking data in the form of a collection object. This object implements the [**IComTrackingInfoCollection**](/windows/desktop/api/ComSvcs/nn-comsvcs-icomtrackinginfocollection) interface, and subscribers can navigate this collection to find the data they are interested in.

For various reasons, it might make more sense for a program to poll tracker server for data. For example, a monitoring tool may need updates much less frequently than a program that displays status in a user interface. Also, a program may use only a small portion of the tracking data available for the system (for example, a tool might only monitor the performance of instances of a single COM+ application). The subscription model sends each subscriber the tracking data for all COM+ applications in each notification, and it is the responsibility of the subscriber to find the data it wants. Finally, COM+ events is a best-effort event notification mechanism. Reliable message delivery services are not provided, and there is no way for a subscriber to detect that the tracker server failed to send it a notification.

A program that needs greater control over its retrieval of tracking data can use the [**IGetAppTrackerData**](/windows/desktop/api/ComSvcs/nn-comsvcs-igetapptrackerdata) interface of the tracker server.

 

 




