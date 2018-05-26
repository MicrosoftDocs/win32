---
Description: Binding Output Nodes to Media Sinks
ms.assetid: d4f93f34-0af1-431f-9333-70ea09691b64
title: Binding Output Nodes to Media Sinks
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Binding Output Nodes to Media Sinks

This topic describes how to initialize the output nodes in a topology, if you are using the topology loader outside of the Media Session. An output node initially contains one of the following:

-   An [**IMFStreamSink**](/windows/win32/mfidl/nn-mfidl-imfstreamsink?branch=master) pointer.
-   An [**IMFActivate**](/windows/win32/mfobjects/nn-mfobjects-imfactivate?branch=master) pointer.

In the latter case, the [**IMFActivate**](/windows/win32/mfobjects/nn-mfobjects-imfactivate?branch=master) pointer must be converted to an [**IMFStreamSink**](/windows/win32/mfidl/nn-mfidl-imfstreamsink?branch=master) pointer before the topology loader resolves the topology. In most scenarios, the process works as follows:

1.  The application queues a partial topology on the Media Session.
2.  For all output nodes, the Media Session converts [**IMFActivate**](/windows/win32/mfobjects/nn-mfobjects-imfactivate?branch=master) pointers to [**IMFStreamSink**](/windows/win32/mfidl/nn-mfidl-imfstreamsink?branch=master) pointers. This process is called *binding* the output node to a media sink.
3.  The Media Session sends the modified topology to the [**IMFTopoLoader::Load**](/windows/win32/mfidl/nf-mfidl-imftopoloader-load?branch=master) method.

However, if you are using the topology loader directly (outside of the media sesssion), your application must bind the output nodes prior to calling [**IMFTopoLoader::Load**](/windows/win32/mfidl/nf-mfidl-imftopoloader-load?branch=master). To bind an output node, do the following:

1.  Call [**IMFTopologyNode::GetObject**](/windows/win32/mfidl/nf-mfidl-imftopologynode-getobject?branch=master) to get the node's object pointer.
2.  Query the object pointer for the [**IMFStreamSink**](/windows/win32/mfidl/nn-mfidl-imfstreamsink?branch=master) interface. If this call succeeds, there is nothing more to do, so skip the remaining steps.
3.  If the previous step failed, query the object pointer for the [**IMFActivate**](/windows/win32/mfobjects/nn-mfobjects-imfactivate?branch=master) interface.
4.  Create the media sink by calling [**IMFActivate::ActivateObject**](/windows/win32/mfobjects/nf-mfobjects-imfactivate-activateobject?branch=master). Specify **IID\_IMFMediaSink** to get a pointer to the media sink's [**IMFMediaSink**](/windows/win32/mfidl/nn-mfidl-imfmediasink?branch=master) interface.
5.  Query the node for the [**MF\_TOPONODE\_STREAMID**](mf-toponode-streamid-attribute.md) attribute. The value of this attribute is the identifier of the stream sink for this node. If the **MF\_TOPONODE\_STREAMID** attribute is not set, the default stream identifier is zero.
6.  The appropriate stream sink might already exist on the media sink. To check, call [**IMFMediaSink::GetStreamSinkById**](/windows/win32/mfidl/nf-mfidl-imfmediasink-getstreamsinkbyid?branch=master) on the media sink. If the stream sink exists, the method returns a pointer to its [**IMFStreamSink**](/windows/win32/mfidl/nn-mfidl-imfstreamsink?branch=master) interface. If this call fails, try to add a new stream sink by calling [**IMFMediaSink::AddStreamSink**](/windows/win32/mfidl/nf-mfidl-imfmediasink-addstreamsink?branch=master). If both calls fail, it means the media sink does not support the requested stream identifier, and this topology node is not configured correctly. Return an error code and skip the next step.
7.  Call [**IMFTopologyNode::SetObject**](/windows/win32/mfidl/nf-mfidl-imftopologynode-setobject?branch=master), passing in the [**IMFStreamSink**](/windows/win32/mfidl/nn-mfidl-imfstreamsink?branch=master) pointer from the previous step. This call replaces the node's object pointer, so that the node contains a pointer to the stream sink, instead of a pointer to the activation object.

The following code shows how to bind an output node.


