---
Description: Plug-ins for the RealTimeStylus class must implement the IStylusSyncPlugin or IStylusAsyncPlugin interface, or both.
ms.assetid: 827ac817-e0e6-4750-9d48-b939ccd5e679
title: Plug-in Data and the RealTimeStylus Class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Plug-in Data and the RealTimeStylus Class

Plug-ins for the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) class must implement the [**IStylusSyncPlugin**](/windows/win32/RTSCom/?branch=master) or [**IStylusAsyncPlugin**](/windows/win32/RTSCom/?branch=master) interface, or both. While you have to implement all of the plug-in interface methods, your plug-in only receives calls on methods flagged in the plug-ins [Microsoft.StylusInput.IStylusSyncPlugin.DataInterest](frlrfMicrosoftStylusInputIStylusSyncPluginClassDataInterestTopic) or [Microsoft.StylusInput.IStylusAsyncPlugin.DataInterest](frlrfMicrosoftStylusInputIStylusAsyncPluginClassDataInterestTopic) property.

The methods defined on the interfaces use objects in the [Microsoft.StylusInput.PluginData](frlrfMicrosoftStylusInputPluginData) namespace to pass the pen data to the plug-ins. The following table describes the data objects that are parameters in the notification methods and lists the [DataInterestMask](frlrfMicrosoftStylusInputDataInterestMaskClassTopic) value associated with the notification.



| Plug-in Data                                                                                          | DataInterestMask Value     | Description                                                                                                                                                                                                                                             |
|-------------------------------------------------------------------------------------------------------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CustomStylusData](frlrfMicrosoftStylusInputPluginDataCustomStylusDataClassTopic)                     | **CustomStylusDataAdded**  | Custom application data that a plug-in adds.<br/>                                                                                                                                                                                                 |
| [ErrorData](frlrfMicrosoftStylusInputPluginDataErrorDataClassTopic)                                   | **Error**                  | Error information that the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object adds in response to an unhandled exception in one of its plug-ins.<br/>                                                                                          |
| [InAirPacketsData](frlrfMicrosoftStylusInputPluginDataInAirPacketsDataClassTopic)                     | **InAirPackets**           | Packet information for stylus motion while the stylus is in-air above the digitizer.<br/>                                                                                                                                                         |
| [PacketsData](frlrfMicrosoftStylusInputPluginDataPacketsDataClassTopic)                               | **Packets**                | Packet information for stylus motion while the stylus is touching the digitizer.<br/>                                                                                                                                                             |
| [RealTimeStylusDisabledData](frlrfMicrosoftStylusInputPluginDataRealTimeStylusDisabledDataClassTopic) | **RealTimeStylusDisabled** | Information the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object adds when it is being disabled.<br/>                                                                                                                                        |
| [RealTimeStylusEnabledData](frlrfMicrosoftStylusInputPluginDataRealTimeStylusEnabledDataClassTopic)   | **RealTimeStylusEnabled**  | Information the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object adds when it is being enabled.<br/>                                                                                                                                         |
| [StylusButtonDownData](frlrfMicrosoftStylusInputPluginDataStylusButtonDownDataClassTopic)             | **StylusButtonDown**       | Information about the particular stylus button that is being pressed.<br/>                                                                                                                                                                        |
| [StylusButtonUpData](frlrfMicrosoftStylusInputPluginDataStylusButtonUpDataClassTopic)                 | **StylusButtonUp**         | Information about the particular stylus button that is being released.<br/>                                                                                                                                                                       |
| [StylusDownData](T:Microsoft.StylusInput.PluginData.StylusDownData)                                   | **StylusDown**             | Packet information for a stylus as the stylus is brought in contact with the digitizer.<br/>                                                                                                                                                      |
| [StylusInRangeData](frlrfMicrosoftStylusInputPluginDataStylusInRangeDataClassTopic)                   | **StylusInRange**          | Information about the particular stylus that is entering the input area of the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object or entering the detection range of the digitizer above the input area of the **RealTimeStylus** object.<br/> |
| [StylusOutOfRangeData](frlrfMicrosoftStylusInputPluginDataStylusOutOfRangeDataClassTopic)             | **StylusOutOfRange**       | Information about the particular stylus that is leaving the input area of the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object or leaving the detection range of the digitizer above the input area of the **RealTimeStylus** object.<br/>   |
| [StylusUpData](frlrfMicrosoftStylusInputPluginDataStylusUpDataClassTopic)                             | **StylusUp**               | Packet information for a stylus as the stylus is lifted from the digitizer.<br/>                                                                                                                                                                  |
| [SystemGestureData](frlrfMicrosoftStylusInputPluginDataSystemGestureDataClassTopic)                   | **SystemGesture**          | Information the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object adds when it detects a system gesture.<br/>                                                                                                                                 |
| [TabletAddedData](frlrfMicrosoftStylusInputPluginDataTabletAddedDataClassTopic)                       | **TabletAdded**            | Information about the [Tablet](frlrfMicrosoftInkTabletClassTopic) object that is being added.<br/>                                                                                                                                                |
| [TabletRemovedData](frlrfMicrosoftStylusInputPluginDataTabletRemovedDataClassTopic)                   | **TabletRemoved**          | Information about the [Tablet](frlrfMicrosoftInkTabletClassTopic) object that is being removed.<br/>                                                                                                                                              |



 

