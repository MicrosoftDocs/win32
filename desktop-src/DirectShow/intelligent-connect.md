---
Description: Intelligent Connect
ms.assetid: '938ba1b0-822e-4871-8786-b7eeee243867'
title: Intelligent Connect
---

# Intelligent Connect

Intelligent Connect is the mechanism the Filter Graph Manager uses to build filter graphs. It consists of several related algorithms that select filters and add them to the filter graph.

Read this topic if you are having trouble building a certain filter graph and want to troubleshoot the problem, or if you are writing your own filter and want to make it available for automatic graph building.

Intelligent Connect involves the following [**IGraphBuilder**](igraphbuilder.md) methods:

-   [**IGraphBuilder::AddSourceFilter**](igraphbuilder-addsourcefilter.md)
-   [**IGraphBuilder::Render**](igraphbuilder-render.md)
-   [**IGraphBuilder::RenderFile**](igraphbuilder-renderfile.md)
-   [**IGraphBuilder::Connect**](igraphbuilder-connect.md)

### IGraphBuilder::AddSourceFilter

The [**IGraphBuilder::AddSourceFilter**](igraphbuilder-addsourcefilter.md) method adds a source filter that can render a specified file. First it looks in the registry and matches against the protocol (such as `http://`), the file name extension, or a set of predetermined *check bytes*, which are bytes at particular offsets in the file that match certain patterns. For details, see [Registering a Custom File Type](registering-a-custom-file-type.md). Assuming that the method locates an appropriate source filter, it then creates an instance of that filter, adds it to the graph, and calls the filter's [**IFileSourceFilter::Load**](ifilesourcefilter-load.md) method with the file name.

### IGraphBuilder::Render

The [**IGraphBuilder::Render**](igraphbuilder-render.md) method builds a subsection of a graph. It starts from an unconnected output pin and works downstream, adding new filters as needed. The starting filter must already be in the graph. At each step, the **Render** method searches for a filter that can connect to the previous filter. The stream can branch if a connecting filter has multiple output pins. The search stops when every stream has a renderer. If the **Render** method gets stuck, it might back up and try again, using a different set of filters.

To connect each output pin, the [**Render**](igraphbuilder-render.md) method does the following:

1.  If the pin supports the [**IStreamBuilder**](istreambuilder.md) interface, the Filter Graph Manager delegates the entire process to the pin's [**IStreamBuilder::Render**](istreambuilder-render.md) method. By exposing this interface, the pin assumes responsibility for building the remainder of the graph, down to the renderer. However, very few pins support this interface.
2.  The Filter Graph Manager tries to use filters that are cached in memory, if any. Throughout the Intelligent Connect process, the Filter Graph Manager may cache filters from earlier steps in the process. (Also, see [Dynamic Graph Building](dynamic-graph-building.md).)
3.  If the filter graph contains any filters with unconnected input pins, the Filter Graph Manager tries them next. You can force the [**Render**](igraphbuilder-render.md) method to try a particular filter by adding that filter to the graph before calling **Render**.
4.  Starting in Windows 7, DirectShow has a list of preferred filters for certain media subtypes. If there is a preferred filter for the media type that is being rendered, the Filter Graph Manager tries that filter next. An application can modify the list of preferred filters by using the [**IAMPluginControl**](iamplugincontrol.md) interface. Changes to the list affect the application's current process, and are discarded after the process ends.
5.  Finally, if no suitable filter has been found, the Filter Graph Manager searches the registry, using the [**IFilterMapper2::EnumMatchingFilters**](ifiltermapper2-enummatchingfilters.md) method. It tries to match the output pin's preferred media types against media types listed in the registry.

    Each filter is registered with a *merit*, a numerical value that indicates how preferable the filter is, relative to other filters. The [**EnumMatchingFilters**](ifiltermapper2-enummatchingfilters.md) method returns filters in order of merit, with a minimum merit of **MERIT\_DO\_NOT\_USE** + 1. It ignores filters with a merit of **MERIT\_DO\_NOT\_USE** or less. Filters are also grouped into categories, defined by GUID. Categories themselves have merit, and the **EnumMatchingFilters** method ignores any category with a merit of **MERIT\_DO\_NOT\_USE** or less, even if the filters in that category have higher merit values.

    Starting in Windows 7, DirectShow has a list of blocked filters for certain media subtypes. The Filter Graph Manager skips filters on this list. An application can modify the list of blocked filters by using the [**IAMPluginControl**](iamplugincontrol.md) interface. Changes to this list affect the application's current process, and are discarded after the process ends.

To summarize, the [**Render**](igraphbuilder-render.md) method tries filters in the following order:

1.  Use [**IStreamBuilder**](istreambuilder.md).
2.  Try cached filters.
3.  Try filters in the graph.
4.  Windows 7 or later: Try the preferred filter for the media type, if any.
5.  Look up filters in the registry.

### IGraphBuilder::RenderFile

The [**IGraphBuilder::RenderFile**](igraphbuilder-renderfile.md) method builds a default playback graph from a file name. Internally, this method uses [**AddSourceFilter**](igraphbuilder-addsourcefilter.md) to locate the correct source filter, and [**Render**](igraphbuilder-render.md) to build the rest of the graph.

### IGraphBuilder::Connect

The [**IGraphBuilder::Connect**](igraphbuilder-connect.md) method connects an output pin to an input pin. This method adds intermediate filters if needed, using a variation of the algorithm described for the [**Render**](igraphbuilder-render.md) method:

1.  Try a direct connection between the filters, with no intermediate filters.
2.  Try cached filters.
3.  Try filters in the graph.
4.  Windows 7 or later: Try the preferred filter for the media type, if any.
5.  Look up filters in the registry.

## Related topics

<dl> <dt>

[Filter Categories](filter-categories.md)
</dt> <dt>

[Merit](merit.md)
</dt> <dt>

[Simulating Graph Building with GraphEdit](simulating-graph-building-with-graphedit.md)
</dt> <dt>

[Building the Filter Graph](building-the-filter-graph.md)
</dt> </dl>

 

 



