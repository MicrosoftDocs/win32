---
Description: 'This topic describes how to set a stop time for playback when using the Media Session.'
ms.assetid: 'B8BA2154-2824-4573-AE71-853EB8AB911D'
title: How to Set the Playback Stop Time
---

# How to Set the Playback Stop Time

This topic describes how to set a stop time for playback when using the [Media Session](media-session.md).

## Setting the Stop Time Before Playback Begins

Before you queue a topology for playback, you can specify the stop time by using the [MF\_TOPONODE\_MEDIASTOP](mf-toponode-mediastop-attribute.md) attribute. For each output node in the topology, set the value of the MF\_TOPONODE\_MEDIASTOP to the stop time in 100-nanosecond units.

Note that setting this attribute after playback starts has no effect. Therefore, set the attribute before calling [**IMFMediaSession::Start**](imfmediasession-start.md).

The following code shows how to set the stop time on an existing topology.


```C++
template <class Q>
HRESULT GetCollectionObject(IMFCollection *pCollection, DWORD dwIndex, Q **ppObject)
{
    *ppObject = NULL;   // zero output

    IUnknown *pUnk = NULL;
    HRESULT hr = pCollection->GetElement(dwIndex, &amp;pUnk);
    if (SUCCEEDED(hr))
    {
        hr = pUnk->QueryInterface(IID_PPV_ARGS(ppObject));
        pUnk->Release();
    }
    return hr;
}

HRESULT SetMediaStop(IMFTopology *pTopology, const LONGLONG&amp; stop)
{
    IMFCollection *pCol = NULL;
    DWORD cNodes;

    HRESULT hr = pTopology->GetSourceNodeCollection(&amp;pCol);
    if (SUCCEEDED(hr))
    {
        hr = pCol->GetElementCount(&amp;cNodes);
    }
    if (SUCCEEDED(hr))
    {
        for (DWORD i = 0; i < cNodes; i++)
        {
            IMFTopologyNode *pNode;
            hr = GetCollectionObject(pCol, i, &amp;pNode);
            if (SUCCEEDED(hr))
            {
                pNode->SetUINT64(MF_TOPONODE_MEDIASTOP, stop);
            }
            pNode->Release();
        }
    }
    SafeRelease(&amp;pCol);
    return hr;
}
```



## Setting the Stop Time After Playback Has Started

There is a way to set the stop time after the [Media Session](media-session.md) starts playback, by using the [**IMFTopologyNodeAttributeEditor**](imftopologynodeattributeeditor.md) interface.

> \[!Important\]  
> This interface has a serious limitation, because the stop time is specified as a 32-bit value. That means the maximum stop time that you can set using this interface is 0xFFFFFFFF, or just over 7 minutes. This limitation is due to an incorrect structure definition.

 

To set the stop time using the [**IMFTopologyNodeAttributeEditor**](imftopologynodeattributeeditor.md) interface, perform the following steps.

1.  Call [**MFGetService**](mfgetservice.md) to get the [**IMFTopologyNodeAttributeEditor**](imftopologynodeattributeeditor.md) interface from the Media Session.
2.  Call [**IMFTopology::GetTopologyID**](imftopology-gettopologyid.md) to get the ID of the playback topology.
3.  For each output node in the topology, call [**IMFTopologyNodeAttributeEditor::UpdateNodeAttributes**](imftopologynodeattributeeditor-updatenodeattributes.md). This method takes the topology ID and a pointer to a [**MFTOPONODE\_ATTRIBUTE\_UPDATE**](mftoponode-attribute-update.md) structure. Initialize the structure as follows.

    | Member               | Value                                                                                                               |
    |----------------------|---------------------------------------------------------------------------------------------------------------------|
    | **NodeId**           | The node ID. To get the node ID, call call [**IMFTopologyNode::GetTopoNodeID**](imftopologynode-gettoponodeid.md). |
    | **guidAttributeKey** | **MF\_TOPONODE\_MEDIASTOP**                                                                                         |
    | **attrType**         | **MF\_ATTRIBUTE\_UINT64**                                                                                           |
    | **u64**              | The stop time, in 100-nanosecond units.                                                                             |

    

     

Be careful to set the value of **attrType** correctly. Although **u64** is a 32-bit type, the method requires that **attrType** be set to **MF\_ATTRIBUTE\_UINT64**.

The following code shows these steps.


```C++
HRESULT SetMediaStopDynamic(IMFMediaSession *pSession, IMFTopology *pTopology, const LONGLONG&amp; stop)
{
    if (stop > MAXUINT32)
    {
        return E_INVALIDARG;
    }

    IMFTopologyNodeAttributeEditor *pAttr = NULL;
    IMFCollection *pCol = NULL;
    IMFTopologyNode *pNode = NULL;

    HRESULT hr = MFGetService(pSession, MF_TOPONODE_ATTRIBUTE_EDITOR_SERVICE, IID_PPV_ARGS(&amp;pAttr));
    if (FAILED(hr))
    {
        goto done;
    }

    TOPOID id;
    hr = pTopology->GetTopologyID(&amp;id);
    if (FAILED(hr))
    {
        goto done;
    }

    DWORD cNodes;
    hr = pTopology->GetSourceNodeCollection(&amp;pCol);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pCol->GetElementCount(&amp;cNodes);
    if (FAILED(hr))
    {
        goto done;
    }

    for (DWORD i = 0; i < cNodes; i++)
    {
        IMFTopologyNode *pNode;
        hr = GetCollectionObject(pCol, i, &amp;pNode);
        if (FAILED(hr))
        {
            goto done;
        }

        TOPOID nodeID;
        hr = pNode->GetTopoNodeID(&amp;nodeID);
        if (FAILED(hr))
        {
            goto done;
        }

        MFTOPONODE_ATTRIBUTE_UPDATE update;
        update.NodeId = nodeID;
        update.guidAttributeKey = MF_TOPONODE_MEDIASTOP;
        update.attrType = MF_ATTRIBUTE_UINT64;
        update.u64 = (UINT32)stop;

        hr = pAttr->UpdateNodeAttributes(id, 1, &amp;update);
        if (FAILED(hr))
        {
            goto done;
        }
        SafeRelease(&amp;pNode);
    }

done:
    SafeRelease(&amp;pNode);
    SafeRelease(&amp;pCol);
    SafeRelease(&amp;pAttr);
    return hr;
}
```



## Related topics

<dl> <dt>

[Audio/Video Playback](audio-video-playback.md)
</dt> </dl>

 

 



