---
Description: A recognizer plug-in is an object that monitors the movement of the tablet pen for gesture, handwriting, or other objects.
ms.assetid: 764a327e-1da0-487f-9245-b6a4f3f43502
title: Recognizer Plug-ins
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Recognizer Plug-ins

A recognizer plug-in is an object that monitors the movement of the tablet pen for gesture, handwriting, or other objects.

## System Gestures

The [**RealTimeStylus**](/windows/desktop/api/RTSCom/) object recognizes system gestures. The **RealTimeStylus** object adds a [SystemGestureData](https://www.bing.com/search?q=SystemGestureData) object to the [StylusQueues](https://www.bing.com/search?q=StylusQueues) queue in response to the data that finishes the gesture, such as a [StylusUpData](https://www.bing.com/search?q=StylusUpData) object for the [SystemGesture](https://www.bing.com/search?q=SystemGesture). For more information, see [Plug-in Data and the RealTimeStylus Class](plug-in-data-and-the-realtimestylus-class.md).

## The GestureRecognizer Object

The [**GestureRecognizer**](/windows/desktop/api/RTSCom/) object implements the [**IStylusSyncPlugin**](/windows/desktop/api/RTSCom/) and [**IStylusAsyncPlugin**](/windows/desktop/api/RTSCom/) interfaces. The **GestureRecognizer** object recognizes application gestures. Internally, the **GestureRecognizer** object uses the Microsoft gesture recognizer to perform gesture recognition.

When the [**GestureRecognizer**](/windows/desktop/api/RTSCom/) object recognizes a gesture, it adds custom stylus data to the [StylusQueues](https://www.bing.com/search?q=StylusQueues) queue in response to the [StylusUpData](https://www.bing.com/search?q=StylusUpData) object for the stroke. The [CustomStylusData](https://www.bing.com/search?q=CustomStylusData) object's [CustomDataId](https://www.bing.com/search?q=CustomDataId) property is set to the [GestureRecognitionDataGuid](https://www.bing.com/search?q=GestureRecognitionDataGuid) value, and the CustomStylusData object's [Data](https://www.bing.com/search?q=Data) property contains a [GestureRecognitionData](https://www.bing.com/search?q=GestureRecognitionData) object.

The following diagram illustrates how the [**GestureRecognizer**](/windows/desktop/api/RTSCom/) object adds data to the tablet pen data.

![illustration of gesturerecognizer data flow](images/c4c77c33-deee-49d0-84bc-12612575ec66.gif)

In this diagram the circle lettered "SD" represents a [StylusDownData](https://www.bing.com/search?q=StylusDownData) object and the circles lettered "P" represent [PacketsData](https://www.bing.com/search?q=PacketsData) objects that have already been added to the [**RealTimeStylus**](/windows/desktop/api/RTSCom/) object's output queue and that have not yet been sent to the asynchronous plug-in collection. The circle lettered "SU" represents a [StylusUpData](https://www.bing.com/search?q=StylusUpData) object that the **RealTimeStylus** object is currently processing. It is sent to the synchronous plug-in collection and then placed on the output queue. The circles lettered "GR" represent custom stylus data that is added to the input queue by the [**GestureRecognizer**](/windows/desktop/api/RTSCom/) plug-in in response to the stylus up notification associated with "SU". The custom stylus data lettered "GR" is then passed to the synchronous plug-ins and then to the output queue before the next tablet pen data is processed. The empty circle represents the position in the output queue where future tablet pen data is added.

By default, the [**GestureRecognizer**](/windows/desktop/api/RTSCom/) object recognizes only single-stroke gestures; however, the **GestureRecognizer** object can be set to recognize multistroke gestures. For multistroke gestures, the [CustomStylusData](https://www.bing.com/search?q=CustomStylusData) object is added to the [StylusQueues](https://www.bing.com/search?q=StylusQueues) queue in response to the [StylusUpData](https://www.bing.com/search?q=StylusUpData) object for the final stroke of the gesture. When recognizing multistroke gestures, you may receive notifications for overlapping sets of strokes. For example, the first and second strokes together may be recognized as one gesture and the second stroke by itself may be recognized as a gesture. For more information about multistroke gesture recognition, see the **GestureRecognizer** class and the [MaxStrokeCount](https://www.bing.com/search?q=MaxStrokeCount) property.

If you are using the [**GestureRecognizer**](/windows/desktop/api/RTSCom/) object for multistroke gesture recognition, you may achieve optimal performance by using a cascaded [**RealTimeStylus**](/windows/desktop/api/RTSCom/) model and attaching the **GestureRecognizer** object to the secondary **RealTimeStylus** object. For more information about the cascading **RealTimeStylus** model, see [The Cascaded RealTimeStylus Model](the-cascaded-realtimestylus-model.md).

### Special Considerations

The following list describes other points to take into consideration when using the [**GestureRecognizer**](/windows/desktop/api/RTSCom/) object.

-   You should not attach a [**GestureRecognizer**](/windows/desktop/api/RTSCom/) object to more than one [**RealTimeStylus**](/windows/desktop/api/RTSCom/) object. Once two **RealTimeStylus** objects to which the **GestureRecognizer** object is attached are enabled, the following occurs.
    -   The [**GestureRecognizer**](/windows/desktop/api/RTSCom/) object throws an exception in response to the second call to its RealTimeStylusEnabled method.
    -   The second [**RealTimeStylus**](/windows/desktop/api/RTSCom/) object that was enabled generates a [ErrorData](https://www.bing.com/search?q=ErrorData) object and notifies the remaining plug-ins in its plug-in collections of the error.
    -   The [**GestureRecognizer**](/windows/desktop/api/RTSCom/) object stops recognizing gestures.
-   The [**RealTimeStylus**](/windows/desktop/api/RTSCom/) object throws an exception when its [AddCustomStylusDataToQueue](https://www.bing.com/search?q=AddCustomStylusDataToQueue) method is called with the *guid* parameter set to the [Microsoft.StylusInput.GestureRecognizer.GestureRecognitionDataGuid](https://www.bing.com/search?q=Microsoft.StylusInput.GestureRecognizer.GestureRecognitionDataGuid) globally unique identifier (GUID).
-   The [**GestureRecognizer**](/windows/desktop/api/RTSCom/) object is implemented as a Component Object Model (COM) wrapper, and you cannot call its [**IStylusSyncPlugin**](/windows/desktop/api/RTSCom/) or [**IStylusAsyncPlugin**](/windows/desktop/api/RTSCom/) interface methods directly. For more information about COM implementation and the [**RealTimeStylus**](/windows/desktop/api/RTSCom/) object, see [Implementation Notes for the StylusInput APIs](implementation-notes-for-the-stylusinput-apis.md).

## Custom Gesture Recognition

You can create a custom recognizer plug-in that recognizes handwriting, gestures, or other objects by:

-   Passing the stroke information to an existing [Recognizer](https://www.bing.com/search?q=Recognizer) object and using the [AddCustomStylusDataToQueue](https://www.bing.com/search?q=AddCustomStylusDataToQueue) method to add the results to the tablet pen data stream.
-   Performing the recognition within your plug-in and using the [AddCustomStylusDataToQueue](https://www.bing.com/search?q=AddCustomStylusDataToQueue) method to add the results to the tablet pen data stream.

## Related topics

<dl> <dt>

[Application Gestures](application-gestures.md)
</dt> <dt>

[System Gestures](system-gestures.md)
</dt> <dt>

[Timeline of Mouse Messages and System Events](timeline-of-mouse-messages-and-system-events.md)
</dt> </dl>

 

 