For information about how the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object handles the tablet pen data stream, see [Working with the RealTimeStylus Class](working-with-the-realtimestylus-class.md).

## Data Interest

The [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object checks the [Microsoft.StylusInput.IStylusSyncPlugin.DataInterest](frlrfMicrosoftStylusInputIStylusSyncPluginClassDataInterestTopic) or [Microsoft.StylusInput.IStylusAsyncPlugin.DataInterest](frlrfMicrosoftStylusInputIStylusAsyncPluginClassDataInterestTopic) property of a plug-in when the plug-in is added to the **RealTimeStylus** object's synchronous or asynchronous plug-in collection. Therefore, you should use the DataInterest property to subscribe to all of the notifications this instance of your plug-in uses, however infrequently, but not to any of the notifications this instance of your plug-in never uses. For notifications that your plug-in only uses occasionally check the state of your plug-in in the notification method first and return if the notification is not used by your plug-in in its current state.

A plug-in only receives calls on methods flagged in the plug-in's [Microsoft.StylusInput.IStylusSyncPlugin.DataInterest](frlrfMicrosoftStylusInputIStylusSyncPluginClassDataInterestTopic) or [Microsoft.StylusInput.IStylusAsyncPlugin.DataInterest](frlrfMicrosoftStylusInputIStylusAsyncPluginClassDataInterestTopic) property. For more information about the possible values of a plug-in's **DataInterest** property, see the [DataInterestMask](frlrfMicrosoftStylusInputDataInterestMaskClassTopic) enumeration.

## Timing

Data is queued in the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object before it is passed to the plug-ins in the asynchronous plug-in collection. The following list describes some situations that you may need to account for when designing an asynchronous plug-in.

-   When the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object is disabled, the asynchronous plug-in may receive other queued notifications before its [RealTimeStylusDisabled](frlrfMicrosoftStylusInputIStylusAsyncPluginClassRealTimeStylusDisabledTopic) method is called. In this situation, calls from the plug-in to some of the **RealTimeStylus** object's methods and properties throw an exception. Information relevant to your plug-in should be cached when the **RealTimeStylus** object is enabled.
-   The [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object's [ClearStylusQueues](frlrfMicrosoftStylusInputRealTimeStylusClassClearStylusQueuesTopic) method may remove information from the output queue. Therefore, asynchronous plug-ins cannot rely on receiving all relevant notifications.
-   When a [Tablet](frlrfMicrosoftInkTabletClassTopic) object that is available to the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object is removed, the asynchronous plug-in may receive queued stylus notification for the tablet before its [TabletRemoved](frlrfMicrosoftStylusInputRealTimeStylusClassTabletRemovedTopic) method is called. In this situation, calling the **RealTimeStylus** object's [GetTabletPropertyDescriptionCollection](frlrfMicrosoftStylusInputRealTimeStylusClassGetTabletPropertyDescriptionCollectionTopic) method does not work. Information relevant to your plug-in should be cached when the **RealTimeStylus** object is enabled or when a new tablet is added.

Depending on your application, you can improve performance when disabling a [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object. When the **RealTimeStylus** object's [Enabled](frlrfMicrosoftStylusInputRealTimeStylusClassEnabledTopic) property is set to **FALSE**, data on the input and output queues are processed until the queues are empty. You can call the **RealTimeStylus** object's [ClearStylusQueues](frlrfMicrosoftStylusInputRealTimeStylusClassClearStylusQueuesTopic) method to clear the queues before disabling the **RealTimeStylus** object.

## Enabled and Disabled Data

When the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object is enabled, each plug-in receives a call to its [Microsoft.StylusInput.IStylusSyncPlugin.RealTimeStylusEnabled](frlrfMicrosoftStylusInputIStylusSyncPluginClassRealTimeStylusEnabledTopic) or [Microsoft.StylusInput.IStylusAsyncPlugin.RealTimeStylusEnabled](frlrfMicrosoftStylusInputIStylusAsyncPluginClassRealTimeStylusEnabledTopic) method. The **RealTimeStylusEnabledData** object passed in the notification contains a collection of the context identifiers for the available tablets at the time the **RealTimeStylus** object is enabled.

> [!Note]  
> Because the plug-in data for the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object's asynchronous plug-in collection is queued, asynchronous plug-ins may receive data prior to receiving a call to its [RealTimeStylusDisabled](frlrfMicrosoftStylusInputIStylusAsyncPluginClassRealTimeStylusDisabledTopic) method but after the **RealTimeStylus** object is disabled. Note that some of the **RealTimeStylus** object's methods and properties throw an exception if the **RealTimeStylus** object is disabled.

 

The [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object calls the [Microsoft.StylusInput.IStylusSyncPlugin.RealTimeStylusEnabled](frlrfMicrosoftStylusInputIStylusSyncPluginClassRealTimeStylusEnabledTopic) and [Microsoft.StylusInput.IStylusSyncPlugin.RealTimeStylusDisabled](frlrfMicrosoftStylusInputIStylusSyncPluginClassRealTimeStylusDisabledTopic) methods on the thread from which the **RealTimeStylus** object is enabled or from which the synchronous plug-in is added.

Generally, add or remove plug-ins while the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object is disabled. For more information about adding and removing plug-ins to the **RealTimeStylus** object, see [Plug-ins and the RealTimeStylus Class](plug-ins-and-the-realtimestylus-class.md).

## Tablet Data

When a tablet that the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object can use is added to or removed from the Tablet PC while the **RealTimeStylus** object is enabled, the **RealTimeStylus** object notifies its plug-ins that a [Tablet](frlrfMicrosoftInkTabletClassTopic) object has been added or removed. Each **RealTimeStylus** object maintains a list of unique identifiers for the Tablet objects it can interact with. The **RealTimeStylus** object has two methods for translating between the unique identifier and the Tablet object, the [GetTabletContextIdFromTablet](frlrfMicrosoftStylusInputRealTimeStylusClassGetTabletContextIdFromTabletTopic) and [GetTabletFromTabletContextId](frlrfMicrosoftStylusInputRealTimeStylusClassGetTabletFromTabletContextIdTopic) methods.

> [!Note]  
> Information about a tablet is no longer available from the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object after the tablet is removed from the Tablet PC.

 

## Tablet Pen Data

The [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object passes information about the tablet pen to its plug-ins in a number of the notification methods. Information about the tablet pen is represented by a [Stylus](frlrfMicrosoftStylusInputStylusClassTopic) object. This object is a snapshot of the state of the tablet pen at the time the data was gathered. Because plug-ins receive the tablet pen data as part of the tablet pen data stream, the plug-ins should use the information in the Stylus object instead of checking for the current state of a particular tablet pen through the [Cursor](frlrfMicrosoftInkCursorClassTopic) class.

Each [Stylus](frlrfMicrosoftStylusInputStylusClassTopic) object contains the tablet context identifier for the tablet that generated the data.

## System Gesture Data

The [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object receives data about system gestures as they are recognized by the Tablet PC. The following table describes the order in which the [SystemGestureData](frlrfMicrosoftStylusInputPluginDataSystemGestureDataClassTopic) objects occur in the tablet pen data stream in relation to other tablet pen data.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>[SystemGesture](frlrfMicrosoftInkSystemGestureClassTopic)</th>
<th>Objects that precede the [SystemGestureData](frlrfMicrosoftStylusInputPluginDataSystemGestureDataClassTopic) object</th>
<th>Objects that come after the [SystemGestureData](frlrfMicrosoftStylusInputPluginDataSystemGestureDataClassTopic) object</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Tap</strong></td>
<td>The [StylusDownData](frlrfMicrosoftStylusInputPluginDataStylusDownDataClassTopic) object.<br/></td>
<td>The [StylusUpData](frlrfMicrosoftStylusInputPluginDataStylusUpDataClassTopic) object.<br/></td>
</tr>
<tr class="even">
<td><strong>DoubleTap</strong></td>
<td>The [StylusDownData](frlrfMicrosoftStylusInputPluginDataStylusDownDataClassTopic) object, the [SystemGestureData](frlrfMicrosoftStylusInputPluginDataSystemGestureDataClassTopic) object for the <strong>Tap</strong> system gesture and the [StylusUpData](frlrfMicrosoftStylusInputPluginDataStylusUpDataClassTopic) objects.<br/></td>
<td>The second [StylusDownData](frlrfMicrosoftStylusInputPluginDataStylusDownDataClassTopic) object.<br/></td>
</tr>
<tr class="odd">
<td><strong>RightTap</strong></td>
<td>The [StylusDownData](frlrfMicrosoftStylusInputPluginDataStylusDownDataClassTopic) object and the [SystemGestureData](frlrfMicrosoftStylusInputPluginDataSystemGestureDataClassTopic) object for the <strong>HoldEnter</strong> member of the [SystemGesure](frlrfMicrosoftInkSystemGestureClassTopic) enumeration.<br/></td>
<td>The [StylusUpData](frlrfMicrosoftStylusInputPluginDataStylusUpDataClassTopic) object.<br/></td>
</tr>
<tr class="even">
<td><strong>Drag</strong></td>
<td>The [StylusDownData](frlrfMicrosoftStylusInputPluginDataStylusDownDataClassTopic) object.<br/></td>
<td>The [StylusUpData](frlrfMicrosoftStylusInputPluginDataStylusUpDataClassTopic) object.<br/></td>
</tr>
<tr class="odd">
<td><strong>RightDrag</strong></td>
<td>The [StylusDownData](frlrfMicrosoftStylusInputPluginDataStylusDownDataClassTopic) object.<br/></td>
<td>The [StylusUpData](frlrfMicrosoftStylusInputPluginDataStylusUpDataClassTopic) object.<br/></td>
</tr>
<tr class="even">
<td><strong>HoldEnter</strong></td>
<td>The [StylusDownData](frlrfMicrosoftStylusInputPluginDataStylusDownDataClassTopic) object.<br/></td>
<td>The [StylusUpData](frlrfMicrosoftStylusInputPluginDataStylusUpDataClassTopic) object.<br/>
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
<td>Several [InAirPacketsData](frlrfMicrosoftStylusInputPluginDataInAirPacketsDataClassTopic) objects of low average velocity.<br/></td>
<td><blockquote>
[!Note]<br />
There may be noticeable delay before receiving the <strong>HoverEnter</strong> system gesture. The [<strong>RealTimeStylus</strong>](/windows/win32/RTSCom/?branch=master) object only receives this data if the <strong>RealTimeStylus</strong> object is attached to the window or control that is directly under the pen at the time of the system gesture.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><strong>HoverLeave</strong></td>
<td>The [SystemGestureData](frlrfMicrosoftStylusInputPluginDataSystemGestureDataClassTopic) object for the <strong>HoverEnter</strong> system gesture and several [InAirPacketsData](frlrfMicrosoftStylusInputPluginDataInAirPacketsDataClassTopic) objects of sufficient average velocity.<br/></td>
<td><blockquote>
[!Note]<br />
There may be noticeable delay before receiving the <strong>HoverLeave</strong> system gesture. The [<strong>RealTimeStylus</strong>](/windows/win32/RTSCom/?branch=master) object only receives this data if the <strong>RealTimeStylus</strong> object is attached to the window or control that is directly under the pen at the time of the system gesture.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

## Custom Stylus Data

Custom stylus data can be added to the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object by calling the [AddCustomStylusDataToQueue](frlrfMicrosoftStylusInputRealTimeStylusClassAddCustomStylusDataToQueueTopic) method. Custom stylus data can be added to the **RealTimeStylus** object's queues in one of three places.

-   When the *queue* parameter is set to **Output**, the custom data is added to the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object's output queue after the data currently being processed by the synchronous plug-in collection.
-   When the *queue* parameter is set to **OutputImmediate**, the custom data is added to the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object's output queue before the data currently being processed by the synchronous plug-in collection.
-   When the *queue* parameter is set to **Input**, the custom data is added to the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object's input queue and is sent to the synchronous plug-in collection before new data from the tablet pen's data stream.

In each of the previous cases, data added by subsequent plug-ins in the synchronous plug-in collection is added after data added by preceding plug-ins.

> [!Note]  
> If the call to the [AddCustomStylusDataToQueue](frlrfMicrosoftStylusInputRealTimeStylusClassAddCustomStylusDataToQueueTopic) method is made from a synchronous plug-in in response to a call to one of its [**IStylusSyncPlugin**](/windows/win32/RTSCom/?branch=master) methods, then the custom stylus data is added to the tablet pen data stream in a predictable manner; otherwise, it is added to the queue in relation to the current pen data the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object is processing, and not in relation to the data that the asynchronous plug-in is processing. The AddCustomStylusDataToQueue method throws an exception if the **RealTimeStylus** object is disabled.

 

Custom stylus data is added to the queue as a [CustomStylusData](frlrfMicrosoftStylusInputPluginDataCustomStylusDataClassTopic) object and plug-ins receive this data through their [Microsoft.StylusInput.IStylusSyncPlugin.CustomStylusDataAdded](frlrfMicrosoftStylusInputIStylusSyncPluginClassCustomStylusDataAddedTopic) or [Microsoft.StylusInput.IStylusAsyncPlugin.CustomStylusDataAdded](frlrfMicrosoftStylusInputIStylusAsyncPluginClassCustomStylusDataAddedTopic) method.

The [**DynamicRenderer**](/windows/win32/RTSCom/?branch=master) and the [**GestureRecognizer**](/windows/win32/RTSCom/?branch=master) objects may add custom stylus data to the queue. For more information about the **DynamicRenderer** and the **GestureRecognizer** objects see [Dynamic-Renderer Plug-ins](dynamic-renderer-plug-ins.md) and [Recognizer Plug-ins](recognizer-plug-ins.md).

The [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object calls the [Microsoft.StylusInput.IStylusSyncPlugin.CustomStylusDataAdded](frlrfMicrosoftStylusInputIStylusSyncPluginClassCustomStylusDataAddedTopic) method on the thread from which it receives the call to its [AddCustomStylusDataToQueue](frlrfMicrosoftStylusInputRealTimeStylusClassAddCustomStylusDataToQueueTopic) method.

The following diagram illustrates the addition of custom stylus data to the output queue with the *queue* parameter set to **Output**.

![illustration showing custom stylus data flow to the output queue ](images/27bc3672-41bc-432e-bf41-18e4ccec78f5.gif)

In this diagram, the circles lettered "A" and "B" represent tablet pen data that has already been added to the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object's output queue and that has not yet been sent to the asynchronous plug-in collection. The circle lettered "C" represents the tablet pen data that the **RealTimeStylus** object is currently processing. It is sent to the synchronous plug-in collection and placed on the output queue. The circles numbered "1", "2", and "3" represent custom stylus data that has been added to the output queue by the first, second, and third synchronous plug-ins respectively in response to the tablet pen data represented by "C". The plug-ins have added the custom stylus data with the *queue* parameter set to **StylusQueues**. The empty circle represents the position in the output queue where future tablet pen data is added.

The following diagram illustrates the addition of custom stylus data to the output queue with the *queue* parameter set to **OutputImmediate**.

![illustration showing custom stylus data flow to the output queue](images/bcf45325-5557-47a2-af43-142c7684e482.gif)

In this diagram, the circles lettered "A" and "B" represent tablet pen data that has already been added to the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object's output queue and that has not yet been sent to the asynchronous plug-in collection. The circle lettered "C" represents the tablet pen data that the **RealTimeStylus** object is currently processing. It is sent to the synchronous plug-in collection and placed on the output queue. The circles numbered "1", "2", and "3" represent custom stylus data that has been added to the output queue by the first, second, and third synchronous plug-ins respectively in response to the tablet pen data represented by "C". The plug-ins have added the custom stylus data with the *queue* parameter set to **OutputImmediate**. The empty circle represents the position in the output queue where future tablet pen data is added.

The following diagram illustrates the addition of custom stylus data to the input queue.

![illustration showing custom stylus data flow to the output queue](images/5dd2cfcc-1086-49b0-a0d5-9276c13c7f61.gif)

In this diagram, the circles lettered "A" and "B" represent tablet pen data that has already been added to the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object's output queue and that has not yet been sent to the asynchronous plug-in collection. The circle lettered "C" represents the tablet pen data that the **RealTimeStylus** object is currently processing. It is sent to the synchronous plug-in collection and placed on the output queue. The circles numbered "1", "2", and "3" represent custom stylus data that has been added to the input queue by the first, second, and third synchronous plug-ins respectively in response to the tablet pen data represented by "C". The plug-ins have added the custom stylus data with the *queue* parameter set to **Input**. The custom stylus data numbered "1" is then passed to the synchronous plug-ins and then to the output queue before the custom stylus data numbered "2" and "3", both of which are processed before the next tablet pen data is processed. The empty circle represents the position in the output queue where future tablet pen data is added.

## Error Data

When a plug-in throws an exception, the normal flow of data is interrupted. The [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object generates an [ErrorData](frlrfMicrosoftStylusInputPluginDataErrorDataClassTopic) object and calls:

-   The [Microsoft.StylusInput.IStylusSyncPlugin.Error](frlrfMicrosoftStylusInputIStylusSyncPluginClassErrorTopic) or [Microsoft.StylusInput.IStylusAsyncPlugin.Error](frlrfMicrosoftStylusInputIStylusAsyncPluginClassErrorTopic) method of the plug-in that threw the exception.
-   The [Microsoft.StylusInput.IStylusSyncPlugin.Error](frlrfMicrosoftStylusInputIStylusSyncPluginClassErrorTopic) or [Microsoft.StylusInput.IStylusAsyncPlugin.Error](frlrfMicrosoftStylusInputIStylusAsyncPluginClassErrorTopic) method of the remaining plug-ins in that collection.

If the plug-in that threw the exception is a synchronous plug-in, the [ErrorData](frlrfMicrosoftStylusInputPluginDataErrorDataClassTopic) object is added to the output queue. Then the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object resumes normal processing of the original data.

The following diagram illustrates the addition of error data to the tablet pen data.

![custom stylus data flow to the output queue with the addition of error data](images/c2f79abe-aeb5-498f-b389-1fad9bf01a13.gif)

In this diagram, the circles lettered "A" and "B" represent tablet pen data that has already been added to the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object's output queue and that has not yet been sent to the asynchronous plug-in collection. The circle lettered "C" represents the tablet pen data that the **RealTimeStylus** object is currently processing. The circle lettered "e" represents a [ErrorData](frlrfMicrosoftStylusInputPluginDataErrorDataClassTopic) object generated by the **RealTimeStylus** object when the second synchronous plug-in, Synchronous Plug-in 2, throws an exception while it is processing "C". The **RealTimeStylus** object then pauses its processing of "C" and passes "e" to the plug-in that generated the exception and all subsequent plug-ins. The **RealTimeStylus** object then puts "e" on the output queue and resumes its processing of "C", which is passed to the remaining plug-ins in the synchronous plug-in collection and placed on the output queue after "e". The empty circle represents the position in the output queue where future tablet pen data is added.

If a plug-in throws an exception from its Error method, the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object catches the exception but does not generate a new [ErrorData](frlrfMicrosoftStylusInputPluginDataErrorDataClassTopic) object. This is to prevent recursion.

The error data is added to the output queue after any custom stylus data that is added at the **OutputImmediate** position prior to the exception that created the error data and before any custom stylus data that is added at the **OutputImmediate** position by subsequent plug-ins in the synchronous plug-in collection.

The following diagram illustrates how the error data is added to the output queue in relation to custom data that is added to the **OutputImmediate** queue.

![error data added to the output queue in relation to custom data added to the outputimmediate queue.](images/b00320c4-6fe7-439d-9855-e5f131feeb69.gif)

In this diagram, the circles lettered "A" and "B" represent tablet pen data that has already been added to the [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object's output queue and that has not yet been sent to the asynchronous plug-in collection. The circle lettered "C" represents the tablet pen data that the **RealTimeStylus** object is currently processing. The circles numbered "1", "2", and "3" are added by the first, second, and third synchronous plug-ins respectively to the **OutputImmediate** queue in response to the data represented by the circle lettered "C". The circle lettered "e" represents error data generated in response to an exception thrown by the second plug-in after the second plug-in added custom data to the output queue at the **OutputImmediate** position.

If any synchronous plug-in adds custom stylus data to the input queue in response to the error data, the data is added immediately before the error data. If any of the synchronous plug-ins adds custom stylus data to the output queue at the **Output** position in response to the error data, the data is added immediately after the error data.

The [**RealTimeStylus**](/windows/win32/RTSCom/?branch=master) object calls the [Microsoft.StylusInput.IStylusSyncPlugin.Error](frlrfMicrosoftStylusInputIStylusSyncPluginClassErrorTopic) method on the thread from which the exception is thrown.

## Related topics

<dl> <dt>

[Microsoft.Ink.Tablet](frlrfMicrosoftInkTabletClassTopic)
</dt> <dt>

[Microsoft.StylusInput.PluginData](frlrfMicrosoftStylusInputPluginData)
</dt> <dt>

[Microsoft.StylusInput.DataInterestMask](frlrfMicrosoftStylusInputDataInterestMaskClassTopic)
</dt> <dt>

[Microsoft.StylusInput.RealTimeStylus](frlrfMicrosoftStylusInputRealTimeStylusClassTopic)
</dt> <dt>

[Working with the RealTimeStylus Class](working-with-the-realtimestylus-class.md)
</dt> </dl>

 

 




