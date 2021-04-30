---
description: This section contains information about the interfaces and classes used in the real time stylus.
ms.assetid: fc0900b4-f08b-4a93-bbc0-d3db067d7917
title: RealTimeStylus Classes and Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# RealTimeStylus Classes and Interfaces

This section contains information about the interfaces and classes used in the real time stylus.

> [!Note]  
> The real time stylus classes and interfaces are not Automation compliant.

 

## In This Section



| Class                                                      | Description                                                                                     |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [**RealTimeStylus Class**](realtimestylus-class.md)       | Implements the [**IRealTimeStylus**](/windows/desktop/api/RTSCom/nn-rtscom-irealtimestylus) interface.<br/>                 |
| [**DynamicRenderer Class**](/previous-versions/windows/desktop/legacy/ms701168(v=vs.85))     | Implements the [**IDynamicRenderer Interface**](/windows/desktop/api/RTSCom/nn-rtscom-idynamicrenderer) interface.<br/>     |
| [**GestureRecognizer Class**](gesturerecognizer-class.md) | Implements the [**IGestureRecognizer Interface**](/windows/desktop/api/RTSCom/nn-rtscom-igesturerecognizer) interface.<br/> |
| [**StrokeBuilder Class**](strokebuilder-class.md)         | Implements the [**IStrokeBuilder Interface**](/windows/desktop/api/RTSCom/nn-rtscom-istrokebuilder) interface.<br/>         |



 

## Interfaces



| Interface                                                                          | Description                                                                                                                                                                                 |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IDynamicRenderer Interface**](/windows/desktop/api/RTSCom/nn-rtscom-idynamicrenderer)                             | Exposes methods enabling you to control the display of stylus data in real time as the data is being handled by the [**RealTimeStylus Class**](realtimestylus-class.md) object.<br/> |
| [**IGestureRecognizer Interface**](/windows/desktop/api/RTSCom/nn-rtscom-igesturerecognizer)                         | Exposes methods enabling you to react to events by recognizing stylus gestures and enabling you to add data to the input queue.<br/>                                                  |
| [**IRealTimeStylus**](/windows/desktop/api/RTSCom/nn-rtscom-irealtimestylus)                                         | Handles the stylus packet data from a digitizer in real time.<br/>                                                                                                                    |
| [**IRealTimeStylus2**](/windows/desktop/api/RTSCom/nn-rtscom-irealtimestylus2)                                       | Extends the IRealTimeStylus interface.<br/>                                                                                                                                           |
| [**IRealTimeStylus3**](/windows/desktop/api/rtscom/nn-rtscom-irealtimestylus3)                                       | Extends the IRealTimeStylus interface.<br/>                                                                                                                                           |
| [**IRealTimeStylusSynchronization Interface**](/windows/desktop/api/RTSCom/nn-rtscom-irealtimestylussynchronization) | Synchronizes access to the [**RealTimeStylus Class**](realtimestylus-class.md) object.<br/>                                                                                          |
| [**IStrokeBuilder Interface**](/windows/desktop/api/RTSCom/nn-rtscom-istrokebuilder)                                 | Exposes methods that enable you to programmatically create strokes.<br/>                                                                                                              |
| [**IStylusPlugin Interface**](/windows/desktop/api/RTSCom/nn-rtscom-istylusplugin)                                   | Exposes methods enabling you to receive notifications of events and to perform custom processing based on those events.<br/>                                                          |
| [**IStylusAsyncPlugin**](/windows/win32/api/rtscom/nn-rtscom-istylusasyncplugin)                                   | Represents an asynchronous plug-in that can be added to the [**RealTimeStylus Class**](realtimestylus-class.md) asynchronous plug-in collection.<br/>                                |
| [**IStylusSyncPlugin**](/windows/win32/api/rtscom/nn-rtscom-istylussyncplugin)                                     | Represents a synchronous plug-in that can be added to the [**RealTimeStylus Class**](realtimestylus-class.md) synchronous plug-in collection.<br/>                                   |



 

## Return Values

Methods in the COM Library return values of **HRESULT**. Unless otherwise noted, the meanings of the **HRESULT** values are described in the following table.



| HRESULT value                                   | Description                                                                              |
|-------------------------------------------------|------------------------------------------------------------------------------------------|
| S\_OK<br/>                                | Success.<br/>                                                                      |
| E\_POINTER<br/>                           | At least one pointer (for either an input or an output parameter) is invalid.<br/> |
| E\_INVALIDARG<br/>                        | Member attempted to pass in an invalid argument.<br/>                              |
| E\_INK\_EXCEPTION<br/>                    | Exception occurred.<br/>                                                           |
| E\_OUTOFMEMORY<br/>                       | System cannot allocate memory to complete the operation.<br/>                      |
| E\_FAIL<br/>                              | Unspecified failure occurred.<br/>                                                 |
| E\_INVALIDOPERATION<br/>                  | Member attempted to use an invalid operation.<br/>                                 |
| TPC\_E\_INVALID\_MODE<br/>                | Member attempted to use an invalid mode.<br/>                                      |
| TPC\_E\_INVALID\_CONFIGURATION<br/>       | Member attempted to use an invalid configuration.<br/>                             |
| TPC\_E\_INVALID\_PACKET\_DESCRIPTION<br/> | Member attempted to use an invalid packet description.<br/>                        |



 

## Related topics

<dl> <dt>

[RealTimeStylus Reference](realtimestylus-reference.md)
</dt> </dl>

 

 
