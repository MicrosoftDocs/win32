---
Description: Plug-ins for the RealTimeStylus class must implement the IStylusSyncPlugin or IStylusAsyncPlugin interface, or both.
ms.assetid: 827ac817-e0e6-4750-9d48-b939ccd5e679
title: Plug-in Data and the RealTimeStylus Class
ms.topic: article
ms.date: 05/31/2018
---

# Plug-in Data and the RealTimeStylus Class

Plug-ins for the [**RealTimeStylus**](realtimestylus-class.md) class must implement the [**IStylusSyncPlugin**](https://msdn.microsoft.com/en-us/library/ms704312(v=VS.85).aspx) or [**IStylusAsyncPlugin**](https://msdn.microsoft.com/en-us/library/ms702522(v=VS.85).aspx) interface, or both. While you have to implement all of the plug-in interface methods, your plug-in only receives calls on methods flagged in the plug-ins [Microsoft.StylusInput.IStylusSyncPlugin.DataInterest](https://msdn.microsoft.com/library/ms574887(v=VS.100).aspx) or [Microsoft.StylusInput.IStylusAsyncPlugin.DataInterest](https://msdn.microsoft.com/library/ms574886(v=VS.100).aspx) property.

The methods defined on the interfaces use objects in the [Microsoft.StylusInput.PluginData](https://msdn.microsoft.com/library/ms823992(v=MSDN.10).aspx) namespace to pass the pen data to the plug-ins. The following table describes the data objects that are parameters in the notification methods and lists the [DataInterestMask](https://msdn.microsoft.com/library/ms824787(v=MSDN.10).aspx) value associated with the notification.



| Plug-in Data                                                                                          | DataInterestMask Value     | Description                                                                                                                                                                                                                                             |
|-------------------------------------------------------------------------------------------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CustomStylusData](https://msdn.microsoft.com/library/ms824747(v=MSDN.10).aspx)                     | **CustomStylusDataAdded**  | Custom application data that a plug-in adds.<br/>                                                                                                                                                                                                 |
| [ErrorData](https://msdn.microsoft.com/library/ms824740(v=MSDN.10).aspx)                                   | **Error**                  | Error information that the [**RealTimeStylus**](realtimestylus-class.md) object adds in response to an unhandled exception in one of its plug-ins.<br/>                                                                                          |
| [InAirPacketsData](https://msdn.microsoft.com/library/ms824592(v=MSDN.10).aspx)                     | **InAirPackets**           | Packet information for stylus motion while the stylus is in-air above the digitizer.<br/>                                                                                                                                                         |
| [PacketsData](https://msdn.microsoft.com/library/ms824590(v=MSDN.10).aspx)                               | **Packets**                | Packet information for stylus motion while the stylus is touching the digitizer.<br/>                                                                                                                                                             |
| [RealTimeStylusDisabledData](https://msdn.microsoft.com/library/ms824576(v=MSDN.10).aspx) | **RealTimeStylusDisabled** | Information the [**RealTimeStylus**](realtimestylus-class.md) object adds when it is being disabled.<br/>                                                                                                                                        |
| [RealTimeStylusEnabledData](https://msdn.microsoft.com/library/ms824229(v=MSDN.10).aspx)   | **RealTimeStylusEnabled**  | Information the [**RealTimeStylus**](realtimestylus-class.md) object adds when it is being enabled.<br/>                                                                                                                                         |
| [StylusButtonDownData](https://msdn.microsoft.com/library/ms824181(v=MSDN.10).aspx)             | **StylusButtonDown**       | Information about the particular stylus button that is being pressed.<br/>                                                                                                                                                                        |
| [StylusButtonUpData](https://msdn.microsoft.com/library/ms824172(v=MSDN.10).aspx)                 | **StylusButtonUp**         | Information about the particular stylus button that is being released.<br/>                                                                                                                                                                       |
| [StylusDownData](https://msdn.microsoft.com/library/ms585582(v=VS.90).aspx)                                   | **StylusDown**             | Packet information for a stylus as the stylus is brought in contact with the digitizer.<br/>                                                                                                                                                      |
| [StylusInRangeData](https://msdn.microsoft.com/library/ms824090(v=MSDN.10).aspx)                   | **StylusInRange**          | Information about the particular stylus that is entering the input area of the [**RealTimeStylus**](realtimestylus-class.md) object or entering the detection range of the digitizer above the input area of the **RealTimeStylus** object.<br/> |
| [StylusOutOfRangeData](https://msdn.microsoft.com/library/ms824072(v=MSDN.10).aspx)             | **StylusOutOfRange**       | Information about the particular stylus that is leaving the input area of the [**RealTimeStylus**](realtimestylus-class.md) object or leaving the detection range of the digitizer above the input area of the **RealTimeStylus** object.<br/>   |
| [StylusUpData](https://msdn.microsoft.com/library/ms824057(v=MSDN.10).aspx)                             | **StylusUp**               | Packet information for a stylus as the stylus is lifted from the digitizer.<br/>                                                                                                                                                                  |
| [SystemGestureData](https://msdn.microsoft.com/library/ms824019(v=MSDN.10).aspx)                   | **SystemGesture**          | Information the [**RealTimeStylus**](realtimestylus-class.md) object adds when it detects a system gesture.<br/>                                                                                                                                 |
| [TabletAddedData](https://msdn.microsoft.com/library/ms824010(v=MSDN.10).aspx)                       | **TabletAdded**            | Information about the [Tablet](https://msdn.microsoft.com/library/ms827783(v=MSDN.10).aspx) object that is being added.<br/>                                                                                                                                                |
| [TabletRemovedData](https://msdn.microsoft.com/library/ms823997(v=MSDN.10).aspx)                   | **TabletRemoved**          | Information about the [Tablet](https://msdn.microsoft.com/library/ms827783(v=MSDN.10).aspx) object that is being removed.<br/>                                                                                                                                              |



 

For information about how the [**RealTimeStylus**](realtimestylus-class.md) object handles the tablet pen data stream, see [Working with the RealTimeStylus Class](working-with-the-realtimestylus-class.md).

## Data Interest

The [**RealTimeStylus**](realtimestylus-class.md) object checks the [Microsoft.StylusInput.IStylusSyncPlugin.DataInterest](https://msdn.microsoft.com/library/ms574887(v=VS.100).aspx) or [Microsoft.StylusInput.IStylusAsyncPlugin.DataInterest](https://msdn.microsoft.com/library/ms574886(v=VS.100).aspx) property of a plug-in when the plug-in is added to the **RealTimeStylus** object's synchronous or asynchronous plug-in collection. Therefore, you should use the DataInterest property to subscribe to all of the notifications this instance of your plug-in uses, however infrequently, but not to any of the notifications this instance of your plug-in never uses. For notifications that your plug-in only uses occasionally check the state of your plug-in in the notification method first and return if the notification is not used by your plug-in in its current state.

A plug-in only receives calls on methods flagged in the plug-in's [Microsoft.StylusInput.IStylusSyncPlugin.DataInterest](https://msdn.microsoft.com/library/ms574887(v=VS.100).aspx) or [Microsoft.StylusInput.IStylusAsyncPlugin.DataInterest](https://msdn.microsoft.com/library/ms574886(v=VS.100).aspx) property. For more information about the possible values of a plug-in's **DataInterest** property, see the [DataInterestMask](https://msdn.microsoft.com/library/ms824787(v=MSDN.10).aspx) enumeration.

## Timing

Data is queued in the [**RealTimeStylus**](realtimestylus-class.md) object before it is passed to the plug-ins in the asynchronous plug-in collection. The following list describes some situations that you may need to account for when designing an asynchronous plug-in.

-   When the [**RealTimeStylus**](realtimestylus-class.md) object is disabled, the asynchronous plug-in may receive other queued notifications before its [RealTimeStylusDisabled](https://msdn.microsoft.com/library/ms824774(v=MSDN.10).aspx) method is called. In this situation, calls from the plug-in to some of the **RealTimeStylus** object's methods and properties throw an exception. Information relevant to your plug-in should be cached when the **RealTimeStylus** object is enabled.
-   The [**RealTimeStylus**](realtimestylus-class.md) object's [ClearStylusQueues](https://msdn.microsoft.com/library/ms825781(v=MSDN.10).aspx) method may remove information from the output queue. Therefore, asynchronous plug-ins cannot rely on receiving all relevant notifications.
-   When a [Tablet](https://msdn.microsoft.com/library/ms827783(v=MSDN.10).aspx) object that is available to the [**RealTimeStylus**](realtimestylus-class.md) object is removed, the asynchronous plug-in may receive queued stylus notification for the tablet before its [TabletRemoved](https://msdn.microsoft.com/library/Bb361092(v=VS.90).aspx) method is called. In this situation, calling the **RealTimeStylus** object's [GetTabletPropertyDescriptionCollection](https://msdn.microsoft.com/library/ms825935(v=MSDN.10).aspx) method does not work. Information relevant to your plug-in should be cached when the **RealTimeStylus** object is enabled or when a new tablet is added.

Depending on your application, you can improve performance when disabling a [**RealTimeStylus**](realtimestylus-class.md) object. When the **RealTimeStylus** object's [Enabled](https://msdn.microsoft.com/library/ms824832(v=MSDN.10).aspx) property is set to **FALSE**, data on the input and output queues are processed until the queues are empty. You can call the **RealTimeStylus** object's [ClearStylusQueues](https://msdn.microsoft.com/library/ms825781(v=MSDN.10).aspx) method to clear the queues before disabling the **RealTimeStylus** object.

## Enabled and Disabled Data

When the [**RealTimeStylus**](realtimestylus-class.md) object is enabled, each plug-in receives a call to its [Microsoft.StylusInput.IStylusSyncPlugin.RealTimeStylusEnabled](https://msdn.microsoft.com/library/ms824758(v=MSDN.10).aspx) or [Microsoft.StylusInput.IStylusAsyncPlugin.RealTimeStylusEnabled](https://msdn.microsoft.com/library/ms824775(v=MSDN.10).aspx) method. The **RealTimeStylusEnabledData** object passed in the notification contains a collection of the context identifiers for the available tablets at the time the **RealTimeStylus** object is enabled.

> [!Note]  
> Because the plug-in data for the [**RealTimeStylus**](realtimestylus-class.md) object's asynchronous plug-in collection is queued, asynchronous plug-ins may receive data prior to receiving a call to its [RealTimeStylusDisabled](https://msdn.microsoft.com/library/ms824774(v=MSDN.10).aspx) method but after the **RealTimeStylus** object is disabled. Note that some of the **RealTimeStylus** object's methods and properties throw an exception if the **RealTimeStylus** object is disabled.

 

The [**RealTimeStylus**](realtimestylus-class.md) object calls the [Microsoft.StylusInput.IStylusSyncPlugin.RealTimeStylusEnabled](https://msdn.microsoft.com/library/ms824758(v=MSDN.10).aspx) and [Microsoft.StylusInput.IStylusSyncPlugin.RealTimeStylusDisabled](https://msdn.microsoft.com/library/ms824757(v=MSDN.10).aspx) methods on the thread from which the **RealTimeStylus** object is enabled or from which the synchronous plug-in is added.

Generally, add or remove plug-ins while the [**RealTimeStylus**](realtimestylus-class.md) object is disabled. For more information about adding and removing plug-ins to the **RealTimeStylus** object, see [Plug-ins and the RealTimeStylus Class](plug-ins-and-the-realtimestylus-class.md).

## Tablet Data

When a tablet that the [**RealTimeStylus**](realtimestylus-class.md) object can use is added to or removed from the Tablet PC while the **RealTimeStylus** object is enabled, the **RealTimeStylus** object notifies its plug-ins that a [Tablet](https://msdn.microsoft.com/library/ms827783(v=MSDN.10).aspx) object has been added or removed. Each **RealTimeStylus** object maintains a list of unique identifiers for the Tablet objects it can interact with. The **RealTimeStylus** object has two methods for translating between the unique identifier and the Tablet object, the [GetTabletContextIdFromTablet](https://msdn.microsoft.com/library/ms825922(v=MSDN.10).aspx) and [GetTabletFromTabletContextId](https://msdn.microsoft.com/library/ms825929(v=MSDN.10).aspx) methods.

> [!Note]  
> Information about a tablet is no longer available from the [**RealTimeStylus**](realtimestylus-class.md) object after the tablet is removed from the Tablet PC.

 

## Tablet Pen Data

The [**RealTimeStylus**](realtimestylus-class.md) object passes information about the tablet pen to its plug-ins in a number of the notification methods. Information about the tablet pen is represented by a [Stylus](https://msdn.microsoft.com/library/ms824824(v=MSDN.10).aspx) object. This object is a snapshot of the state of the tablet pen at the time the data was gathered. Because plug-ins receive the tablet pen data as part of the tablet pen data stream, the plug-ins should use the information in the Stylus object instead of checking for the current state of a particular tablet pen through the [Cursor](https://msdn.microsoft.com/library/ms839521(v=MSDN.10).aspx) class.

Each [Stylus](https://msdn.microsoft.com/library/ms824824(v=MSDN.10).aspx) object contains the tablet context identifier for the tablet that generated the data.

## System Gesture Data

The [**RealTimeStylus**](realtimestylus-class.md) object receives data about system gestures as they are recognized by the Tablet PC. The following table describes the order in which the [SystemGestureData](https://msdn.microsoft.com/library/ms824019(v=MSDN.10).aspx) objects occur in the tablet pen data stream in relation to other tablet pen data.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><a href="/previous-versions/ms827134(v=msdn.10)">SystemGesture</a></th>
<th>Objects that precede the <a href="/previous-versions/ms824019(v=msdn.10)">SystemGestureData</a> object</th>
<th>Objects that come after the <a href="/previous-versions/ms824019(v=msdn.10)">SystemGestureData</a> object</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Tap</strong></td>
<td>The <a href="/previous-versions/ms824107(v=msdn.10)">StylusDownData</a> object.<br/></td>
<td>The [StylusUpData](https://msdn.microsoft.com/library/ms824057(v=MSDN.10).aspx) object.<br/></td>
</tr>
<tr class="even">
<td><strong>DoubleTap</strong></td>
<td>The <a href="/previous-versions/ms824107(v=msdn.10)">StylusDownData</a> object, the <a href="/previous-versions/ms824019(v=msdn.10)">SystemGestureData</a> object for the <strong>Tap</strong> system gesture and the [StylusUpData](https://msdn.microsoft.com/library/ms824057(v=MSDN.10).aspx) objects.<br/></td>
<td>The second <a href="/previous-versions/ms824107(v=msdn.10)">StylusDownData</a> object.<br/></td>
</tr>
<tr class="odd">
<td><strong>RightTap</strong></td>
<td>The <a href="/previous-versions/ms824107(v=msdn.10)">StylusDownData</a> object and the <a href="/previous-versions/ms824019(v=msdn.10)">SystemGestureData</a> object for the <strong>HoldEnter</strong> member of the <a href="/previous-versions/ms827134(v=msdn.10)">SystemGesure</a> enumeration.<br/></td>
<td>The [StylusUpData](https://msdn.microsoft.com/library/ms824057(v=MSDN.10).aspx) object.<br/></td>
</tr>
<tr class="even">
<td><strong>Drag</strong></td>
<td>The <a href="/previous-versions/ms824107(v=msdn.10)">StylusDownData</a> object.<br/></td>
<td>The [StylusUpData](https://msdn.microsoft.com/library/ms824057(v=MSDN.10).aspx) object.<br/></td>
</tr>
<tr class="odd">
<td><strong>RightDrag</strong></td>
<td>The <a href="/previous-versions/ms824107(v=msdn.10)">StylusDownData</a> object.<br/></td>
<td>The [StylusUpData](https://msdn.microsoft.com/library/ms824057(v=MSDN.10).aspx) object.<br/></td>
</tr>
<tr class="even">
<td><strong>HoldEnter</strong></td>
<td>The <a href="/previous-versions/ms824107(v=msdn.10)">StylusDownData</a> object.<br/></td>
<td>The [StylusUpData](https://msdn.microsoft.com/library/ms824057(v=MSDN.10).aspx) object.<br/>
<blockquote>
[!Note]<br />
This system gesture isn't recognized if the user begins a <strong>Drag</strong> or <strong>RightDrag</strong> system gesture.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><strong>HoldLeave</strong></td>
<td>Not implemented.<br/></td>
<td>Not implemented.<br/></td>
</tr>
<tr class="even">
<td><strong>HoverEnter</strong></td>
<td>Several <a href="/previous-versions/ms824592(v=msdn.10)">InAirPacketsData</a> objects of low average velocity.<br/></td>
<td><blockquote>
[!Note]<br />
There may be noticeable delay before receiving the <strong>HoverEnter</strong> system gesture. The <a href="realtimestylus-class"><strong>RealTimeStylus</strong></a> object only receives this data if the <strong>RealTimeStylus</strong> object is attached to the window or control that is directly under the pen at the time of the system gesture.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><strong>HoverLeave</strong></td>
<td>The <a href="/previous-versions/ms824019(v=msdn.10)">SystemGestureData</a> object for the <strong>HoverEnter</strong> system gesture and several <a href="/previous-versions/ms824592(v=msdn.10)">InAirPacketsData</a> objects of sufficient average velocity.<br/></td>
<td><blockquote>
[!Note]<br />
There may be noticeable delay before receiving the <strong>HoverLeave</strong> system gesture. The <a href="realtimestylus-class"><strong>RealTimeStylus</strong></a> object only receives this data if the <strong>RealTimeStylus</strong> object is attached to the window or control that is directly under the pen at the time of the system gesture.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

## Custom Stylus Data

Custom stylus data can be added to the [**RealTimeStylus**](realtimestylus-class.md) object by calling the [AddCustomStylusDataToQueue](https://msdn.microsoft.com/library/ms825761(v=MSDN.10).aspx) method. Custom stylus data can be added to the **RealTimeStylus** object's queues in one of three places.

-   When the *queue* parameter is set to **Output**, the custom data is added to the [**RealTimeStylus**](realtimestylus-class.md) object's output queue after the data currently being processed by the synchronous plug-in collection.
-   When the *queue* parameter is set to **OutputImmediate**, the custom data is added to the [**RealTimeStylus**](realtimestylus-class.md) object's output queue before the data currently being processed by the synchronous plug-in collection.
-   When the *queue* parameter is set to **Input**, the custom data is added to the [**RealTimeStylus**](realtimestylus-class.md) object's input queue and is sent to the synchronous plug-in collection before new data from the tablet pen's data stream.

In each of the previous cases, data added by subsequent plug-ins in the synchronous plug-in collection is added after data added by preceding plug-ins.

> [!Note]  
> If the call to the [AddCustomStylusDataToQueue](https://msdn.microsoft.com/library/ms825761(v=MSDN.10).aspx) method is made from a synchronous plug-in in response to a call to one of its [**IStylusSyncPlugin**](https://msdn.microsoft.com/en-us/library/ms704312(v=VS.85).aspx) methods, then the custom stylus data is added to the tablet pen data stream in a predictable manner; otherwise, it is added to the queue in relation to the current pen data the [**RealTimeStylus**](realtimestylus-class.md) object is processing, and not in relation to the data that the asynchronous plug-in is processing. The AddCustomStylusDataToQueue method throws an exception if the **RealTimeStylus** object is disabled.

 

Custom stylus data is added to the queue as a [CustomStylusData](https://msdn.microsoft.com/library/ms824747(v=MSDN.10).aspx) object and plug-ins receive this data through their [Microsoft.StylusInput.IStylusSyncPlugin.CustomStylusDataAdded](https://msdn.microsoft.com/library/ms824753(v=MSDN.10).aspx) or [Microsoft.StylusInput.IStylusAsyncPlugin.CustomStylusDataAdded](https://msdn.microsoft.com/library/ms824770(v=MSDN.10).aspx) method.

The [**DynamicRenderer**](https://msdn.microsoft.com/en-us/library/ms701168(v=VS.85).aspx) and the [**GestureRecognizer**](gesturerecognizer-class.md) objects may add custom stylus data to the queue. For more information about the **DynamicRenderer** and the **GestureRecognizer** objects see [Dynamic-Renderer Plug-ins](dynamic-renderer-plug-ins.md) and [Recognizer Plug-ins](recognizer-plug-ins.md).

The [**RealTimeStylus**](realtimestylus-class.md) object calls the [Microsoft.StylusInput.IStylusSyncPlugin.CustomStylusDataAdded](https://msdn.microsoft.com/library/ms824753(v=MSDN.10).aspx) method on the thread from which it receives the call to its [AddCustomStylusDataToQueue](https://msdn.microsoft.com/library/ms825761(v=MSDN.10).aspx) method.

The following diagram illustrates the addition of custom stylus data to the output queue with the *queue* parameter set to **Output**.

![illustration showing custom stylus data flow to the output queue ](images/27bc3672-41bc-432e-bf41-18e4ccec78f5.gif)

In this diagram, the circles lettered "A" and "B" represent tablet pen data that has already been added to the [**RealTimeStylus**](realtimestylus-class.md) object's output queue and that has not yet been sent to the asynchronous plug-in collection. The circle lettered "C" represents the tablet pen data that the **RealTimeStylus** object is currently processing. It is sent to the synchronous plug-in collection and placed on the output queue. The circles numbered "1", "2", and "3" represent custom stylus data that has been added to the output queue by the first, second, and third synchronous plug-ins respectively in response to the tablet pen data represented by "C". The plug-ins have added the custom stylus data with the *queue* parameter set to **StylusQueues**. The empty circle represents the position in the output queue where future tablet pen data is added.

The following diagram illustrates the addition of custom stylus data to the output queue with the *queue* parameter set to **OutputImmediate**.

![illustration showing custom stylus data flow to the output queue](images/bcf45325-5557-47a2-af43-142c7684e482.gif)

In this diagram, the circles lettered "A" and "B" represent tablet pen data that has already been added to the [**RealTimeStylus**](realtimestylus-class.md) object's output queue and that has not yet been sent to the asynchronous plug-in collection. The circle lettered "C" represents the tablet pen data that the **RealTimeStylus** object is currently processing. It is sent to the synchronous plug-in collection and placed on the output queue. The circles numbered "1", "2", and "3" represent custom stylus data that has been added to the output queue by the first, second, and third synchronous plug-ins respectively in response to the tablet pen data represented by "C". The plug-ins have added the custom stylus data with the *queue* parameter set to **OutputImmediate**. The empty circle represents the position in the output queue where future tablet pen data is added.

The following diagram illustrates the addition of custom stylus data to the input queue.

![illustration showing custom stylus data flow to the output queue](images/5dd2cfcc-1086-49b0-a0d5-9276c13c7f61.gif)

In this diagram, the circles lettered "A" and "B" represent tablet pen data that has already been added to the [**RealTimeStylus**](realtimestylus-class.md) object's output queue and that has not yet been sent to the asynchronous plug-in collection. The circle lettered "C" represents the tablet pen data that the **RealTimeStylus** object is currently processing. It is sent to the synchronous plug-in collection and placed on the output queue. The circles numbered "1", "2", and "3" represent custom stylus data that has been added to the input queue by the first, second, and third synchronous plug-ins respectively in response to the tablet pen data represented by "C". The plug-ins have added the custom stylus data with the *queue* parameter set to **Input**. The custom stylus data numbered "1" is then passed to the synchronous plug-ins and then to the output queue before the custom stylus data numbered "2" and "3", both of which are processed before the next tablet pen data is processed. The empty circle represents the position in the output queue where future tablet pen data is added.

## Error Data

When a plug-in throws an exception, the normal flow of data is interrupted. The [**RealTimeStylus**](realtimestylus-class.md) object generates an [ErrorData](https://msdn.microsoft.com/library/ms824740(v=MSDN.10).aspx) object and calls:

-   The [Microsoft.StylusInput.IStylusSyncPlugin.Error](https://msdn.microsoft.com/library/ms824754(v=MSDN.10).aspx) or [Microsoft.StylusInput.IStylusAsyncPlugin.Error](https://msdn.microsoft.com/library/ms824771(v=MSDN.10).aspx) method of the plug-in that threw the exception.
-   The [Microsoft.StylusInput.IStylusSyncPlugin.Error](https://msdn.microsoft.com/library/ms824754(v=MSDN.10).aspx) or [Microsoft.StylusInput.IStylusAsyncPlugin.Error](https://msdn.microsoft.com/library/ms824771(v=MSDN.10).aspx) method of the remaining plug-ins in that collection.

If the plug-in that threw the exception is a synchronous plug-in, the [ErrorData](https://msdn.microsoft.com/library/ms824740(v=MSDN.10).aspx) object is added to the output queue. Then the [**RealTimeStylus**](realtimestylus-class.md) object resumes normal processing of the original data.

The following diagram illustrates the addition of error data to the tablet pen data.

![custom stylus data flow to the output queue with the addition of error data](images/c2f79abe-aeb5-498f-b389-1fad9bf01a13.gif)

In this diagram, the circles lettered "A" and "B" represent tablet pen data that has already been added to the [**RealTimeStylus**](realtimestylus-class.md) object's output queue and that has not yet been sent to the asynchronous plug-in collection. The circle lettered "C" represents the tablet pen data that the **RealTimeStylus** object is currently processing. The circle lettered "e" represents a [ErrorData](https://msdn.microsoft.com/library/ms824740(v=MSDN.10).aspx) object generated by the **RealTimeStylus** object when the second synchronous plug-in, Synchronous Plug-in 2, throws an exception while it is processing "C". The **RealTimeStylus** object then pauses its processing of "C" and passes "e" to the plug-in that generated the exception and all subsequent plug-ins. The **RealTimeStylus** object then puts "e" on the output queue and resumes its processing of "C", which is passed to the remaining plug-ins in the synchronous plug-in collection and placed on the output queue after "e". The empty circle represents the position in the output queue where future tablet pen data is added.

If a plug-in throws an exception from its Error method, the [**RealTimeStylus**](realtimestylus-class.md) object catches the exception but does not generate a new [ErrorData](https://msdn.microsoft.com/library/ms824740(v=MSDN.10).aspx) object. This is to prevent recursion.

The error data is added to the output queue after any custom stylus data that is added at the **OutputImmediate** position prior to the exception that created the error data and before any custom stylus data that is added at the **OutputImmediate** position by subsequent plug-ins in the synchronous plug-in collection.

The following diagram illustrates how the error data is added to the output queue in relation to custom data that is added to the **OutputImmediate** queue.

![error data added to the output queue in relation to custom data added to the outputimmediate queue.](images/b00320c4-6fe7-439d-9855-e5f131feeb69.gif)

In this diagram, the circles lettered "A" and "B" represent tablet pen data that has already been added to the [**RealTimeStylus**](realtimestylus-class.md) object's output queue and that has not yet been sent to the asynchronous plug-in collection. The circle lettered "C" represents the tablet pen data that the **RealTimeStylus** object is currently processing. The circles numbered "1", "2", and "3" are added by the first, second, and third synchronous plug-ins respectively to the **OutputImmediate** queue in response to the data represented by the circle lettered "C". The circle lettered "e" represents error data generated in response to an exception thrown by the second plug-in after the second plug-in added custom data to the output queue at the **OutputImmediate** position.

If any synchronous plug-in adds custom stylus data to the input queue in response to the error data, the data is added immediately before the error data. If any of the synchronous plug-ins adds custom stylus data to the output queue at the **Output** position in response to the error data, the data is added immediately after the error data.

The [**RealTimeStylus**](realtimestylus-class.md) object calls the [Microsoft.StylusInput.IStylusSyncPlugin.Error](https://msdn.microsoft.com/library/ms824754(v=MSDN.10).aspx) method on the thread from which the exception is thrown.

## Related topics

<dl> <dt>

[Microsoft.Ink.Tablet](https://msdn.microsoft.com/library/ms827783(v=MSDN.10).aspx)
</dt> <dt>

[Microsoft.StylusInput.PluginData](https://msdn.microsoft.com/library/ms823992(v=MSDN.10).aspx)
</dt> <dt>

[Microsoft.StylusInput.DataInterestMask](https://msdn.microsoft.com/library/ms575174(v=VS.100).aspx)
</dt> <dt>

[Microsoft.StylusInput.RealTimeStylus](https://msdn.microsoft.com/library/ms824830(v=MSDN.10).aspx)
</dt> <dt>

[Working with the RealTimeStylus Class](working-with-the-realtimestylus-class.md)
</dt> </dl>

 

 




