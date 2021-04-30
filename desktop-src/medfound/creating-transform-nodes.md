---
description: Creating Transform Nodes
ms.assetid: d70a3c2b-2f0e-4e29-9a8f-84a50d9f1682
title: Creating Transform Nodes
ms.topic: article
ms.date: 05/31/2018
---

# Creating Transform Nodes

A transform node represents a Media Foundation transform (MFT), such as a decoder or encoder. There are several different ways to initialize a transform node:

-   From a pointer to the MFT.
-   From a CLSID for the MFT.
-   From a pointer to an activation object for the MFT.

If you are going to load the topology inside the protected media path (PMP), you must use either the CLSID or an activation object, so that the MFT can be created inside the protected process. The first approach (using a pointer to the MFT) does not work with the PMP.

## Creating a Transform Node from an MFT

To create a transform node from an MFT, do the following:

1.  Create an instance of the MFT and get a pointer to the [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) interface of the MFT.
2.  Call [**MFCreateTopologyNode**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatetopologynode) with the **MF\_TOPOLOGY\_TRANSFORM\_NODE** flag to create the transform node.
3.  Call [**IMFTopologyNode::SetObject**](/windows/desktop/api/mfidl/nf-mfidl-imftopologynode-setobject) and pass in the [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) pointer.
4.  Call [**IMFTopology::AddNode**](/windows/desktop/api/mfidl/nf-mfidl-imftopology-addnode) to add the node to the topology.

The following example creates and initializes a transform node from an MFT.


```C++
HRESULT AddTransformNode(
    IMFTopology *pTopology,     // Topology.
    IMFTransform *pMFT,         // MFT.
    IMFTopologyNode **ppNode    // Receives the node pointer.
    )
{
    *ppNode = NULL;

    IMFTopologyNode *pNode = NULL;
    
    // Create the node.
    HRESULT hr = MFCreateTopologyNode(MF_TOPOLOGY_TRANSFORM_NODE, &pNode);

    // Set the object pointer.
    if (SUCCEEDED(hr))
    {
        hr = pNode->SetObject(pMFT);
    }

    // Add the node to the topology.
    if (SUCCEEDED(hr))
    {
        hr = pTopology->AddNode(pNode);
    }

    // Return the pointer to the caller.
    if (SUCCEEDED(hr))
    {
        *ppNode = pNode;
        (*ppNode)->AddRef();
    }

    SafeRelease(&pNode);
    return hr;
}
```



## Creating a Transform Node from a CLSID

To create a transform node from a CLSID, do the following:

1.  Find the CLSID of the MFT. You can use the [**MFTEnum**](/windows/desktop/api/mfapi/nf-mfapi-mftenum) function to find the CLSIDs of MFTs by category, such as decoders or encoders. You might also know the CLSID of a particular MFT that you want to use (for example, if you implemented your own custom MFT).
2.  Call [**MFCreateTopologyNode**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatetopologynode) with the **MF\_TOPOLOGY\_TRANSFORM\_NODE** flag to create the transform node.
3.  Set the **MF\_TOPONODE\_TRANSFORM\_OBJECTID** attribute on the node. The attribute value is the CLSID.
4.  Call [**IMFTopology::AddNode**](/windows/desktop/api/mfidl/nf-mfidl-imftopology-addnode) to add the node to the topology.

The following example creates and initializes a transform node from a CLSID.


```C++
HRESULT AddTransformNode(
    IMFTopology *pTopology,     // Topology.
    const CLSID& clsid,         // CLSID of the MFT.
    IMFTopologyNode **ppNode    // Receives the node pointer.
    )
{
    *ppNode = NULL;

    IMFTopologyNode *pNode = NULL;
    
    // Create the node.
    HRESULT hr = MFCreateTopologyNode(MF_TOPOLOGY_TRANSFORM_NODE, &pNode);

    // Set the CLSID attribute.

    if (SUCCEEDED(hr))
    {
        hr = pNode->SetGUID(MF_TOPONODE_TRANSFORM_OBJECTID, clsid);
    }

    // Add the node to the topology.
    if (SUCCEEDED(hr))
    {
        hr = pTopology->AddNode(pNode);
    }

    // Return the pointer to the caller.
    if (SUCCEEDED(hr))
    {
        *ppNode = pNode;
        (*ppNode)->AddRef();
    }

    SafeRelease(&pNode);
    return hr;
}
```



## Creating a Transform Node from an Activation Object

Some MFTs provide activation objects. For example, the [**MFCreateWMAEncoderActivate**](/windows/desktop/api/wmcontainer/nf-wmcontainer-mfcreatewmaencoderactivate) function returns an activation object for the Windows Media Audio (WMA) encoder. The exact function depends on the MFT. Not every MFT provides an activation object. For more information, see [Activation Objects](activation-objects.md).

You can also get an MFT activation object by calling the [**MFTEnumEx**](/windows/desktop/api/mfapi/nf-mfapi-mftenumex) function.

To create a transform node from an activation object, do the following:

1.  Create the activation object and get a pointer to the [**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate) interface of the activation object.
2.  Call [**MFCreateTopologyNode**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatetopologynode) with the **MF\_TOPOLOGY\_TRANSFORM\_NODE** flag to create the transform node.
3.  Call [**IMFTopologyNode::SetObject**](/windows/desktop/api/mfidl/nf-mfidl-imftopologynode-setobject) and pass in the [**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate) pointer.
4.  Call [**IMFTopology::AddNode**](/windows/desktop/api/mfidl/nf-mfidl-imftopology-addnode) to add the node to the topology.

The following example creates and initializes a transform node from an activation object.


```C++
HRESULT AddTransformNode(
    IMFTopology *pTopology,     // Topology.
    IMFActivate *pActivate,     // MFT activation object.
    IMFTopologyNode **ppNode    // Receives the node pointer.
    )
{
    *ppNode = NULL;

    IMFTopologyNode *pNode = NULL;
    
    // Create the node.
    HRESULT hr = MFCreateTopologyNode(MF_TOPOLOGY_TRANSFORM_NODE, &pNode);

    // Set the object pointer.
    if (SUCCEEDED(hr))
    {
        hr = pNode->SetObject(pActivate);
    }

    // Add the node to the topology.
    if (SUCCEEDED(hr))
    {
        hr = pTopology->AddNode(pNode);
    }

    // Return the pointer to the caller.
    if (SUCCEEDED(hr))
    {
        *ppNode = pNode;
        (*ppNode)->AddRef();
    }

    SafeRelease(&pNode);
    return hr;
}
```



## Related topics

<dl> <dt>

[Creating Topologies](creating-topologies.md)
</dt> <dt>

[Topologies](topologies.md)
</dt> <dt>

[**IMFTopologyNode**](/windows/desktop/api/mfidl/nn-mfidl-imftopologynode)
</dt> </dl>

 

 



