---
title: Compartments
description: Compartments
ms.assetid: '7bffab6f-be40-4d3a-9342-6f81557a9656'
keywords: ["Text Services Framework (TSF),compartments", "TSF (Text Services Framework),compartments", "text services,compartments", "TSF-enabled applications,compartments", "compartments", "Text Services Framework (TSF),compartment types", "TSF (Text Services Framework),compartment types", "text services,compartment types", "TSF-enabled applications,compartment types", "compartment types", "Text Services Framework (TSF),compartment change notifications", "TSF (Text Services Framework),compartment change notifications", "text services,compartment change notifications", "TSF-enabled applications,compartment change notifications", "compartment change notifications"]
---

# Compartments

## Compartment Types

There are several different types of compartments. There is a global compartment, and each thread manager, document manager, and context can contain a compartment.

The global compartment enables clients to share data across processes. To obtain the global compartment manager, call [**ITfThreadMgr::GetGlobalCompartment**](itfthreadmgr-getglobalcompartment.md).

The thread manager contains a compartment manager that contains compartments on a per-thread basis. This allows data to be shared within a thread. To obtain a thread manager compartment manager, call **ITfThreadMgr::QueryInterface** with IID\_ITfCompartmentMgr.

Each document manager created also contains a compartment manager. This allows data to be shared within a specific document manager. To obtain the document manager compartment manager, call **ITfDocumentMgr::QueryInterface** with IID\_ITfCompartmentMgr.

Each context created also contains a compartment manager. This allows data to be shared within a specific context. To obtain a context compartment manager, call **ITfContext::QueryInterface** with IID\_ITfCompartmentMgr.

## Creating and Deleting a Compartment

A compartment is created the first time [**ITfCompartmentMgr::GetCompartment**](itfcompartmentmgr-getcompartment.md) is called with the compartment GUID. The installing client should set the initial value of the compartment using [**ITfCompartment::SetValue**](itfcompartment-setvalue.md). Until a value is set, the compartment value is empty. Because of this, there is no way to verify that the compartment existed before **GetCompartment** was called. To avoid this situation, the installing client should set the value to some initial value so that other clients can determine if the compartment already exists.

The [**ITfCompartmentMgr::ClearCompartment**](itfcompartmentmgr-clearcompartment.md) method is used to remove a compartment. Any existing references to the compartment are marked invalid.

## Obtaining Compartments

Using the [**ITfCompartmentMgr**](itfcompartmentmgr.md) interface, a client can enumerate compartments by calling [**ITfCompartmentMgr::EnumCompartments**](itfcompartmentmgr-enumcompartments.md). This method provides an **IEnumGUID** object that contains the GUIDs of all of the installed compartments.

Using the compartment GUID , **ITfCompartmentMgr::GetCompartment** is used to obtain a specific compartment. This method provides the caller with an [**ITfCompartment**](itfcompartment.md) object that can obtain and set the compartment data.

## Receiving Compartment Change Notifications

When the value of a compartment changes, the TSF manager notifies any installed advise sinks that the compartment has changed. To install a compartment change advise sink, create an object that implements [**ITfCompartmentEventSink**](itfcompartmenteventsink.md). Then call **ITfCompartment::QueryInterface** with IID\_ITfSource on the compartment object to be monitored to obtain an [**ITfSource**](itfsource.md) interface. Now call [**ITfSource::AdviseSink**](itfsource-advisesink.md) with IID\_ITfCompartmentEventSink and the pointer to the **ITfCompartmentEventSink** object. When the value of the compartment changes, the advise sink's [**ITfCompartmentEventSink::OnChange**](itfcompartmenteventsink-onchange.md) is called with the GUID of the compartment. The advise sink can call [**ITfCompartment::GetValue**](itfcompartment-getvalue.md) to obtain the new value.

## Related topics

<dl> <dt>

[**ITfCompartmentMgr**](itfcompartmentmgr.md)
</dt> <dt>

[**ITfCompartment**](itfcompartment.md)
</dt> <dt>

[**ITfCompartmentEventSink**](itfcompartmenteventsink.md)
</dt> <dt>

[**TfClientId**](tfclientid.md)
</dt> <dt>

[**ITfThreadMgr::GetGlobalCompartment**](itfthreadmgr-getglobalcompartment.md)
</dt> <dt>

[**ITfCompartmentMgr::GetCompartment**](itfcompartmentmgr-getcompartment.md)
</dt> <dt>

[**ITfCompartment::SetValue**](itfcompartment-setvalue.md)
</dt> <dt>

[**ITfCompartmentMgr::ClearCompartment**](itfcompartmentmgr-clearcompartment.md)
</dt> <dt>

[**ITfCompartmentMgr::EnumCompartments**](itfcompartmentmgr-enumcompartments.md)
</dt> <dt>

[**ITfSource**](itfsource.md)
</dt> <dt>

[**ITfSource::AdviseSink**](itfsource-advisesink.md)
</dt> <dt>

[**ITfCompartmentEventSink::OnChange**](itfcompartmenteventsink-onchange.md)
</dt> </dl>

 

 




