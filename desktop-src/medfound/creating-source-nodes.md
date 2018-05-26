---
Description: Creating Source Nodes
ms.assetid: 44c26bcd-04a9-48c3-b536-25c2b18c34c1
title: Creating Source Nodes
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating Source Nodes

A source node represents one stream from a media source. The source node must contain pointers to the media source, the presentation descriptor, and the stream descriptor.

To add a source node to a topology, do the following:

1.  Call [**MFCreateTopologyNode**](/windows/win32/mfidl/nf-mfidl-mfcreatetopologynode?branch=master) with the **MF\_TOPOLOGY\_SOURCESTREAM\_NODE** flag to create the source node.
2.  Set the [**MF\_TOPONODE\_SOURCE**](mf-toponode-source-attribute.md) attribute on the node, with a pointer to the media source.
3.  Set the [**MF\_TOPONODE\_PRESENTATION\_DESCRIPTOR**](mf-toponode-presentation-descriptor-attribute.md) attribute on the node, with a pointer to the presentation descriptor of the media source.
4.  Set the [**MF\_TOPONODE\_STREAM\_DESCRIPTOR**](mf-toponode-stream-descriptor-attribute.md) attribute on the node, with a pointer to the stream descriptor for the stream.
5.  Call [**IMFTopology::AddNode**](/windows/win32/mfidl/nf-mfidl-imftopology-addnode?branch=master) to add the node to the topology.

The following example creates and initializes a source node.


```C++
// Add a source node to a topology.
HRESULT AddSourceNode(
    IMFTopology *pTopology,           // Topology.
    IMFMediaSource *pSource,          // Media source.
    IMFPresentationDescriptor *pPD,   // Presentation descriptor.
    IMFStreamDescriptor *pSD,         // Stream descriptor.
    IMFTopologyNode **ppNode)         // Receives the node pointer.
{
    IMFTopologyNode *pNode = NULL;

    // Create the node.
    HRESULT hr = MFCreateTopologyNode(MF_TOPOLOGY_SOURCESTREAM_NODE, &amp;pNode);
    if (FAILED(hr))
    {
        goto done;
    }

    // Set the attributes.
    hr = pNode->SetUnknown(MF_TOPONODE_SOURCE, pSource);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pNode->SetUnknown(MF_TOPONODE_PRESENTATION_DESCRIPTOR, pPD);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pNode->SetUnknown(MF_TOPONODE_STREAM_DESCRIPTOR, pSD);
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
    SafeRelease(&amp;pNode);
    return hr;
}
```



## Related topics

<dl> <dt>

[Creating Topologies](creating-topologies.md)
</dt> <dt>

[Media Sources](media-sources.md)
</dt> <dt>

[Topologies](topologies.md)
</dt> <dt>

[**IMFTopologyNode**](/windows/win32/mfidl/nn-mfidl-imftopologynode?branch=master)
</dt> </dl>

 

 