```C++
// BindOutputNode
// Sets the IMFStreamSink pointer on an output node.

HRESULT BindOutputNode(IMFTopologyNode *pNode)
{
    IUnknown *pNodeObject = NULL;
    IMFActivate *pActivate = NULL;
    IMFStreamSink *pStream = NULL;
    IMFMediaSink *pSink = NULL;

    // Get the node's object pointer.
    HRESULT hr = pNode->GetObject(&amp;pNodeObject);
    if (FAILED(hr))
    {
        return hr;
    }

    // The object pointer should be one of the following:
    // 1. An activation object for the media sink.
    // 2. The stream sink.

    // If it's #2, then we're already done.

    // First, check if it's an activation object.
    hr = pNodeObject->QueryInterface(IID_PPV_ARGS(&amp;pActivate));

    if (SUCCEEDED(hr))
    {
        DWORD dwStreamID = 0;

        // The object pointer is an activation object. 
        
        // Try to create the media sink.
        hr = pActivate->ActivateObject(IID_PPV_ARGS(&amp;pSink));

        // Look up the stream ID. (Default to zero.)

        if (SUCCEEDED(hr))
        {
           dwStreamID = MFGetAttributeUINT32(pNode, MF_TOPONODE_STREAMID, 0);
        }

        // Now try to get or create the stream sink.

        // Check if the media sink already has a stream sink with the requested ID.

        if (SUCCEEDED(hr))
        {
            hr = pSink->GetStreamSinkById(dwStreamID, &amp;pStream);
            if (FAILED(hr))
            {
                // Try to add a new stream sink.
                hr = pSink->AddStreamSink(dwStreamID, NULL, &amp;pStream);
            }
        }

        // Replace the node's object pointer with the stream sink. 
        if (SUCCEEDED(hr))
        {
            hr = pNode->SetObject(pStream);
        }
    }
    else
    {
        // Not an activation object. Is it a stream sink?
        hr = pNodeObject->QueryInterface(IID_PPV_ARGS(&amp;pStream));
    }

    SafeRelease(&amp;pNodeObject);
    SafeRelease(&amp;pActivate);
    SafeRelease(&amp;pStream);
    SafeRelease(&amp;pSink);
    return hr;
}
```



> [!Note]  
> This example uses the [SafeRelease](saferelease.md) function to release interface pointers.

 

The next example shows how to bind all of the output nodes in a topology. This example uses the [**IMFTopology::GetOutputNodeCollection**](/windows/win32/mfidl/nf-mfidl-imftopology-getoutputnodecollection?branch=master) method to get a collection of output nodes from the topology. Then it calls the function shown in the previous example on each of those nodes in turn.


```C++
// BindOutputNodes
// Sets the IMFStreamSink pointers on all of the output nodes in a topology.

HRESULT BindOutputNodes(IMFTopology *pTopology)
{
    DWORD cNodes = 0;

    IMFCollection *pCol = NULL;
    IUnknown *pUnk = NULL;
    IMFTopologyNode *pNode = NULL;

    // Get the collection of output nodes. 
    HRESULT hr = pTopology->GetOutputNodeCollection(&amp;pCol);
    
    // Enumerate all of the nodes in the collection.
    if (SUCCEEDED(hr))
    {
        hr = pCol->GetElementCount(&amp;cNodes);
    }

    if (SUCCEEDED(hr))
    {
        for (DWORD i = 0; i < cNodes; i++)
        {
            hr = pCol->GetElement(i, &amp;pUnk);

            if (FAILED(hr)) { break; }

            hr = pUnk->QueryInterface(IID_IMFTopologyNode, (void**)&amp;pNode);

            if (FAILED(hr)) { break; }

            // Bind this node.
            hr = BindOutputNode(pNode);

            if (FAILED(hr)) { break; }
        }
    }

    SafeRelease(&amp;pCol);
    SafeRelease(&amp;pUnk);
    SafeRelease(&amp;pNode);
    return hr;
}
```



## Related topics

<dl> <dt>

[Advanced Topology Building](advanced-topology-building.md)
</dt> <dt>

[Media Sinks](media-sinks.md)
</dt> <dt>

[**IMFTopoLoader**](/windows/win32/mfidl/nn-mfidl-imftopoloader?branch=master)
</dt> </dl>

 

 



