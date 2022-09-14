---
description: Creating Output Nodes
ms.assetid: 6e548f2a-77cd-460e-9ffd-c098f6ee75eb
title: Creating Output Nodes
ms.topic: article
ms.date: 05/31/2018
---

# Creating Output Nodes

An output node represents a stream sink on a media sink. There are two ways to initialize an output node:

-   From a pointer to the stream sink.
-   From a pointer to an activation object for the media sink.

If you are going to load the topology inside the protected media path (PMP), you must use an activation object, so that the media sink can be created inside the protected process. The first approach (using a pointer to the stream sink) does not work with the PMP.

## Creating an Output Node from a Stream Sink

To create an output node from a stream sink, do the following:

1.  Create an instance of the media sink.
2.  Use the media sink's [**IMFMediaSink**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasink) interface to get a pointer to the desired stream sink. (The **IMFMediaSink** interface has several methods that return pointers to a stream sink.)
3.  Call [**MFCreateTopologyNode**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatetopologynode) with the **MF\_TOPOLOGY\_OUTPUT\_NODE** flag to create the output node.
4.  Call [**IMFTopologyNode::SetObject**](/windows/desktop/api/mfidl/nf-mfidl-imftopologynode-setobject) and pass in a pointer to the stream sink's [**IMFStreamSink**](/windows/desktop/api/mfidl/nn-mfidl-imfstreamsink) interface.
5.  Set the [**MF\_TOPONODE\_NOSHUTDOWN\_ON\_REMOVE**](mf-toponode-noshutdown-on-remove-attribute.md) attribute to **FALSE** (optional but recommended).
6.  Call [**IMFTopology::AddNode**](/windows/desktop/api/mfidl/nf-mfidl-imftopology-addnode) to add the node to the topology.

The following example creates and initializes an output node from a stream sink.


```C++
HRESULT AddOutputNode(
    IMFTopology *pTopology,     // Topology.
    IMFStreamSink *pStreamSink, // Stream sink.
    IMFTopologyNode **ppNode    // Receives the node pointer.
    )
{
    IMFTopologyNode *pNode = NULL;
    HRESULT hr = S_OK;
    
    // Create the node.
    hr = MFCreateTopologyNode(MF_TOPOLOGY_OUTPUT_NODE, &pNode);

    // Set the object pointer.
    if (SUCCEEDED(hr))
    {
        hr = pNode->SetObject(pStreamSink);
    }

    // Add the node to the topology.
    if (SUCCEEDED(hr))
    {
        hr = pTopology->AddNode(pNode);
    }

    if (SUCCEEDED(hr))
    {
        hr = pNode->SetUINT32(MF_TOPONODE_NOSHUTDOWN_ON_REMOVE, TRUE);
    }

    // Return the pointer to the caller.
    if (SUCCEEDED(hr))
    {
        *ppNode = pNode;
        (*ppNode)->AddRef();
    }

    if (pNode)
    {
        pNode->Release();
    }
    return hr;
}
```



When the application shuts down the Media Session, the Media Session automatically shuts down the media sink. Therefore, you cannot re-use the media sink with another instance of the Media Session.

## Creating an Output Node from an Activation Object

Any trusted media sink must provide an activation object, so that the media sink can be created inside the protected process. For more information, see [Activation Objects](activation-objects.md). The particular function that creates the activation object will depend on the media sink.

To create an output node from an activation object, do the following:

1.  Create the activation object and get a pointer to the activation object's [**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate) interface.
2.  Call [**MFCreateTopologyNode**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatetopologynode) with the **MF\_TOPOLOGY\_OUTPUT\_NODE** flag to create the output node.
3.  Optionally, set the [**MF\_TOPONODE\_STREAMID**](mf-toponode-streamid-attribute.md) attribute on the node to specify the stream identifier of the stream sink. If you omit this attribute, the node defaults to using stream sink 0.
4.  Set the [**MF\_TOPONODE\_NOSHUTDOWN\_ON\_REMOVE**](mf-toponode-noshutdown-on-remove-attribute.md) attribute to **TRUE** (optional but recommended).
5.  Call [**IMFTopologyNode::SetObject**](/windows/desktop/api/mfidl/nf-mfidl-imftopologynode-setobject) and pass in the [**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate) pointer.
6.  Call [**IMFTopology::AddNode**](/windows/desktop/api/mfidl/nf-mfidl-imftopology-addnode) to add the node to the topology.

The following example creates and initializes an output node from an activation object.


```C++
// Add an output node to a topology.
HRESULT AddOutputNode(
    IMFTopology *pTopology,     // Topology.
    IMFActivate *pActivate,     // Media sink activation object.
    DWORD dwId,                 // Identifier of the stream sink.
    IMFTopologyNode **ppNode)   // Receives the node pointer.
{
    IMFTopologyNode *pNode = NULL;

    // Create the node.
    HRESULT hr = MFCreateTopologyNode(MF_TOPOLOGY_OUTPUT_NODE, &pNode);
    if (FAILED(hr))
    {
        goto done;
    }

    // Set the object pointer.
    hr = pNode->SetObject(pActivate);
    if (FAILED(hr))
    {
        goto done;
    }

    // Set the stream sink ID attribute.
    hr = pNode->SetUINT32(MF_TOPONODE_STREAMID, dwId);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pNode->SetUINT32(MF_TOPONODE_NOSHUTDOWN_ON_REMOVE, FALSE);
    if (FAILED(hr))
    {
        goto done;
    }

    // Add the node to the topology.
    hr = pTopology->AddNode(pNode);
    if (FAILED(hr))
    {
        goto done;
    }

    // Return the pointer to the caller.
    *ppNode = pNode;
    (*ppNode)->AddRef();

done:
    SafeRelease(&pNode);
    return hr;
}
```



## Related topics

<dl> <dt>

[**IMFTopologyNode**](/windows/desktop/api/mfidl/nn-mfidl-imftopologynode)
</dt> <dt>

[Creating Topologies](creating-topologies.md)
</dt> <dt>

[Media Sinks](media-sinks.md)
</dt> <dt>

[Topologies](topologies.md)
</dt> </dl>

 

 



