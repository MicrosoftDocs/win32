---
Description: This section contains information about the interfaces and classes used in the real time stylus.
ms.assetid: fc0900b4-f08b-4a93-bbc0-d3db067d7917
title: RealTimeStylus Classes and Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RealTimeStylus Classes and Interfaces

This section contains information about the interfaces and classes used in the real time stylus.

> [!Note]  
> The real time stylus classes and interfaces are not Automation compliant.

 

## In This Section



| Class                                                      | Description                                                                                     |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [**RealTimeStylus Class**](/windows/win32/RTSCom/?branch=master)       | Implements the [**IRealTimeStylus**](/windows/win32/RTSCom/nn-rtscom-irealtimestylus?branch=master) interface.<br/>                 |
| [**DynamicRenderer Class**](/windows/win32/RTSCom/?branch=master)     | Implements the [**IDynamicRenderer Interface**](/windows/win32/RTSCom/nn-rtscom-idynamicrenderer?branch=master) interface.<br/>     |
| [**GestureRecognizer Class**](/windows/win32/RTSCom/?branch=master) | Implements the [**IGestureRecognizer Interface**](/windows/win32/RTSCom/nn-rtscom-igesturerecognizer?branch=master) interface.<br/> |
| [**StrokeBuilder Class**](/windows/win32/RTSCom/?branch=master)         | Implements the [**IStrokeBuilder Interface**](/windows/win32/RTSCom/nn-rtscom-istrokebuilder?branch=master) interface.<br/>         |



 

## Interfaces



| Interface                                                                          | Description                                                                                                                                                                                 |
|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IDynamicRenderer Interface**](/windows/win32/RTSCom/nn-rtscom-idynamicrenderer?branch=master)                             | Exposes methods enabling you to control the display of stylus data in real time as the data is being handled by the [**RealTimeStylus Class**](/windows/win32/RTSCom/?branch=master) object.<br/> |
| [**IGestureRecognizer Interface**](/windows/win32/RTSCom/nn-rtscom-igesturerecognizer?branch=master)                         | Exposes methods enabling you to react to events by recognizing stylus gestures and enabling you to add data to the input queue.<br/>                                                  |
| [**IRealTimeStylus**](/windows/win32/RTSCom/nn-rtscom-irealtimestylus?branch=master)                                         | Handles the stylus packet data from a digitizer in real time.<br/>                                                                                                                    |
| [**IRealTimeStylus2**](/windows/win32/RTSCom/nn-rtscom-irealtimestylus2?branch=master)                                       | Extends the IRealTimeStylus interface.<br/>                                                                                                                                           |
| [**IRealTimeStylus3**](/windows/win32/rtscom/nn-rtscom-irealtimestylus3?branch=master)                                       | Extends the IRealTimeStylus interface.<br/>                                                                                                                                           |
| [**IRealTimeStylusSynchronization Interface**](/windows/win32/RTSCom/nn-rtscom-irealtimestylussynchronization?branch=master) | Synchronizes access to the [**RealTimeStylus Class**](/windows/win32/RTSCom/?branch=master) object.<br/>                                                                                          |
| [**IStrokeBuilder Interface**](/windows/win32/RTSCom/nn-rtscom-istrokebuilder?branch=master)                                 | Exposes methods that enable you to programmatically create strokes.<br/>                                                                                                              |
| [**IStylusPlugin Interface**](/windows/win32/RTSCom/nn-rtscom-istylusplugin?branch=master)                                   | Exposes methods enabling you to receive notifications of events and to perform custom processing based on those events.<br/>                                                          |
| [**IStylusAsyncPlugin**](/windows/win32/RTSCom/?branch=master)                                   | Represents an asynchronous plug-in that can be added to the [**RealTimeStylus Class**](/windows/win32/RTSCom/?branch=master) asynchronous plug-in collection.<br/>                                |
| [**IStylusSyncPlugin**](/windows/win32/RTSCom/?branch=master)                                     | Represents a synchronous plug-in that can be added to the [**RealTimeStylus Class**](/windows/win32/RTSCom/?branch=master) synchronous plug-in collection.<br/>                                   |



 

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

 

 




