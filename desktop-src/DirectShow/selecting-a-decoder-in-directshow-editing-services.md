---
description: Selecting a Decoder in DirectShow Editing Services
ms.assetid: dc6b0445-7fc1-4331-9000-a652b44a8364
title: Selecting a Decoder in DirectShow Editing Services
ms.topic: article
ms.date: 05/31/2018
---

# Selecting a Decoder in DirectShow Editing Services

\[This API is not supported and may be altered or unavailable in the future.\]

When [DirectShow Editing Services](directshow-editing-services.md) (DES) renders a video editing project, the Rendering Engine automatically selects the necessary decoders. This may happen inside the [**IRenderEngine::ConnectFrontEnd**](irenderengine-connectfrontend.md) method, or else dynamically during rendering.

A user might install several decoders that are capable of decoding a particular file. When multiple decoders are available, DES uses the [Intelligent Connect](intelligent-connect.md) algorithm to select the decoder.

There is no way for the application to specify directly which decoder to use. However, you can choose the decoder indirectly through the [**IAMGraphBuilderCallback**](/windows/desktop/api/Strmif/nn-strmif-iamgraphbuildercallback) callback interface. By implementing this interface in your application, you can receive notifications during the graph-building process and reject certain filters from the graph.

Start by implementing a class that exposes the [**IAMGraphBuilderCallback**](/windows/desktop/api/Strmif/nn-strmif-iamgraphbuildercallback) interface:


```C++
class GraphBuilderCB : public IAMGraphBuilderCallback
{
public:
     // Method declarations (not shown).
};
```



Then create an instance of the Filter Graph Manager and register your class to receive callback notifications:


```C++
// Declare an instance of the callback object.
GraphBuilderCB GraphCB; 

// Create the Filter Graph Manager.
CComPtr<IGraphBuilder> pGraph;
hr = pGraph.CoCreateInstance(CLSID_FilterGraph);
if (FAILED(hr))
{
    // Handle error (not shown).
}
// Register to receive the callbacks.
CComQIPtr<IObjectWithSite> pSite(pGraph);
if (pSite)
{
    hr = pSite->SetSite((IUnknown*)&GraphCB);
}
```



Next, create the Render Engine and call the [**IRenderEngine::SetFilterGraph**](irenderengine-setfiltergraph.md) method with a pointer to the Filter Graph Manager. This ensures that the Render Engine does not create its own Filter Graph Manager, but instead uses the instance that you have configured for callbacks.


```C++
CComPtr<IRenderEngine> pRender;
hr = pRender.CoCreateInstance(CLSID_RenderEngine);
if (FAILED(hr))
{
    // Handle error (not shown).
}

hr = pRender->SetFilterGraph(pGraph);
```



When the project is rendered, the application's [**IAMGraphBuilderCallback::SelectedFilter**](/windows/desktop/api/Strmif/nf-strmif-iamgraphbuildercallback-selectedfilter) method is called immediately before the Filter Graph Manager creates a new filter. The **SelectedFilter** method receives a pointer to an **IMoniker** interface that represents a moniker for the filter. Examine the moniker, and if you decide to reject the filter, return a failure code from the **SelectedFilter** method.

The difficult part is to identify which monikers represent decoders — and in particular, which monikers represent decoders that you want to reject. One solution is the following:

-   Before rendering the project, use the [**IFilterMapper2::EnumMatchingFilters**](/windows/desktop/api/Strmif/nf-strmif-ifiltermapper2-enummatchingfilters) method to create a list of filters that are registered as accepting the desired input type. For video or audio compression types, this list should map to a set of decoders.
-   The **EnumMatchingFilters** method returns a collection of monikers. For each moniker in the collection, get the **DisplayName** property, as described in [Using the Filter Mapper](using-the-filter-mapper.md).
-   Store a list of the display names, but omit the display name that matches the filter you want to use for decoding. Display names for software filters have the following form:

    ```C++
    OLESTR("@device:sw:{CategoryGUID}\{FilterCLSID}");
    ```

    

    where

    ```C++
    CategoryGUID
    ```

    

    is the GUID of the filter category, and

    ```C++
    FilterCLSID
    ```

    

    is the filter's CLSID. For DMOs, the format is the same, but change `sw` to `dmo`.

    The list now contains display names for every filter that outputs the desired media type but is not your preferred filter.

-   In the **SelectedFilter** method, get the **DisplayName** property on the proposed moniker and check it against the stored list. If the display name matches an entry in the list, reject that filter. Otherwise, accept it by returning S\_OK.

## Related topics

<dl> <dt>

[Rendering a Project](rendering-a-project.md)
</dt> </dl>

 

 



