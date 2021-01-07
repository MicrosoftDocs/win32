---
description: Applications can listen to system events by using the InkCollector object and listening for the SystemGesture event on it.
ms.assetid: 141afdbe-b5a7-47dc-b505-46089a5eda75
title: Listening to System Events
ms.topic: article
ms.date: 05/31/2018
---

# Listening to System Events

Applications can listen to system events by using the [**InkCollector**](inkcollector-class.md) object and listening for the [**SystemGesture**](inkcollector-systemgesture.md) event on it. You can set which events an application listens to. When a tablet pen action occurs, the corresponding **SystemGesture** event is sent to the application on its **InkCollector** object. An application can cancel the mouse message that corresponds to a given **SystemGesture** event when it receives the event. For details about canceling mouse messages, see **SystemGesture** event.

 

 



