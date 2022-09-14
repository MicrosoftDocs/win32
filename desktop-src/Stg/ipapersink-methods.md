---
title: IPaperSink Methods
description: COPaper exposes the IConnectionPointContainer interface so clients can connect to COPaper in order to receive notifications of specified events that occur in COPaper.
ms.assetid: 2466c721-b275-4dbc-a604-2d5e6a29d6a1
ms.topic: reference
ms.date: 05/31/2018
---

# IPaperSink Methods

COPaper exposes the [**IConnectionPointContainer**](/windows/win32/api/ocidl/nn-ocidl-iconnectionpointcontainer) interface so clients can connect to COPaper in order to receive notifications of specified events that occur in COPaper. By exposing this interface, COPaper becomes a connectable object. A client can call [**QueryInterface**](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) for this interface and use it to obtain the object's connection points. The client participation in this scheme is covered in the associated **StoClien** sample.

Basically, the client implements what is called a sink in the form of a sink object with a sink interface. The sink interface receives outgoing event notification calls from COPaper after the sink is properly connected by the client to a COPaper instance. The client makes the connection by using a connection point object that is managed by COPaper. There can be numerous connection points on a single connectable COM object. In the **StoServe** sample, COPaper has only one connection point, which handles drawing paper events.

Any number of clients can connect to a single connection point. The CONNPOINT\_PAPERSINK connection point in COPaper maintains a group of connections that can grow dynamically at run time. The full details on COPaper's connectable object support is coded in files CONNECT.H and CONNECT.CPP and will not be covered here. The construction is very similar to what was studied in the CONSERVE code sample.

The **StoClien** client implements appropriate sink objects for the connection points it expects to find in COPaper. From the context of COPaper, the important sink object that **StoClien** implements exposes the **IPaperSink** interface. This is the outgoing interface used by COPaper to notify **StoClien** of various events in COPaper.

Here is a summary of the methods in **IPaperSink** from IPAPER.H in the \\INC sibling directory.



| Method   | Description                                                   |
|----------|---------------------------------------------------------------|
| Locked   | A client has taken control of and locked the paper.           |
| Unlocked | A client has relinquished control of the paper.               |
| Loaded   | A client has loaded paper content from its own compound file. |
| Saved    | A client has saved paper content to its own compound file.    |
| InkStart | A client started a color ink drawing sequence to the paper.   |
| InkDraw  | A client is putting ink data points on the paper surface.     |
| InkStop  | A client has stopped its ink drawing sequence to the paper.   |
| Erased   | A client has erased all ink data from the paper.              |
| Resized  | A client has resized the paper.                               |



 

These methods are largely self-explanatory. Although the sink must implement all these methods in some fashion, many are implemented as stubs and are not used in the **StoServe**/**StoClien** samples.

An important method used in these samples is the Loaded method. When COPaper is told by the client to load a new drawing from file, it needs a way to notify the client when the new data is loaded. To do this, COPaper Calls **IPaperSink::Loaded** on the client sink. The client can then call [**IPaper::Redraw**](ipaper--redraw.md) to request that COPaper play back the new data to the client. Redraw causes the loaded drawing in the client's display to be repainted. When the load is completed, the newly loaded drawing is displayed automatically in the window provided by the client.

See [**IPaper::Redraw**](ipaper--redraw.md) for complete information of this IPaper method's connectivity to **IPaperSink**.

The **IPaperSink** methods **InkStart**, **InkDraw**, and **InkStop** are used to send individual ink data packets back to the client. On reception, the client paints them in its display in the same manner as when it originally sent them to COPaper. The above logic is general enough to allow for multiple clients that are all listening on the same CONNPOINT\_PAPERSINK connection point. If a common COPaper instance was shared by these clients, they could all display the same drawing by connecting to this connection point.

 

 